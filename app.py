"""
Streamlit Web Application UI for AI Resume Analyzer & Matcher.
"""

import streamlit as st
import os
from dotenv import load_dotenv
from resume_parser import extract_text_from_file
from analyzer import analyze_resume, generate_tailored_resume

# Load environment variables
load_dotenv()

st.set_page_config(
    page_title="AI Resume Analyzer & Job Matcher",
    page_icon="📄",
    layout="wide",
)

st.title("📄 AI Resume Analyzer & Job Matcher")
st.markdown("Upload your resume and paste a job description to get an instant ATS analysis, match score, and personalized resume tailoring tips.")

# Sidebar - Settings
st.sidebar.header("⚙️ Configuration")
env_api_key = os.getenv("GEMINI_API_KEY", "")
user_api_key = st.sidebar.text_input("Gemini API Key", value=env_api_key, type="password", help="Enter your Google Gemini API key.")

model_choice = st.sidebar.selectbox(
    "Select Model",["gemini-1.5-flash"]
    index=0
)

# Main UI Layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("1. Upload Resume")
    uploaded_file = st.file_uploader("Upload PDF, DOCX, or TXT file", type=["pdf", "docx", "txt"])
    
    resume_text = ""
    if uploaded_file is not None:
        try:
            resume_text = extract_text_from_file(uploaded_file)
            st.success(f"Successfully loaded {uploaded_file.name}")
            with st.expander("Preview Extracted Resume Text"):
                st.text_area("Resume Content", resume_text, height=200, disabled=True)
        except Exception as e:
            st.error(f"Error reading file: {e}")

with col2:
    st.subheader("2. Job Description")
    job_description = st.text_area("Paste the target Job Description (JD) here", height=250, placeholder="Paste JD requirements, skills, and responsibilities...")

st.markdown("---")

# Action Buttons
btn_col1, btn_col2 = st.columns(2)

with btn_col1:
    analyze_btn = st.button("🔍 Analyze Match & Get Feedback", type="primary", use_container_width=True)

with btn_col2:
    tailor_btn = st.button("✨ Generate Tailored Resume Suggestions", use_container_width=True)

# Execution logic
if analyze_btn:
    if not user_api_key:
        st.error("Please provide a Gemini API key in the sidebar.")
    elif not resume_text:
        st.warning("Please upload a resume file first.")
    elif not job_description.strip():
        st.warning("Please enter a job description.")
    else:
        with st.spinner("Analyzing resume against job description..."):
            try:
                analysis = analyze_resume(resume_text, job_description, api_key=user_api_key, model_name=model_choice)
                st.subheader("📊 Analysis Results")
                st.markdown(analysis)
            except Exception as e:
                st.error(f"Analysis failed: {e}")

if tailor_btn:
    if not user_api_key:
        st.error("Please provide a Gemini API key in the sidebar.")
    elif not resume_text:
        st.warning("Please upload a resume file first.")
    elif not job_description.strip():
        st.warning("Please enter a job description.")
    else:
        with st.spinner("Generating tailored bullet points & suggestions..."):
            try:
                tailored = generate_tailored_resume(resume_text, job_description, api_key=user_api_key, model_name=model_choice)
                st.subheader("✨ Tailored Resume Output")
                st.markdown(tailored)
            except Exception as e:
                st.error(f"Tailoring failed: {e}")
