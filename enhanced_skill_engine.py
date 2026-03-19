# enhanced_skill_engine.py
# Advanced skill recommendation with complementary skills

COMPREHENSIVE_SKILLS = {
    # ========================================================================
    # META & FOUNDATIONAL SKILLS
    # ========================================================================
    "meta": [
        {
            "skill": "Learning How to Learn",
            "domain": "Meta",
            "difficulty": "Easy",
            "why": "Improves retention and long-term growth across any field",
            "duration_weeks": 2,
            "prerequisites": [],
            "complements": ["Problem Solving", "Critical Thinking"],
            "fit_score": 10,
            "risk": None
        },
        {
            "skill": "Problem Solving & Critical Thinking",
            "domain": "Meta",
            "difficulty": "Medium",
            "why": "Foundational for technical, business, and creative roles",
            "duration_weeks": 4,
            "prerequisites": [],
            "complements": ["Logic", "Data Structures", "Algorithms"],
            "fit_score": 9,
            "risk": None
        },
        {
            "skill": "Communication & Documentation",
            "domain": "Meta",
            "difficulty": "Easy",
            "why": "Essential for career growth and team collaboration",
            "duration_weeks": 3,
            "prerequisites": [],
            "complements": ["All skills"],
            "fit_score": 8,
            "risk": None
        },
        {
            "skill": "Time & Project Management",
            "domain": "Meta",
            "difficulty": "Easy",
            "why": "Helps balance learning with real life",
            "duration_weeks": 2,
            "prerequisites": [],
            "complements": ["All skills"],
            "fit_score": 7,
            "risk": None
        }
    ],

    # ========================================================================
    # PROGRAMMING & SOFTWARE ENGINEERING
    # ========================================================================
    "programming": [
        {
            "skill": "Programming Fundamentals",
            "domain": "Engineering",
            "difficulty": "Medium",
            "why": "Core skill for building software",
            "duration_weeks": 6,
            "prerequisites": [],
            "complements": ["Problem Solving", "Logic", "Debugging"],
            "fit_score": 9,
            "risk": "Can feel overwhelming if rushed"
        },
        {
            "skill": "Python Programming",
            "domain": "Engineering",
            "difficulty": "Easy-Medium",
            "why": "Most beginner-friendly language",
            "duration_weeks": 8,
            "prerequisites": ["Programming Fundamentals"],
            "complements": ["Data Science", "Automation", "Web Backend"],
            "fit_score": 9,
            "risk": None
        },
        {
            "skill": "JavaScript & Web Development",
            "domain": "Engineering",
            "difficulty": "Medium",
            "why": "Essential for web applications",
            "duration_weeks": 10,
            "prerequisites": ["Programming Fundamentals"],
            "complements": ["Frontend Design", "Backend", "Databases"],
            "fit_score": 8,
            "risk": "Large ecosystem can be overwhelming"
        },
        {
            "skill": "Data Structures",
            "domain": "Engineering",
            "difficulty": "Medium",
            "why": "Essential for efficient programming",
            "duration_weeks": 6,
            "prerequisites": ["Programming Fundamentals"],
            "complements": ["Algorithms", "System Design"],
            "fit_score": 8,
            "risk": None
        },
        {
            "skill": "Algorithms",
            "domain": "Engineering",
            "difficulty": "Hard",
            "why": "Needed for coding interviews and efficiency",
            "duration_weeks": 8,
            "prerequisites": ["Data Structures", "Problem Solving"],
            "complements": ["System Design", "Optimization"],
            "fit_score": 7,
            "risk": "Can be mathematically intensive"
        },
        {
            "skill": "Version Control (Git)",
            "domain": "Engineering",
            "difficulty": "Easy",
            "why": "Essential for professional development",
            "duration_weeks": 2,
            "prerequisites": [],
            "complements": ["All programming"],
            "fit_score": 9,
            "risk": None
        },
        {
            "skill": "Debugging & Testing",
            "domain": "Engineering",
            "difficulty": "Medium",
            "why": "Critical for quality software",
            "duration_weeks": 4,
            "prerequisites": ["Programming Fundamentals"],
            "complements": ["All programming"],
            "fit_score": 8,
            "risk": None
        },
        {
            "skill": "Code Quality & Best Practices",
            "domain": "Engineering",
            "difficulty": "Medium",
            "why": "Improves maintainability and team collaboration",
            "duration_weeks": 3,
            "prerequisites": ["Programming Fundamentals"],
            "complements": ["All programming"],
            "fit_score": 7,
            "risk": None
        }
    ],

    # ========================================================================
    # DATA & DATABASES
    # ========================================================================
    "data": [
        {
            "skill": "SQL & Databases",
            "domain": "Data",
            "difficulty": "Medium",
            "why": "Essential for data management",
            "duration_weeks": 6,
            "prerequisites": [],
            "complements": ["Backend Development", "Data Science"],
            "fit_score": 8,
            "risk": None
        },
        {
            "skill": "Data Analysis Fundamentals",
            "domain": "Data",
            "difficulty": "Easy-Medium",
            "why": "Foundation for data-driven roles",
            "duration_weeks": 4,
            "prerequisites": [],
            "complements": ["Statistics", "Machine Learning"],
            "fit_score": 7,
            "risk": None
        },
        {
            "skill": "Statistics & Probability",
            "domain": "Data",
            "difficulty": "Medium-Hard",
            "why": "Essential for data science",
            "duration_weeks": 8,
            "prerequisites": [],
            "complements": ["Data Analysis", "Machine Learning"],
            "fit_score": 7,
            "risk": "Can be mathematically intensive"
        },
        {
            "skill": "Data Visualization",
            "domain": "Data",
            "difficulty": "Easy",
            "why": "Communicate insights effectively",
            "duration_weeks": 3,
            "prerequisites": ["Data Analysis Fundamentals"],
            "complements": ["Data Science", "Business Intelligence"],
            "fit_score": 8,
            "risk": None
        }
    ],

    # ========================================================================
    # MACHINE LEARNING & AI
    # ========================================================================
    "ai_ml": [
        {
            "skill": "Machine Learning Fundamentals",
            "domain": "AI/ML",
            "difficulty": "Hard",
            "why": "Foundation for AI roles",
            "duration_weeks": 10,
            "prerequisites": ["Python Programming", "Statistics"],
            "complements": ["Deep Learning", "Data Science"],
            "fit_score": 7,
            "risk": "Mathematically intensive, steep learning curve"
        },
        {
            "skill": "Deep Learning & Neural Networks",
            "domain": "AI/ML",
            "difficulty": "Very Hard",
            "why": "Advanced AI systems",
            "duration_weeks": 12,
            "prerequisites": ["Machine Learning Fundamentals"],
            "complements": ["Computer Vision", "NLP"],
            "fit_score": 5,
            "risk": "Very steep learning curve"
        },
        {
            "skill": "Natural Language Processing",
            "domain": "AI/ML",
            "difficulty": "Hard",
            "why": "Work with language and text",
            "duration_weeks": 8,
            "prerequisites": ["Machine Learning Fundamentals"],
            "complements": ["Deep Learning", "ChatBots"],
            "fit_score": 6,
            "risk": "Complex domain"
        },
        {
            "skill": "Computer Vision",
            "domain": "AI/ML",
            "difficulty": "Hard",
            "why": "Work with images and visual data",
            "duration_weeks": 10,
            "prerequisites": ["Deep Learning"],
            "complements": ["Deep Learning"],
            "fit_score": 6,
            "risk": "Complex domain"
        }
    ],

    # ========================================================================
    # WEB & FRONTEND
    # ========================================================================
    "frontend": [
        {
            "skill": "HTML & CSS Fundamentals",
            "domain": "Frontend",
            "difficulty": "Easy",
            "why": "Foundation for web development",
            "duration_weeks": 3,
            "prerequisites": [],
            "complements": ["JavaScript", "React", "UI/UX"],
            "fit_score": 8,
            "risk": None
        },
        {
            "skill": "React & Modern Frontend",
            "domain": "Frontend",
            "difficulty": "Medium",
            "why": "Most popular frontend framework",
            "duration_weeks": 8,
            "prerequisites": ["JavaScript", "HTML & CSS"],
            "complements": ["TypeScript", "Testing", "Web Design"],
            "fit_score": 8,
            "risk": "Large ecosystem"
        },
        {
            "skill": "UI/UX Design Fundamentals",
            "domain": "Frontend",
            "difficulty": "Medium",
            "why": "Create better user experiences",
            "duration_weeks": 6,
            "prerequisites": [],
            "complements": ["Frontend Development", "Product Thinking"],
            "fit_score": 6,
            "risk": "Subjective domain"
        },
        {
            "skill": "Web Design Principles",
            "domain": "Frontend",
            "difficulty": "Easy-Medium",
            "why": "Make websites look great",
            "duration_weeks": 4,
            "prerequisites": [],
            "complements": ["Frontend Development", "UI/UX"],
            "fit_score": 6,
            "risk": None
        }
    ],

    # ========================================================================
    # BACKEND & INFRASTRUCTURE
    # ========================================================================
    "backend": [
        {
            "skill": "Backend Development (Node.js/Express)",
            "domain": "Backend",
            "difficulty": "Medium",
            "why": "Build server-side applications",
            "duration_weeks": 8,
            "prerequisites": ["JavaScript", "Databases"],
            "complements": ["Databases", "APIs", "Authentication"],
            "fit_score": 8,
            "risk": None
        },
        {
            "skill": "Backend Development (Python/Django)",
            "domain": "Backend",
            "difficulty": "Medium",
            "why": "Robust backend development",
            "duration_weeks": 8,
            "prerequisites": ["Python Programming", "Databases"],
            "complements": ["Databases", "APIs", "Testing"],
            "fit_score": 7,
            "risk": None
        },
        {
            "skill": "REST APIs & GraphQL",
            "domain": "Backend",
            "difficulty": "Medium",
            "why": "Communication between systems",
            "duration_weeks": 5,
            "prerequisites": ["Backend Development basics"],
            "complements": ["Frontend", "System Design"],
            "fit_score": 8,
            "risk": None
        },
        {
            "skill": "Authentication & Security",
            "domain": "Backend",
            "difficulty": "Medium",
            "why": "Protect applications and data",
            "duration_weeks": 4,
            "prerequisites": ["Backend Development basics"],
            "complements": ["All backend"],
            "fit_score": 8,
            "risk": None
        },
        {
            "skill": "Cloud & DevOps (AWS/Docker)",
            "domain": "Backend",
            "difficulty": "Medium-Hard",
            "why": "Deploy and manage applications",
            "duration_weeks": 10,
            "prerequisites": ["Backend Development basics"],
            "complements": ["System Design", "Scaling"],
            "fit_score": 7,
            "risk": "Large cloud ecosystem"
        },
        {
            "skill": "Microservices Architecture",
            "domain": "Backend",
            "difficulty": "Hard",
            "why": "Build scalable systems",
            "duration_weeks": 8,
            "prerequisites": ["System Design", "Backend Development"],
            "complements": ["DevOps", "System Design"],
            "fit_score": 6,
            "risk": "Complex patterns"
        }
    ],

    # ========================================================================
    # ADVANCED CONCEPTS
    # ========================================================================
    "advanced": [
        {
            "skill": "System Design",
            "domain": "Advanced",
            "difficulty": "Very Hard",
            "why": "Design large-scale systems",
            "duration_weeks": 12,
            "prerequisites": ["All backend basics", "Data Structures", "Algorithms"],
            "complements": ["Microservices", "DevOps"],
            "fit_score": 5,
            "risk": "Very steep learning curve"
        },
        {
            "skill": "Performance Optimization",
            "domain": "Advanced",
            "difficulty": "Hard",
            "why": "Make systems faster",
            "duration_weeks": 6,
            "prerequisites": ["Profiling", "Algorithms"],
            "complements": ["System Design"],
            "fit_score": 6,
            "risk": None
        },
        {
            "skill": "Database Optimization",
            "domain": "Advanced",
            "difficulty": "Hard",
            "why": "Optimize data handling",
            "duration_weeks": 6,
            "prerequisites": ["Databases", "SQL"],
            "complements": ["System Design"],
            "fit_score": 6,
            "risk": None
        },
        {
            "skill": "Cybersecurity Fundamentals",
            "domain": "Advanced",
            "difficulty": "Hard",
            "why": "Protect systems from attacks",
            "duration_weeks": 8,
            "prerequisites": ["Networking basics"],
            "complements": ["All backend"],
            "fit_score": 6,
            "risk": "Complex domain"
        }
    ]
}

# Flatten all skills for easier access
def get_all_skills():
    """Get all available skills"""
    all_skills = []
    for category, skills in COMPREHENSIVE_SKILLS.items():
        all_skills.extend(skills)
    return all_skills

# Recommend skills based on user profile
def recommend_skills_enhanced(profile, quiz_results=None):
    """
    Enhanced skill recommendation with complementary skills
    
    Args:
        profile: User profile dict with interests, background, goals, etc.
        quiz_results: Dict with quiz scores {quiz_id: score_percentage}
    
    Returns:
        {
            "primary_skills": [...],  # Top 5-7 recommended skills
            "complementary_skills": [...],  # Skills that complement primary
            "advanced_skills": [...],  # For future learning
            "reasoning": str  # Why these recommendations
        }
    """
    
    all_skills = get_all_skills()
    recommended = []
    
    interests = profile.get("interests", [])
    background = profile.get("background", "")
    goal = profile.get("primary_goal", "")
    prog_conf = profile.get("programming_skills", 5)
    math_conf = profile.get("math_skills", 5)
    consistency = profile.get("consistency", 5)
    
    # ============================================================================
    # ALWAYS RECOMMEND META SKILLS FIRST
    # ============================================================================
    meta_skills = COMPREHENSIVE_SKILLS["meta"]
    for skill in meta_skills[:2]:  # Top 2 meta skills
        recommended.append({
            **skill,
            "recommended_reason": "Foundational for all learning",
            "priority": "HIGH"
        })
    
    # ============================================================================
    # PROGRAMMING & CORE ENGINEERING
    # ============================================================================
    if "Building things from scratch" in interests or goal in ["Get a job", "Start something of my own"]:
        recommended.append({
            **get_skill_by_name("Programming Fundamentals"),
            "recommended_reason": "Core skill for building software",
            "priority": "HIGH"
        })
        
        if prog_conf >= 4:
            recommended.append({
                **get_skill_by_name("Data Structures"),
                "recommended_reason": "Essential for efficient programming",
                "priority": "HIGH"
            })
    
    # ============================================================================
    # LANGUAGE-SPECIFIC RECOMMENDATIONS
    # ============================================================================
    if "Solving complex logic problems" in interests or goal == "Build strong fundamentals":
        recommended.append({
            **get_skill_by_name("Python Programming"),
            "recommended_reason": "Excellent for logic and problem-solving",
            "priority": "HIGH"
        })
    
    # ============================================================================
    # FRONTEND/FULL-STACK
    # ============================================================================
    if "Building things from scratch" in interests or any(x in profile.get("domain_interests", []) for x in ["Web Development", "Frontend"]):
        recommended.append({
            **get_skill_by_name("HTML & CSS Fundamentals"),
            "recommended_reason": "Foundation for web applications",
            "priority": "MEDIUM"
        })
        
        if prog_conf >= 5:
            recommended.append({
                **get_skill_by_name("React & Modern Frontend"),
                "recommended_reason": "Build modern, interactive web apps",
                "priority": "MEDIUM"
            })
    
    # ============================================================================
    # DATA & ANALYTICS
    # ============================================================================
    if "Analyzing data & finding patterns" in interests or any(x in profile.get("domain_interests", []) for x in ["Data Science", "Analytics"]):
        recommended.append({
            **get_skill_by_name("SQL & Databases"),
            "recommended_reason": "Essential for data work",
            "priority": "HIGH"
        })
        
        recommended.append({
            **get_skill_by_name("Data Analysis Fundamentals"),
            "recommended_reason": "Foundation for data-driven roles",
            "priority": "HIGH"
        })
        
        if math_conf >= 6:
            recommended.append({
                **get_skill_by_name("Statistics & Probability"),
                "recommended_reason": "Essential for statistical analysis",
                "priority": "HIGH"
            })
    
    # ============================================================================
    # AI/ML
    # ============================================================================
    if "AI/ML/Deep Learning" in interests or any(x in profile.get("domain_interests", []) for x in ["AI / Machine Learning", "Data Science"]):
        if prog_conf >= 6 and math_conf >= 5:
            recommended.append({
                **get_skill_by_name("Machine Learning Fundamentals"),
                "recommended_reason": "Foundation for AI/ML careers",
                "priority": "MEDIUM"
            })
    
    # ============================================================================
    # BACKEND & DEVOPS
    # ============================================================================
    if any(x in interests for x in ["Backend/infrastructure", "DevOps/Cloud"]):
        recommended.append({
            **get_skill_by_name("Backend Development (Node.js/Express)"),
            "recommended_reason": "Build server-side systems",
            "priority": "HIGH"
        })
        
        recommended.append({
            **get_skill_by_name("Cloud & DevOps (AWS/Docker)"),
            "recommended_reason": "Deploy and manage applications",
            "priority": "MEDIUM"
        })
    
    # ============================================================================
    # COMPLEMENTARY SKILLS
    # ============================================================================
    complementary = []
    for skill in recommended:
        if "complements" in skill:
            for complement_name in skill["complements"]:
                complement_skill = get_skill_by_name(complement_name)
                if complement_skill and complement_skill not in complementary:
                    complementary.append({
                        **complement_skill,
                        "complements": skill["skill"],
                        "recommended_reason": f"Complements {skill['skill']}",
                        "priority": "MEDIUM"
                    })
    
    # ============================================================================
    # ADVANCED SKILLS FOR LATER
    # ============================================================================
    advanced = []
    if prog_conf >= 7 and consistency >= 7:
        advanced_skills_list = COMPREHENSIVE_SKILLS["advanced"][:2]
        for skill in advanced_skills_list:
            advanced.append({
                **skill,
                "recommended_reason": "Advanced path after mastering fundamentals",
                "priority": "LOW",
                "timeline": "6+ months"
            })
    
    # Create reasoning
    reasoning = f"""Based on your profile:
    - Primary goal: {goal}
    - Interests: {', '.join(interests[:3]) if interests else 'General learning'}
    - Programming confidence: {prog_conf}/10
    - Math confidence: {math_conf}/10
    - Consistency: {consistency}/10
    
    We recommend starting with foundational skills, then moving to domain-specific skills
    that align with your interests and goals.
    """
    
    return {
        "primary_skills": recommended[:5],
        "complementary_skills": complementary[:5],
        "advanced_skills": advanced,
        "total_recommendations": len(recommended) + len(complementary),
        "reasoning": reasoning
    }

def get_skill_by_name(skill_name):
    """Get a skill by its name"""
    for skill in get_all_skills():
        if skill["skill"] == skill_name:
            return skill
    return None

def get_learning_path_for_skill(skill_name):
    """Get recommended learning path for a skill"""
    skill = get_skill_by_name(skill_name)
    if not skill:
        return None
    
    return {
        "skill": skill,
        "prerequisites": skill.get("prerequisites", []),
        "estimated_duration_weeks": skill.get("duration_weeks", 8),
        "complementary": skill.get("complements", []),
        "difficulty_level": skill.get("difficulty", "Medium"),
        "risk_factors": skill.get("risk", "None")
    }

def suggest_learning_sequence(profile, selected_skill):
    """Suggest a learning sequence for a skill"""
    skill = get_skill_by_name(selected_skill)
    if not skill:
        return None
    
    sequence = []
    
    # Add prerequisites if not already learned
    learned = profile.get("skills_learned", [])
    for prereq in skill.get("prerequisites", []):
        if prereq not in learned:
            prereq_skill = get_skill_by_name(prereq)
            if prereq_skill:
                sequence.append({
                    "phase": "Prerequisites",
                    "skill": prereq_skill,
                    "duration_weeks": prereq_skill.get("duration_weeks", 4)
                })
    
    # Main skill
    sequence.append({
        "phase": "Main Learning",
        "skill": skill,
        "duration_weeks": skill.get("duration_weeks", 8)
    })
    
    # Complementary skills for depth
    for complement in skill.get("complements", [])[:2]:
        complement_skill = get_skill_by_name(complement)
        if complement_skill:
            sequence.append({
                "phase": "Complementary",
                "skill": complement_skill,
                "duration_weeks": complement_skill.get("duration_weeks", 4),
                "note": f"Enhances {skill['skill']}"
            })
    
    return {
        "main_skill": skill,
        "sequence": sequence,
        "total_duration_weeks": sum(s["duration_weeks"] for s in sequence),
        "total_duration_months": sum(s["duration_weeks"] for s in sequence) / 4
    }
