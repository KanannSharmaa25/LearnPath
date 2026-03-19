# expanded_questions.py
# Comprehensive multi-level assessment system

EXPANDED_ASSESSMENT_LEVELS = {
    
    # ========================================================================
    # LEVEL 1: BASIC BACKGROUND
    # ========================================================================
    "level_1_background": {
        "title": "Your Background & Journey",
        "icon": "🎓",
        "description": "Let's start with understanding who you are",
        "questions": [
            {
                "key": "role",
                "question": "What's your current role?",
                "type": "single",
                "options": [
                    "Student (High School)",
                    "Student (Undergraduate)",
                    "Student (Graduate)",
                    "Working Professional",
                    "Career Switcher",
                    "Self-Taught Learner",
                    "Freelancer",
                    "Entrepreneur",
                    "Unemployed / Looking for work",
                    "Other"
                ]
            },
            {
                "key": "background",
                "question": "What's your educational background?",
                "type": "single",
                "options": [
                    "Computer Science / IT",
                    "Engineering (non-CS)",
                    "Science / Math",
                    "Business / Management",
                    "Economics / Finance",
                    "Arts / Humanities",
                    "Social Sciences",
                    "Medicine / Health",
                    "No formal education",
                    "Other"
                ]
            },
            {
                "key": "years_experience",
                "question": "Years of professional experience?",
                "type": "single",
                "options": [
                    "No experience",
                    "Less than 1 year",
                    "1-2 years",
                    "2-5 years",
                    "5-10 years",
                    "10+ years"
                ]
            },
            {
                "key": "tech_experience",
                "question": "How comfortable are you with technology?",
                "type": "slider",
                "min": 1,
                "max": 10,
                "labels": ["Beginner", "Intermediate", "Advanced", "Expert"]
            }
        ]
    },

    # ========================================================================
    # LEVEL 2: GOALS & URGENCY
    # ========================================================================
    "level_2_goals": {
        "title": "Your Goals & Motivation",
        "icon": "🎯",
        "description": "What are you trying to achieve?",
        "questions": [
            {
                "key": "primary_goal",
                "question": "What's your primary learning goal?",
                "type": "single",
                "options": [
                    "Get a job in tech",
                    "Switch to a better role",
                    "Advance in current role",
                    "Build a side project",
                    "Start a business",
                    "Build strong fundamentals",
                    "Explore interests",
                    "Personal growth",
                    "Freelance/Freelancing",
                    "Other"
                ]
            },
            {
                "key": "secondary_goals",
                "question": "Any secondary goals?",
                "type": "multi",
                "options": [
                    "Earn more money",
                    "Gain credibility/certification",
                    "Build a portfolio",
                    "Network with professionals",
                    "Contribute to open source",
                    "Start teaching others",
                    "Build AI/ML systems",
                    "None"
                ]
            },
            {
                "key": "urgency",
                "question": "How urgent is this goal?",
                "type": "single",
                "options": [
                    "Very urgent (3-6 months)",
                    "Somewhat urgent (6-12 months)",
                    "Medium (1-2 years)",
                    "Long-term (2+ years)",
                    "No specific timeline"
                ]
            },
            {
                "key": "motivation_type",
                "question": "What motivates you most?",
                "type": "multi",
                "options": [
                    "Curiosity",
                    "Financial rewards",
                    "Career advancement",
                    "Competition / Challenge",
                    "Achievement / Mastery",
                    "Fear of falling behind",
                    "Helping others",
                    "Building something"
                ]
            }
        ]
    },

    # ========================================================================
    # LEVEL 3: LEARNING CAPACITY & LIFESTYLE
    # ========================================================================
    "level_3_capacity": {
        "title": "Your Learning Capacity",
        "icon": "⏰",
        "description": "How much time can you realistically dedicate?",
        "questions": [
            {
                "key": "daily_hours",
                "question": "Hours per day you can study?",
                "type": "slider",
                "min": 0.5,
                "max": 8,
                "step": 0.5,
                "labels": ["30 min", "1 hr", "2 hrs", "4 hrs", "6 hrs", "8+ hrs"]
            },
            {
                "key": "study_consistency",
                "question": "How many days per week can you study?",
                "type": "slider",
                "min": 1,
                "max": 7,
                "labels": ["1 day", "2-3 days", "4-5 days", "Daily"]
            },
            {
                "key": "sleep_hours",
                "question": "Average sleep per night?",
                "type": "slider",
                "min": 4,
                "max": 12,
                "labels": ["4 hrs", "6 hrs", "8 hrs", "10+ hrs"]
            },
            {
                "key": "current_commitments",
                "question": "What's taking up your time?",
                "type": "multi",
                "options": [
                    "Full-time job",
                    "Part-time job",
                    "Studies/University",
                    "Family responsibilities",
                    "Health conditions",
                    "Other hobbies",
                    "Freelance work",
                    "Side projects"
                ]
            },
            {
                "key": "timezone",
                "question": "Your timezone for personalized timing?",
                "type": "single",
                "options": [
                    "IST (India)",
                    "UTC (UK)",
                    "EST (US East)",
                    "CST (US Central)",
                    "PST (US West)",
                    "CET (Europe)",
                    "JST (Japan)",
                    "AEST (Australia)",
                    "Other"
                ]
            }
        ]
    },

    # ========================================================================
    # LEVEL 4: LEARNING STYLE & PREFERENCES
    # ========================================================================
    "level_4_learning_style": {
        "title": "Your Learning Style",
        "icon": "🧠",
        "description": "How do you learn best?",
        "questions": [
            {
                "key": "preferred_format",
                "question": "What's your preferred learning format?",
                "type": "multi",
                "options": [
                    "Video tutorials",
                    "Text/Articles",
                    "Interactive coding",
                    "Live sessions",
                    "Books & docs",
                    "Project-based",
                    "Hands-on exercises",
                    "Visual diagrams"
                ]
            },
            {
                "key": "pace_preference",
                "question": "Do you prefer learning at your own pace or structured schedule?",
                "type": "single",
                "options": [
                    "Self-paced (total flexibility)",
                    "Structured schedule (deadlines help)",
                    "Hybrid (mix of both)",
                    "Coach/mentor guided"
                ]
            },
            {
                "key": "learning_depth",
                "question": "When learning, what matters more?",
                "type": "single",
                "options": [
                    "Understanding deeply (theory first)",
                    "Practical skills (learn by doing)",
                    "Quick wins (get working fast)",
                    "Balanced approach",
                    "Mastery & perfection"
                ]
            },
            {
                "key": "struggle_tolerance",
                "question": "How do you handle struggling with difficult concepts?",
                "type": "single",
                "options": [
                    "Take breaks, come back later",
                    "Power through immediately",
                    "Ask for help quickly",
                    "Look for different resources",
                    "Need structured guidance"
                ]
            },
            {
                "key": "feedback_frequency",
                "question": "How often do you want feedback?",
                "type": "single",
                "options": [
                    "Real-time feedback",
                    "Daily feedback",
                    "Weekly feedback",
                    "Monthly feedback",
                    "Only at milestones"
                ]
            }
        ]
    },

    # ========================================================================
    # LEVEL 5: INTERESTS & CAREER PATH
    # ========================================================================
    "level_5_interests": {
        "title": "Your Interests & Career Path",
        "icon": "🚀",
        "description": "What excites you most?",
        "questions": [
            {
                "key": "work_excites",
                "question": "What kind of work excites you?",
                "type": "multi",
                "options": [
                    "Building things from scratch",
                    "Solving complex logic problems",
                    "Analyzing data & patterns",
                    "Designing architectures",
                    "Real-world impact",
                    "Optimizing performance",
                    "Understanding how things work",
                    "Teaching others",
                    "Creative problem-solving",
                    "AI/ML/Deep Learning",
                    "Backend/Infrastructure",
                    "Frontend/UI/UX",
                    "DevOps/Cloud",
                    "Security",
                    "Blockchain",
                    "Mobile apps",
                    "Automation",
                    "Scientific computing"
                ]
            },
            {
                "key": "career_direction",
                "question": "Where do you see yourself in 3-5 years?",
                "type": "single",
                "options": [
                    "Senior engineer at big tech",
                    "Lead/Manager role",
                    "Specialist/Expert in niche",
                    "Startup founder",
                    "Freelancer/Consultant",
                    "Not sure yet"
                ]
            },
            {
                "key": "domain_interests",
                "question": "Which domains interest you?",
                "type": "multi",
                "options": [
                    "Web Development",
                    "Mobile Development",
                    "Data Science / Analytics",
                    "AI / Machine Learning",
                    "Cloud / DevOps",
                    "Cybersecurity",
                    "Blockchain",
                    "Game Development",
                    "Embedded Systems",
                    "Open Source",
                    "Fintech",
                    "Healthcare Tech",
                    "EdTech",
                    "E-commerce"
                ]
            },
            {
                "key": "work_environment",
                "question": "What work environment appeals to you?",
                "type": "single",
                "options": [
                    "Big tech company (FAANG)",
                    "Growing startup",
                    "Small team",
                    "Self-employed",
                    "Academic/Research",
                    "Not important"
                ]
            }
        ]
    },

    # ========================================================================
    # LEVEL 6: SELF-ASSESSMENT & SKILLS
    # ========================================================================
    "level_6_self_assessment": {
        "title": "Your Current Skills",
        "icon": "💡",
        "description": "Rate yourself honestly",
        "questions": [
            {
                "key": "programming_skills",
                "question": "Programming confidence?",
                "type": "slider",
                "min": 1,
                "max": 10,
                "labels": ["Beginner", "Intermediate", "Advanced", "Expert"]
            },
            {
                "key": "math_skills",
                "question": "Math confidence?",
                "type": "slider",
                "min": 1,
                "max": 10,
                "labels": ["Beginner", "Intermediate", "Advanced", "Expert"]
            },
            {
                "key": "problem_solving",
                "question": "Problem-solving ability?",
                "type": "slider",
                "min": 1,
                "max": 10,
                "labels": ["Weak", "Fair", "Good", "Excellent"]
            },
            {
                "key": "communication_skills",
                "question": "Communication skills?",
                "type": "slider",
                "min": 1,
                "max": 10,
                "labels": ["Weak", "Fair", "Good", "Excellent"]
            },
            {
                "key": "languages_known",
                "question": "Programming languages you know?",
                "type": "multi",
                "options": [
                    "Python",
                    "JavaScript",
                    "Java",
                    "C++",
                    "C",
                    "Go",
                    "Rust",
                    "Ruby",
                    "PHP",
                    "Swift",
                    "Kotlin",
                    "R",
                    "MATLAB",
                    "SQL",
                    "None"
                ]
            },
            {
                "key": "tools_experience",
                "question": "Tools/frameworks you've used?",
                "type": "multi",
                "options": [
                    "Git/GitHub",
                    "Docker",
                    "AWS/Cloud",
                    "React",
                    "Django/Flask",
                    "Node.js",
                    "TensorFlow/PyTorch",
                    "SQL/Database",
                    "REST APIs",
                    "GraphQL",
                    "CI/CD",
                    "Kubernetes",
                    "None"
                ]
            }
        ]
    },

    # ========================================================================
    # LEVEL 7: CHALLENGES & OBSTACLES
    # ========================================================================
    "level_7_challenges": {
        "title": "Challenges & Obstacles",
        "icon": "⚠️",
        "description": "What might hold you back?",
        "questions": [
            {
                "key": "burnout_frequency",
                "question": "How often do you experience burnout?",
                "type": "single",
                "options": [
                    "Very often (weekly)",
                    "Often (2-3x/month)",
                    "Sometimes (monthly)",
                    "Rarely (few times/year)",
                    "Never"
                ]
            },
            {
                "key": "burnout_triggers",
                "question": "What triggers your burnout?",
                "type": "multi",
                "options": [
                    "Too much workload",
                    "Lack of progress",
                    "Difficult concepts",
                    "Boredom/Repetition",
                    "External pressure",
                    "Perfectionism",
                    "Comparison with others",
                    "Not applicable"
                ]
            },
            {
                "key": "procrastination_level",
                "question": "How much do you procrastinate?",
                "type": "slider",
                "min": 1,
                "max": 10,
                "labels": ["Never", "Rarely", "Sometimes", "Often"]
            },
            {
                "key": "consistency",
                "question": "How consistent are you typically?",
                "type": "slider",
                "min": 1,
                "max": 10,
                "labels": ["Very inconsistent", "Somewhat inconsistent", "Fairly consistent", "Very consistent"]
            },
            {
                "key": "self_doubt",
                "question": "How often do you doubt yourself?",
                "type": "slider",
                "min": 1,
                "max": 10,
                "labels": ["Never", "Rarely", "Often", "Always"]
            },
            {
                "key": "main_obstacles",
                "question": "What are your main obstacles?",
                "type": "multi",
                "options": [
                    "Lack of time",
                    "Motivation issues",
                    "Health problems",
                    "Financial constraints",
                    "Unclear learning path",
                    "Imposter syndrome",
                    "Difficulty concentrating",
                    "Lack of accountability",
                    "Fear of failure",
                    "Family/social pressure",
                    "None"
                ]
            }
        ]
    },

    # ========================================================================
    # LEVEL 8: SUPPORT & RESOURCES
    # ========================================================================
    "level_8_support": {
        "title": "Support & Resources",
        "icon": "🤝",
        "description": "What support do you need?",
        "questions": [
            {
                "key": "accountability_need",
                "question": "How much accountability do you need?",
                "type": "single",
                "options": [
                    "I work best alone",
                    "Occasional check-ins",
                    "Weekly accountability",
                    "Daily accountability",
                    "Strict monitoring"
                ]
            },
            {
                "key": "mentorship_interest",
                "question": "Would you benefit from a mentor?",
                "type": "single",
                "options": [
                    "Yes, absolutely",
                    "Maybe, if available",
                    "Not necessary",
                    "No, I prefer independence"
                ]
            },
            {
                "key": "community_preference",
                "question": "How important is community?",
                "type": "single",
                "options": [
                    "Very important - I learn better in groups",
                    "Somewhat important - occasional interaction",
                    "Not important - I prefer solo learning",
                    "Doesn't matter"
                ]
            },
            {
                "key": "budget",
                "question": "Learning budget per month?",
                "type": "single",
                "options": [
                    "Free only",
                    "$0-50/month",
                    "$50-200/month",
                    "$200-500/month",
                    "500+/month (no budget limit)",
                    "Not sure"
                ]
            },
            {
                "key": "learning_resources",
                "question": "Preferred learning resource providers?",
                "type": "multi",
                "options": [
                    "YouTube",
                    "Udemy",
                    "Coursera",
                    "DataCamp",
                    "LinkedIn Learning",
                    "Pluralsight",
                    "Books",
                    "Documentation",
                    "GitHub projects",
                    "Medium/Blogs",
                    "No preference"
                ]
            }
        ]
    },

    # ========================================================================
    # LEVEL 9: HABITS & PERSONALITY
    # ========================================================================
    "level_9_habits": {
        "title": "Your Habits & Personality",
        "icon": "🎭",
        "description": "Understanding your learning personality",
        "questions": [
            {
                "key": "morning_person",
                "question": "When are you most productive?",
                "type": "single",
                "options": [
                    "Early morning (5-8 AM)",
                    "Late morning (8-11 AM)",
                    "Noon-afternoon (11 AM-3 PM)",
                    "Late afternoon (3-6 PM)",
                    "Evening (6-9 PM)",
                    "Night (9 PM+)"
                ]
            },
            {
                "key": "break_preferences",
                "question": "How often do you need breaks?",
                "type": "single",
                "options": [
                    "Every 30 mins",
                    "Every 45-50 mins (Pomodoro)",
                    "Every 90 mins (Ultradian)",
                    "Every few hours",
                    "As needed",
                    "I prefer no breaks"
                ]
            },
            {
                "key": "perfectionism",
                "question": "How perfectionist are you?",
                "type": "slider",
                "min": 1,
                "max": 10,
                "labels": ["Not at all", "Somewhat", "Moderately", "Extremely"]
            },
            {
                "key": "risk_taking",
                "question": "How comfortable are you with risk?",
                "type": "slider",
                "min": 1,
                "max": 10,
                "labels": ["Very risk-averse", "Cautious", "Balanced", "Risk-taker"]
            },
            {
                "key": "deadline_response",
                "question": "How do you respond to deadlines?",
                "type": "single",
                "options": [
                    "I need them to stay motivated",
                    "They help but aren't necessary",
                    "They stress me out",
                    "They don't affect me"
                ]
            },
            {
                "key": "learning_satisfaction",
                "question": "What feels most satisfying while learning?",
                "type": "multi",
                "options": [
                    "Seeing visible results",
                    "Understanding concepts deeply",
                    "Speed & quick wins",
                    "Mastery & expertise",
                    "Helping others",
                    "Building projects",
                    "Solving problems"
                ]
            }
        ]
    },

    # ========================================================================
    # LEVEL 10: PREVIOUS LEARNING EXPERIENCE
    # ========================================================================
    "level_10_past_learning": {
        "title": "Your Learning History",
        "icon": "📚",
        "description": "Learn from your past experiences",
        "questions": [
            {
                "key": "successful_learning",
                "question": "When have you learned something successfully?",
                "type": "multi",
                "options": [
                    "Online courses",
                    "Bootcamps",
                    "University",
                    "Self-taught",
                    "Mentorship",
                    "Project-based",
                    "Books/documentation",
                    "Never succeeded",
                    "Still figuring it out"
                ]
            },
            {
                "key": "failed_learning",
                "question": "What caused past learning failures?",
                "type": "multi",
                "options": [
                    "Lost motivation",
                    "Too difficult",
                    "Ran out of time",
                    "Wrong learning style",
                    "Poor course quality",
                    "Lacked support",
                    "Bad timing",
                    "Health issues",
                    "Never failed",
                    "Not sure"
                ]
            },
            {
                "key": "courses_taken",
                "question": "How many online courses have you completed?",
                "type": "single",
                "options": [
                    "None",
                    "1-3",
                    "4-10",
                    "10+",
                    "Lost count"
                ]
            },
            {
                "key": "learning_longest_time",
                "question": "Longest you've consistently learned for?",
                "type": "single",
                "options": [
                    "Less than 1 week",
                    "1-4 weeks",
                    "1-3 months",
                    "3-6 months",
                    "6-12 months",
                    "1+ year"
                ]
            },
            {
                "key": "lessons_learned",
                "question": "Key lessons from past learning?",
                "type": "multi",
                "options": [
                    "Need clear goals",
                    "Need accountability",
                    "Need good teaching",
                    "Need project-based learning",
                    "Need breaks/rest",
                    "Need community",
                    "Need flexible timing",
                    "Nothing yet"
                ]
            }
        ]
    }
}

# Helper function to flatten all questions for easier access
def get_all_questions_flat():
    """Returns a flat list of all questions across all levels"""
    all_questions = []
    for level_key, level_data in EXPANDED_ASSESSMENT_LEVELS.items():
        for question in level_data["questions"]:
            question["level"] = level_key
            question["level_title"] = level_data["title"]
            all_questions.append(question)
    return all_questions

# Get total number of questions
def get_total_questions_count():
    """Returns total number of questions across all levels"""
    total = 0
    for level_data in EXPANDED_ASSESSMENT_LEVELS.values():
        total += len(level_data["questions"])
    return total
