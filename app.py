import streamlit as st
import pandas as pd
import os
from dotenv import load_dotenv

from job_matcher import get_job_matches
from cover_letter_generator import generate_cover_letters
from job_tracker import build_job_tracker

load_dotenv()

st.set_page_config(page_title="Nononsense Agent", layout="wide")

# 🧠 Title & Description
st.markdown("""
<style>
.big-title {
    font-size:48px !important;
    font-weight:800;
    color:#2e8b57;
    font-family: 'Segoe UI', sans-serif;
}
.small-note {
    font-size:16px;
    color: #666;
}
.block {
    padding: 1.2rem;
    background-color: #f9f9f9;
    border-radius: 0.5rem;
    border: 1px solid #ddd;
    margin-bottom: 1rem;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="big-title">🤖 Nononsense Job Agent</div>', unsafe_allow_html=True)
st.markdown('<div class="small-note">Upload your resume and job listings — get match scores and personalized cover letters in one click.</div>', unsafe_allow_html=True)
st.markdown('<div class="block">', unsafe_allow_html=True)

# 🗂 Uploaders
st.subheader("📄 Upload Files")

resume_file = st.file_uploader("Upload your resume (.txt)", type=["txt"], key="resume")
jobs_file = st.file_uploader("Upload job listings (.csv)", type=["csv"], key="jobs")


st.markdown('</div>', unsafe_allow_html=True)


if resume_file and jobs_file:
    resume_text = resume_file.read().decode("utf-8")
    jobs_df = pd.read_csv(jobs_file)

    with st.spinner("🤔 Scoring job matches..."):
        scored_df = get_job_matches(jobs_df, resume_text)

    with st.spinner("✍️ Generating cover letters..."):
        result_df = generate_cover_letters(scored_df, resume_text)

    st.success("✅ All done! Scroll down to view your results.")
    st.subheader("📊 Job Matches")
    st.dataframe(result_df[["job_title", "company_name", "keyword_score", "gpt_score"]])

    if st.checkbox("Show cover letters"):
        for _, row in result_df.iterrows():
            st.markdown(f"### {row['job_title']} at {row['company_name']}")
            st.markdown(row['cover_letter'])
            st.markdown("---")
    build_job_tracker(result_df)
    with open("output/job_tracker.xlsx", "rb") as f:
        st.download_button("📥 Download Excel Tracker", f, file_name="job_tracker.xlsx")
else:
    st.info("👆 Upload both your resume and job listings to begin.")