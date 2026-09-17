def compute_match(cv_skills, tender_skills):
    """
    Computes match percentage and highlights missing/extra skills.
    """
    cv_set = set(cv_skills)
    tender_set = set(tender_skills)
    
    match_count = len(cv_set.intersection(tender_set))
    total_required = len(tender_set)
    
    match_score = int((match_count / total_required) * 100) if total_required else 0
    
    missing = list(tender_set - cv_set)
    extra = list(cv_set - tender_set)
    
    return match_score, missing, extra