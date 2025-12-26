import spacy
nlp = spacy.load("en_core_web_sm")

REQUIRED = ["age", "onset_date", "dosage"]

def analyze_report(text):
    found = set()
    doc = nlp(text.lower())
    for t in doc:
        if t.text in REQUIRED:
            found.add(t.text)

    missing = list(set(REQUIRED) - found)
    risk = "HIGH" if "onset_date" in missing else "MEDIUM"

    return missing, risk
