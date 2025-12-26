from fastapi import HTTPException, Depends
from jose import jwt

SECRET = "SAFETY_SECRET"

def create_token(username):
    return jwt.encode({"user": username}, SECRET, algorithm="HS256")

def verify(token):
    try:
        jwt.decode(token, SECRET, algorithms=["HS256"])
    except:
        raise HTTPException(status_code=401)
