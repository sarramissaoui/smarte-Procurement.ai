def extract_keywords(tenders_cleaned):

    skill_list = [
        "python", "java", "c++", "c", "javascript",
        "machine learning", "deep learning",
        "natural language processing", "nlp",
        "computer vision", "tensorflow", "pytorch",
        "arduino", "stm32", "raspberry pi",
        "solidworks", "matlab", "sql",
        "power bi", "flask", "spring boot",
        "docker", "linux", "git"
    ]

    results = {}

    for name, text in tenders_cleaned.items():

        found_skills = []

        for skill in skill_list:
            if skill in text:
                found_skills.append(skill)

        results[name] = found_skills

    return results

def extract_skills_from_text(text, skill_list):
    """
    Extract skills found in a text based on the predefined skill_list.
    """
    found_skills = []
    for skill in skill_list:
        if skill.lower() in text.lower():
            found_skills.append(skill)
    return found_skills