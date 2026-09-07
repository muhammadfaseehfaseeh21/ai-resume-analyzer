"""
Prompt templates for the AI Resume Analyzer powered by Gemini.
"""

RESUME_ANALYSIS_PROMPT = """
You are an expert ATS (Applicant Tracking System) specialist and senior technical recruiter. 
Analyze the provided resume against the given Job Description (JD).

### Resume Text:
{resume_text}

### Job Description:
{job_description}

### Task:
Provide a comprehensive evaluation structured in the following JSON-like key sections (use clean Markdown formatting with clear headers, bold text, bullet points, and tables):

1. **Overall Match Percentage & Summary**:
   - Provide an estimated Match Score (0-100%).
   - Write a 2-3 sentence executive summary of the candidate's fit.

2. **Key Strengths & Matched Qualifications**:
   - List key skills, experiences, and qualifications from the resume that directly match the JD.

3. **Gaps & Missing Skills**:
   - Identify critical skills, tools, certifications, or experience requirements mentioned in the JD that are missing or weak in the resume.

4. **Detailed Section-by-Section Feedback**:
   - **Work Experience**: Impact, metrics, action verbs.
   - **Skills**: Relevance, depth, organization.
   - **Education & Certifications**: Alignment with requirements.

5. **Actionable Recommendations for Resume Optimization**:
   - Specific bullet points to rewrite using the STAR method (Situation, Task, Action, Result).
   - Recommended keywords to add for ATS optimization.
"""

RESUME_TAILORING_PROMPT = """
You are a professional resume writer. Rewrite and tailor the following resume sections specifically to target the provided Job Description.

### Original Resume Text:
{resume_text}

### Job Description:
{job_description}

### Task:
Generate an optimized, ATS-friendly version of the resume bullet points and summary:
1. **Professional Summary**: A compelling summary customized for this role.
2. **Key Skills Section**: Categorized into Technical and Soft Skills aligned with JD keywords.
3. **Optimized Experience Bullets**: Rewrite key bullet points using strong action verbs and quantitative metrics wherever plausible.
"""
