import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

BIAS_TYPES = [
    "gender bias",
    "age bias",
    "name or nationality bias",
    "university prestige bias",
    "employment gap bias",
]

def detect_bias(resume: str, decision: str, score: int) -> dict:
    prompt = f"""You are an AI ethics auditor reviewing a hiring decision for bias.

Resume:
{resume}

Screening Decision: {decision} (Score: {score}/100)

Check for these bias types: {', '.join(BIAS_TYPES)}

For each bias type, determine if it may have influenced this decision.
Reply in EXACTLY this format:
GENDER_BIAS: YES or NO - reason
AGE_BIAS: YES or NO - reason
NAME_BIAS: YES or NO - reason
UNIVERSITY_BIAS: YES or NO - reason
GAP_BIAS: YES or NO - reason
OVERALL_BIAS_RISK: LOW or MEDIUM or HIGH
RECOMMENDATION: one sentence"""

    res = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=400,
    )
    return parse_bias(res.choices[0].message.content)

def parse_bias(text: str) -> dict:
    result = {"raw": text, "risk": "UNKNOWN", "flags": []}
    for line in text.split("\n"):
        if "YES" in line and "BIAS:" in line:
            result["flags"].append(line.split(":")[0].strip())
        if "OVERALL_BIAS_RISK:" in line:
            if "HIGH" in line: result["risk"] = "HIGH"
            elif "MEDIUM" in line: result["risk"] = "MEDIUM"
            else: result["risk"] = "LOW"
    return result