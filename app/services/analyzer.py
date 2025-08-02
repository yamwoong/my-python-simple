from transformers import pipeline
from google.cloud import translate_v2 as translate
from langdetect import detect
from app.services.db import summaries_collection

# Load the English summarization pipeline
en_summarizer = pipeline("summarization")

# Load the Google Cloud Translation client
translate_client = translate.Client()

import asyncio

async def save_summary(input_text, en_summary, ko_summary):
    doc = {
        "input": input_text,
        "en_summary": en_summary,
        "ko_summary": ko_summary
    }
    result = await summaries_collection.insert_one(doc)
    return str(result.inserted_id)

async def summarize_email_en_and_ko(text: str):
    """
    Summarize the input English text in both English and Korean.
    Returns both summaries regardless of input language.
    Returns error if the input is too short.
    """
    # Check if the input is empty or too short to summarize
    if not text or len(text.strip()) < 10:
        return {"error": "The input text is too short to summarize. Please enter at least 10 characters."}

    # Detect input language
    lang = detect(text)
    if lang != "en":
        return {"error": "Only English input is supported for summarization."}


    # Summarize in English using the English summarization model
    try:
        en_summary = en_summarizer(text, max_length=60, min_length=10, do_sample=False)
        en_summary_text = en_summary[0]["summary_text"]
    except Exception as e:
        en_summary_text = f"English summarization failed: {str(e)}"

    # Translate the English summary to Korean using Google Cloud Translation API
    try:
        ko_summary = translate_client.translate(en_summary_text, target_language='ko')
        ko_summary_text = ko_summary['translatedText']
    except Exception as e:
        ko_summary_text = f"Korean translation failed: {str(e)}"
    
    # Save to MongoDB
    summary_id = await save_summary(text, en_summary_text, ko_summary_text)
    
    return {
        "id": summary_id,
        "input": text,
        "en_summary": en_summary_text,
        "ko_summary": ko_summary_text
    }
