"""
Module for extracting text from resume files (PDF, DOCX, TXT).
"""

import io
from pypdf import PdfReader
import docx

def parse_pdf(file_bytes: bytes) -> str:
    """Extract text from a PDF file."""
    text = ""
    pdf_file = io.BytesIO(file_bytes)
    reader = PdfReader(pdf_file)
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"
    return text.strip()

def parse_docx(file_bytes: bytes) -> str:
    """Extract text from a DOCX file."""
    docx_file = io.BytesIO(file_bytes)
    doc = docx.Document(docx_file)
    full_text = [paragraph.text for paragraph in doc.paragraphs if paragraph.text.strip()]
    return "\n".join(full_text).strip()

def parse_txt(file_bytes: bytes) -> str:
    """Extract text from a plain TXT file."""
    return file_bytes.decode("utf-8", errors="ignore").strip()

def extract_text_from_file(uploaded_file) -> str:
    """
    Main parser router based on file extension.
    """
    filename = uploaded_file.name.lower()
    file_bytes = uploaded_file.read()
    
    if filename.endswith(".pdf"):
        return parse_pdf(file_bytes)
    elif filename.endswith(".docx"):
        return parse_docx(file_bytes)
    elif filename.endswith(".txt"):
        return parse_txt(file_bytes)
    else:
        raise ValueError("Unsupported file format. Please upload a PDF, DOCX, or TXT file.")
