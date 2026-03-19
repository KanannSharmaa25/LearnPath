import streamlit as st
import pandas as pd
import json
import os
from datetime import datetime
import random

st.set_page_config(
    page_title="LearnPath - AI-Powered Learning",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Check for query params
query_params = st.query_params
if "step" in query_params:
    try:
        st.session_state.current_step = int(query_params["step"])
        st.query_params.clear()
    except:
        pass

if "current_step" not in st.session_state:
    st.session_state.current_step = 0

if "user_profile" not in st.session_state:
    st.session_state.user_profile = {}

if "quiz_results" not in st.session_state:
    st.session_state.quiz_results = {}

if "daily_logs" not in st.session_state:
    st.session_state.daily_logs = []

if "learning_path" not in st.session_state:
    st.session_state.learning_path = []

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "assessment_results" not in st.session_state:
    st.session_state.assessment_results = {}

if "combined_results" not in st.session_state:
    st.session_state.combined_results = {}

from styles import load_styles
load_styles()

def go_to_step(step):
    st.session_state.current_step = step
    st.query_params["step"] = str(step)
    st.rerun()

# Header hiding
st.markdown("""
<style>
header { display: none !important; }
[data-testid="stSidebar"] { display: none !important; }
</style>
""", unsafe_allow_html=True)

# ===============================================================================
# SIDEBAR NAVIGATION
# ===============================================================================
if st.session_state.current_step != 0:
    with st.sidebar:
        st.markdown("""
        <style>
        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, #232338 0%, #181826 100%) !important;
            border-right: 1px solid rgba(167, 139, 250, 0.15) !important;
        }
        </style>
        <div style="padding: 20px 16px; border-bottom: 1px solid rgba(167, 139, 250, 0.15); margin-bottom: 16px;">
            <div style="font-size: 24px; font-weight: 700; color: #a78bfa;">🎓 LearnPath</div>
            <div style="font-size: 12px; color: #94a3b8; margin-top: 4px;">AI-Powered Learning</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### 🧭 Navigation")
        
        nav_options = [
            ("🏠 Dashboard", 6),
            ("👤 Profile", 1),
            ("📝 Assessment", 2),
            ("📋 Quizzes", 3),
            ("🛤️ Learning Path", 4),
            ("📚 Courses", 5),
            ("🤖 AI Coach", 7),
            ("📈 Predictions", 8),
            ("📊 Progress", 9),
            ("⚙️ Settings", 10),
        ]
        
        for label, step in nav_options:
            if st.session_state.current_step == step:
                st.markdown(f"**{label}**")
            else:
                if st.button(label, use_container_width=True, key=f"nav_{step}"):
                    go_to_step(step)
        
        st.divider()
        
        if st.session_state.user_profile:
            with st.expander("👤 Your Profile"):
                st.json(st.session_state.user_profile)

# ===============================================================================
# LANDING PAGE (Step 0)
# ===============================================================================
if st.session_state.current_step == 0:
    st.markdown("""
<style>
.stApp { background: #0f0f1a !important; }
.block-container { padding-top: 0 !important; max-width: 100% !important; }
</style>
""", unsafe_allow_html=True)
    
    st.html("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');
* { margin: 0; padding: 0; box-sizing: border-box; }
.landing { font-family: 'Plus Jakarta Sans', sans-serif; background: #0f0f1a; min-height: 100vh; color: #fff; overflow-x: hidden; }
.orb { position: absolute; border-radius: 50%; filter: blur(100px); opacity: 0.4; z-index: 0; }
.orb-1 { width: 600px; height: 600px; background: #7c3aed; top: -250px; left: -150px; }
.orb-2 { width: 500px; height: 500px; background: #a78bfa; top: 40%; right: -150px; }
.orb-3 { width: 400px; height: 400px; background: #6366f1; bottom: -150px; left: 25%; }
@keyframes fadeUp { from { opacity: 0; transform: translateY(40px); } to { opacity: 1; transform: translateY(0); } }
.hero { position: relative; min-height: 100vh; display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 60px 20px; z-index: 1; }
.hero h1 { font-size: clamp(56px, 10vw, 96px); font-weight: 800; text-align: center; line-height: 1.05; margin-bottom: 20px; animation: fadeUp 0.8s ease-out; }
.hero h1 .brand { display: block; background: linear-gradient(135deg, #fff 0%, #e2e8f0 50%, #a78bfa 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
.hero h1 .tagline { display: block; font-size: clamp(24px, 4vw, 40px); background: linear-gradient(135deg, #a78bfa 0%, #c084fc 50%, #7c3aed 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-top: 10px; }
.hero p { font-size: clamp(16px, 2vw, 20px); color: #94a3b8; text-align: center; max-width: 600px; line-height: 1.7; margin-bottom: 48px; animation: fadeUp 0.8s ease-out 0.15s both; }
.hero-stats { display: flex; gap: 80px; margin-top: 100px; animation: fadeUp 0.8s ease-out 0.45s both; }
.hero-stat { text-align: center; }
.hero-stat-num { font-size: 48px; font-weight: 800; background: linear-gradient(135deg, #a78bfa, #c084fc); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
.hero-stat-label { font-size: 15px; color: #64748b; margin-top: 8px; }
.features { padding: 120px 20px; max-width: 1300px; margin: 0 auto; position: relative; z-index: 1; }
.section-title { text-align: center; margin-bottom: 80px; animation: fadeUp 0.8s ease-out; }
.section-title h2 { font-size: clamp(32px, 5vw, 48px); font-weight: 700; margin-bottom: 16px; }
.section-title p { color: #64748b; font-size: 18px; }
.features-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(340px, 1fr)); gap: 28px; }
.feature-card { background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.06); border-radius: 28px; padding: 36px; transition: all 0.4s; animation: fadeUp 0.8s ease-out; }
.feature-card:hover { background: rgba(167,139,250,0.08); border-color: rgba(167,139,250,0.25); transform: translateY(-8px); }
.feature-icon { width: 70px; height: 70px; background: linear-gradient(135deg, rgba(167,139,250,0.25), rgba(124,58,237,0.15)); border-radius: 20px; display: flex; align-items: center; justify-content: center; font-size: 32px; margin-bottom: 24px; }
.feature-card h3 { font-size: 22px; font-weight: 600; margin-bottom: 14px; }
.feature-card p { color: #64748b; line-height: 1.7; font-size: 15px; }
.how-it-works { padding: 120px 20px; background: rgba(255,255,255,0.015); position: relative; z-index: 1; }
.steps-container { display: flex; justify-content: center; gap: 24px; flex-wrap: wrap; max-width: 1300px; margin: 0 auto; }
.step-card { background: rgba(24,24,38,0.8); border: 1px solid rgba(255,255,255,0.06); border-radius: 24px; padding: 40px 28px; width: 240px; text-align: center; transition: all 0.4s; animation: fadeUp 0.8s ease-out; }
.step-card:hover { border-color: rgba(167,139,250,0.35); transform: translateY(-8px); }
.step-num { width: 56px; height: 56px; background: linear-gradient(135deg, #7c3aed, #a78bfa); border-radius: 18px; display: inline-flex; align-items: center; justify-content: center; font-size: 24px; font-weight: 700; color: white; margin-bottom: 24px; }
.step-card h4 { font-size: 20px; font-weight: 600; margin-bottom: 10px; }
.step-card p { color: #64748b; font-size: 14px; line-height: 1.6; }
.cta { padding: 120px 20px; text-align: center; position: relative; z-index: 1; }
.cta-box { max-width: 900px; margin: 0 auto; background: linear-gradient(135deg, rgba(124,58,237,0.25), rgba(167,139,250,0.1)); border: 1px solid rgba(167,139,250,0.25); border-radius: 40px; padding: 80px 60px; animation: fadeUp 0.8s ease-out; }
.cta h2 { font-size: clamp(28px, 4vw, 42px); font-weight: 700; margin-bottom: 20px; }
.cta p { color: #94a3b8; font-size: 18px; margin-bottom: 40px; }
@media (max-width: 768px) { .hero-stats { gap: 40px; flex-wrap: wrap; justify-content: center; } .hero-stat-num { font-size: 36px; } .features-grid { grid-template-columns: 1fr; } .step-card { width: 100%; max-width: 300px; } .cta-box { padding: 50px 30px; } }
</style>

<div class="landing">
    <div class="orb orb-1"></div>
    <div class="orb orb-2"></div>
    <div class="orb orb-3"></div>
    
    <div class="hero">
        <h1>
            <span class="brand">LearnPath</span>
            <span class="tagline">AI-Powered Learning</span>
        </h1>
        <p>Your personal AI tutor that adapts to your unique learning style. Track progress, take adaptive quizzes, and achieve your goals faster than ever before.</p>
        
        <div class="hero-stats">
            <div class="hero-stat">
                <div class="hero-stat-num">50K+</div>
                <div class="hero-stat-label">Active Learners</div>
            </div>
            <div class="hero-stat">
                <div class="hero-stat-num">500+</div>
                <div class="hero-stat-label">Courses</div>
            </div>
            <div class="hero-stat">
                <div class="hero-stat-num">95%</div>
                <div class="hero-stat-label">Success Rate</div>
            </div>
        </div>
    </div>
    
    <div class="features">
        <div class="section-title">
            <h2>Everything You Need to Succeed</h2>
            <p>Powerful features designed to accelerate your learning journey</p>
        </div>
        <div class="features-grid">
            <div class="feature-card">
                <div class="feature-icon">🧠</div>
                <h3>AI-Powered Learning</h3>
                <p>Our AI analyzes your learning style and creates personalized paths tailored to your strengths.</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">📊</div>
                <h3>Smart Progress Tracking</h3>
                <p>Track your progress with detailed analytics and get actionable insights to improve.</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">🎯</div>
                <h3>Adaptive Assessments</h3>
                <p>Take quizzes that adapt to your skill level and focus on areas that need improvement.</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">🤖</div>
                <h3>AI Coach</h3>
                <p>Get instant answers to your questions from your personal AI learning assistant.</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">🔮</div>
                <h3>Predictive Analytics</h3>
                <p>AI predictions help you anticipate challenges and stay ahead of your learning curve.</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">📚</div>
                <h3>Course Recommendations</h3>
                <p>Get personalized course recommendations based on your goals and interests.</p>
            </div>
        </div>
    </div>
    
    <div class="how-it-works">
        <div class="section-title">
            <h2>How It Works</h2>
            <p>Start your learning journey in minutes</p>
        </div>
        <div class="steps-container">
            <div class="step-card">
                <div class="step-num">1</div>
                <h4>Create Profile</h4>
                <p>Tell us about your goals</p>
            </div>
            <div class="step-card">
                <div class="step-num">2</div>
                <h4>Take Assessment</h4>
                <p>Gauge your current level</p>
            </div>
            <div class="step-card">
                <div class="step-num">3</div>
                <h4>Take Quizzes</h4>
                <p>Test your knowledge</p>
            </div>
            <div class="step-card">
                <div class="step-num">4</div>
                <h4>Get Your Path</h4>
                <p>Personalized learning path</p>
            </div>
            <div class="step-card">
                <div class="step-num">5</div>
                <h4>Track Progress</h4>
                <p>Monitor your growth</p>
            </div>
        </div>
    </div>
    
    <div class="cta">
        <div class="cta-box">
            <h2>Ready to Transform Your Learning?</h2>
            <p>Join thousands of learners achieving their goals with LearnPath</p>
        </div>
    </div>
</div>
""")
    
    col1, col2, col3 = st.columns([1,1,1])
    with col2:
        if st.button("🎯 Start Your Journey", type="primary", use_container_width=True):
            go_to_step(1)

# ===============================================================================
# PROFILE (Step 1)
# ===============================================================================
elif st.session_state.current_step == 1:
    st.markdown("## 👤 Create Your Profile")
    st.markdown("Let's get to know you better to personalize your learning experience.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        name = st.text_input("Your Name", placeholder="Enter your name")
        age = st.selectbox("Age Group", ["Under 18", "18-24", "25-34", "35-44", "45-54", "55+"])
        education = st.selectbox("Education Level", ["High School", "Some College", "Bachelor's", "Master's", "PhD", "Other"])
        role = st.selectbox("Current Role", ["Student", "Working Professional", "Career Switcher", "Self-Taught", "Freelancer", "Entrepreneur", "Unemployed", "Other"])
    
    with col2:
        learning_goal = st.selectbox("Primary Learning Goal", [
            "Get a job in tech", "Switch to a better role", "Advance in current role",
            "Build a side project", "Start a business", "Build strong fundamentals",
            "Explore interests", "Personal growth", "Freelancing", "Other"
        ])
        preferred_style = st.multiselect("Preferred Learning Style", [
            "Visual", "Auditory", "Reading/Writing", "Kinesthetic"
        ], default=["Visual"])
        study_duration = st.slider("Daily Study Time (hours)", 0.5, 8.0, 2.0)
        tech_comfort = st.slider("Tech Comfort Level (1-10)", 1, 10, 5)
    
    if st.button("Save Profile & Continue", type="primary"):
        st.session_state.user_profile = {
            "name": name,
            "age": age,
            "education": education,
            "role": role,
            "learning_goal": learning_goal,
            "preferred_style": preferred_style,
            "study_duration": study_duration,
            "tech_comfort": tech_comfort,
            "created_at": datetime.now().isoformat()
        }
        st.success("Profile saved!")
        go_to_step(2)

# ===============================================================================
# SMART ASSESSMENT (Step 2) - Comprehensive with psychology & work questions
# ===============================================================================
elif st.session_state.current_step == 2:
    st.markdown("## 📝 Smart Assessment")
    st.markdown("Comprehensive assessment to understand your background, work style, and psychology.")
    
    # Comprehensive assessment questions
    assessment_sections = {
        "Background & Education": {
            "icon": "🎓",
            "questions": [
                {"q": "What is your highest education level?", "options": ["High School", "Some College", "Bachelor's Degree", "Master's Degree", "PhD", "Other"], "key": "education"},
                {"q": "What was your major/field of study?", "options": ["Computer Science", "Engineering", "Business", "Arts", "Science", "Mathematics", "Other", "Not Applicable"], "key": "major"},
                {"q": "How long has it been since you studied formally?", "options": ["Currently studying", "Less than 1 year", "1-3 years", "3-5 years", "5-10 years", "10+ years"], "key": "time_since_study"},
                {"q": "Do you have any professional certifications?", "options": ["Yes, tech related", "Yes, non-tech", "No certifications", "Currently pursuing"], "key": "certifications"},
            ]
        },
        "Work Experience": {
            "icon": "💼",
            "questions": [
                {"q": "What is your current work status?", "options": ["Employed full-time", "Employed part-time", "Self-employed", "Student", "Unemployed", "Freelancer"], "key": "work_status"},
                {"q": "Years of professional work experience?", "options": ["No experience", "Less than 1 year", "1-3 years", "3-5 years", "5-10 years", "10+ years"], "key": "experience_years"},
                {"q": "How do you typically handle tight deadlines?", "options": ["Work extra hours to complete", "Prioritize and focus on essentials", "Ask for extension", "Stress and procrastinate", "Delegate if possible"], "key": "deadline_handling"},
                {"q": "When working on a complex project, you:", "options": ["Plan thoroughly before starting", "Start immediately and figure out along the way", "Break it into small tasks", "Wait for clear instructions", "Work best under pressure"], "key": "project_approach"},
            ]
        },
        "Work Under Pressure": {
            "icon": "🔥",
            "questions": [
                {"q": "How do you perform under pressure?", "options": ["Thrive and deliver excellent work", "Perform adequately but feel stressed", "Struggle and make mistakes", "Need breaks to function", "Avoid pressure situations"], "key": "pressure_performance"},
                {"q": "When faced with multiple urgent tasks, you:", "options": ["Create a prioritized list immediately", "Panic and don't know where to start", "Work on all simultaneously", "Delegate what you can", "Focus on one and let others wait"], "key": "multi_task"},
                {"q": "How do you handle unexpected challenges?", "options": ["Quickly adapt and find solutions", "Take time to think before acting", "Seek help immediately", "Avoid the problem", "Document and escalate"], "key": "challenge_handling"},
                {"q": "Your preferred work environment is:", "options": ["Fast-paced and challenging", "Steady and predictable", "Flexible with variety", "Structured and organized", "Collaborative and social"], "key": "work_environment"},
            ]
        },
        "Learning Style & Psychology": {
            "icon": "🧠",
            "questions": [
                {"q": "When learning something new, you prefer:", "options": ["Reading documentation", "Watching video tutorials", "Hands-on practice", "Asking questions", "A combination"], "key": "learning_preference"},
                {"q": "When you get stuck on a problem, you:", "options": ["Research and try multiple solutions", "Ask for help immediately", "Take a break and think", "Look for similar examples", "Give up temporarily"], "key": "problem_solving"},
                {"q": "How do you stay motivated during long projects?", "options": ["Set milestones and celebrate", "Focus on the end goal", "Take regular breaks", "Get accountability partners", "Reward yourself"], "key": "motivation"},
                {"q": "When you make a mistake, you:", "options": ["Analyze and learn from it", "Feel discouraged but move on", "Blame external factors", "Ignore and move on", "Seek feedback"], "key": "mistake_handling"},
                {"q": "Your biggest challenge in learning is:", "options": ["Staying consistent", "Understanding concepts", "Finding time", "Lack of resources", "Self-doubt", "No clear direction"], "key": "learning_challenge"},
            ]
        },
        "Goals & Aspirations": {
            "icon": "🎯",
            "questions": [
                {"q": "What is your primary motivation for learning?", "options": ["Career advancement", "Personal interest", "Financial improvement", "Problem solving", "Recognition", "Helping others"], "key": "motivation_type"},
                {"q": "How soon do you want to see results?", "options": ["Immediately", "Within a month", "Within 3 months", "Within 6 months", "Within a year", "Long-term"], "key": "timeline_expectation"},
                {"q": "How would you rate your self-discipline?", "options": ["Very high - I stick to plans", "High - mostly consistent", "Medium - varies by day", "Low - need accountability", "Very low - struggle"], "key": "self_discipline"},
                {"q": "What scares you most about learning a new skill?", "options": ["Not being good enough", "Running out of time", "Wasting effort", "Not knowing where to start", "Failure", "Nothing scares me"], "key": "fear"},
            ]
        },
        "Technical Skills": {
            "icon": "💻",
            "questions": [
                {"q": "Rate your current programming knowledge:", "options": ["Expert - can build complex systems", "Advanced - can build full applications", "Intermediate - understand fundamentals", "Beginner - know basics", "None - total beginner"], "key": "programming_level"},
                {"q": "Which technologies are you familiar with?", "options": ["Python", "JavaScript", "Java", "C++", "SQL", "HTML/CSS", "None", "Multiple"], "key": "tech_familiarity"},
                {"q": "Have you built any projects before?", "options": ["Yes, multiple professional projects", "Yes, some personal projects", "Started but never finished", "No, but have ideas", "No, never tried"], "key": "project_experience"},
                {"q": "How do you debug when something breaks?", "options": ["Use debugger tools", "Print statements", "Research error messages", "Ask for help", "Try random changes"], "key": "debugging_approach"},
            ]
        }
    }
    
    # Initialize assessment state
    if "assessment_state" not in st.session_state:
        st.session_state.assessment_state = {"current_section": 0, "answers": {}, "completed": False}
    
    sections = list(assessment_sections.keys())
    current_section_idx = st.session_state.assessment_state["current_section"]
    
    if not st.session_state.assessment_state["completed"]:
        current_section = sections[current_section_idx]
        section_data = assessment_sections[current_section]
        
        st.markdown(f"### {section_data['icon']} {current_section}")
        st.markdown(f"**Question {current_section_idx + 1} of {len(sections)}**")
        
        progress = current_section_idx / len(sections)
        st.progress(progress)
        
        for q in section_data["questions"]:
            answer = st.radio(q["q"], q["options"], key=f"assess_{q['key']}")
            st.session_state.assessment_state["answers"][q["key"]] = answer
        
        col1, col2 = st.columns(2)
        with col1:
            if current_section_idx > 0:
                if st.button("← Previous Section"):
                    st.session_state.assessment_state["current_section"] -= 1
                    st.rerun()
        with col2:
            if current_section_idx < len(sections) - 1:
                if st.button("Next Section →", type="primary"):
                    st.session_state.assessment_state["current_section"] += 1
                    st.rerun()
            else:
                if st.button("Complete Assessment", type="primary"):
                    st.session_state.assessment_state["completed"] = True
                    st.session_state.assessment_results = st.session_state.assessment_state["answers"]
                    st.success("Assessment complete!")
                    go_to_step(3)
    else:
        st.success("✅ Assessment Completed!")
        st.markdown("### Your Assessment Summary")
        st.json(st.session_state.assessment_results)
        
        if st.button("Take Quizzes Now →", type="primary"):
            go_to_step(3)
    
    if st.button("← Back"):
        go_to_step(6)

# ===============================================================================
# QUIZZES (Step 3) - More topics and questions
# ===============================================================================
elif st.session_state.current_step == 3:
    st.markdown("## 📋 Knowledge Quizzes")
    st.markdown("Test your technical knowledge in various topics.")
    
    # Extensive quiz bank
    quiz_bank = {
        "Python Programming": {
            "icon": "🐍",
            "questions": [
                {"q": "What is the output of print(type([]))?", "options": ["list", "tuple", "dict", "set"], "answer": "list"},
                {"q": "Which keyword defines a function?", "options": ["function", "def", "func", "define"], "answer": "def"},
                {"q": "What is Python's list comprehension?", "options": ["Loop", "Creating lists inline", "Function", "Class"], "answer": "Creating lists inline"},
                {"q": "What does 'self' refer to?", "options": ["Class", "Instance/object", "Function", "Module"], "answer": "Instance/object"},
                {"q": "What is a lambda?", "options": ["Variable", "Anonymous function", "Class", "Loop"], "answer": "Anonymous function"},
                {"q": "What is the difference between '==' and 'is'?", "options": ["Same thing", "== compares value, is compares identity", "is compares value", "== compares identity"], "answer": "== compares value, is compares identity"},
                {"q": "What is a dictionary in Python?", "options": ["Ordered collection", "Key-value pairs", "Set", "Tuple"], "answer": "Key-value pairs"},
                {"q": "How do you handle exceptions?", "options": ["try/except", "catch/throw", "if/else", "handle/error"], "answer": "try/except"},
                {"q": "What is pip?", "options": ["Python installer package", "Python internal processor", "Python IDE", "Python test tool"], "answer": "Python installer package"},
                {"q": "What is __init__?", "options": ["Main function", "Constructor", "Destructor", "Import"], "answer": "Constructor"},
            ]
        },
        "JavaScript": {
            "icon": "📜",
            "questions": [
                {"q": "What is the correct way to declare a variable?", "options": ["var x = 5", "variable x = 5", "int x = 5", "x := 5"], "answer": "var x = 5"},
                {"q": "What does === compare?", "options": ["Value only", "Type only", "Value and type", "Reference"], "answer": "Value and type"},
                {"q": "What is a closure?", "options": ["Function with access to outer scope", "End of function", "Error handler", "Loop"], "answer": "Function with access to outer scope"},
                {"q": "What is DOM?", "options": ["Data Object Model", "Document Object Model", "Digital Ocean Map", "Direct Output Mode"], "answer": "Document Object Model"},
                {"q": "How do you create an array?", "options": ["var arr = {}", "var arr = []", "var arr = ()", "var arr = <>"], "answer": "var arr = []"},
                {"q": "What is 'undefined'?", "options": ["Empty string", "No value assigned", "Error", "Null"], "answer": "No value assigned"},
                {"q": "What does Promise handle?", "options": ["HTML", "Async operations", "CSS", "Database"], "answer": "Async operations"},
                {"q": "What is arrow function syntax?", "options": ["function => x", "x => function", "(x) => x", "=> x function"], "answer": "(x) => x"},
                {"q": "What is event bubbling?", "options": ["Events go up DOM", "Events go down DOM", "Events stay in place", "Events delete"], "answer": "Events go up DOM"},
                {"q": "What is localStorage?", "options": ["Server storage", "Browser storage", "Database", "Cache"], "answer": "Browser storage"},
            ]
        },
        "Data Structures & Algorithms": {
            "icon": "📊",
            "questions": [
                {"q": "Time complexity of array access?", "options": ["O(1)", "O(n)", "O(log n)", "O(n²)"], "answer": "O(1)"},
                {"q": "What is a hash table?", "options": ["Array", "Key-value store", "Tree", "Stack"], "answer": "Key-value store"},
                {"q": "LIFO structure?", "options": ["Queue", "Stack", "Array", "Tree"], "answer": "Stack"},
                {"q": "Binary search requires?", "options": ["Array", "Sorted array", "Linked list", "Heap"], "answer": "Sorted array"},
                {"q": "What is a linked list?", "options": ["Array", "Nodes with pointers", "Hash table", "Tree"], "answer": "Nodes with pointers"},
                {"q": "Worst case of quicksort?", "options": ["O(n log n)", "O(n)", "O(n²)", "O(log n)"], "answer": "O(n²)"},
                {"q": "What is a binary tree?", "options": ["Each node has 2 children", "Each node has 1 child", "Tree with binary values", "Sorted tree"], "answer": "Each node has 2 children"},
                {"q": "BFS uses?", "options": ["Stack", "Queue", "Heap", "Tree"], "answer": "Queue"},
                {"q": "DFS uses?", "options": ["Queue", "Stack", "Array", "Heap"], "answer": "Stack"},
                {"q": "What is a heap?", "options": ["Tree structure", "Priority queue", "Both", "Neither"], "answer": "Priority queue"},
            ]
        },
        "Machine Learning": {
            "icon": "🤖",
            "questions": [
                {"q": "Supervised learning uses?", "options": ["Unlabeled data", "Labeled data", "Random data", "No data"], "answer": "Labeled data"},
                {"q": "What is overfitting?", "options": ["Good fit", "Model too complex", "Underfitting", "Perfect"], "answer": "Model too complex"},
                {"q": "Neural network activation function?", "options": ["Input", "Sigmoid/ReLU", "Output only", "None"], "answer": "Sigmoid/ReLU"},
                {"q": "What is gradient descent?", "options": ["Climbing up", "Optimization algorithm", "Data processing", "Visualization"], "answer": "Optimization algorithm"},
                {"q": "Cross-validation is for?", "options": ["Training", "Model evaluation", "Prediction", "Preprocessing"], "answer": "Model evaluation"},
                {"q": "What is accuracy?", "options": ["Correct predictions / Total", "True positive / All positive", "True negative / All negative", "False predictions"], "answer": "Correct predictions / Total"},
                {"q": "Random Forest is?", "options": ["Single tree", "Multiple trees", "Neural network", "Regression"], "answer": "Multiple trees"},
                {"q": "What is feature scaling?", "options": ["Adding features", "Normalizing features", "Removing features", "Creating features"], "answer": "Normalizing features"},
                {"q": "K-means is?", "options": ["Supervised", "Unsupervised", "Reinforcement", "Semi-supervised"], "answer": "Unsupervised"},
                {"q": "What is recall?", "options": ["TP/(TP+FP)", "TP/(TP+FN)", "TN/(TN+FP)", "Accuracy + Precision"], "answer": "TP/(TP+FN)"},
            ]
        },
        "Web Development": {
            "icon": "🌐",
            "questions": [
                {"q": "HTTP GET method?", "options": ["Create data", "Read data", "Update data", "Delete data"], "answer": "Read data"},
                {"q": "What is CSS flexbox?", "options": ["Database", "Layout system", "Programming language", "Server"], "answer": "Layout system"},
                {"q": "What is JSON?", "options": ["Database", "Data format", "Programming language", "Server"], "answer": "Data format"},
                {"q": "What is a cookie?", "options": ["Food", "User data storage", "Programming", "Network"], "answer": "User data storage"},
                {"q": "What is API?", "options": ["Database", "Interface for communication", "Programming language", "Web server"], "answer": "Interface for communication"},
                {"q": "What is REST?", "options": ["Database", "API architecture", "Programming style", "Server type"], "answer": "API architecture"},
                {"q": "What does HTML stand for?", "options": ["Hyper Text Markup Language", "High Tech Modern Language", "Home Tool Markup Language", "Hyper Transfer Markup Language"], "answer": "Hyper Text Markup Language"},
                {"q": "CSS handles?", "options": ["Server logic", "Styling web pages", "Database", "Security"], "answer": "Styling web pages"},
                {"q": "What is responsive design?", "options": ["Fast loading", "Adapts to screen sizes", "Secure design", "Database design"], "answer": "Adapts to screen sizes"},
                {"q": "What is AJAX?", "options": ["Database", "Async web requests", "Programming language", "Server"], "answer": "Async web requests"},
            ]
        },
        "Database & SQL": {
            "icon": "🗄️",
            "questions": [
                {"q": "What is SQL?", "options": ["Programming language", "Query language for databases", "Web server", "Operating system"], "answer": "Query language for databases"},
                {"q": "What is a primary key?", "options": ["First column", "Unique identifier", "Foreign field", "Index"], "answer": "Unique identifier"},
                {"q": "What is a JOIN?", "options": ["Database connection", "Combines tables", "Deletes data", "Creates table"], "answer": "Combines tables"},
                {"q": "What is NoSQL?", "options": ["SQL version", "Non-relational database", "Old database", "Network database"], "answer": "Non-relational database"},
                {"q": "What is indexing?", "options": ["Deleting records", "Speed up queries", "Creating backups", "Encryption"], "answer": "Speed up queries"},
                {"q": "What does SELECT do?", "options": ["Creates table", "Deletes data", "Reads data", "Updates data"], "answer": "Reads data"},
                {"q": "What is normalization?", "options": ["Data encryption", "Organizing database", "Data backup", "Compression"], "answer": "Organizing database"},
                {"q": "What is a foreign key?", "options": ["Primary key in another table", "External index", "Unique key", "Security key"], "answer": "Primary key in another table"},
                {"q": "What does GROUP BY do?", "options": ["Sorts data", "Filters data", "Aggregates data", "Joins tables"], "answer": "Aggregates data"},
                {"q": "What is a transaction?", "options": ["Single operation", "Multiple operations as unit", "Backup process", "Security check"], "answer": "Multiple operations as unit"},
            ]
        },
        "DevOps & Cloud": {
            "icon": "☁️",
            "questions": [
                {"q": "What is Docker?", "options": ["Programming language", "Container platform", "Cloud provider", "Database"], "answer": "Container platform"},
                {"q": "What is CI/CD?", "options": ["Code Insurance", "Continuous Integration/Deployment", "Computer Interface", "Cloud Infrastructure"], "answer": "Continuous Integration/Deployment"},
                {"q": "What does Git do?", "options": ["Database", "Version control", "Web server", "Programming"], "answer": "Version control"},
                {"q": "What is AWS?", "options": ["Programming language", "Cloud platform", "Database", "Operating system"], "answer": "Cloud platform"},
                {"q": "What is Kubernetes?", "options": ["Programming language", "Container orchestration", "Database", "Web server"], "answer": "Container orchestration"},
                {"q": "What is Infrastructure as Code?", "options": ["Coding databases", "Managing infrastructure with code", "Writing server scripts", "Programming languages"], "answer": "Managing infrastructure with code"},
                {"q": "What is load balancing?", "options": ["Balancing code", "Distributing traffic", "Sorting data", "Compression"], "answer": "Distributing traffic"},
                {"q": "What is a VPN?", "options": ["Programming language", "Virtual private network", "Database type", "Server type"], "answer": "Virtual private network"},
                {"q": "What is monitoring?", "options": ["Backing up", "Tracking system health", "Writing code", "Security"], "answer": "Tracking system health"},
                {"q": "What is microservices?", "options": ["Small programs", "Architecture style", "Database design", "Programming paradigm"], "answer": "Architecture style"},
            ]
        },
        "Soft Skills & Communication": {
            "icon": "💬",
            "questions": [
                {"q": "Best way to explain complex technical concepts?", "options": ["Use jargon", "Use analogies", "Avoid explanation", "Give documentation"], "answer": "Use analogies"},
                {"q": "How should you handle disagreements with teammates?", "options": ["Insist on your way", "Ignore them", "Discuss respectfully with data", "Escalate immediately"], "answer": "Discuss respectfully with data"},
                {"q": "What is active listening?", "options": ["Speaking a lot", "Fully concentrating on speaker", "Interrupt frequently", "Talk while others listen"], "answer": "Fully concentrating on speaker"},
                {"q": "How do you give constructive feedback?", "options": ["Be harsh", "Focus on behavior not person", "Avoid giving feedback", "Complain to others"], "answer": "Focus on behavior not person"},
                {"q": "When is it appropriate to say no?", "options": ["Never", "When overloaded or unethical", "Always", "When asked by seniors"], "answer": "When overloaded or unethical"},
                {"q": "How do you prioritize tasks?", "options": ["Random order", "By urgency and importance", "By alphabetical", "By who asks first"], "answer": "By urgency and importance"},
                {"q": "What makes a good mentor?", "options": ["Having all answers", "Guiding discovery", "Doing work for them", "Being strict"], "answer": "Guiding discovery"},
                {"q": "How do you handle scope creep?", "options": ["Accept all changes", "Push back professionally", "Ignore it", "Quit the project"], "answer": "Push back professionally"},
                {"q": "What is emotional intelligence?", "options": ["Technical skills", "Understanding emotions", "IQ test", "Programming skill"], "answer": "Understanding emotions"},
                {"q": "How should you present to stakeholders?", "options": ["Use heavy technical jargon", "Focus on business value", "Read slides only", "Avoid questions"], "answer": "Focus on business value"},
            ]
        }
    }
    
    # Initialize quiz state
    if "quiz_state" not in st.session_state:
        st.session_state.quiz_state = {}
    
    # Show all quiz topics
    st.markdown("### Select Topics to Take Quiz")
    
    quiz_topics = list(quiz_bank.keys())
    selected_topics = st.multiselect("Choose quiz topics:", quiz_topics, default=[])
    
    if selected_topics:
        # Show results from previous quizzes
        st.markdown("### 📝 Your Quiz Results")
        for topic in selected_topics:
            if topic in st.session_state.quiz_results:
                result = st.session_state.quiz_results[topic]
                st.success(f"**{topic}:** {result['score']}/{result['total']} ({result['percentage']:.0f}%)")
        
        st.markdown("---")
        st.markdown("### Take New Quiz")
        
        # Select topic to take
        topic_to_take = st.selectbox("Select topic to attempt:", selected_topics)
        
        quiz_data = quiz_bank[topic_to_take]
        questions = quiz_data["questions"]
        
        if topic_to_take not in st.session_state.quiz_state:
            st.session_state.quiz_state[topic_to_take] = {"current": 0, "score": 0, "answers": {}}
        
        state = st.session_state.quiz_state[topic_to_take]
        current = state["current"]
        
        if current < len(questions):
            q = questions[current]
            st.markdown(f"### {quiz_data['icon']} {topic_to_take}")
            st.markdown(f"**Question {current + 1}/{len(questions)}**")
            
            answer = st.radio(q["q"], q["options"], key=f"quiz_{topic_to_take}_{current}")
            
            if st.button("Submit", type="primary", key=f"submit_{topic_to_take}_{current}"):
                if answer == q["answer"]:
                    state["score"] += 1
                    st.success("Correct! ✅")
                else:
                    st.error(f"Wrong! Answer: {q['answer']}")
                state["current"] += 1
                st.rerun()
        else:
            score = state["score"]
            total = len(questions)
            pct = (score / total) * 100
            
            st.markdown(f"## Quiz Complete: {topic_to_take}")
            st.markdown(f"**Score: {score}/{total} ({pct:.0f}%)**")
            
            if pct >= 80:
                st.success("🌟 Excellent!")
            elif pct >= 60:
                st.info("👍 Good job!")
            else:
                st.warning("📚 Keep practicing!")
            
            # Save result
            st.session_state.quiz_results[topic_to_take] = {
                "score": score,
                "total": total,
                "percentage": pct,
                "date": datetime.now().isoformat()
            }
            
            if st.button(f"Retake {topic_to_take}"):
                state["current"] = 0
                state["score"] = 0
                st.rerun()
            
            # Generate learning path button
            if st.button("Generate Learning Path →", type="primary"):
                generate_combined_results()
                go_to_step(4)
    
    if st.button("← Back"):
        go_to_step(6)

# ===============================================================================
# LEARNING PATH (Step 4)
# ===============================================================================
elif st.session_state.current_step == 4:
    quiz_results = st.session_state.quiz_results
    
    # Calculate overall skill levels
    skill_levels = {}
    
    # Map quiz topics to skill areas
    topic_mapping = {
        "Python Programming": ["Python"],
        "JavaScript": ["JavaScript", "Web"],
        "Data Structures & Algorithms": ["Algorithms"],
        "Machine Learning": ["Machine Learning", "AI"],
        "Web Development": ["Web", "HTML", "CSS"],
        "Database & SQL": ["Database", "SQL"],
        "DevOps & Cloud": ["DevOps", "Cloud"],
    }
    
    for quiz_topic, score_data in quiz_results.items():
        skill_areas = topic_mapping.get(quiz_topic, [quiz_topic])
        for area in skill_areas:
            skill_levels[area] = score_data["percentage"]
    
    # Determine learning path based on assessment + quiz
    learning_path = []
    
    # Based on goals and skill gaps
    goal = assessment.get("learning_goal", "")
    programming_level = assessment.get("programming_level", "")
    tech_familiarity = assessment.get("tech_familiarity", "")
    
    if "job" in goal.lower() or "career" in goal.lower():
        if skill_levels.get("Python", 0) < 60:
            learning_path.extend([
                {"title": "Python Fundamentals", "description": "Master Python basics, syntax, and data structures", "duration": "2 weeks", "progress": 0, "priority": "high"},
                {"title": "Python Advanced Concepts", "description": "OOP, decorators, generators, and best practices", "duration": "2 weeks", "progress": 0, "priority": "high"},
            ])
        
        if skill_levels.get("Algorithms", 0) < 60:
            learning_path.append({"title": "Data Structures & Algorithms", "description": "Arrays, linked lists, trees, graphs, sorting", "duration": "4 weeks", "progress": 0, "priority": "high"})
        
        if skill_levels.get("Web", 0) < 60:
            learning_path.extend([
                {"title": "HTML & CSS", "description": "Web page structure and styling", "duration": "1 week", "progress": 0, "priority": "medium"},
                {"title": "JavaScript Essentials", "description": "Programming for the web", "duration": "2 weeks", "progress": 0, "priority": "medium"},
            ])
        
        if skill_levels.get("Database", 0) < 60:
            learning_path.append({"title": "SQL & Databases", "description": "Database design and queries", "duration": "2 weeks", "progress": 0, "priority": "medium"})
        
        learning_path.append({"title": "Build Projects", "description": "Apply skills with real-world projects", "duration": "3 weeks", "progress": 0, "priority": "high"})
        learning_path.append({"title": "Interview Prep", "description": "Practice coding interviews", "duration": "2 weeks", "progress": 0, "priority": "high"})
    
    elif "data" in goal.lower() or "machine" in goal.lower():
        if skill_levels.get("Python", 0) < 60:
            learning_path.append({"title": "Python for Data Science", "description": "Python fundamentals with data focus", "duration": "2 weeks", "progress": 0, "priority": "high"})
        
        learning_path.extend([
            {"title": "Data Analysis with Pandas", "description": "Data manipulation and analysis", "duration": "2 weeks", "progress": 0, "priority": "high"},
            {"title": "Statistics & Probability", "description": "Essential math for data science", "duration": "3 weeks", "progress": 0, "priority": "high"},
            {"title": "Machine Learning Fundamentals", "description": "Supervised and unsupervised learning", "duration": "4 weeks", "progress": 0, "priority": "high"},
            {"title": "Deep Learning", "description": "Neural networks and TensorFlow/PyTorch", "duration": "4 weeks", "progress": 0, "priority": "medium"},
            {"title": "ML Projects", "description": "Build ML portfolio projects", "duration": "3 weeks", "progress": 0, "priority": "high"},
        ])
    
    else:
        learning_path = [
            {"title": "Foundation Building", "description": "Learn fundamentals based on your goals", "duration": "4 weeks", "progress": 0, "priority": "high"},
            {"title": "Practice & Application", "description": "Apply what you learn", "duration": "4 weeks", "progress": 0, "priority": "medium"},
            {"title": "Advanced Topics", "description": "Deep dive into advanced concepts", "duration": "4 weeks", "progress": 0, "priority": "medium"},
            {"title": "Build Portfolio", "description": "Showcase your skills", "duration": "2 weeks", "progress": 0, "priority": "high"},
        ]
    
    st.session_state.learning_path = learning_path
    
    # Generate curated courses based on results
    generate_curated_courses(learning_path, skill_levels)
    
    return learning_path

def generate_curated_courses(learning_path, skill_levels):
    """Generate curated course recommendations based on learning path and skills"""
    
    all_courses = [
        {"title": "Python for Beginners", "instructor": "Dr. Angela Yu", "duration": "12 hours", "level": "Beginner", "rating": 4.8, "students": 45000, "price": "Free", "tags": ["Python"], "match": 95},
        {"title": "Complete Python Developer", "instructor": "Andrei Neagoie", "duration": "30 hours", "level": "Beginner-Advanced", "rating": 4.9, "students": 80000, "price": "$89", "tags": ["Python", "Web", "Django"], "match": 90},
        {"title": "Data Science Bootcamp", "instructor": "Kirill Eremenko", "duration": "40 hours", "level": "Intermediate", "rating": 4.7, "students": 65000, "price": "$99", "tags": ["Python", "Data Science", "ML"], "match": 85},
        {"title": "Machine Learning A-Z", "instructor": "Kirill Eremenko", "duration": "44 hours", "level": "Intermediate", "rating": 4.5, "students": 85000, "price": "$89", "tags": ["Machine Learning", "Python", "TensorFlow"], "match": 88},
        {"title": "Algorithms & Data Structures", "instructor": "Stephen Grider", "duration": "27 hours", "level": "Intermediate", "rating": 4.8, "students": 55000, "price": "$79", "tags": ["Algorithms", "JavaScript"], "match": 92},
        {"title": "The Web Developer Bootcamp", "instructor": "Colt Steele", "duration": "63 hours", "level": "Beginner", "rating": 4.8, "students": 120000, "price": "$89", "tags": ["Web", "HTML", "CSS", "JavaScript", "Node"], "match": 87},
        {"title": "Modern React with Redux", "instructor": "Stephen Grider", "duration": "27 hours", "level": "Intermediate", "rating": 4.7, "students": 45000, "price": "$79", "tags": ["React", "JavaScript", "Frontend"], "match": 80},
        {"title": "SQL - The Complete Developer's Guide", "instructor": "Academind", "duration": "12 hours", "level": "Beginner-Intermediate", "rating": 4.7, "students": 25000, "price": "$49", "tags": ["SQL", "Database", "PostgreSQL"], "match": 85},
        {"title": "AWS Solutions Architect", "instructor": "Stephane Maarek", "duration": "20 hours", "level": "Intermediate", "rating": 4.7, "students": 55000, "price": "$79", "tags": ["AWS", "Cloud", "DevOps"], "match": 82},
        {"title": "Docker & Kubernetes", "instructor": "Bret Fisher", "duration": "26 hours", "level": "Intermediate", "rating": 4.8, "students": 35000, "price": "$69", "tags": ["Docker", "Kubernetes", "DevOps"], "match": 80},
        {"title": "Deep Learning Specialization", "instructor": "Andrew Ng", "duration": "40 hours", "level": "Advanced", "rating": 4.9, "students": 150000, "price": "$49/month", "tags": ["Deep Learning", "AI", "TensorFlow"], "match": 90},
        {"title": "Full Stack Web Development", "instructor": "Jonas Schmedtmann", "duration": "40 hours", "level": "Intermediate", "rating": 4.8, "students": 35000, "price": "$79", "tags": ["Web", "JavaScript", "Node", "MongoDB"], "match": 88},
    ]
    
    recommended_courses = []
    path_topics = set()
    for item in learning_path:
        title_lower = item["title"].lower()
        if "python" in title_lower: path_topics.add("Python")
        if "algorithm" in title_lower or "data structure" in title_lower: path_topics.add("Algorithms")
        if "web" in title_lower or "javascript" in title_lower or "html" in title_lower: path_topics.add("Web")
        if "machine learning" in title_lower or "ml" in title_lower: path_topics.add("Machine Learning")
        if "data" in title_lower: path_topics.add("Data Science")
        if "database" in title_lower or "sql" in title_lower: path_topics.add("SQL")
        if "aws" in title_lower or "cloud" in title_lower or "devops" in title_lower: path_topics.add("Cloud")
        if "deep" in title_lower or "neural" in title_lower: path_topics.add("Deep Learning")
        if "react" in title_lower: path_topics.add("React")
    
    for course in all_courses:
        for tag in course["tags"]:
            if tag in path_topics or "General" in str(path_topics):
                course["match"] = min(95, course["match"] + 10)
                if course not in recommended_courses:
                    recommended_courses.append(course)
                break
    
    recommended_courses.sort(key=lambda x: x["match"], reverse=True)
    st.session_state.curated_courses = recommended_courses[:6]

def generate_combined_results():
    """Combine assessment and quiz results to generate learning path"""
    return []

# ===============================================================================
# LEARNING PATH (Step 4)
# ===============================================================================
elif st.session_state.current_step == 4:
    st.markdown("## 🛤️ Your Personalized Learning Path")
    st.markdown("Generated from your assessment results and quiz performance.")
    
    if not st.session_state.learning_path:
        st.warning("Complete quizzes to generate your learning path!")
        if st.button("Take Quizzes Now"):
            go_to_step(3)
    else:
        # Show skill analysis
        st.markdown("### 📊 Your Skill Analysis")
        
        skill_levels = st.session_state.combined_results.get("skill_levels", {})
        if skill_levels:
            for skill, level in skill_levels.items():
                st.markdown(f"**{skill}:**")
                st.progress(level / 100)
                st.caption(f"{level:.0f}% proficiency")
        
        st.markdown("---")
        
        # Show learning path
        st.markdown("### 🎯 Your Learning Path")
        
        for i, item in enumerate(st.session_state.learning_path):
            priority_color = "🔴" if item.get("priority") == "high" else "🟡" if item.get("priority") == "medium" else "🟢"
            with st.expander(f"{priority_color} {i+1}. {item['title']} - {item['progress']}% complete"):
                st.markdown(f"**📝 {item['description']}**")
                st.markdown(f"⏱️ **Duration:** {item['duration']}")
                st.markdown(f"**Priority:** {item.get('priority', 'normal').upper()}")
                
                new_progress = st.slider(f"Update progress: {item['title']}", 0, 100, item['progress'], key=f"lp_{i}")
                st.session_state.learning_path[i]['progress'] = new_progress
                st.progress(new_progress / 100)
        
        total_progress = sum(item['progress'] for item in st.session_state.learning_path) / len(st.session_state.learning_path)
        st.markdown(f"### Overall Progress: {total_progress:.0f}%")
        st.progress(total_progress / 100)
        
        # Show curated courses
        if st.session_state.get("curated_courses"):
            st.markdown("---")
            st.markdown("### 📚 Recommended Courses for You")
            st.markdown("Curated based on your assessment and quiz results!")
            
            for course in st.session_state.curated_courses:
                with st.container():
                    col1, col2, col3 = st.columns([3, 1, 1])
                    with col1:
                        st.markdown(f"**{course['title']}**")
                        st.markdown(f"👨‍🏫 {course['instructor']} • ⏱️ {course['duration']}")
                        st.markdown(f"🏷️ {' • '.join(course['tags'])}")
                    with col2:
                        st.markdown(f"**{course['level']}**")
                        st.markdown(f"⭐ {course['rating']}")
                    with col3:
                        st.markdown(f"**{course['price']}**")
                        st.markdown(f"**Match: {course['match']}%**")
                        if st.button(f"Enroll", key=f"enroll_{course['title']}"):
                            st.success(f"Enrolled in {course['title']}!")
                    st.markdown("---")
    
    if st.button("← Back to Dashboard"):
        go_to_step(6)

# ===============================================================================
# COURSES (Step 5) - Shows curated courses
# ===============================================================================
elif st.session_state.current_step == 5:
    st.markdown("## 📚 Course Catalog")
    st.markdown("Browse all available courses or see your curated recommendations.")
    
    # Tabs
    tab1, tab2 = st.tabs(["🎯 Recommended for You", "📚 All Courses"])
    
    with tab1:
        if st.session_state.get("curated_courses"):
            st.markdown("Based on your assessment & quiz results:")
            for course in st.session_state.curated_courses:
                with st.container():
                    col1, col2, col3 = st.columns([3, 1, 1])
                    with col1:
                        st.markdown(f"**{course['title']}**")
                        st.markdown(f"👨‍🏫 {course['instructor']} • ⏱️ {course['duration']}")
                    with col2:
                        st.markdown(f"⭐ {course['rating']}")
                    with col3:
                        st.markdown(f"**{course['price']}**")
                    if st.button(f"Enroll in {course['title']}", key=f"rec_{course['title']}"):
                        st.success(f"Enrolled!")
        else:
            st.info("Complete quizzes to get personalized recommendations!")
    
    with tab2:
        # All courses
        courses_db = [
            {"title": "Python for Beginners", "instructor": "Dr. Angela Yu", "duration": "12 hours", "level": "Beginner", "rating": 4.8, "students": 45000, "price": "Free"},
            {"title": "Complete Python Developer", "instructor": "Andrei Neagoie", "duration": "30 hours", "level": "Beginner-Advanced", "rating": 4.9, "students": 80000, "price": "$89"},
            {"title": "Data Science Bootcamp", "instructor": "Kirill Eremenko", "duration": "40 hours", "level": "Intermediate", "rating": 4.7, "students": 65000, "price": "$99"},
            {"title": "Machine Learning A-Z", "instructor": "Kirill Eremenko", "duration": "44 hours", "level": "Intermediate", "rating": 4.5, "students": 85000, "price": "$89"},
            {"title": "Algorithms & Data Structures", "instructor": "Stephen Grider", "duration": "27 hours", "level": "Intermediate", "rating": 4.8, "students": 55000, "price": "$79"},
            {"title": "The Web Developer Bootcamp", "instructor": "Colt Steele", "duration": "63 hours", "level": "Beginner", "rating": 4.8, "students": 120000, "price": "$89"},
            {"title": "Modern React with Redux", "instructor": "Stephen Grider", "duration": "27 hours", "level": "Intermediate", "rating": 4.7, "students": 45000, "price": "$79"},
            {"title": "SQL - The Complete Developer's Guide", "instructor": "Academind", "duration": "12 hours", "level": "Beginner-Intermediate", "rating": 4.7, "students": 25000, "price": "$49"},
        ]
        
        for course in courses_db:
            with st.container():
                col1, col2, col3 = st.columns([3, 1, 1])
                with col1:
                    st.markdown(f"**{course['title']}**")
                    st.markdown(f"👨‍🏫 {course['instructor']} • ⏱️ {course['duration']}")
                with col2:
                    st.markdown(f"**{course['level']}**")
                    st.markdown(f"⭐ {course['rating']}")
                with col3:
                    st.markdown(f"**{course['price']}**")
                st.markdown("---")
    
    if st.button("← Back to Dashboard"):
        go_to_step(6)

# ===============================================================================
# DASHBOARD (Step 6)
# ===============================================================================
elif st.session_state.current_step == 6:
    st.markdown("## 🎓 Your Learning Dashboard")
    name = st.session_state.user_profile.get("name", "Learner")
    st.markdown(f"Welcome back, {name}! Here's your progress overview.")
    
    # Stats
    col1, col2, col3, col4 = st.columns(4)
    days_active = len(st.session_state.daily_logs)
    total_hours = sum(log.get("hours_spent", 0) for log in st.session_state.daily_logs)
    quiz_count = len(st.session_state.quiz_results)
    avg_score = sum(r.get("percentage", 0) for r in st.session_state.quiz_results.values()) / max(1, len(st.session_state.quiz_results))
    
    with col1:
        st.metric("Days Active", days_active)
    with col2:
        st.metric("Total Hours", f"{total_hours:.1f}h")
    with col3:
        st.metric("Quizzes Done", quiz_count)
    with col4:
        st.metric("Avg Score", f"{avg_score:.0f}%")
    
    st.markdown("---")
    
    # Quick actions
    st.markdown("### 🚀 Quick Actions")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button("📝 Log Learning", use_container_width=True):
            go_to_step(9)
    with col2:
        if st.button("🎯 Take Quiz", use_container_width=True):
            go_to_step(3)
    with col3:
        if st.button("🤖 Ask AI", use_container_width=True):
            go_to_step(7)
    with col4:
        if st.button("📚 Courses", use_container_width=True):
            go_to_step(5)
    
    # Progress
    if st.session_state.learning_path:
        st.markdown("### 🛤️ Learning Path Progress")
        total = sum(item['progress'] for item in st.session_state.learning_path) / len(st.session_state.learning_path)
        st.progress(total / 100)
        st.markdown(f"**{total:.0f}% Complete**")
    
    # Assessment status
    st.markdown("### 📊 Your Assessment Status")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.session_state.assessment_results:
            st.success("✅ Smart Assessment Completed")
        else:
            st.warning("⚠️ Take Smart Assessment")
            if st.button("Start Assessment"):
                go_to_step(2)
    
    with col2:
        if st.session_state.quiz_results:
            st.success(f"✅ {len(st.session_state.quiz_results)} Quizzes Completed")
        else:
            st.warning("⚠️ Take Quizzes")
            if st.button("Start Quizzes"):
                go_to_step(3)

# ===============================================================================
# AI COACH (Step 7)
# ===============================================================================
elif st.session_state.current_step == 7:
    st.markdown("## 🤖 AI Coach")
    st.markdown("Your personal AI learning assistant.")
    
    # Chat display
    for msg in st.session_state.get("chat_history", []):
        if msg["role"] == "user":
            st.markdown(f"**👤 You:** {msg['content']}")
        else:
            st.markdown(f"**🤖 AI Coach:** {msg['content']}")
        st.markdown("---")
    
    question = st.text_input("Ask your AI Coach:")
    
    if st.button("Ask", type="primary") and question:
        if "chat_history" not in st.session_state:
            st.session_state.chat_history = []
        st.session_state.chat_history.append({"role": "user", "content": question})
        
        response = generate_ai_response(question)
        st.session_state.chat_history.append({"role": "ai", "content": response})
        st.rerun()
    
    if st.button("Clear Chat"):
        st.session_state.chat_history = []
        st.rerun()
    
    if st.button("← Back to Dashboard"):
        go_to_step(6)

# ===============================================================================
# PREDICTIONS (Step 8)
# ===============================================================================
elif st.session_state.current_step == 8:
    st.markdown("## 📈 Predictive Analytics")
    st.markdown("AI-powered insights about your learning journey.")
    
    if st.session_state.daily_logs and len(st.session_state.daily_logs) >= 3:
        avg_understanding = sum(log.get("understanding_level", 0) for log in st.session_state.daily_logs) / len(st.session_state.daily_logs)
        avg_productivity = sum(log.get("productivity_rating", 0) for log in st.session_state.daily_logs) / len(st.session_state.daily_logs)
        
        st.markdown("### 🎯 Your Prediction")
        
        if st.session_state.learning_path:
            total_progress = sum(item['progress'] for item in st.session_state.learning_path) / len(st.session_state.learning_path)
            remaining = 100 - total_progress
            
            if avg_understanding >= 7 and avg_productivity >= 7:
                weeks_left = remaining / 15
                st.success(f"🚀 You're excelling! Estimated completion in {weeks_left:.1f} weeks!")
            elif avg_understanding >= 5 and avg_productivity >= 5:
                weeks_left = remaining / 10
                st.info(f"📈 You're on track! Estimated completion in {weeks_left:.1f} weeks.")
            else:
                weeks_left = remaining / 5
                st.warning(f"💪 Keep pushing! Estimated completion in {weeks_left:.1f} weeks.")
    else:
        st.info("Log more activities to get predictions!")
    
    if st.button("← Back to Dashboard"):
        go_to_step(6)

# ===============================================================================
# PROGRESS (Step 9)
# ===============================================================================
elif st.session_state.current_step == 9:
    st.markdown("## 📊 Progress Tracking")
    
    with st.form("log_form"):
        st.markdown("### 📝 Log Today's Learning")
        
        col1, col2 = st.columns(2)
        with col1:
            course = st.text_input("What did you learn?")
            hours = st.slider("Hours spent", 0.5, 12.0, 1.0)
        with col2:
            understanding = st.slider("Understanding (1-10)", 1, 10, 5)
            productivity = st.slider("Productivity (1-10)", 1, 10, 5)
        
        mood = st.selectbox("How do you feel?", ["😊 Great", "🙂 Good", "😐 Okay", "😔 Struggling"])
        
        if st.form_submit_button("Save Log", type="primary"):
            st.session_state.daily_logs.append({
                "date": datetime.now().strftime("%Y-%m-%d"),
                "learning_course": course,
                "hours_spent": hours,
                "understanding_level": understanding,
                "productivity_rating": productivity,
                "mood": mood
            })
            st.success("Activity logged!")
            go_to_step(6)
    
    if st.button("← Back to Dashboard"):
        go_to_step(6)

# ===============================================================================
# SETTINGS (Step 10)
# ===============================================================================
elif st.session_state.current_step == 10:
    st.markdown("## ⚙️ Settings")
    
    st.markdown("### 👤 Your Profile")
    st.json(st.session_state.user_profile)
    
    st.markdown("### 📝 Assessment & Quiz Results")
    if st.session_state.assessment_results:
        st.markdown("**Assessment:** Completed")
    if st.session_state.quiz_results:
        for quiz, result in st.session_state.quiz_results.items():
            st.markdown(f"**{quiz}:** {result['score']}/{result['total']}")
    
    st.markdown("### 💾 Data Management")
    
    if st.button("Export My Data"):
        data = {
            "profile": st.session_state.user_profile,
            "assessment_results": st.session_state.assessment_results,
            "quiz_results": st.session_state.quiz_results,
            "daily_logs": st.session_state.daily_logs,
            "learning_path": st.session_state.learning_path
        }
        st.download_button("Download JSON", json.dumps(data, indent=2), "learnpath_data.json")
    
    if st.button("← Back to Dashboard"):
        go_to_step(6)

# ===============================================================================
# AI RESPONSE GENERATOR
# ===============================================================================
def generate_ai_response(question, topic="general"):
    question = question.lower()
    
    responses = {
        "python": {"default": "Python is a versatile, high-level programming language known for its readability.", "variable": "A variable is a named container that stores data in memory.", "function": "A function is a reusable block of code. Use 'def' to create one."},
        "javascript": {"default": "JavaScript is the language of the web.", "variable": "Use 'let' or 'const' to declare variables.", "function": "Functions can be declared as 'function name()' or as arrow functions."},
        "ml": {"default": "Machine Learning is a subset of AI that enables systems to learn from data.", "supervised": "Supervised learning uses labeled data to train models.", "neural": "Neural networks are inspired by the human brain."},
        "web": {"default": "Web development involves creating websites and applications.", "html": "HTML provides structure to web pages.", "css": "CSS handles styling and layout."},
    }
    
    for t in responses:
        if t in question:
            topic_responses = responses[t]
            for key, value in topic_responses.items():
                if key in question:
                    return value
            return topic_responses.get("default", "I'm here to help!")
    
    return "I'm here to help! Could you please rephrase your question?"

# ===============================================================================
# FOOTER
# ===============================================================================
st.divider()
st.markdown("""
    <div style="text-align: center; color: #64748b; font-size: 13px; padding: 24px;">
        <p style="margin: 0;">🎓 LearnPath © 2024 · AI-Powered Personalized Learning System</p>
    </div>
""", unsafe_allow_html=True)
