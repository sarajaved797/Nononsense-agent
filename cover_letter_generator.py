import pandas as pd

def generate_cover_letters(jobs_df, resume_text):
    # Just add a dummy cover letter to every job so app works without OpenAI
    jobs_df["cover_letter"] = jobs_df.apply(
        lambda row: f"Cover letter for {row['job_title']} at {row['company_name']}: This is a placeholder letter.",
        axis=1
    )
    return jobs_df
