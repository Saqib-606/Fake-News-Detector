# 📰 Fake News Detector (Python – OOP Based)

A Python-based Fake News Detection system that evaluates the credibility of news articles using **source credibility analysis**, **keyword detection**, and **sensational content analysis**, designed with strong **Object-Oriented Programming (OOP)** principles.

---

## 📌 Project Overview

Fake news spreads rapidly through digital platforms and can manipulate public opinion.  
This project aims to **analyze news articles** and determine whether the content is:

- ✅ Likely Real  
- ⚠️ Suspicious  
- ❌ Likely Fake  

The system evaluates news based on **text quality**, **sensational language**, and **source reliability**.

---

## ⚙️ Key Features

- 📚 Structured using Object-Oriented Programming (OOP)
- 🏷️ Source credibility checking (Trusted, Neutral, Blacklisted, Unknown)
- 🔍 Keyword-based fake news indicators
- 😱 Sensational & emotional language detection
- 📊 Final credibility score & verdict
- 🖥️ Console-based interactive system

---

## 🧠 Core Components (Classes)

### 1️⃣ `NewsArticle`
Stores all news-related data:
- Title
- Full content
- Source name
- Publish date
- Author

---

### 2️⃣ `Source`
Evaluates the credibility of news sources:
- Trusted sources
- Neutral sources
- Blacklisted sources
- Unknown sources

Each category contributes a predefined credibility score.

---

### 3️⃣ `KeywordEngine`
Detects:
- Clickbait keywords
- Conspiracy-related terms
- Urgency-based manipulation phrases

Returns a keyword suspicion score and detected keywords.

---

### 4️⃣ `SensationDetector`
Analyzes sensational content using:
- Emotional language detection
- Excessive punctuation
- Overuse of capital letters
- Shock / fear / anger indicators

---

### 5️⃣ `TextAnalyzer`
Combines keyword and sensation analysis to:
- Evaluate content quality
- Detect manipulation tactics
- Generate issues and deduct credibility score

---

### 6️⃣ `CredibilityEngine`
Final decision engine that:
- Combines source score + text score
- Generates final credibility score
- Classifies news as Real, Suspicious, or Fake

---

## ▶️ How to Run the Project

### 🔹 Requirements
- Python 3.x

### 🔹 Steps
1. Clone the repository or download the `.py` file
2. Open terminal / command prompt
3. Run the file:

```bash
python FakeNewsDetector.py

