import os, re
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def blind_resume(resume: str) -> str:
    # Remove identifying info for blind screening
    prompt = f"""Remove all personally identifying information from this resume.
Remove: full name, email, phone, LinkedIn URL, address, photo references.
Keep: skills, experience, education institution names, job titles, achievements.
Return only the cleaned resume text.

Resume:
{resume}"""
    res = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=800,
    )
    return res.choices[0].message.content

def screen_resume(resume: str, job_description: str, blind: bool = False) -> dict:
    resume_text = blind_resume(resume) if blind else resume
    prompt = f"""You are an expert HR recruiter. Screen this resume against the job description.

Job Description:
{job_description}

Resume:
{resume_text}

Provide your assessment in EXACTLY this format:
DECISION: SHORTLIST or REJECT
SCORE: [0-100]
STRENGTHS: [list 3 key strengths]
WEAKNESSES: [list 3 key gaps]
SUMMARY: [2 sentence summary]"""

    res = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500,
    )
    return parse_screening(res.choices[0].message.content)

def parse_screening(text: str) -> dict:
    result = {"raw": text, "decision": "UNKNOWN", "score": 0}
    for line in text.split("\n"):
        if "DECISION:" in line:
            result["decision"] = "SHORTLIST" if "SHORTLIST" in line else "REJECT"
        elif "SCORE:" in line:
            nums = re.findall(r'\d+', line)
            if nums: result["score"] = int(nums[0])
    return result