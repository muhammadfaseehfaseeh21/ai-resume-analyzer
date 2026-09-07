"""
Core business logic for interacting with Google Gemini API.
"""

import os
import google.generativeai as genai
from prompts import RESUME_ANALYSIS_PROMPT, RESUME_TAILORING_PROMPT

def configure_gemini(api_key: str = None):
    """Configure Gemini API with key from parameter or environment."""
    key = api_key or os.getenv("GEMINI_API_KEY")
    if not key:
        raise ValueError("Gemini API key is required. Provide it via UI or set GEMINI_API_KEY in environment.")
    genai.configure(api_key=key)

def analyze_resume(resume_text: str, job_description: str, api_key: str = None, model_name: str = "gemini-3.8-flash") -> str:
    """
    Analyzes resume against job description and returns detailed feedback.
    """
    configure_gemini(api_key)
    model = genai.GenerativeModel(model_name)
    
    prompt = RESUME_ANALYSIS_PROMPT.format(
        resume_text=resume_text,
        job_description=job_description
    )
    
    response = model.generate_content(prompt)
    return response.text

def generate_tailored_resume(resume_text: str, job_description: str, api_key: str = None, model_name: str = "gemini-1.5-flash") -> str:
    """
    Generates tailored bullet points and suggestions for resume improvement.
    """
    configure_gemini(api_key)
    model = genai.GenerativeModel(model_name)
    
    prompt = RESUME_TAILORING_PROMPT.format(
        resume_text=resume_text,
        job_description=job_description
    )
    
    response = model.generate_content(prompt)
    return response.text
