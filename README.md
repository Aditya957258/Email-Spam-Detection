# 📧 Email Fraud Detection using Naive Bayes

## 📘 Project Description

This project aims to detect **fraudulent (spam)** emails using machine learning, specifically the **Naive Bayes classifier**. By analyzing the content of emails, the model predicts whether a message is **spam** or **not spam (ham)**, helping to automate email filtering and improve inbox security.

---

## 🎯 Objectives

- Automatically classify emails as spam or not spam.
- Improve email security using natural language processing (NLP).
- Build a lightweight, efficient, and accurate machine learning model for text classification.

---

## 🧰 Tech Stack & Tools

- **Programming Language**: Python  
- **Libraries**:  
  - `scikit-learn` – Machine learning & Naive Bayes  
  - `pandas`, `numpy` – Data handling  
  - `re`, `NLTK` – Text preprocessing  
  - `matplotlib`, `seaborn` – Visualization

---

## 📂 Project Structure


---

## 📊 Dataset Information

- **Dataset Used**: SMS Spam Collection  
- **Source**: UCI Machine Learning Repository  
- **Format**:  
  - `label`: Indicates "spam" or "ham"  
  - `message`: The actual email or SMS content

---

## 🔄 How It Works

1. **Preprocessing**: Clean and normalize text (lowercase, remove punctuation, stopwords).
2. **Feature Extraction**: Convert text to numeric features using CountVectorizer or TF-IDF.
3. **Model Training**: Train a **Multinomial Naive Bayes** classifier.
4. **Prediction**: Classify new messages as spam or ham.
5. **Evaluation**: Measure model performance using accuracy, precision, recall, and F1-score.

---

## 🚀 How to Run the Project

### 🔧 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/username/email-fraud-detection.git
   cd email-fraud-detection
