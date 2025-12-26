from fastapi import FastAPI, Depends,HTTPException, Header


from datetime import datetime, timedelta
import secrets

from database import SessionLocal
from security import encrypt, hash_token
from ai_engine import analyze_report
from auth import verify, create_token

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Pharmacovigilance API is running"}


@app.post("/login")
def login(username: str, password: str):
    if username == "safety" and password == "admin":
        return {"token": create_token(username)}
    raise HTTPException(401)

@app.post("/report")
def ingest(case_id: str, report: str, email: str):
    missing, risk = analyze_report(report)
    db = SessionLocal()

    db.execute("INSERT INTO adverse_events VALUES (%s,%s,'OPEN',NOW())",
               (case_id, risk))
    db.execute("INSERT INTO identity_vault (case_id, encrypted_email) VALUES (%s,%s)",
               (case_id, encrypt(email)))

    if missing:
        token = secrets.token_urlsafe(32)
        db.execute(
            "INSERT INTO followup_tokens VALUES (%s,%s,%s,%s,0)",
            (hash_token(token), case_id, ",".join(missing),
             datetime.utcnow() + timedelta(hours=48))
        )
        db.commit()
        return {"followup_link": f"http://localhost:3000/f/{token}"}

    db.commit()
    return {"message": "Complete"}

@app.get("/followup/{token}")
def validate(token: str):
    db = SessionLocal()
    h = hash_token(token)
    row = db.execute(
        "SELECT case_id, required_fields FROM followup_tokens "
        "WHERE token_hash=%s AND used=0 AND expires_at>NOW()", (h,)
    ).fetchone()

    if not row:
        raise HTTPException(401)
    return {"case_id": row[0], "fields": row[1].split(",")}

@app.post("/followup/{token}")
def submit(token: str, answers: dict):
    db = SessionLocal()
    h = hash_token(token)

    row = db.execute(
        "SELECT case_id FROM followup_tokens WHERE token_hash=%s AND used=0", (h,)
    ).fetchone()

    if not row:
        raise HTTPException(401)

    case_id = row[0]

    for k, v in answers.items():
        db.execute(
            "INSERT INTO clinical_data (case_id,field_name,encrypted_value,source) "
            "VALUES (%s,%s,%s,'FOLLOWUP')",
            (case_id, k, encrypt(v))
        )

    db.execute("UPDATE followup_tokens SET used=1 WHERE token_hash=%s", (h,))
    db.execute("INSERT INTO audit_logs (case_id,action) VALUES (%s,'FOLLOWUP_SUBMITTED')", (case_id,))
    db.commit()
    return {"message": "Submitted"}

@app.get("/dashboard", dependencies=[Depends(verify)])
def dashboard():
    db = SessionLocal()
    rows = db.execute("SELECT * FROM adverse_events").fetchall()
    return rows
