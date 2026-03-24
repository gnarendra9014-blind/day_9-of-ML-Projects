# Day 9: AI Resume Screener & Bias Detector 🚀

Welcome to Day 9 of the **25 Days of ML Projects**. This project features a sophisticated, AI-driven recruitment tool that goes beyond automated screening by incorporating an **Ethical Bias Audit** for every decision.

## 🌟 Key Features

- **Match Scoring (0-100)**: Instantly assess the compatibility of a resume with a specific job description.
- **Deep Assessment**: Analyzes key strengths, weaknesses, and gaps in a candidate's profile.
- **Blind Screening Mode**: Anonymizes resumes before screening to eliminate unconscious bias from the AI's initial evaluation.
- **AI Ethics Audit**: Automatically audits the screening results for various bias types:
  - Gender Bias
  - Age Bias
  - Name or Nationality Bias
  - University Prestige Bias
  - Employment Gap Bias

## 🛠️ Technology Stack

- **Core**: Python 3.x
- **LLM API**: [Groq Cloud](https://groq.com/) for lightning-fast inference.
- **Models**: 
  - `llama-3.3-70b-versatile` (Screening & Bias Audit)
  - `llama-3.1-8b-instant` (Anonymization)
- **Environment**: `python-dotenv` for managing API keys.

## 🚀 Getting Started

### 1. Prerequisites
- Python 3.9+ installed.
- A Groq Cloud API Key (Get one at [console.groq.com](https://console.groq.com/)).

### 2. Installation
1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/gnarendra9014-blind/day_9-of-ML-Projects.git
   cd day9-resume-screener
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # Windows
   # source venv/bin/activate  # Mac/Linux
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### 3. Setup Your API Key
1. Create a `.env` file in the root directory (or rename `.env.example`).
2. Add your Groq API Key:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   ```

## 🎮 How to Run

Execute the main application:
```bash
python app.py
```

### Modes:
1. **Standard Mode**: Screens the resume as-is.
2. **Blind Mode**: The AI first processes the resume to remove names, email addresses, and other identifiers before starting the evaluation, ensuring a more objective score.

## 📁 Project Structure

- `app.py`: The CLI handler for the application.
- `screener.py`: Handles resume-to-JD matching and anonymization.
- `bias_detector.py`: Performs ethical audits on screening decisions.
- `sample_resume.txt` / `sample_jd.txt`: Example files to get you started.

---
*Developed as part of the 25 Days of ML Projects challenge.*