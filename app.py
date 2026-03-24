import os
from screener import screen_resume
from bias_detector import detect_bias

def load_file(path: str) -> str:
    with open(path, "r") as f:
        return f.read()

def main():
    print("\n=== Resume Screener + Bias Detector ===")
    print("1. Screen a resume")
    print("2. Screen with blind mode (removes name/identity)")
    mode = input("\nChoose mode (1 or 2): ").strip()
    blind = mode == "2"

    resume_path = input("Path to resume .txt file (or press Enter for sample): ").strip()
    jd_path = input("Path to job description .txt file (or press Enter for sample): ").strip()

    resume = load_file(resume_path if resume_path else "sample_resume.txt")
    jd = load_file(jd_path if jd_path else "sample_jd.txt")

    print(f"\nMode: {'BLIND' if blind else 'STANDARD'}")
    print("\nScreening resume...")
    screening = screen_resume(resume, jd, blind=blind)

    print("\n--- SCREENING RESULT ---")
    print(f"Decision: {screening['decision']}")
    print(f"Match Score: {screening['score']}/100")
    print("\nFull Assessment:")
    print(screening["raw"])

    print("\nChecking for bias...")
    bias = detect_bias(resume, screening["decision"], screening["score"])

    print("\n--- BIAS AUDIT ---")
    print(f"Overall Bias Risk: {bias['risk']}")
    if bias["flags"]:
        print(f"Bias Flags: {', '.join(bias['flags'])}")
    else:
        print("No bias flags detected")
    print("\nFull Bias Report:")
    print(bias["raw"])

if __name__ == "__main__":
    main()