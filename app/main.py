from fastapi import FastAPI
from pydantic import BaseModel
from app.agent import summarize_text

app = FastAPI()

# ✅ Health check (root URL)
@app.get("/")
def health():
    return {"status": "running"}

class Request(BaseModel):
    text: str

# ✅ Main API
@app.post("/summarize")
def summarize(req: Request):
    try:
        return {"summary": summarize_text(req.text)}
    except Exception as e:
        print("ERROR:", str(e))
        return {"error": str(e)}