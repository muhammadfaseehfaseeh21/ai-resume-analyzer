# 📄 AI Resume Analyzer & Job Matcher

An end-to-end Python application using Streamlit and Google Gemini API to analyze resumes against job descriptions, output match scores, detect skill gaps, and provide tailored resume rewrites.

## 📁 Project Structure

```text
.
├── app.py              # Streamlit web user interface
├── analyzer.py         # Gemini API integration logic
├── resume_parser.py    # Multi-format document parser (PDF, DOCX, TXT)
├── prompts.py          # Prompt engineering templates
├── requirements.txt    # Project dependencies
├── .env.example        # Environment variable sample file
├── .gitignore          # Git ignore configuration
└── README.md           # Documentation
```

## 🚀 Quickstart Guide

### 1. Clone & Set Up Environment
```bash
# Set up virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configure API Key
Create a `.env` file from `.env.example`:
```bash
cp .env.example .env
```
Edit `.env` and insert your Google Gemini API key:
```env
GEMINI_API_KEY=your_actual_gemini_api_key
```
*(Alternatively, you can enter your key directly in the Streamlit web sidebar).*

### 3. Run the Streamlit App
```bash
streamlit run app.py
```

## 🛠️ Tech Stack
- **UI Framework**: Streamlit
- **LLM Engine**: Google Gemini API (`google-generativeai`)
- **Parsers**: `pypdf`, `python-docx`
- **Environment Management**: `python-dotenv`
