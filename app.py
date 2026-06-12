import streamlit as st
import re

# ─── Load Dataset ─────────────────────────────────────────────
with open("training_data.txt", "r", encoding="utf-8") as f:
    raw_data = f.read().lower()

# Split into sentences once (important for performance)
sentences = raw_data.split(".")

# ─── Page Setup ───────────────────────────────────────────────
st.set_page_config(page_title="AI Career Chatbot", page_icon="🤖")

st.title("🤖 AI Career Guidance Chatbot")
st.write("Ask questions about AI, Machine Learning, Python, Data Science")

# ─── Input ────────────────────────────────────────────────────
user_input = st.text_input("Enter your question")

# ─── CLEAN FUNCTION ───────────────────────────────────────────
def clean(text):
    return re.sub(r"[^a-zA-Z ]", "", text.lower()).strip()

# ─── SMART ANSWER ENGINE ──────────────────────────────────────
def get_answer(query):
    query = clean(query)
    query_words = query.split()

    scored = []

    for s in sentences:
        s_clean = clean(s)

        # ignore useless/short sentences
        if len(s_clean) < 60:
            continue

        # count matches
        match_count = 0
        for w in query_words:
            if w in s_clean:
                match_count += 1

        # strong match rule
        if match_count >= 2:
            score = match_count / len(s_clean.split())
            scored.append((score, s.strip()))

    # sort best results
    scored.sort(reverse=True, key=lambda x: x[0])

    top = [x[1] for x in scored[:3]]

    if top:
        return "\n\n".join(top)

    return "No exact match found. Try: What is AI, Machine Learning, Python, Data Science."

# ─── OUTPUT ───────────────────────────────────────────────────
if user_input:
    answer = get_answer(user_input)

    st.success(answer)

    st.markdown("---")
    st.caption("AI Career Chatbot • Smart Search Version")