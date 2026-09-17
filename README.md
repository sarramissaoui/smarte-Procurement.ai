# 🚀 smarte-Procurement.ai
## Intelligent Automation of the Tendering Process

---

# 📌 Project Overview

SmartTender AI is a mini-prototype developed for the Inetum Challenge.

It automates key steps in the tendering workflow by:
- Matching CVs with tender requirements
- Generating HR-ready evaluation reports

The system reduces manual effort, improves accuracy, and accelerates decision-making.

---

# 🎯 Implemented Modules

## 1️⃣ CV ↔ Tender Matching

- Skill extraction using a predefined skill dictionary
- Text preprocessing (lowercasing, stopwords removal, cleaning)
- Match score computation (%)
- Identification of missing skills
- Identification of extra skills

## 2️⃣ AI-Assisted Document Generation

- Automatic generation of stylish PDF reports
- Match score percentage visualization
- Color-coded missing and extra skills
- HR-ready summary and recommendation

---

# 🏗️ System Flow

CV & Tender PDFs  
→ Text Extraction  
→ Preprocessing  
→ Skill Extraction  
→ Matching Engine  
→ PDF Report Generation  
→ HR Decision Support  

---

# ⚙️ Technologies Used

- Python
- NLTK
- FPDF
- scikit-learn (optional experimentation)

---

# 🚀 How to Run the Project

1. Clone the repository
2. Navigate to the project folder
3. Install dependencies
4. Run main.py

Example:

git clone https://github.com/yourusername/smarttender-ai.git  
cd smarttender-ai  
pip install -r requirements.txt  
python main.py  

Generated reports will appear in the:

reports_stylish/

---

# ⚠️ Limitations

- Skill extraction is dictionary-based
- Matching is rule-based (not semantic yet)
- Works only with PDF inputs
- No live tender scraping implemented

---

# 🔮 Future Improvements

- Add semantic matching using embeddings (BERT / Sentence Transformers)
- Implement smart tender detection via web scraping
- Add a web interface (Streamlit / Flask)
- Support multi-candidate ranking dashboard
- Improve scalability and automation

---

# 🏆 Challenge Context

Developed for the SmartTender AI Challenge  
Organized by AI 4 LIFE team 
