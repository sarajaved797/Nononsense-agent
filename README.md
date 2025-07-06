# 🧰 Nononsense Agent  
**Your no-BS job application assistant**

A lightweight AI agent to help job seekers:

✅ Filter job listings based on resume + preferences  
✅ Score best matches (with keywords + GPT-style logic)  
✅ Auto-draft tailored cover letters *(mocked — no key required)*  
✅ Export everything into a clean Excel tracker  

> Built by a real human to cut through job-hunt fog — fast, focused, and fluff-free.

---

## ⚡ Why This Exists

Job hunting shouldn’t feel like a full-time job — especially when:

- Listings are vague, repetitive, or spammy  
- You rewrite the same cover letter 10 times  
- You’re tracking 20+ roles across tabs, notes, and screenshots  

**Nononsense Agent** was built to solve the exact burnout I faced while job searching.  
If it’s helping me, it might help you too.

---

## 🧠 What It Does

1. Loads your resume (`.txt`) and job descriptions (`.csv`)
2. Scores match quality using real keyword logic
3. Generates short, job-specific cover letters (mocked for now — works without API key)
4. Writes everything to an Excel tracker with links, scores, and content

---

## 🛠️ How to Run It (Locally)

```bash
git clone https://github.com/yourusername/nononsense-agent.git
cd nononsense-agent
pip install -r requirements.txt
streamlit run app.py
