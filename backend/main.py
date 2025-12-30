from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from reviewer import review_code

# Create FastAPI app
app = FastAPI(title="AI Code Review Assistant")

# Enable CORS (to allow frontend access)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request model
class CodeInput(BaseModel):
    code: str
    language: str

# Root endpoint (optional test)
@app.get("/")
def home():
    return {"message": "AI Code Review Assistant Backend is running"}

# Code review endpoint
@app.post("/review")
def review(data: CodeInput):
    result = review_code(data.code, data.language)
    return {"review": result}
