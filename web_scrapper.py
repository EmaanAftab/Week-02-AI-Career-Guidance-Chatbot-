"""
web_scraper.py
───────────────
Step 1: AI Career Guidance Chatbot Dataset Creator
"""

import requests
from bs4 import BeautifulSoup

# ─── Selected Career / AI / Learning Sources ────────────────────────────────
urls = [
    "https://www.geeksforgeeks.org/career-options-in-artificial-intelligence/",
    "https://www.geeksforgeeks.org/machine-learning/",
    "https://www.geeksforgeeks.org/data-science-tutorial/",
    "https://www.geeksforgeeks.org/what-is-python/",
    "https://www.ibm.com/topics/artificial-intelligence",
    "https://www.coursera.org/articles/what-is-data-science",
    "https://www.edx.org/learn/artificial-intelligence",
    "https://en.wikipedia.org/wiki/Artificial_intelligence"
]

# ─── Headers (browser-like request) ─────────────────────────────────────────
headers = {
    "User-Agent": "Mozilla/5.0"
}

# ─── Final dataset container ────────────────────────────────────────────────
all_text = ""

# Words to remove noisy content
ignore_words = [
    "cookie", "subscribe", "advertisement",
    "sign up", "course", "refund"
]

# ─── Scraping loop ──────────────────────────────────────────────────────────
for url in urls:
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        # Extract paragraphs
        paragraphs = soup.find_all("p")

        page_text = " ".join(p.get_text(" ", strip=True) for p in paragraphs)

        # Clean unwanted sentences
        clean_sentences = []

        for sentence in page_text.split("."):
            sentence = sentence.strip().lower()

            if sentence and not any(word in sentence for word in ignore_words):
                clean_sentences.append(sentence)

        page_text = ". ".join(clean_sentences)

        all_text += page_text + "\n\n"

        print("Scraped successfully:", url)

    except Exception as e:
        print("Failed:", url, "| Error:", e)

# ─── Save dataset ───────────────────────────────────────────────────────────
with open("training_data.txt", "w", encoding="utf-8") as file:
    file.write(all_text)

print("\nDONE!")
print("Total characters collected:", len(all_text))