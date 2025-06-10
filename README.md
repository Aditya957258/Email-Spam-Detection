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
# Advanced Data Visualization Dashboard

![Dashboard Screenshot](https://via.placeholder.com/800x500.png?text=Data+Visualization+Dashboard)

An interactive dashboard featuring multiple data visualization charts built with D3.js and Chart.js, designed for responsive and insightful data analysis.

## Features

- **Interactive Bar Chart**: Visualize quarterly performance metrics with toggle between revenue and growth views
- **Dynamic Pie Chart**: Display market distribution with percentage or absolute value options
- **Customizable Scatter Plot**: Analyze customer data by age or income dimensions
- **Responsive Design**: Adapts to different screen sizes for optimal viewing
- **Interactive Elements**: 
  - Hover tooltips for detailed data inspection
  - Legend displays with color coding
  - Dynamic metric selection

## Technologies Used

- **D3.js** (v7) - For custom bar charts and scatter plots
- **Chart.js** - For interactive pie/doughnut charts
- **Vanilla JavaScript** - For all interactivity and logic
- **CSS3** - Modern styling with CSS variables and responsive grid
- **HTML5** - Semantic structure

## Installation

No installation required - this is a client-side only application. Simply:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/data-visualization-dashboard.git
