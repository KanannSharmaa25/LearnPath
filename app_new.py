import streamlit as st
import json
from datetime import datetime

try:
    from styles import load_styles
    load_styles()
except:
    pass

st.set_page_config(page_title="LearnPath", page_icon="🎓", layout="wide")

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
if "assessment_answers" not in st.session_state:
    st.session_state.assessment_answers = {}
if "quiz_batch_scores" not in st.session_state:
    st.session_state.quiz_batch_scores = {}

def go_to_step(step):
    st.session_state.current_step = step
    st.rerun()

# Global theme CSS
st.markdown("""
<style>
/* Purple Theme */
:root {
    --bg-primary: #f5f3ff;
    --bg-secondary: #ede9fe;
    --bg-card: #ffffff;
    --text-primary: #1e1b4b;
    --text-secondary: #6b7280;
    --accent-primary: #8b5cf6;
    --accent-secondary: #a78bfa;
    --accent-dark: #7c3aed;
    --accent-light: #ede9fe;
    --border-color: #ddd6fe;
}

[data-testid="stAppViewContainer"] { 
    background: var(--bg-primary) !important; 
}

.stApp {
    background: var(--bg-primary) !important;
}

/* Typography */
h1, h2, h3, h4, h5, h6 {
    color: var(--text-primary) !important;
}

/* Labels and general text - make readable */
.stTextInput label,
.stSelectbox label,
.stTextArea label,
.stCheckbox label,
p, span:not([class]), div:not([class]) {
    color: #374151 !important;
}

/* Make sure input text is always dark */
input[type="text"],
input[type="number"],
input[type="email"],
input[type="password"],
textarea,
select {
    color: #1e1b4b !important;
}

/* Cards */
.stCard, .card {
    background: var(--bg-card) !important;
    border: 1px solid var(--border-color) !important;
    border-radius: 16px !important;
    box-shadow: 0 2px 8px rgba(139,92,246,0.1) !important;
}

/* Buttons */
.stButton > button {
    background: linear-gradient(135deg, #8b5cf6, #7c3aed) !important;
    color: white !important;
    border: none !important;
    border-radius: 12px !important;
    font-weight: 600 !important;
    padding: 12px 28px !important;
    box-shadow: 0 4px 12px rgba(139,92,246,0.3) !important;
    transition: all 0.3s ease !important;
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 20px rgba(139,92,246,0.4) !important;
    background: linear-gradient(135deg, #a78bfa, #8b5cf6) !important;
}

/* White input styling with visible text */
.stTextInput input,
.stTextArea textarea,
.stSelectbox input,
.stNumberInput input,
.stDateInput input {
    background-color: white !important;
    color: #1e1b4b !important;
    border: 2px solid #ddd6fe !important;
    border-radius: 8px !important;
    padding: 12px 14px !important;
}

.stTextInput input:focus,
.stTextArea textarea:focus {
    border-color: #8b5cf6 !important;
    box-shadow: 0 0 0 3px rgba(139, 92, 246, 0.15) !important;
}

.stTextArea textarea {
    border-radius: 8px !important;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: white !important;
    border-right: 1px solid var(--border-color) !important;
}

section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3 {
    color: var(--accent-primary) !important;
}

/* Metrics */
[data-testid="stMetric"] {
    background: var(--bg-card);
    border: 1px solid var(--border-color);
    border-radius: 16px;
    padding: 20px;
}

/* Progress bars */
.stProgress > div > div > div {
    background: linear-gradient(90deg, #8b5cf6, #a78bfa) !important;
    border-radius: 10px !important;
}

/* Tabs */
.stTabs [data-baseweb="tab"] {
    background: var(--bg-card) !important;
    border: 1px solid var(--border-color) !important;
    border-radius: 12px 12px 0 0 !important;
    color: var(--text-secondary) !important;
}

.stTabs [data-baseweb="tab"][aria-selected="true"] {
    background: var(--accent-light) !important;
    border-color: var(--accent-primary) !important;
    color: var(--accent-primary) !important;
}

/* Expanders */
[data-testid="stExpander"] {
    background: var(--bg-card) !important;
    border: 1px solid var(--border-color) !important;
    border-radius: 16px !important;
}

/* Alerts */
.stSuccess {
    background: #dcfce7 !important;
    border: 1px solid #86efac !important;
    color: #166534 !important;
    border-radius: 12px !important;
}

.stInfo {
    background: var(--accent-light) !important;
    border: 1px solid var(--accent-secondary) !important;
    color: var(--accent-dark) !important;
    border-radius: 12px !important;
}

.stWarning {
    background: #fef3c7 !important;
    border: 1px solid #fcd34d !important;
    color: #92400e !important;
    border-radius: 12px !important;
}

.stError {
    background: #fee2e2 !important;
    border: 1px solid #fca5a5 !important;
    color: #991b1b !important;
    border-radius: 12px !important;
}

/* Slider */
.stSlider [data-baseweb="slider"] {
    color: var(--accent-primary) !important;
}

/* Scrollbar */
::-webkit-scrollbar { width: 8px; }
::-webkit-scrollbar-track { background: var(--bg-primary); }
::-webkit-scrollbar-thumb { background: #c4b5fd; border-radius: 4px; }
::-webkit-scrollbar-thumb:hover { background: #a78bfa; }

/* Hide default elements */
#MainMenu { visibility: hidden; }
footer { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# SIDEBAR
if st.session_state.current_step != 0:
    st.markdown("""
    <style>
    section[data-testid="stSidebar"] {
        background: white !important;
        border-right: 1px solid #e2e8f0 !important;
    }
    section[data-testid="stSidebar"] h3 {
        color: #8b5cf6 !important;
        font-weight: 700;
    }
    [data-testid="stSidebarNav"] {
        background: #f5f3ff;
        border-radius: 12px;
        padding: 8px;
    }
    </style>
    """, unsafe_allow_html=True)
    
    with st.sidebar:
        st.markdown("### 🧭 Navigation")
        nav = [
            ("🏠 Dashboard",6),
            ("👤 Profile",1),
            ("📝 Assessment",2),
            ("📋 Quizzes",3),
            ("🛤️ Learning Path",4),
            ("📚 Courses",5),
            ("🤖 AI Coach",7),
            ("📈 Predictions",8),
            ("📊 Progress",9),
            ("⚙️ Settings",10)
        ]
        for l,s in nav:
            idx = nav.index((l,s)) + 1
            bg = '#ede9fe' if st.session_state.current_step == s else 'white'
            border = '#8b5cf6' if st.session_state.current_step == s else '#e2e8f0'
            color = '#7c3aed' if st.session_state.current_step == s else '#64748b'
            st.markdown(f"""
            <style>
            [data-testid="stSidebarNav"] button:nth-of-type({idx}) {{
                background: {bg} !important;
                border: 1px solid {border} !important;
                border-radius: 12px !important;
                color: {color} !important;
                padding: 12px 16px !important;
                margin: 4px 0 !important;
                font-weight: 600 !important;
                transition: all 0.3s ease !important;
            }}
            [data-testid="stSidebarNav"] button:nth-of-type({idx}):hover {{
                background: #ede9fe !important;
                border-color: #8b5cf6 !important;
                color: #7c3aed !important;
            }}
            </style>
            """, unsafe_allow_html=True)
            if st.button(l, use_container_width=True, key=f"nav_{s}"):
                go_to_step(s)

# ----------------------------------------------------
# LANDING PAGE
# ----------------------------------------------------

if st.session_state.current_step == 0:

    st.markdown("""
    <style>
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-20px); }
    }
    @keyframes pulse {
        0%, 100% { transform: scale(1); opacity: 1; }
        50% { transform: scale(1.05); opacity: 0.9; }
    }
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(40px); }
        to { opacity: 1; transform: translateY(0); }
    }
    @keyframes fadeInLeft {
        from { opacity: 0; transform: translateX(-40px); }
        to { opacity: 1; transform: translateX(0); }
    }
    @keyframes fadeInRight {
        from { opacity: 0; transform: translateX(40px); }
        to { opacity: 1; transform: translateX(0); }
    }
    @keyframes scaleIn {
        from { opacity: 0; transform: scale(0.8); }
        to { opacity: 1; transform: scale(1); }
    }
    @keyframes shimmer {
        0% { background-position: -200% 0; }
        100% { background-position: 200% 0; }
    }
    @keyframes bounce {
        0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
        40% { transform: translateY(-20px); }
        60% { transform: translateY(-10px); }
    }
    @keyframes rotate {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
    }
    @keyframes wiggle {
        0%, 100% { transform: rotate(0deg); }
        25% { transform: rotate(-5deg); }
        75% { transform: rotate(5deg); }
    }
    @keyframes glow {
        0%, 100% { box-shadow: 0 0 20px rgba(139,92,246,0.3); }
        50% { box-shadow: 0 0 40px rgba(139,92,246,0.6); }
    }
    @keyframes slideInFromBottom {
        from { opacity: 0; transform: translateY(100px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .landing-container {
        min-height: 100vh;
        padding: 0 20px;
        background: #f5f3ff;
        overflow-x: hidden;
    }
    .floating-bg {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: 0;
        overflow: hidden;
    }
    .floating-circle {
        position: absolute;
        border-radius: 50%;
        background: linear-gradient(135deg, rgba(139,92,246,0.1), rgba(167,139,250,0.1));
        animation: float 6s ease-in-out infinite, pulse 4s ease-in-out infinite;
    }
    .floating-circle:nth-child(1) { width: 300px; height: 300px; top: 10%; left: -50px; animation-delay: 0s; }
    .floating-circle:nth-child(2) { width: 200px; height: 200px; top: 60%; right: -30px; animation-delay: 1s; }
    .floating-circle:nth-child(3) { width: 150px; height: 150px; bottom: 20%; left: 10%; animation-delay: 2s; }
    .hero-section {
        position: relative;
        z-index: 1;
        text-align: center;
        padding: 80px 20px 60px;
    }
    .main-title {
        font-size: 72px;
        font-weight: 900;
        background: linear-gradient(135deg, #8b5cf6, #a78bfa, #8b5cf6, #7c3aed);
        background-size: 300% 300%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 20px;
        letter-spacing: -3px;
        animation: gradientShift 4s ease infinite, fadeInUp 1s ease-out;
    }
    .title-icon {
        display: inline-block;
        animation: bounce 2s ease-in-out infinite, wiggle 3s ease-in-out infinite;
        margin-right: 10px;
    }
    .main-subtitle {
        font-size: 22px;
        color: #6b7280;
        max-width: 700px;
        margin: 0 auto 50px;
        line-height: 1.7;
        animation: fadeInUp 1s ease-out 0.3s both;
    }
    .stats-row {
        display: flex;
        justify-content: center;
        gap: 40px;
        margin: 50px 0;
        flex-wrap: wrap;
    }
    .stat-box {
        background: white;
        border: 2px solid #ddd6fe;
        border-radius: 24px;
        padding: 32px 48px;
        text-align: center;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        box-shadow: 0 4px 16px rgba(139,92,246,0.1);
        animation: fadeInUp 0.8s ease-out both;
        position: relative;
        overflow: hidden;
    }
    .stat-box::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(139,92,246,0.1), transparent);
        animation: shimmer 3s infinite;
    }
    .stat-box:nth-child(1) { animation-delay: 0.5s; }
    .stat-box:nth-child(2) { animation-delay: 0.7s; }
    .stat-box:nth-child(3) { animation-delay: 0.9s; }
    .stat-box:hover {
        transform: translateY(-12px) scale(1.05) rotate(2deg);
        border-color: #8b5cf6;
        box-shadow: 0 25px 60px rgba(139,92,246,0.3);
        animation: glow 2s ease-in-out infinite;
    }
    .stat-box:hover .stat-number {
        animation: pulse 0.5s ease-in-out;
    }
    .stat-number {
        font-size: 48px;
        font-weight: 800;
        color: #8b5cf6;
        transition: all 0.3s ease;
    }
    .stat-label {
        font-size: 13px;
        color: #6b7280;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        margin-top: 8px;
    }
    .features-section {
        position: relative;
        z-index: 1;
        padding: 40px 0;
    }
    .section-title {
        font-size: 38px;
        font-weight: 700;
        color: #1e1b4b;
        text-align: center;
        margin-bottom: 40px;
        animation: fadeInUp 0.8s ease-out;
    }
    .features-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 24px;
        max-width: 1200px;
        margin: 0 auto;
    }
    .feature-card {
        background: white;
        border: 1px solid #ddd6fe;
        border-radius: 28px;
        padding: 40px 28px;
        text-align: center;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        box-shadow: 0 2px 8px rgba(139,92,246,0.08);
        animation: scaleIn 0.6s ease-out both;
        position: relative;
        overflow: hidden;
    }
    .feature-card::after {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(139,92,246,0.1) 0%, transparent 70%);
        opacity: 0;
        transition: opacity 0.5s ease;
        pointer-events: none;
    }
    .feature-card:nth-child(1) { animation-delay: 0.2s; }
    .feature-card:nth-child(2) { animation-delay: 0.4s; }
    .feature-card:nth-child(3) { animation-delay: 0.6s; }
    .feature-card:nth-child(4) { animation-delay: 0.8s; }
    .feature-card:hover {
        transform: translateY(-16px) scale(1.02);
        border-color: #8b5cf6;
        box-shadow: 0 30px 70px rgba(139,92,246,0.2);
    }
    .feature-card:hover::after {
        opacity: 1;
    }
    .feature-card:hover .feature-icon {
        animation: bounce 0.8s ease-in-out, rotate 2s ease-in-out;
    }
    .feature-icon {
        font-size: 56px;
        margin-bottom: 16px;
        transition: all 0.3s ease;
    }
    .feature-title {
        font-size: 20px;
        font-weight: 700;
        color: #1e1b4b;
        margin: 12px 0 10px;
    }
    .feature-desc {
        font-size: 14px;
        color: #6b7280;
        line-height: 1.5;
    }
    .steps-section {
        position: relative;
        z-index: 1;
        padding: 50px 0;
        background: #ede9fe;
        margin: 40px -20px;
        padding: 60px 20px;
        animation: slideInFromBottom 1s ease-out;
    }
    .steps-grid {
        display: flex;
        justify-content: center;
        gap: 24px;
        flex-wrap: wrap;
        max-width: 1000px;
        margin: 0 auto;
    }
    .step-card {
        background: white;
        border: 1px solid #ddd6fe;
        border-radius: 24px;
        padding: 32px 24px;
        text-align: center;
        min-width: 160px;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        animation: fadeInUp 0.8s ease-out both;
        position: relative;
    }
    .step-card::before {
        content: '';
        position: absolute;
        bottom: 0;
        left: 50%;
        transform: translateX(-50%);
        width: 0;
        height: 3px;
        background: linear-gradient(90deg, #8b5cf6, #a78bfa);
        transition: width 0.4s ease;
    }
    .step-card:nth-child(1) { animation-delay: 0.3s; }
    .step-card:nth-child(2) { animation-delay: 0.5s; }
    .step-card:nth-child(3) { animation-delay: 0.7s; }
    .step-card:nth-child(4) { animation-delay: 0.9s; }
    .step-card:nth-child(5) { animation-delay: 1.1s; }
    .step-card:hover {
        transform: translateY(-10px) rotate(-2deg);
        border-color: #8b5cf6;
        box-shadow: 0 15px 40px rgba(139,92,246,0.2);
    }
    .step-card:hover::before {
        width: 80%;
    }
    .step-card:hover .step-number {
        animation: bounce 0.6s ease-in-out;
    }
    .step-card:hover .step-icon {
        animation: wiggle 0.5s ease-in-out;
    }
    .step-number {
        width: 52px;
        height: 52px;
        background: linear-gradient(135deg, #8b5cf6, #7c3aed);
        border-radius: 16px;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        font-size: 24px;
        font-weight: 800;
        color: white;
        margin-bottom: 16px;
        box-shadow: 0 8px 25px rgba(139,92,246,0.3);
        transition: all 0.3s ease;
    }
    .step-icon {
        font-size: 36px;
        display: block;
        margin-bottom: 10px;
        transition: all 0.3s ease;
    }
    .step-text {
        font-size: 14px;
        color: #6b7280;
    }
    .cta-section {
        position: relative;
        z-index: 1;
        text-align: center;
        padding: 60px 20px 80px;
    }
    .cta-btn {
        display: inline-block;
        background: linear-gradient(135deg, #8b5cf6, #7c3aed);
        color: white;
        font-weight: 700;
        font-size: 20px;
        padding: 22px 60px;
        border-radius: 60px;
        box-shadow: 0 12px 45px rgba(139,92,246,0.4);
        border: none;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        text-decoration: none;
        cursor: pointer;
        animation: pulse 2s ease-in-out infinite, fadeInUp 1s ease-out 1.5s both;
        position: relative;
        overflow: hidden;
    }
    .cta-btn::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
        transition: left 0.6s ease;
    }
    .cta-btn:hover {
        transform: translateY(-6px) scale(1.08);
        box-shadow: 0 25px 70px rgba(139,92,246,0.5);
        animation: glow 1.5s ease-in-out infinite;
    }
    .cta-btn:hover::before {
        left: 100%;
    }
    .divider {
        height: 1px;
        background: linear-gradient(90deg, transparent, #ddd6fe, transparent);
        margin: 40px auto;
        max-width: 800px;
        animation: scaleIn 1s ease-out 1.3s both;
    }
    @media (max-width: 768px) {
        .features-grid { grid-template-columns: repeat(2, 1fr); }
        .main-title { font-size: 48px; }
        .stat-box { padding: 24px 32px; }
        .stat-number { font-size: 36px; }
    }
    </style>
    """, unsafe_allow_html=True)
    
    landing_html = """
    <div class="landing-container">
        <div class="floating-bg">
            <div class="floating-circle"></div>
            <div class="floating-circle"></div>
            <div class="floating-circle"></div>
        </div>
        <div class="hero-section">
            <h1 class="main-title"><span class="title-icon">🎓</span>LearnPath</h1>
            <p class="main-subtitle">Your AI-powered learning companion that analyzes your unique psychology, learning style, and career goals to create a personalized learning journey just for you.</p>
            
            <div class="stats-row">
                <div class="stat-box">
                    <div class="stat-number">50K+</div>
                    <div class="stat-label">Active Learners</div>
                </div>
                <div class="stat-box">
                    <div class="stat-number">500+</div>
                    <div class="stat-label">Expert Courses</div>
                </div>
                <div class="stat-box">
                    <div class="stat-number">95%</div>
                    <div class="stat-label">Success Rate</div>
                </div>
            </div>
        </div>
        
        <div class="features-section">
            <h2 class="section-title">What We Offer</h2>
            <div class="features-grid">
                <div class="feature-card">
                    <div class="feature-icon">🧠</div>
                    <div class="feature-title">Deep Psychology Assessment</div>
                    <div class="feature-desc">Understand your learning psychology, interests, and how you work under pressure</div>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">📋</div>
                    <div class="feature-title">Knowledge Quizzes</div>
                    <div class="feature-desc">Test yourself across 8 topics with 250+ expert-curated questions</div>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">🛤️</div>
                    <div class="feature-title">AI Learning Path</div>
                    <div class="feature-desc">Personalized roadmap based on your psychology, skills, and goals</div>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">🎯</div>
                    <div class="feature-title">Curated Courses</div>
                    <div class="feature-desc">Expert-selected courses matched to your unique learning needs</div>
                </div>
            </div>
        </div>
        
        <div class="steps-section">
            <h2 class="section-title">Your Journey</h2>
            <div class="steps-grid">
                <div class="step-card">
                    <div class="step-number">1</div>
                    <span class="step-icon">👤</span>
                    <div class="step-text">Create Profile</div>
                </div>
                <div class="step-card">
                    <div class="step-number">2</div>
                    <span class="step-icon">🧠</span>
                    <div class="step-text">Psychology Assessment</div>
                </div>
                <div class="step-card">
                    <div class="step-number">3</div>
                    <span class="step-icon">📋</span>
                    <div class="step-text">Knowledge Quizzes</div>
                </div>
                <div class="step-card">
                    <div class="step-number">4</div>
                    <span class="step-icon">🛤️</span>
                    <div class="step-text">Get Your Path</div>
                </div>
                <div class="step-card">
                    <div class="step-number">5</div>
                    <span class="step-icon">📚</span>
                    <div class="step-text">Learn & Grow</div>
                </div>
            </div>
        </div>
        
        <div class="cta-section">
            <div class="divider"></div>
        </div>
    </div>
    """
    
    st.html(landing_html)
    
    if st.button("🎯 Start Your Journey", type="primary", use_container_width=True):
        go_to_step(1)

# ----------------------------------------------------
# PROFILE
# ----------------------------------------------------

elif st.session_state.current_step == 1:

    st.markdown("## 👤 Create Your Profile")
    st.markdown("*Tell us about yourself so we can personalize your learning experience.*")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("### Personal Info")
        name = st.text_input("Full Name", placeholder="Enter your name")
        email = st.text_input("Email (optional)", placeholder="your@email.com")
        age = st.selectbox("Age Range", ["Under 18", "18-24", "25-34", "35-44", "45-54", "55+"])
        gender = st.selectbox("Gender (optional)", ["Prefer not to say", "Male", "Female", "Non-binary", "Other"])

    with c2:
        st.markdown("### Background")
        edu = st.selectbox("Education Level", ["High School", "Some College", "Associate's", "Bachelor's", "Master's", "PhD", "Other"])
        field = st.selectbox("Field of Study", ["Computer Science", "Engineering", "Business", "Arts & Design", "Mathematics", "Science", "Healthcare", "Other", "Not applicable"])
        role = st.selectbox("Current Role", ["Student", "Employed Full-time", "Employed Part-time", "Freelancer", "Career Switcher", "Unemployed", "Retired", "Other"])
        experience = st.slider("Years of Experience", 0, 20, 0)

    with c3:
        st.markdown("### Learning Preferences")
        goal = st.selectbox("Primary Goal", ["Get a job in tech", "Switch careers", "Advance in current role", "Build personal projects", "Start a business", "Personal growth", "Other"])
        style = st.multiselect("Learning Style", ["Visual", "Auditory", "Reading/Writing", "Kinesthetic", "Social", "Solitary"], default=["Visual"])
        hours = st.slider("Daily Learning Hours", 0.5, 12.0, 2.0, step=0.5)
        tech = st.slider("Tech Comfort Level", 1, 10, 5)

    st.markdown("---")
    st.markdown("### Additional Details")

    c4, c5, c6 = st.columns(3)

    with c4:
        st.markdown("##### Work & Schedule")
        work_env = st.selectbox("Work Environment", ["Remote", "Office", "Hybrid", "Field Work", "Varies", "Not applicable"])
        schedule = st.multiselect("Available Times", ["Weekday Mornings", "Weekday Afternoons", "Weekday Evenings", "Weekends", "Flexible"], default=["Flexible"])
        commute = st.slider("Daily Commute (mins)", 0, 120, 30)

    with c5:
        st.markdown("##### Career & Skills")
        interest = st.selectbox("Tech Interest", ["Web Development", "Mobile Development", "Data Science/ML", "Cloud/DevOps", "Cybersecurity", "UI/UX Design", "Game Development", "Not sure yet"])
        current_skills = st.multiselect("Current Skills", ["Python", "JavaScript", "HTML/CSS", "SQL", "Java", "C/C++", "Go/Rust", "None yet"], default=[])
        certifications = st.selectbox("Certifications", ["None", "AWS Certified", "Google Certified", "Microsoft Certified", "Other", "Working on it"])

    with c6:
        st.markdown("##### Lifestyle & Motivation")
        stress = st.slider("Stress Tolerance (1-10)", 1, 10, 5)
        motivation = st.selectbox("Motivation Source", ["Career growth", "Money/Financial", "Passion for tech", "Problem solving", "Helping others", "Recognition", "Other"])
        constraints = st.multiselect("Constraints", ["Limited time", "Budget limited", "No tech background", "Family responsibilities", "Health issues", "None"], default=[])

    st.markdown("---")

    if st.button("Save & Continue", type="primary", use_container_width=True):
        st.session_state.user_profile = {
            "name": name,
            "email": email,
            "age": age,
            "gender": gender,
            "education": edu,
            "field": field,
            "role": role,
            "experience": experience,
            "goal": goal,
            "style": style,
            "hours": hours,
            "tech": tech,
            "work_env": work_env,
            "schedule": schedule,
            "commute": commute,
            "interest": interest,
            "current_skills": current_skills,
            "certifications": certifications,
            "stress": stress,
            "motivation": motivation,
            "constraints": constraints
        }
        st.success("Profile saved! Let's continue with the assessment.")
        go_to_step(2)

# ----------------------------------------------------
# ASSESSMENT
# ----------------------------------------------------

elif st.session_state.current_step == 2:

    st.markdown("## 🧠 Smart Assessment")
    st.markdown("*Answer these questions to help us understand your psychology, learning style, and work habits.*")

    # Initialize assessment page
    if "assessment_page" not in st.session_state:
        st.session_state.assessment_page = 0
    if "assessment_answers" not in st.session_state:
        st.session_state.assessment_answers = {}

    # All assessment questions grouped
    questions = [
        # Page 1: Background (10 questions)
        ("Background & Education", [
            ("What's your highest education level?", ["High School","Some College","Bachelor's","Master's","PhD","Other"]),
            ("What field is your education in?", ["Computer Science","Engineering","Business","Arts & Design","Mathematics","Science","Other","Not applicable"]),
            ("How long has it been since your last formal study?", ["Currently studying","Less than 1 year","1-3 years","3-5 years","5-10 years","10+ years"]),
            ("Do you have any professional certifications?", ["Yes, in technology","Yes, in another field","No certifications","Currently pursuing certifications"]),
            ("What's your current work situation?", ["Employed full-time","Employed part-time","Self-employed / Freelancer","Student","Unemployed and seeking work","Unemployed by choice"]),
            ("How many years of professional experience do you have?", ["No experience","Less than 1 year","1-3 years","3-5 years","5-10 years","10+ years"]),
            ("What's your typical work environment?", ["Remote / Work from home","Office","Hybrid (mix)","Field work","Varies frequently"]),
            ("How would you describe your work pace?", ["Fast-paced with tight deadlines","Moderate pace","Steady and predictable","Slow-paced","It varies significantly"]),
            ("What's your current role/position?", ["Junior/Entry-level","Mid-level","Senior","Lead/Manager","Executive","Not applicable"]),
            ("Do you work in tech-related field?", ["Yes, fully tech","Yes, partially tech","No, not tech","Student"]),
        ]),
        # Page 2: Work Under Pressure (10 questions)
        ("Work Under Pressure & Deadlines", [
            ("When facing a tight deadline, you typically:", ["Work faster and more focused","Feel motivated but stressed","Get anxious and procrastinate","Ask for deadline extension","Break it into smaller tasks"]),
            ("How do you perform under time pressure?", ["Excel - do my best work","Adequate - complete but stressed","Struggle - make more mistakes","Need breaks to stay effective","Avoid time pressure when possible"]),
            ("When multiple urgent tasks come at once, you:", ["Create a priority list and execute","Tackle them simultaneously","Feel overwhelmed and freeze","Delegate what you can","Work on whichever feels most urgent"]),
            ("How do you handle unexpected challenges right before a deadline?", ["Quickly adapt and problem-solve","Think through options carefully","Seek help immediately","Feel paralyzed and panic","Document and escalate the issue"]),
            ("When you have a week-long project due in 2 days, you:", ["Start immediately and work non-stop","Plan first, then work efficiently","Feel overwhelmed, then gradually start","Pull an all-nighter","Ask for an extension if possible"]),
            ("How do you handle it when you're falling behind on a deadline?", ["Work overtime to catch up","Adjust scope or quality","Communicate and request extension","Panic and hope for the best","Delegate tasks if possible"]),
            ("When a deadline is unrealistic, you usually:", ["Negotiate for more time","Work late to meet it anyway","Compromise on quality","Escalate to management","Follow instructions regardless"]),
            ("How do you feel when working on last-minute assignments?", ["Energized and focused","Somewhat stressed","Very anxious","Disinterested","Neutral"]),
            ("When approaching a deadline, your typical output:", ["Gets better as pressure increases","Stays consistent","Decreases due to stress","Becomes rushed and error-prone","Varies significantly"]),
            ("How do you prioritize when everything seems urgent?", ["By impact and importance","By deadline proximity","By who's asking","Randomly","I struggle to prioritize"]),
        ]),
        # Page 3: Psychology & Personality (10 questions)
        ("Psychology & Personality", [
            ("How do you typically handle mistakes?", ["Analyze them and learn quickly","Feel discouraged temporarily","Blame external factors","Move on without dwelling","Seek feedback to improve"]),
            ("What motivates you most to learn?", ["Career advancement opportunities","Personal interest and curiosity","Financial improvement","Solving interesting problems","Recognition and praise","Helping others learn"]),
            ("When learning something difficult, you usually:", ["Pushing through until I get it","Take breaks to process","Ask others for help","Look for examples and tutorials","Give up temporarily and try later"]),
            ("How would you describe your self-discipline?", ["Very strong - follow plans strictly","Strong - mostly consistent","Moderate - varies by day","Weak - need external accountability","Very weak - struggle to stay on track"]),
            ("Do you experience impostor syndrome?", ["Never","Rarely","Sometimes","Often","Almost always"]),
            ("How do you respond to constructive criticism?", ["Grateful and use it to improve","Slightly defensive but accept it","Take it personally","Ignore it","Depends on how it's delivered"]),
            ("What's your biggest fear about learning new skills?", ["Not being smart enough","Running out of time","Wasting effort on wrong things","Not knowing where to start","Not seeing results","Nothing - I'm confident"]),
            ("When you fail at something, you:", ["Try again immediately","Take time to recover","Change your approach","Give up on that goal","Learn from it and move on"]),
            ("How do you handle feelings of overwhelm?", ["Break tasks into smaller pieces","Take a break and relax","Seek support from others","Push through regardless","Organize and prioritize"]),
            ("What describes your relationship with failure?", ["A learning opportunity","A temporary setback","Something to avoid","Motivating","I don't experience failure often"]),
        ]),
        # Page 4: Interests & Goals (10 questions)
        ("Interests & Goals", [
            ("What interests you most in tech?", ["Building websites and apps","Data science and AI/ML","Cloud and DevOps","Mobile development","Cybersecurity","Game development","Other"]),
            ("What's your primary learning goal?", ["Get a job in tech","Switch careers successfully","Get promoted at work","Build personal projects","Keep up with industry trends","Explore new technologies"]),
            ("What's your expected timeline to see results?", ["Immediately - within weeks","Short-term - within 1 month","Medium-term - 3-6 months","Long-term - within a year","I'm patient, no rush"]),
            ("How important is earning potential in your learning choices?", ["Very important - top priority","Important but not everything","Somewhat important","Not very important","Not important at all"]),
            ("Do you prefer learning alone or in community?", ["Alone - self-paced learning","With a mentor/teacher","In a group/class","Mix of all approaches","Online community forums"]),
            ("What's your ideal learning environment?", ["Quiet and focused","Collaborative and social","Flexible and varied","Structured and organized","Coffee shop vibes"]),
            ("How do you feel about learning from videos vs reading?", ["Prefer watching videos","Prefer reading","Mix of both","Depends on the topic","Prefer hands-on practice"]),
            ("What type of learner are you?", ["Visual - need diagrams","Auditory - need to hear","Reading/Writing - notes","Kinesthetic - hands-on","Multimodal - mix of all"]),
            ("What rewards keep you motivated?", ["Career advancement","Money","Recognition","Personal satisfaction","Helping others","Knowledge itself"]),
            ("Where do you see yourself in 2 years?", ["Working as a developer","Running my own business","In a leadership role","Freelancing","Still learning and exploring","Other"]),
        ]),
        # Page 5: Time & Productivity (10 questions)
        ("Time Management & Productivity", [
            ("How many hours per day can you realistically commit to learning?", ["Less than 1 hour","1-2 hours","2-4 hours","4-6 hours","More than 6 hours"]),
            ("When do you prefer to learn?", ["Early morning (5-9 AM)","Morning (9-12 PM)","Afternoon (12-5 PM)","Evening (5-9 PM)","Late night (after 9 PM)","Flexible - varies daily"]),
            ("How often do you meet your self-set learning goals?", ["Almost always","Most of the time","About half the time","Rarely","Almost never"]),
            ("What's your biggest obstacle to consistent learning?", ["Lack of time","Procrastination","Lack of motivation","Too many resources/overwhelmed","No clear direction","Other"]),
            ("How do you stay accountable to your learning goals?", ["Track progress in a journal/app","Tell friends/family","Join a community","Hire a coach/mentor","Don't have accountability methods"]),
            ("How do you handle learning when feeling tired after work?", ["Push through anyway","Take a short nap then study","Skip that day","Switch to lighter activities","Use caffeine/energy drinks"]),
            ("What's your best time management technique?", ["Time blocking","Pomodoro technique","To-do lists","No specific technique","Flexible approach"]),
            ("How do you deal with distractions while learning?", ["Use focus apps/website blockers","Embrace them sometimes","Create a dedicated space","Listen to music","Struggle with distractions"]),
            ("When you miss a learning session, you:", ["Catch up the next day","Skip and continue as planned","Feel guilty and beat yourself up","Modify your schedule","It's not a big deal"]),
            ("How do you maintain work-life-learning balance?", ["Strict schedule boundaries","Flexible approach","Learning is my hobby","Struggle to balance","Make work-life balance a priority"]),
        ]),
        # Page 6: Technical Background (8 questions)
        ("Technical Background & Skills", [
            ("How would you rate your current programming knowledge?", ["Expert - can build complex systems","Advanced - build full applications","Intermediate - understand fundamentals","Beginner - just starting out","None - complete beginner"]),
            ("Which technologies are you most comfortable with?", ["Python","JavaScript/TypeScript","Java","C/C++","Go/Rust","SQL/Databases","None of these","Multiple technologies"]),
            ("Have you built and shipped complete projects before?", ["Yes, professionally","Yes, personal projects","Started but didn't finish","No, but have project ideas","No, never tried"]),
            ("What's your debugging approach?", ["Use professional debugging tools","Print statements and logs","Research error messages online","Ask for help immediately","Trial and error until fixed"]),
            ("How comfortable are you with command line?", ["Expert - use daily","Comfortable - use when needed","Basic - occasional use","Uncomfortable - avoid it","Never used it"]),
            ("Have you contributed to open source projects?", ["Yes, regularly","Yes, a few times","No, but want to","No, not interested","Working on it now"]),
            ("How do you typically solve new programming problems?", ["Search documentation","Google/Stack Overflow","Video tutorials","Ask in communities","Trial and error","Read source code"]),
            ("What's your experience with version control?", ["Git expert - daily use","Comfortable - regular use","Basic knowledge","Heard of it","Never used it"]),
        ]),
    ]

    total_pages = len(questions)
    current_page = st.session_state.assessment_page

    # Progress indicator
    progress = (current_page + 1) / total_pages
    st.progress(progress)
    st.markdown(f"**Page {current_page + 1} of {total_pages}** — {questions[current_page][0]}")

    # Display questions for current page
    for i, (question, options) in enumerate(questions[current_page][1]):
        q_key = f"q_{current_page}_{i}"
        st.session_state.assessment_answers[q_key] = st.radio(question, options, key=q_key)

    # Navigation buttons
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col1:
        if current_page > 0:
            if st.button("⬅️ Previous", use_container_width=True):
                st.session_state.assessment_page -= 1
                st.rerun()
    
    with col2:
        if st.button("Clear Answers", use_container_width=True):
            for key in list(st.session_state.assessment_answers.keys()):
                if key.startswith(f"q_{current_page}_"):
                    del st.session_state.assessment_answers[key]
            st.rerun()
    
    with col3:
        if current_page < total_pages - 1:
            if st.button("Next ➡️", type="primary", use_container_width=True):
                st.session_state.assessment_page += 1
                st.rerun()
        else:
            if st.button("Complete Assessment ✅", type="primary", use_container_width=True):
                st.success("Assessment complete! Let's move to the quizzes.")
                go_to_step(3)

# ----------------------------------------------------
# QUIZZES
# ----------------------------------------------------

elif st.session_state.current_step == 3:

    st.markdown("## 📋 Knowledge Quiz")
    st.markdown("*Test your knowledge across different topics. Questions are shown in batches of 10.*")

    QUIZZES = {
        "programming_fundamentals": {
            "title": "Programming Fundamentals",
            "icon": "💻",
            "description": "Variables, loops, functions, debugging",
            "questions": [
                ("What is a variable?", ["A name that stores a value in memory", "A type of programming language", "A function that changes", "A mathematical constant"]),
                ("What does a loop do?", ["Creates an error", "Repeats code multiple times", "Stores data", "Defines a function"]),
                ("What is a function?", ["A variable that stores numbers", "Reusable block of code that performs a task", "A type of data", "A programming error"]),
                ("What is debugging?", ["Writing code", "Finding and fixing errors", "Running a program", "Creating variables"]),
                ("What is an array/list?", ["A single value", "An ordered collection of values", "A function definition", "A type of error"]),
                ("What is a conditional statement?", ["A loop that repeats", "A statement that executes code based on a condition", "A way to store data", "A type of function"]),
                ("What is the purpose of comments in code?", ["Execute faster", "Document and explain code", "Encrypt code", "Store variables"]),
                ("What is code refactoring?", ["Deleting code", "Changing code structure without changing behavior", "Running code faster", "Creating new features only"]),
                ("What is an algorithm?", ["A programming language", "Step-by-step instructions to solve a problem", "A type of data structure", "A software bug"]),
                ("What is object-oriented programming?", ["Writing code in objects", "Programming paradigm using objects and classes", "A text editor feature", "Database management"]),
            ],
            "correct": [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        },
        "problem_solving": {
            "title": "Problem Solving & Logic",
            "icon": "🧩",
            "description": "Logical reasoning and problem decomposition",
            "questions": [
                ("When solving a problem, what's the first step?", ["Start coding immediately", "Understand the problem", "Copy from StackOverflow", "Ask someone else"]),
                ("What's algorithmic complexity?", ["How hard it is to understand", "How much time and space an algorithm needs", "The number of lines of code", "The programming language used"]),
                ("If a task has 2 subtasks (each 5 mins), total time is?", ["5 minutes", "10 minutes", "2.5 minutes", "20 minutes"]),
                ("What's the benefit of breaking problems into smaller parts?", ["Wastes more time", "Makes problems easier to solve", "Confuses the solution", "Reduces code quality"]),
                ("What's edge case handling?", ["Using the edge of your desk", "Testing unusual/extreme inputs", "A programming error", "A type of variable"]),
                ("What's heuristic approach mean?", ["Exact solution always", "Rule-of-thumb approach to find a good solution", "A formal proof", "Copying code"]),
                ("What's greedy algorithm approach?", ["Considering all possibilities", "Making the locally optimal choice at each step", "Random selection", "Backtracking always"]),
                ("Why write pseudocode before coding?", ["To avoid documentation", "To plan logic in plain language", "To test performance", "To compile it"]),
                ("What is recursion?", ["A loop", "Function calling itself", "A data structure", "A sorting method"]),
                ("What is Big O notation used for?", ["Email notation", "Measuring algorithm efficiency", "Mathematical operations", "Sorting data"]),
            ],
            "correct": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        },
        "data_structures": {
            "title": "Data Structures",
            "icon": "🏗️",
            "description": "Arrays, linked lists, trees, graphs",
            "questions": [
                ("What's the main advantage of a Hash Map?", ["Always sorted", "Fast lookups", "Small memory", "Easy to visualize"]),
                ("What's a linked list?", ["A list on the web", "Elements connected by pointers/references", "A type of array", "A database structure"]),
                ("Stack follows which principle?", ["First In First Out (FIFO)", "Last In First Out (LIFO)", "Random order", "Sorted order"]),
                ("Queue follows which principle?", ["LIFO", "FIFO", "Random", "Sorted"]),
                ("What's a tree data structure used for?", ["Growing plants", "Hierarchical data organization", "Storing strings", "Random storage"]),
                ("What's a graph used to model?", ["Hierarchies", "Pairs of connected entities (nodes/edges)", "Linear arrays", "Sorted lists"]),
                ("What's amortized analysis?", ["Worst-case only", "Average cost over sequence of operations", "Space complexity", "A sorting algorithm"]),
                ("What's a priority queue used for?", ["Random access", "Retrieving highest-priority element efficiently", "Sorting strings", "Storing characters"]),
                ("What's the time complexity of array lookup by index?", ["O(n)", "O(1)", "O(log n)", "O(n²)"]),
                ("What data structure uses LIFO?", ["Queue", "Stack", "Array", "Tree"]),
            ],
            "correct": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        },
        "web_development": {
            "title": "Web Development",
            "icon": "🌐",
            "description": "HTML, CSS, JavaScript, APIs",
            "questions": [
                ("What does HTML do?", ["Styles the website", "Structures web content", "Creates interactivity", "Stores data"]),
                ("What's the role of CSS?", ["Structures content", "Styles and layouts", "Creates logic", "Stores databases"]),
                ("What's JavaScript primarily used for?", ["Server storage", "Client-side interactivity", "Database management", "Styling"]),
                ("What's a REST API?", ["A way to take breaks", "A method for server-client communication", "A type of database", "A styling framework"]),
                ("What's responsive design?", ["Quick website loading", "Works on all device sizes", "Uses many colors", "Requires JavaScript"]),
                ("What is the DOM?", ["A styling library", "Document Object Model representing HTML structure", "A database", "A server"]),
                ("What does AJAX allow?", ["Synchronous page reloads", "Background server requests without full reload", "CSS animations", "Python execution in browser"]),
                ("What's accessibility in web design?", ["Using many colors", "Designing for users with diverse abilities", "Faster load times", "SEO only"]),
                ("What is a CDN?", ["Content Delivery Network", "Coding Development Network", "Central Database Node", "Client Data Number"]),
                ("What does API stand for?", ["Application Programming Interface", "Automated Program Integration", "Advanced Protocol Interface", "Application Process Integration"]),
            ],
            "correct": [1, 1, 1, 1, 1, 1, 1, 1, 0, 0]
        },
        "databases": {
            "title": "Databases & SQL",
            "icon": "🗄️",
            "description": "SQL, NoSQL, data modeling",
            "questions": [
                ("What's SQL primarily used for?", ["Website styling", "Querying and managing data", "Building apps", "Creating graphics"]),
                ("What's a primary key?", ["The first column", "Uniquely identifies each row", "A password", "A type of index"]),
                ("What's normalization in databases?", ["Making data normal", "Organizing data to reduce redundancy", "Encrypting data", "Backing up data"]),
                ("What's a JOIN in SQL?", ["Combining rows from multiple tables", "Creating new tables", "Deleting data", "A type of error"]),
                ("What's an index in a database?", ["A table of contents", "A structure for faster searches", "A backup method", "A type of table"]),
                ("What's ACID in databases?", ["A chemical", "Set of transactional properties (Atomicity, Consistency, Isolation, Durability)", "Indexing type", "Compression method"]),
                ("What is denormalization used for?", ["Reducing redundancy", "Improving read performance by duplicating data", "Encrypting data", "Backing up data"]),
                ("What's a transaction log?", ["A user log", "Record of database changes for recovery", "A performance metric", "A query"]),
                ("What is a foreign key?", ["Key outside the database", "References primary key in another table", "User authentication key", "Encryption key"]),
                ("NoSQL databases are best for:", ["Structured data only", "Unstructured/semi-structured data", "Only large enterprises", "Offline applications"]),
            ],
            "correct": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        },
        "python_basics": {
            "title": "Python Basics",
            "icon": "🐍",
            "description": "Python syntax, functions, data types",
            "questions": [
                ("What's Python primarily known for?", ["Web design", "Readability and simplicity", "Gaming", "Graphics"]),
                ("What's a Python virtual environment?", ["A computer in the cloud", "Isolated Python setup for projects", "A game", "A type of file"]),
                ("What does 'pip' do?", ["Installs Python", "Manages Python packages", "Edits code", "Runs programs"]),
                ("What's a Python decorator?", ["A visual element", "Modifies functions or classes", "A type of loop", "A string type"]),
                ("What's list comprehension?", ["Understanding lists", "Concise way to create lists", "A reading technique", "A type of loop"]),
                ("What's a dictionary in Python?", ["An ordered sequence", "Key-value mapping", "A list of functions", "A loop"]),
                ("What's exception handling used for?", ["Optimizing speed", "Handling runtime errors gracefully", "Formatting strings", "Declaring variables"]),
                ("What is a module in Python?", ["A function", "A file containing Python definitions and statements", "A data type", "A package manager"]),
                ("What does 'self' refer to in a class?", ["The class itself", "The current instance", "A global variable", "A parameter"]),
                ("What is 'None' in Python?", ["Zero", "Empty string", "Null value", "False"]),
            ],
            "correct": [1, 1, 1, 1, 1, 1, 1, 1, 1, 2]
        },
        "cloud_computing": {
            "title": "Cloud Computing",
            "icon": "☁️",
            "description": "AWS, Azure, cloud services",
            "questions": [
                ("What is IaaS?", ["Internet as a Service", "Infrastructure as a Service", "Integration as a Service", "Image as a Service"]),
                ("What is SaaS?", ["Software as a Service", "Storage as a Service", "System as a Service", "Server as a Service"]),
                ("What is PaaS?", ["Platform as a Service", "Programming as a Service", "Process as a Service", "Private as a Service"]),
                ("What's serverless computing?", ["No servers exist", "Automatically scaling compute service", "Free computing", "Offline computing"]),
                ("What is auto-scaling?", ["Automatic code compilation", "Automatically adjusting resources based on demand", "Auto-saving files", "Automatic testing"]),
                ("What's a VPC?", ["Virtual Private Cloud", "Very Private Computer", "Virtual Process Container", "Verified Program Code"]),
                ("What is load balancing?", ["Weighing server components", "Distributing network traffic across servers", "Balancing code quality", "Measuring server weight"]),
                ("What is a region in cloud?", ["A country border", "Geographic area with cloud availability zones", "A state", "A server room"]),
                ("What is edge computing?", ["Computing at the edge of networks", "Computing with edges", "Border computing", "Side computing"]),
                ("What's cloud migration?", ["Moving to the sky", "Transferring data/applications to cloud", "Cloudy weather computing", "Data backup"]),
            ],
            "correct": [1, 0, 0, 1, 1, 0, 1, 1, 0, 1]
        },
        "devops": {
            "title": "DevOps & CI/CD",
            "icon": "🔄",
            "description": "CI/CD pipelines, Docker, Kubernetes",
            "questions": [
                ("What is Docker container?", ["Physical shipping container", "Lightweight executable package", "Virtual machine", "Storage unit"]),
                ("What is a Dockerfile?", ["Container runtime", "Script to build container images", "Container registry", "Orchestration tool"]),
                ("What is Kubernetes?", ["Container orchestration platform", "Programming language", "Database system", "Web server"]),
                ("What is a Kubernetes pod?", ["Storage unit", "Smallest deployable unit", "Network protocol", "Container registry"]),
                ("What is container orchestration?", ["Playing music", "Managing containerized applications", "Building containers", "Container storage"]),
                ("What is CI/CD?", ["Continuous Integration/Deployment", "Code library", "Version control", "Database system"]),
                ("What is Git?", ["A programming language", "Version control system", "A database", "An operating system"]),
                ("What does 'git merge' do?", ["Deletes branches", "Combines branch changes", "Creates new repository", "Uploads code"]),
                ("What is Docker image?", ["A running container", "Template to create containers", "Container logs", "Network configuration"]),
                ("What is a container registry?", ["Container storage", "Repository for container images", "Container network", "Container monitoring"]),
            ],
            "correct": [1, 1, 0, 1, 1, 0, 1, 1, 1, 1]
        },
    }

    # Initialize quiz state
    if "quiz_topic" not in st.session_state:
        st.session_state.quiz_topic = None
    if "quiz_batch" not in st.session_state:
        st.session_state.quiz_batch = 0
    if "quiz_answers" not in st.session_state:
        st.session_state.quiz_answers = {}
    if "quiz_batch_scores" not in st.session_state:
        st.session_state.quiz_batch_scores = {}
    if "quiz_submitted" not in st.session_state:
        st.session_state.quiz_submitted = False

    # Show completed quiz summary if all topics done
    completed_topics = list(st.session_state.quiz_batch_scores.keys())
    
    if completed_topics and st.session_state.quiz_topic is None:
        st.markdown("### 📊 Quiz Results Summary")
        
        col1, col2, col3 = st.columns(3)
        scores = list(st.session_state.quiz_batch_scores.values())
        
        with col1:
            st.metric("Topics Completed", len(completed_topics))
        with col2:
            total_correct = sum(s["correct"] for s in scores)
            total_questions = sum(s["total"] for s in scores)
            st.metric("Total Correct", f"{total_correct}/{total_questions}")
        with col3:
            if total_questions > 0:
                st.metric("Average Score", f"{int(100*total_correct/total_questions)}%")
        
        st.markdown("---")
        
        for topic, score_data in st.session_state.quiz_batch_scores.items():
            quiz_info = QUIZZES.get(topic, {})
            st.markdown(f"**{quiz_info.get('icon', '📋')} {quiz_info.get('title', topic)}**: {score_data['correct']}/{score_data['total']} correct ({score_data['score']}%)")
        
        st.markdown("---")
        
        if st.button("Generate My Learning Path", type="primary"):
            go_to_step(4)
        
        st.markdown("---")
        st.markdown("### 📚 Choose Another Quiz Topic")
        
        cols = st.columns(3)
        topics_list = list(QUIZZES.keys())
        
        for idx, topic_key in enumerate(topics_list):
            quiz = QUIZZES[topic_key]
            with cols[idx % 3]:
                st.markdown(f"""
                <div style="background: white; border: 1px solid #ddd6fe; border-radius: 16px; padding: 20px; text-align: center; transition: all 0.3s;">
                    <div style="font-size: 48px; margin-bottom: 12px;">{quiz['icon']}</div>
                    <h4 style="color: #1e1b4b; margin: 8px 0;">{quiz['title']}</h4>
                    <p style="color: #6b7280; font-size: 14px;">{quiz['description']}</p>
                    <p style="color: #8b5cf6; font-size: 12px;">{len(quiz['questions'])} questions</p>
                </div>
                """, unsafe_allow_html=True)
                
                score_display = ""
                if topic_key in st.session_state.quiz_batch_scores:
                    score = st.session_state.quiz_batch_scores[topic_key]["score"]
                    score_display = f" ({score}% completed)"
                    if st.button(f"Retake Quiz{score_display}", key=f"retake_{topic_key}"):
                        st.session_state.quiz_topic = topic_key
                        st.session_state.quiz_batch = 0
                        st.session_state.quiz_submitted = False
                        st.rerun()
                else:
                    if st.button(f"Start Quiz", key=f"start_{topic_key}"):
                        st.session_state.quiz_topic = topic_key
                        st.session_state.quiz_batch = 0
                        st.session_state.quiz_submitted = False
                        st.rerun()
        
        st.markdown("---")
        if st.button("← Back to Dashboard", use_container_width=True):
            go_to_step(6)
        
        st.stop()

    # Topic selection
    if st.session_state.quiz_topic is None:
        st.markdown("### Select a Topic to Test")
        
        cols = st.columns(3)
        topics_list = list(QUIZZES.keys())
        
        for idx, topic_key in enumerate(topics_list):
            quiz = QUIZZES[topic_key]
            with cols[idx % 3]:
                st.markdown(f"""
                <div style="background: white; border: 1px solid #ddd6fe; border-radius: 16px; padding: 20px; text-align: center; transition: all 0.3s;">
                    <div style="font-size: 48px; margin-bottom: 12px;">{quiz['icon']}</div>
                    <h4 style="color: #1e1b4b; margin: 8px 0;">{quiz['title']}</h4>
                    <p style="color: #6b7280; font-size: 14px;">{quiz['description']}</p>
                    <p style="color: #8b5cf6; font-size: 12px;">{len(quiz['questions'])} questions</p>
                </div>
                """, unsafe_allow_html=True)
                
                if topic_key in st.session_state.quiz_batch_scores:
                    score = st.session_state.quiz_batch_scores[topic_key]["score"]
                    st.success(f"Completed: {score}%")
                else:
                    if st.button(f"Start Quiz", key=f"start_{topic_key}"):
                        st.session_state.quiz_topic = topic_key
                        st.session_state.quiz_batch = 0
                        st.session_state.quiz_submitted = False
                        st.rerun()
        
        st.markdown("---")
        if st.button("Skip to Learning Path", type="secondary"):
            go_to_step(4)
    
    # Quiz taking
    else:
        quiz = QUIZZES[st.session_state.quiz_topic]
        all_questions = quiz["questions"]
        correct_answers = quiz["correct"]
        
        # Calculate batches
        batch_size = 10
        total_batches = (len(all_questions) + batch_size - 1) // batch_size
        current_batch = st.session_state.quiz_batch
        
        start_idx = current_batch * batch_size
        end_idx = min(start_idx + batch_size, len(all_questions))
        batch_questions = all_questions[start_idx:end_idx]
        batch_correct = correct_answers[start_idx:end_idx]
        
        st.markdown(f"### {quiz['icon']} {quiz['title']}")
        st.markdown(f"**Batch {current_batch + 1} of {total_batches}** — Questions {start_idx + 1} to {end_idx}")
        
        progress = (current_batch + 1) / total_batches
        st.progress(progress)
        
        # Show batch score if batch completed
        if st.session_state.quiz_submitted:
            batch_score_key = f"{st.session_state.quiz_topic}_batch_{current_batch}"
            if batch_score_key not in st.session_state.quiz_batch_scores:
                answered = [i for i in range(len(batch_questions)) if f"quiz_{start_idx + i}" in st.session_state.quiz_answers]
                correct = sum(1 for i in answered if st.session_state.quiz_answers.get(f"quiz_{start_idx + i}") == batch_correct[i])
                st.session_state.quiz_batch_scores[batch_score_key] = {
                    "correct": correct,
                    "total": len(batch_questions),
                    "score": int(100 * correct / len(batch_questions)) if batch_questions else 0
                }
            
            score = st.session_state.quiz_batch_scores[batch_score_key]
            st.success(f"**Batch Score: {score['correct']}/{score['total']} ({score['score']}%)**")
            
            # Show explanations
            for i, (q, opts) in enumerate(batch_questions):
                user_ans = st.session_state.quiz_answers.get(f"quiz_{start_idx + i}")
                correct_ans = batch_correct[i]
                is_correct = user_ans == correct_ans
                
                with st.expander(f"Q{start_idx + i + 1}: {'✓' if is_correct else '✗'} {q}", expanded=False):
                    st.markdown(f"**Your answer:** {user_ans if user_ans else 'Not answered'}")
                    st.markdown(f"**Correct:** {opts[correct_ans]}")
            
            col1, col2, col3 = st.columns([1, 1, 1])
            with col1:
                if current_batch > 0:
                    if st.button("← Previous Batch", use_container_width=True):
                        st.session_state.quiz_batch -= 1
                        st.session_state.quiz_submitted = False
                        st.rerun()
            with col2:
                if st.button("Back to Topics"):
                    st.session_state.quiz_topic = None
                    st.session_state.quiz_batch = 0
                    st.session_state.quiz_submitted = False
                    st.rerun()
            with col3:
                if current_batch < total_batches - 1:
                    if st.button("Next Batch →", type="primary", use_container_width=True):
                        st.session_state.quiz_batch += 1
                        st.session_state.quiz_submitted = False
                        st.rerun()
                else:
                    if st.button("Finish Quiz ✓", type="primary", use_container_width=True):
                        st.session_state.quiz_topic = None
                        st.rerun()
        else:
            # Show questions
            for i, (q, opts) in enumerate(batch_questions):
                st.session_state.quiz_answers[f"quiz_{start_idx + i}"] = st.radio(
                    f"**Q{start_idx + i + 1}. {q}**",
                    opts,
                    key=f"quiz_{start_idx + i}"
                )
            
            st.markdown("---")
            col1, col2 = st.columns([1, 1])
            with col1:
                if st.button("← Back to Topics", use_container_width=True):
                    st.session_state.quiz_topic = None
                    st.rerun()
            with col2:
                if st.button("Submit Batch ✓", type="primary", use_container_width=True):
                    st.session_state.quiz_submitted = True
                    st.rerun()

# ----------------------------------------------------
# LEARNING PATH
# ----------------------------------------------------

elif st.session_state.current_step == 4:

    st.markdown("## 🛤️ Create Your Learning Path")
    st.markdown("*Compare AI-generated path with your custom path and choose the best one for you.*")

    profile = st.session_state.user_profile
    quiz_scores = st.session_state.quiz_batch_scores

    # Initialize session states
    if "ai_learning_path" not in st.session_state:
        st.session_state.ai_learning_path = []
    if "user_learning_path" not in st.session_state:
        st.session_state.user_learning_path = []
    if "selected_path_type" not in st.session_state:
        st.session_state.selected_path_type = None

    # Analyze quiz results
    weak_areas = []
    strong_areas = []
    if quiz_scores:
        for topic, score_data in quiz_scores.items():
            topic_name = topic.replace("_batch_0", "").replace("_batch_1", "").replace("_batch_2", "").replace("_", " ").title()
            if score_data["score"] < 70:
                weak_areas.append((topic_name, score_data["score"]))
            else:
                strong_areas.append((topic_name, score_data["score"]))

    # Generate AI Learning Path
    def generate_ai_path():
        path = []
        goal = profile.get("goal", "")
        hours = profile.get("hours", 2)
        experience = profile.get("experience", 0)
        weak_topics = [w[0].lower() for w in weak_areas]

        # Core foundational skills
        if experience < 1:
            path.append({"title": "Programming Basics", "duration": "3 weeks", "priority": 1, "icon": "💻", "level": "Beginner", "reason": "Build strong foundation"})
        
        # Goal-based specialization
        if "web" in goal.lower() or "project" in goal.lower():
            path.extend([
                {"title": "HTML & CSS Fundamentals", "duration": "2 weeks", "priority": 1, "icon": "🎨", "level": "Beginner", "reason": "Web development foundation"},
                {"title": "JavaScript Essentials", "duration": "4 weeks", "priority": 1, "icon": "⚡", "level": "Beginner", "reason": "Interactive web development"},
                {"title": "React Framework", "duration": "5 weeks", "priority": 2, "icon": "⚛️", "level": "Intermediate", "reason": "Modern frontend development"},
                {"title": "Backend Development", "duration": "4 weeks", "priority": 2, "icon": "🔗", "level": "Intermediate", "reason": "Full-stack capability"},
            ])
        elif "data" in goal.lower() or "ai" in goal.lower() or "ml" in goal.lower():
            path.extend([
                {"title": "Python Programming", "duration": "4 weeks", "priority": 1, "icon": "🐍", "level": "Beginner", "reason": "Primary language for data/ML"},
                {"title": "Statistics & Mathematics", "duration": "4 weeks", "priority": 1, "icon": "📊", "level": "Intermediate", "reason": "Essential for data science"},
                {"title": "Machine Learning Fundamentals", "duration": "6 weeks", "priority": 2, "icon": "🤖", "level": "Intermediate", "reason": "Core ML concepts"},
                {"title": "Deep Learning", "duration": "6 weeks", "priority": 2, "icon": "🧠", "level": "Advanced", "reason": "Advanced AI techniques"},
            ])
        elif "cloud" in goal.lower() or "devops" in goal.lower():
            path.extend([
                {"title": "Linux Fundamentals", "duration": "3 weeks", "priority": 1, "icon": "🐧", "level": "Beginner", "reason": "Server management basics"},
                {"title": "Docker & Containers", "duration": "3 weeks", "priority": 1, "icon": "📦", "level": "Intermediate", "reason": "Modern deployment"},
                {"title": "Kubernetes", "duration": "4 weeks", "priority": 2, "icon": "☸️", "level": "Intermediate", "reason": "Container orchestration"},
                {"title": "CI/CD Pipelines", "duration": "3 weeks", "priority": 2, "icon": "🔄", "level": "Intermediate", "reason": "Automation skills"},
            ])
        else:
            path.extend([
                {"title": "Python Fundamentals", "duration": "4 weeks", "priority": 1, "icon": "🐍", "level": "Beginner", "reason": "Versatile programming"},
                {"title": "Data Structures", "duration": "4 weeks", "priority": 1, "icon": "🏗️", "level": "Intermediate", "reason": "Problem-solving skills"},
                {"title": "Web Development", "duration": "6 weeks", "priority": 2, "icon": "🌐", "level": "Intermediate", "reason": "Practical applications"},
            ])

        # Address weak areas
        for topic, score in weak_areas:
            if "problem" in topic.lower():
                path.insert(0, {"title": "Problem Solving & Algorithms", "duration": "4 weeks", "priority": 0, "icon": "🧩", "level": "Intermediate", "reason": f"Boost {topic} score (currently {score}%)"})
            if "programming" in topic.lower():
                path.insert(0, {"title": "Programming Fundamentals", "duration": "3 weeks", "priority": 0, "icon": "💻", "level": "Beginner", "reason": f"Strengthen basics (currently {score}%)"})

        # Limit based on time commitment
        if hours < 2:
            path = path[:4]
        elif hours < 4:
            path = path[:6]
        
        for p in path:
            p["progress"] = 0
            p["status"] = "Not Started"
        
        return path

    # Tabs for different sections
    tab1, tab2, tab3, tab4 = st.tabs(["📊 Analysis", "🤖 AI Path", "✏️ Your Path", "⚖️ Compare & Choose"])

    with tab1:
        st.markdown("### 📊 Your Strengths & Weaknesses")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### 💪 Strong Areas")
            if strong_areas:
                for area, score in strong_areas:
                    st.markdown(f"- **{area}**: {score}%")
            else:
                st.info("Complete quizzes to see your strong areas!")
        
        with col2:
            st.markdown("#### 📈 Areas to Improve")
            if weak_areas:
                for area, score in weak_areas:
                    st.markdown(f"- **{area}**: {score}%")
            else:
                st.success("Great job! No weak areas detected.")
        
        st.markdown("---")
        st.markdown("#### 🎯 Profile-Based Insights")
        
        insights = []
        if profile.get("experience", 0) < 1:
            insights.append("You're a beginner - focus on fundamentals first")
        if profile.get("hours", 2) < 2:
            insights.append("Limited daily time - we'll create a focused, efficient path")
        if len(weak_areas) > 2:
            insights.append("Multiple areas need improvement - prioritize strategically")
        
        for insight in insights:
            st.markdown(f"- {insight}")
        
        if st.button("🤖 Generate AI Learning Path", type="primary", use_container_width=True):
            st.session_state.ai_learning_path = generate_ai_path()
            st.success("AI learning path generated!")

    with tab2:
        st.markdown("### 🤖 AI-Generated Learning Path")
        st.markdown("*Based on your assessment, quiz results, and goals*")
        
        if not st.session_state.ai_learning_path:
            st.info("Generate your AI path from the Analysis tab first!")
        else:
            for i, p in enumerate(st.session_state.ai_learning_path):
                with st.expander(f"{p.get('icon', '📚')} {p['title']} - {p.get('duration', '')}"):
                    st.markdown(f"**Level:** {p.get('level', 'N/A')}")
                    st.markdown(f"**Duration:** {p.get('duration', 'N/A')}")
                    st.markdown(f"**Why this:** {p.get('reason', 'Based on your profile')}")
        
        if st.session_state.ai_learning_path:
            if st.button("Use This AI Path", type="primary", use_container_width=True):
                st.session_state.selected_path_type = "ai"
                st.session_state.learning_path = st.session_state.ai_learning_path.copy()
                st.success("AI learning path selected!")

    with tab3:
        st.markdown("### ✏️ Create Your Custom Learning Path")
        st.markdown("*Describe what you want to learn and how*")
        
        user_description = st.text_area(
            "What do you want to learn?",
            placeholder="Example: I want to become a full-stack developer, focusing on Python for backend and React for frontend. I prefer hands-on projects over theory...",
            height=120
        )
        
        col1, col2 = st.columns(2)
        with col1:
            preferred_topics = st.multiselect(
                "Topics you're interested in",
                ["Web Development", "Mobile Development", "Data Science", "Machine Learning", 
                 "Cloud/DevOps", "Cybersecurity", "UI/UX Design", "Backend Development", "Frontend Development"]
            )
        
        with col2:
            learning_style_pref = st.selectbox(
                "Preferred learning style",
                ["Project-based (hands-on)", "Theory-first (concepts)", "Mix of both", "Video tutorials", "Reading documentation"]
            )
        
        preferred_pace = st.selectbox(
            "Preferred pace",
            ["Intensive (8+ hours/day)", "Moderate (4-6 hours/day)", "Relaxed (1-3 hours/day)", "Weekend only"]
        )
        
        specific_goals = st.text_input(
            "Specific goals (optional)",
            placeholder="e.g., Build a portfolio, Get a job in 6 months, Learn for personal project..."
        )
        
        if st.button("✨ Generate My Custom Path", type="primary", use_container_width=True):
            # Generate custom path based on user input
            custom_path = []
            
            topic_map = {
                "Web Development": {"title": "Web Development", "icon": "🌐", "level": "Beginner", "duration": "6 weeks"},
                "Mobile Development": {"title": "Mobile App Development", "icon": "📱", "level": "Intermediate", "duration": "5 weeks"},
                "Data Science": {"title": "Data Science", "icon": "📊", "level": "Intermediate", "duration": "6 weeks"},
                "Machine Learning": {"title": "Machine Learning", "icon": "🤖", "level": "Advanced", "duration": "8 weeks"},
                "Cloud/DevOps": {"title": "Cloud & DevOps", "icon": "☁️", "level": "Intermediate", "duration": "5 weeks"},
                "Backend Development": {"title": "Backend Development", "icon": "🔗", "level": "Intermediate", "duration": "4 weeks"},
                "Frontend Development": {"title": "Frontend Development", "icon": "🎨", "level": "Beginner", "duration": "4 weeks"},
            }
            
            for topic in preferred_topics:
                if topic in topic_map:
                    info = topic_map[topic]
                    custom_path.append({
                        "title": info["title"],
                        "duration": info["duration"],
                        "priority": 1,
                        "icon": info["icon"],
                        "level": info["level"],
                        "reason": "Based on your preferences"
                    })
            
            # Add fundamentals if beginner
            if "experience" not in profile or profile.get("experience", 0) < 1:
                custom_path.insert(0, {
                    "title": "Programming Fundamentals",
                    "duration": "3 weeks",
                    "priority": 0,
                    "icon": "💻",
                    "level": "Beginner",
                    "reason": "Build strong foundation"
                })
            
            for p in custom_path:
                p["progress"] = 0
                p["status"] = "Not Started"
            
            st.session_state.user_learning_path = custom_path
            st.success("Your custom learning path is ready!")
        
        if st.session_state.user_learning_path:
            st.markdown("#### Your Custom Path:")
            for i, p in enumerate(st.session_state.user_learning_path):
                with st.expander(f"{p.get('icon', '📚')} {p['title']} - {p.get('duration', '')}"):
                    st.markdown(f"**Level:** {p.get('level', 'N/A')}")
                    st.markdown(f"**Duration:** {p.get('duration', 'N/A')}")
                    st.markdown(f"**Reason:** {p.get('reason', 'Your choice')}")
            
            if st.button("Use This Custom Path", type="primary", use_container_width=True):
                st.session_state.selected_path_type = "user"
                st.session_state.learning_path = st.session_state.user_learning_path.copy()
                st.success("Custom learning path selected!")

    with tab4:
        st.markdown("### ⚖️ Compare & Choose Your Path")
        
        if not st.session_state.ai_learning_path and not st.session_state.user_learning_path:
            st.info("Generate at least one learning path to compare!")
        else:
            # AI Path Summary
            st.markdown("#### 🤖 AI-Generated Path")
            if st.session_state.ai_learning_path:
                ai_duration = sum([int(p.get('duration', '0').split()[0]) for p in st.session_state.ai_learning_path])
                ai_topics = len(st.session_state.ai_learning_path)
                
                st.markdown(f"**Topics:** {ai_topics}")
                st.markdown(f"**Est. Duration:** {ai_duration} weeks")
                st.markdown(f"**Strengths:**")
                st.markdown("- Based on quiz results & assessment")
                st.markdown("- Addresses your weak areas")
                st.markdown("- Optimized for your goals")
                st.markdown("- Evidence-based recommendations")
                
                st.markdown(f"**Weaknesses:**")
                st.markdown("- May not match personal preferences")
                st.markdown("- Generic approach")
            else:
                st.info("AI path not generated yet")
            
            st.markdown("---")
            
            # User Path Summary
            st.markdown("#### ✏️ Your Custom Path")
            if st.session_state.user_learning_path:
                user_duration = sum([int(p.get('duration', '0').split()[0]) for p in st.session_state.user_learning_path])
                user_topics = len(st.session_state.user_learning_path)
                
                st.markdown(f"**Topics:** {user_topics}")
                st.markdown(f"**Est. Duration:** {user_duration} weeks")
                st.markdown(f"**Strengths:**")
                st.markdown("- Matches your preferences")
                st.markdown("- You chose the focus areas")
                st.markdown("- Personalized approach")
                
                st.markdown(f"**Weaknesses:**")
                st.markdown("- May have gaps in knowledge")
                st.markdown("- Not optimized for weaknesses")
                st.markdown("- May miss important fundamentals")
            else:
                st.info("Custom path not created yet")
            
            st.markdown("---")
            
            # AI Suggestions
            st.markdown("#### 💡 AI Recommendations")
            
            suggestions = []
            if st.session_state.ai_learning_path and st.session_state.user_learning_path:
                ai_titles = [p['title'] for p in st.session_state.ai_learning_path]
                user_titles = [p['title'] for p in st.session_state.user_learning_path]
                
                # Check for missing fundamentals
                if "Programming Fundamentals" in ai_titles and "Programming Fundamentals" not in user_titles:
                    suggestions.append("⚠️ Your custom path might be missing fundamentals. Consider adding 'Programming Fundamentals' if you're a beginner.")
                
                # Check for weak area coverage
                if weak_areas and len(weak_areas) > 0:
                    suggestions.append(f"💡 Your assessment shows {len(weak_areas)} weak areas. Make sure your path addresses: {', '.join([w[0] for w in weak_areas])}")
                
                # Time recommendation
                if profile.get("hours", 2) < 2:
                    suggestions.append("⏱️ With limited time, focus on fewer topics with deeper learning rather than broad coverage.")
                
                if not suggestions:
                    suggestions.append("✅ Your paths look good! Consider combining elements from both for the best result.")
            
            for suggestion in suggestions:
                st.markdown(suggestion)
            
            st.markdown("---")
            
            # Final Selection
            st.markdown("#### 🎯 Select Your Final Learning Path")
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                if st.button("🤖 Use AI Path", use_container_width=True, type="primary"):
                    st.session_state.learning_path = st.session_state.ai_learning_path.copy()
                    st.session_state.selected_path_type = "ai"
                    st.success("AI learning path selected as your final path!")
            
            with col2:
                if st.button("✏️ Use Custom Path", use_container_width=True, type="primary"):
                    st.session_state.learning_path = st.session_state.user_learning_path.copy()
                    st.session_state.selected_path_type = "user"
                    st.success("Custom learning path selected as your final path!")
            
            with col3:
                if st.button("🔄 Combine Both", use_container_width=True, type="primary"):
                    combined = []
                    if st.session_state.ai_learning_path:
                        combined.extend(st.session_state.ai_learning_path[:3])
                    if st.session_state.user_learning_path:
                        combined.extend(st.session_state.user_learning_path[:3])
                    # Remove duplicates
                    seen = set()
                    unique_combined = []
                    for p in combined:
                        if p['title'] not in seen:
                            seen.add(p['title'])
                            unique_combined.append(p)
                    st.session_state.learning_path = unique_combined
                    st.session_state.selected_path_type = "combined"
                    st.success("Combined learning path created!")

    # Show final selected path
    if st.session_state.learning_path:
        st.markdown("---")
        st.markdown("### 📚 Your Selected Learning Path")
        
        for i, p in enumerate(st.session_state.learning_path):
            with st.container():
                col1, col2, col3 = st.columns([3, 1, 1])
                
                with col1:
                    icon = p.get("icon", "📚")
                    level = p.get("level", "")
                    st.markdown(f"**{icon} {p['title']}**")
                    st.caption(f"{p.get('duration', '')} • {level}")
                
                with col2:
                    new_progress = st.slider(
                        f"Progress {i}",
                        0, 100, p.get("progress", 0),
                        key=f"path_progress_{i}"
                    )
                    st.session_state.learning_path[i]["progress"] = new_progress
                    if new_progress == 100:
                        st.session_state.learning_path[i]["status"] = "Completed ✓"
                    elif new_progress > 0:
                        st.session_state.learning_path[i]["status"] = "In Progress..."
                
                with col3:
                    status = p.get("status", "Not Started")
                    if "Completed" in status:
                        st.success(status)
                    elif "In Progress" in status:
                        st.info(status)
                    else:
                        st.write(status)
        
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("📚 Browse Courses", use_container_width=True):
                go_to_step(5)
        with col2:
            if st.button("🏠 Back to Dashboard", use_container_width=True):
                go_to_step(6)

# ----------------------------------------------------
# COURSES
# ----------------------------------------------------

elif st.session_state.current_step == 5:

    st.markdown("## 📚 Curated Courses")
    
    profile = st.session_state.user_profile
    goal = profile.get("goal", "")
    
    COURSES = [
        {
            "title": "Complete Python Developer",
            "provider": "Zero to Mastery",
            "duration": "30+ hours",
            "level": "Beginner-Intermediate",
            "price": "$$",
            "rating": 4.8,
            "icon": "🐍",
            "tags": ["Python", "Backend", "Projects"],
            "description": "Master Python from zero to hero. Build 12+ projects including web apps, APIs, and automation scripts."
        },
        {
            "title": "The Web Developer Bootcamp",
            "provider": "Colt Steele",
            "duration": "60+ hours",
            "level": "Beginner",
            "price": "$$",
            "rating": 4.7,
            "icon": "🌐",
            "tags": ["HTML", "CSS", "JavaScript", "Node.js"],
            "description": "The only course you need to learn web development. Covers frontend and backend with real projects."
        },
        {
            "title": "Machine Learning A-Z",
            "provider": "Kirill Eremenko",
            "duration": "44+ hours",
            "level": "Intermediate",
            "price": "$$$",
            "rating": 4.5,
            "icon": "🤖",
            "tags": ["ML", "Data Science", "Python"],
            "description": "Learn to create Machine Learning algorithms in Python and R from industry experts."
        },
        {
            "title": "Docker & Kubernetes",
            "provider": "Bret Fisher",
            "duration": "25+ hours",
            "level": "Intermediate",
            "price": "$$",
            "rating": 4.8,
            "icon": "📦",
            "tags": ["Docker", "Kubernetes", "DevOps"],
            "description": "Master containerization with Docker and orchestration with Kubernetes for modern deployment."
        },
        {
            "title": "Algorithms & Data Structures",
            "provider": "Stephen Grider",
            "duration": "20+ hours",
            "level": "Intermediate",
            "price": "$$",
            "rating": 4.6,
            "icon": "🏗️",
            "tags": ["Algorithms", "Interviews", "Problem Solving"],
            "description": "Ace technical interviews with hands-on practice on common data structures and algorithms."
        },
        {
            "title": "React - The Complete Guide",
            "provider": "Academind",
            "duration": "50+ hours",
            "level": "Intermediate",
            "price": "$$",
            "rating": 4.7,
            "icon": "⚛️",
            "tags": ["React", "JavaScript", "Frontend"],
            "description": "Dive deep into React 18 with hooks, Redux, React Router, and Next.js framework."
        },
        {
            "title": "SQL for Data Science",
            "provider": "Mosh Hamedani",
            "duration": "8+ hours",
            "level": "Beginner",
            "price": "$",
            "rating": 4.5,
            "icon": "🗄️",
            "tags": ["SQL", "Databases", "Data Science"],
            "description": "Master SQL for data analysis with hands-on exercises and real-world datasets."
        },
        {
            "title": "AWS Certified Developer",
            "provider": "Stephane Maarek",
            "duration": "35+ hours",
            "level": "Advanced",
            "price": "$$",
            "rating": 4.7,
            "icon": "☁️",
            "tags": ["AWS", "Cloud", "Certification"],
            "description": "Prepare for AWS Developer Associate certification with hands-on labs and practice exams."
        },
    ]
    
    # Filter based on user goal
    filtered_courses = COURSES
    if "web" in goal.lower() or "build project" in goal.lower():
        filtered_courses = [c for c in COURSES if any(t in ["HTML", "CSS", "JavaScript", "React", "Frontend"] for t in c["tags"])]
    elif "data" in goal.lower() or "ai" in goal.lower():
        filtered_courses = [c for c in COURSES if any(t in ["ML", "Data Science", "SQL"] for t in c["tags"])]
    elif "cloud" in goal.lower() or "devops" in goal.lower():
        filtered_courses = [c for c in COURSES if any(t in ["Docker", "Kubernetes", "AWS", "Cloud"] for t in c["tags"])]
    
    st.markdown(f"Showing {len(filtered_courses)} courses recommended for your goals")
    
    cols = st.columns(2)
    for idx, course in enumerate(filtered_courses):
        with cols[idx % 2]:
            st.markdown(f"""
            <div style="background: white; border: 1px solid #ddd6fe; border-radius: 16px; padding: 24px; margin-bottom: 16px; transition: all 0.3s;">
                <div style="display: flex; align-items: center; margin-bottom: 12px;">
                    <span style="font-size: 36px; margin-right: 12px;">{course['icon']}</span>
                    <div>
                        <h4 style="color: #1e1b4b; margin: 0;">{course['title']}</h4>
                        <span style="color: #6b7280; font-size: 14px;">{course['provider']}</span>
                    </div>
                </div>
                <p style="color: #475569; font-size: 14px; margin-bottom: 12px;">{course['description']}</p>
                <div style="display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 12px;">
                    <span style="background: #ede9fe; color: #7c3aed; padding: 4px 12px; border-radius: 20px; font-size: 12px;">⏱️ {course['duration']}</span>
                    <span style="background: #dcfce7; color: #166534; padding: 4px 12px; border-radius: 20px; font-size: 12px;">📊 {course['level']}</span>
                    <span style="background: #fef3c7; color: #92400e; padding: 4px 12px; border-radius: 20px; font-size: 12px;">💰 {course['price']}</span>
                    <span style="background: #fee2e2; color: #991b1b; padding: 4px 12px; border-radius: 20px; font-size: 12px;">⭐ {course['rating']}</span>
                </div>
                <div style="display: flex; gap: 6px; flex-wrap: wrap;">
                    {"".join(f'<span style="background: #f5f3ff; color: #6b7280; padding: 3px 10px; border-radius: 12px; font-size: 11px;">{tag}</span>' for tag in course['tags'])}
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button(f"Enroll in Course", key=f"enroll_{idx}"):
                st.success(f"Added '{course['title']}' to your learning plan!")
    
    st.markdown("---")
    if st.button("🏠 Back to Dashboard", use_container_width=True):
        go_to_step(6)

# ----------------------------------------------------
# DASHBOARD
# ----------------------------------------------------

elif st.session_state.current_step == 6:

    profile = st.session_state.user_profile
    name = profile.get("name", "Learner")
    
    # Time-based greeting
    hour = datetime.now().hour
    if hour < 12:
        greeting = "Good morning"
    elif hour < 17:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"
    
    # Add custom CSS for dashboard cards
    st.markdown("""
    <style>
    .dashboard-welcome {
        background: linear-gradient(135deg, #8b5cf6 0%, #7c3aed 100%);
        border-radius: 20px;
        padding: 32px;
        color: white;
        margin-bottom: 24px;
    }
    .dashboard-welcome h1 {
        color: white !important;
        margin-bottom: 8px;
    }
    .dashboard-welcome p {
        color: rgba(255,255,255,0.9) !important;
        font-size: 18px;
    }
    .stat-card {
        background: white;
        border: 1px solid #ddd6fe;
        border-radius: 16px;
        padding: 24px;
        text-align: center;
        transition: all 0.3s ease;
    }
    .stat-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 8px 25px rgba(139,92,246,0.15);
    }
    .stat-icon {
        font-size: 36px;
        margin-bottom: 12px;
    }
    .stat-value {
        font-size: 32px;
        font-weight: 700;
        color: #8b5cf6;
    }
    .stat-label {
        font-size: 14px;
        color: #6b7280;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    .section-card {
        background: white;
        border: 1px solid #ddd6fe;
        border-radius: 20px;
        padding: 24px;
        margin-bottom: 20px;
    }
    .section-title {
        font-size: 20px;
        font-weight: 700;
        color: #1e1b4b;
        margin-bottom: 16px;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    .progress-item {
        margin-bottom: 16px;
    }
    .progress-header {
        display: flex;
        justify-content: space-between;
        margin-bottom: 8px;
    }
    .quick-action {
        background: white;
        border: 2px solid #ddd6fe;
        border-radius: 16px;
        padding: 20px;
        text-align: center;
        transition: all 0.3s ease;
        cursor: pointer;
    }
    .quick-action:hover {
        border-color: #8b5cf6;
        background: #f5f3ff;
        transform: translateY(-2px);
    }
    .quick-action-icon {
        font-size: 32px;
        margin-bottom: 8px;
    }
    .activity-item {
        display: flex;
        align-items: center;
        padding: 12px;
        border-radius: 12px;
        margin-bottom: 8px;
        background: #f5f3ff;
    }
    .activity-icon {
        font-size: 20px;
        margin-right: 12px;
    }
    .streak-badge {
        background: linear-gradient(135deg, #f97316, #ea580c);
        color: white;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 14px;
        font-weight: 600;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Welcome banner
    st.markdown(f"""
    <div class="dashboard-welcome">
        <h1>{greeting}, {name}! 👋</h1>
        <p>Ready to continue your learning journey? You have {len(st.session_state.learning_path)} topics in your path waiting for you.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Stats row
    col1, col2, col3, col4 = st.columns(4)
    
    quiz_count = len(st.session_state.quiz_batch_scores)
    quiz_score = 0
    if st.session_state.quiz_batch_scores:
        total_correct = sum(s["correct"] for s in st.session_state.quiz_batch_scores.values())
        total_q = sum(s["total"] for s in st.session_state.quiz_batch_scores.values())
        quiz_score = int(100 * total_correct / total_q) if total_q > 0 else 0
    
    path = st.session_state.learning_path
    completed = sum(1 for p in path if p.get("progress", 0) == 100)
    total_hours = sum(log.get("hours", 0) for log in st.session_state.daily_logs)
    
    stats = [
        (col1, "📝", quiz_count, "Quizzes Taken"),
        (col2, "🎯", f"{quiz_score}%", "Avg Score"),
        (col3, "📚", f"{completed}/{len(path)}", "Path Progress"),
        (col4, "⏱️", f"{total_hours}h", "Hours Logged"),
    ]
    
    for col, icon, value, label in stats:
        with col:
            st.markdown(f"""
            <div class="stat-card">
                <div class="stat-icon">{icon}</div>
                <div class="stat-value">{value}</div>
                <div class="stat-label">{label}</div>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Main content: Quick Actions + Learning Path
    col_left, col_right = st.columns([1, 1])
    
    with col_left:
        st.markdown("""
        <div class="section-card">
            <div class="section-title">⚡ Quick Actions</div>
        </div>
        """, unsafe_allow_html=True)
        
        actions = [
            ("📝", "Take Quiz", "Test your knowledge", 3),
            ("🛤️", "Learning Path", "View your roadmap", 4),
            ("📚", "Browse Courses", "Find new courses", 5),
            ("🤖", "AI Coach", "Get help & tips", 7),
        ]
        
        action_cols = st.columns(2)
        for idx, (icon, title, desc, step) in enumerate(actions):
            with action_cols[idx % 2]:
                if st.button(f"{icon} {title}\n{desc}", use_container_width=True, key=f"action_{step}"):
                    go_to_step(step)
    
    with col_right:
        st.markdown("""
        <div class="section-card">
            <div class="section-title">📈 Your Progress</div>
        </div>
        """, unsafe_allow_html=True)
        
        if path:
            for p in path[:4]:
                progress = p.get("progress", 0)
                icon = p.get("icon", "📚")
                title = p["title"]
                
                st.markdown(f"""
                <div class="progress-item">
                    <div class="progress-header">
                        <span><span style="font-size: 18px;">{icon}</span> {title}</span>
                        <span style="color: #8b5cf6; font-weight: 600;">{progress}%</span>
                    </div>
                    <div style="background: #f5f3ff; border-radius: 10px; height: 8px; overflow: hidden;">
                        <div style="background: linear-gradient(90deg, #8b5cf6, #a78bfa); width: {progress}%; height: 100%; border-radius: 10px; transition: width 0.5s ease;"></div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.info("Complete your assessment to see your personalized learning path!")
    
    st.markdown("---")
    
    # Bottom section: Recent Activity + Profile
    col_activity, col_profile = st.columns([1.5, 1])
    
    with col_activity:
        st.markdown("""
        <div class="section-card">
            <div class="section-title">📋 Recent Activity</div>
        </div>
        """, unsafe_allow_html=True)
        
        if st.session_state.daily_logs:
            for log in reversed(st.session_state.daily_logs[-5:]):
                st.markdown(f"""
                <div class="activity-item">
                    <span class="activity-icon">📖</span>
                    <div>
                        <div style="font-weight: 600; color: #1e1b4b;">{log.get('topic', 'Learning session')}</div>
                        <div style="font-size: 12px; color: #6b7280;">{log.get('date', 'N/A')} • {log.get('hours', 0)} hours</div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.info("No learning activities logged yet. Start tracking your progress!")
        
        if st.button("📝 Log Today's Learning", use_container_width=True):
            go_to_step(9)
    
    with col_profile:
        st.markdown("""
        <div class="section-card">
            <div class="section-title">👤 Your Profile</div>
        </div>
        """, unsafe_allow_html=True)
        
        profile_items = [
            ("🎯", "Goal", profile.get("goal", "Not set")),
            ("⏰", "Daily Hours", f"{profile.get('hours', 'Not set')}h"),
            ("📊", "Tech Level", f"{profile.get('tech', 'Not set')}/10"),
            ("🏆", "Experience", f"{profile.get('experience', 0)} years"),
        ]
        
        for icon, label, value in profile_items:
            st.markdown(f"""
            <div style="display: flex; justify-content: space-between; padding: 12px; background: #f5f3ff; border-radius: 12px; margin-bottom: 8px;">
                <span><span style="font-size: 16px;">{icon}</span> {label}</span>
                <span style="font-weight: 600; color: #8b5cf6;">{value}</span>
            </div>
            """, unsafe_allow_html=True)
        
        if profile.get("style"):
            st.markdown(f"**Learning Styles:** {', '.join(profile.get('style', []))}")
        
        if st.button("✏️ Edit Profile", use_container_width=True):
            go_to_step(1)

# ----------------------------------------------------
# AI COACH
# ----------------------------------------------------

elif st.session_state.current_step == 7:

    st.markdown("## 🤖 AI Learning Coach")
    st.markdown("*Get personalized guidance based on your learning profile and progress.*")
    
    # Suggested questions based on profile
    profile = st.session_state.user_profile
    goal = profile.get("goal", "")
    
    st.markdown("### 💡 Suggested Questions")
    
    suggested = [
        f"What's the best way to reach my goal of '{goal}'?",
        "How should I structure my daily learning sessions?",
        "I'm struggling with motivation, any tips?",
        "What's the most efficient learning path for my skill level?",
        "How do I know if I'm ready for the next topic?",
    ]
    
    cols = st.columns(2)
    for idx, q in enumerate(suggested):
        with cols[idx % 2]:
            if st.button(q, key=f"suggested_{idx}"):
                st.session_state.chat_input = q
    
    st.markdown("---")
    
    # Chat interface
    st.markdown("### 💬 Ask Your Coach")
    
    chat_input = st.text_input(
        "What would you like to know?",
        value=st.session_state.get("chat_input", ""),
        placeholder="e.g., How can I improve my problem-solving skills?"
    )
    
    if st.button("Ask Coach", type="primary") and chat_input:
        st.session_state.chat_history.append({"role": "user", "content": chat_input})
        
        # Generate contextual response
        profile = st.session_state.user_profile
        path = st.session_state.learning_path
        completed = sum(1 for p in path if p.get("progress", 0) == 100) if path else 0
        
        # Simple response logic
        if "motivation" in chat_input.lower() or "stay" in chat_input.lower():
            response = "Based on your profile, you're committing {} hours daily - that's great! Here are my tips:\n\n1. Set micro-goals for each session\n2. Track your progress visually\n3. Join our learning community\n4. Take breaks when needed\n5. Celebrate small wins!".format(profile.get("hours", 2))
        elif "path" in chat_input.lower() or "next" in chat_input.lower():
            if path:
                next_topic = next((p["title"] for p in path if p.get("progress", 0) < 100), "None")
                response = f"Your current path has {len(path)} topics. You've completed {completed} so far. I recommend starting with **{next_topic}** next since you have a strong foundation to build upon."
            else:
                response = "Complete your assessment and quizzes first to get a personalized learning path!"
        elif "time" in chat_input.lower() or "hours" in chat_input.lower():
            hours = profile.get("hours", 2)
            if hours < 2:
                response = "With limited time, focus on consistency over volume. Try the Pomodoro technique (25 min focused work + 5 min break). Even 1 hour daily adds up to 365 hours per year!"
            elif hours < 4:
                response = "Great commitment! Structure your time: 60% on core concepts, 30% on practice/projects, 10% on review. This balance works well for most learners."
            else:
                response = "Impressive dedication! Make sure to avoid burnout. Mix intensive learning sessions with lighter review days. Quality over quantity matters too."
        elif "python" in chat_input.lower():
            response = "Python is a great choice! Based on your assessment, you should start with Python fundamentals. Focus on: 1) Basic syntax, 2) Functions and modules, 3) Data structures, 4) File handling. Then move to projects!"
        elif "quiz" in chat_input.lower():
            response = "Taking quizzes helps identify knowledge gaps. Based on your results, I can suggest specific topics to focus on. Would you like to take another quiz?"
        else:
            response = f"Great question! Based on your learning profile:\n\n- Your goal: {goal}\n- Learning style: {', '.join(profile.get('style', ['Visual']))}\n- Daily commitment: {profile.get('hours', 2)} hours\n\nKeep building projects and don't be afraid to make mistakes - they're the best teachers! 🚀"
        
        st.session_state.chat_history.append({"role": "assistant", "content": response})
        st.session_state.chat_input = ""
    
    # Display chat history
    st.markdown("---")
    st.markdown("### Conversation History")
    
    if not st.session_state.chat_history:
        st.info("Start a conversation with your AI coach above!")
    else:
        for msg in st.session_state.chat_history:
            if msg["role"] == "user":
                st.markdown(f"""
                <div style="background: #ede9fe; padding: 16px; border-radius: 16px 16px 4px 16px; margin: 12px 0; max-width: 80%; margin-left: auto;">
                    <strong style="color: #7c3aed;">You:</strong>
                    <p style="color: #1e1b4b; margin: 8px 0 0 0;">{msg['content']}</p>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div style="background: white; border: 1px solid #ddd6fe; padding: 16px; border-radius: 16px 16px 16px 4px; margin: 12px 0; max-width: 80%;">
                    <strong style="color: #8b5cf6;">🤖 Coach:</strong>
                    <p style="color: #475569; margin: 8px 0 0 0; white-space: pre-line;">{msg['content']}</p>
                </div>
                """, unsafe_allow_html=True)
    
    if st.button("Clear Chat History"):
        st.session_state.chat_history = []
        st.rerun()

# ----------------------------------------------------
# PREDICTIONS
# ----------------------------------------------------

elif st.session_state.current_step == 8:

    st.markdown("## 📈 Predictions")

    st.info("Complete more activities to get predictions.")

# ----------------------------------------------------
# PROGRESS
# ----------------------------------------------------

elif st.session_state.current_step == 9:

    st.markdown("## 📊 Log Your Learning Journey")
    st.markdown("*Track your daily learning activities, progress, and reflections.*")

    # Add custom CSS for this page
    st.markdown("""
    <style>
    .log-form-card {
        background: white;
        border: 1px solid #ddd6fe;
        border-radius: 20px;
        padding: 24px;
        margin-bottom: 20px;
    }
    .log-form-card h3 {
        color: #1e1b4b;
        margin-bottom: 16px;
        font-size: 18px;
    }
    </style>
    """, unsafe_allow_html=True)

    # Learning log form
    with st.form("log_form"):
        
        # Basic info
        st.markdown("### 📚 Learning Details")
        
        col1, col2 = st.columns(2)
        
        with col1:
            topic = st.text_input("What did you learn?", placeholder="e.g., Python functions, React hooks...")
            learning_type = st.selectbox("Learning Type", [
                "Watching tutorials/videos",
                "Reading documentation/articles",
                "Taking a course",
                "Building a project",
                "Practice exercises",
                "Code review",
                "Reading books",
                "Attending a workshop/webinar",
                "Pair programming",
                "Other"
            ])
            hours = st.slider("Hours spent", 0.5, 12.0, 1.0, step=0.5)
        
        with col2:
            date = st.date_input("Date", datetime.now())
            difficulty = st.select_slider("Difficulty Level", options=["Easy", "Medium", "Hard"], value="Medium")
            resource = st.text_input("Resource Used (optional)", placeholder="e.g., Udemy Course, YouTube, Official Docs...")
        
        st.markdown("---")
        
        # Progress & Achievement
        st.markdown("### 🎯 Progress & Achievements")
        
        col3, col4 = st.columns(2)
        
        with col3:
            topic_tags = st.multiselect("Topics Covered", [
                "Python", "JavaScript", "Web Dev", "React", "Data Science", 
                "Machine Learning", "Databases", "APIs", "Git/GitHub", 
                "Cloud", "DevOps", "Mobile", "UI/UX", "Algorithms",
                "Cybersecurity", "Other"
            ])
            mood = st.selectbox("How did you feel?", ["😊 Great", "🙂 Good", "😐 Okay", "😕 Struggled", "😤 Frustrated"])
        
        with col4:
            completed = st.checkbox("Completed a milestone/sub-goal")
            new_concept = st.checkbox("Learned something new")
            struggled = st.checkbox("Struggled with something")
            notes = st.text_area("Quick notes (optional)", placeholder="Any thoughts, questions, or key takeaways...", height=80)
        
        st.markdown("---")
        
        # Tomorrow's plan
        st.markdown("### 🔮 Tomorrow's Plan")
        
        col5, col6 = st.columns(2)
        
        with col5:
            next_topics = st.text_input("What will you learn next?", placeholder="e.g., Python decorators, API routes...")
        
        with col6:
            priority = st.selectbox("Priority for next session", ["High", "Medium", "Low"])
        
        st.markdown("---")
        
        submitted = st.form_submit_button("💾 Save Log", use_container_width=True)
        
        if submitted:
            log_entry = {
                "topic": topic,
                "type": learning_type,
                "hours": hours,
                "date": date.strftime("%Y-%m-%d"),
                "difficulty": difficulty,
                "resource": resource,
                "tags": topic_tags,
                "mood": mood,
                "completed": completed,
                "new_concept": new_concept,
                "struggled": struggled,
                "notes": notes,
                "next_topics": next_topics,
                "priority": priority,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M")
            }
            
            st.session_state.daily_logs.append(log_entry)
            
            st.success("✅ Learning log saved! Keep up the great work!")
            st.balloons()
    
    # Show recent logs
    st.markdown("---")
    st.markdown("### 📜 Recent Logs")
    
    if st.session_state.daily_logs:
        for log in reversed(st.session_state.daily_logs[-5:]):
            with st.expander(f"📅 {log.get('date', 'N/A')} - {log.get('topic', 'Untitled')}"):
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown(f"**Type:** {log.get('type', 'N/A')}")
                    st.markdown(f"**Hours:** {log.get('hours', 0)}")
                    st.markdown(f"**Difficulty:** {log.get('difficulty', 'N/A')}")
                    st.markdown(f"**Mood:** {log.get('mood', 'N/A')}")
                with col2:
                    if log.get('tags'):
                        st.markdown(f"**Topics:** {', '.join(log.get('tags', []))}")
                    st.markdown(f"**Resource:** {log.get('resource', 'N/A')}")
                    if log.get('notes'):
                        st.markdown(f"**Notes:** {log.get('notes', '')}")
    else:
        st.info("No logs yet. Start tracking your learning journey above!")
    
    st.markdown("---")
    if st.button("🏠 Back to Dashboard", use_container_width=True):
        go_to_step(6)

# ----------------------------------------------------
# SETTINGS
# ----------------------------------------------------

elif st.session_state.current_step == 10:

    st.markdown("## ⚙️ Settings")

    st.json(st.session_state.user_profile)

    data={
        "profile":st.session_state.user_profile,
        "logs":st.session_state.daily_logs
    }

    st.download_button(
        "Download Data",
        json.dumps(data),
        "learnpath.json"
    )

st.divider()
st.markdown("<p style='text-align:center;color:#64748b;'>🎓 LearnPath © 2024</p>", unsafe_allow_html=True)