from fastapi import FastAPI
from pydantic import BaseModel
from app.services.analyzer import summarize_email_en_and_ko

# Create a FastAPI app instance
app = FastAPI()

# Define the request body schema
class EmailSummaryRequest(BaseModel):
    text: str   # The email text to be summarized

# Define the API endpoint for summarization
@app.post("/summarize")
async def summarize_email(request: EmailSummaryRequest):
    """
    Accepts an English email text, returns both English summary and Korean translation.
    """
    result = await summarize_email_en_and_ko(request.text)
    return result