from extract_pdf import extract_text_from_folder
from preprocess import preprocess_text
from keywords import extract_keywords, extract_skills_from_text
from matching import compute_match
from report import generate_report


cv_folder = "CV_pdf/"  
tender_folder = "tenders_pdf_tenders/"  


cv_texts = extract_text_from_folder(cv_folder)
cv_cleaned = {name: preprocess_text(text) for name, text in cv_texts.items()}
cv_skills = {name: extract_keywords({name: text})[name] for name, text in cv_cleaned.items()}


tender_texts = extract_text_from_folder(tender_folder)
tender_cleaned = {name: preprocess_text(text) for name, text in tender_texts.items()}
skill_list = [
    "python", "java", "c++", "c", "javascript",
    "machine learning", "deep learning", "natural language processing",
    "nlp", "computer vision", "tensorflow", "pytorch",
    "arduino", "stm32", "raspberry pi", "solidworks",
    "matlab", "sql", "power bi", "flask", "spring boot",
    "docker", "linux", "git"
]
tender_skills = {name: extract_skills_from_text(text, skill_list) for name, text in tender_cleaned.items()}


for cv_name, skills in cv_skills.items():
    for tender_name, t_skills in tender_skills.items():
        score, missing, extra = compute_match(skills, t_skills)
        print(f"\nCV: {cv_name} ↔ Tender: {tender_name}")
        print(f"Match Score: {score}%")
        print(f"Missing Skills: {missing}")
        print(f"Extra Skills: {extra}")
        
     
        generate_report(cv_name, tender_name, score, missing, extra)