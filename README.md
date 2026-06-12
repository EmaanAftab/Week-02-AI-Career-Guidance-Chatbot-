# 🤖 AI Career Guidance Chatbot

## 📌 Overview
This project is an AI-based Career Guidance Chatbot built using Python and Streamlit.  
It helps students get information about AI, Machine Learning, Python, Data Science, and career paths.

The chatbot uses **web scraping** to collect educational content from multiple websites and then provides answers based on that dataset.


## 🚀 Features
- 🌐 Web scraping from educational websites
- 📚 Dataset creation from real online sources
- 🤖 Simple AI-based question answering system
- 💬 Interactive Streamlit web interface
- ⚡ Fast keyword-based response system
- 🎯 Career guidance support for students


## Technologies Used
- Python 🐍
- Streamlit 
- BeautifulSoup (bs4)
- Requests
- Regular Expressions (re)


## Project Structure
AI-Career-Guidance-Chatbot/
│
├── app.py # Streamlit chatbot UI
├── web_scraper.py # Web scraping script
├── training_data.txt # Collected dataset
├── README.md # Project documentation


## How It Works

### Data Collection
- Scrapes text from AI & career-related websites
- Extracts useful paragraphs
- Stores cleaned data in `training_data.txt`

### Processing
- Splits text into sentences
- Matches user input with dataset keywords
- Finds most relevant answers

### Output
- Displays relevant information in chatbot format


## How to Run

### Step 1: Install dependencies
```bash
- pip install streamlit requests beautifulsoup4

### Step 2: Run scraper
- python web_scraper.py

### Step 3: Run chatbot
- streamlit run app.py


## Limitations
- Does not use a deep learning model
- Works on keyword matching
- Depends on scraped data quality

## Future Improvements
- Add real AI/ML model (NLP or Transformers)
- Improve chatbot intelligence
- Add ChatGPT-style UI
- Deploy online (Streamlit Cloud)

## Author

- Student Project – AI Career Guidance Chatbot
- Built for learning purposes (AI + Web Scraping + Streamlit)