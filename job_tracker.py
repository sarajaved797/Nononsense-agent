import pandas as pd

def build_job_tracker(jobs_df):
    output_df = jobs_df[["job_title", "company_name", "keyword_score", "gpt_score", "cover_letter"]]
    output_df.to_excel("output/job_tracker.xlsx", index=False)