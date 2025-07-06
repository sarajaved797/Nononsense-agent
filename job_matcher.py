import pandas as pd

def get_job_matches(jobs_df, resume_text):
    def score_keywords(description, resume):
        keywords = ["Excel", "SQL", "report", "clean", "data", "pandas", "dashboard"]
        score = sum(1 for kw in keywords if kw.lower() in description.lower() and kw.lower() in resume.lower())
        return score

    jobs_df["keyword_score"] = jobs_df["job_description"].apply(lambda desc: score_keywords(desc, resume_text))
    jobs_df["gpt_score"] = 3 + jobs_df["keyword_score"] * 1.5  # Placeholder logic
    return jobs_df