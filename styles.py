import streamlit as st


def load_styles():
    st.markdown("""
<style>
/* ========================================
   LAVENDER CALM THEME
   Soft, peaceful, calming
   ======================================== */

/* Import Fonts */
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');

/* Global Styles */
html, body {
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    background: #181826;
    color: #ffffff;
}

/* Main app background - Deep lavender with subtle patterns */
.stApp {
    background: 
        radial-gradient(ellipse at 20% 20%, rgba(167, 139, 250, 0.08) 0%, transparent 50%),
        radial-gradient(ellipse at 80% 80%, rgba(129, 140, 248, 0.06) 0%, transparent 50%),
        radial-gradient(ellipse at 50% 100%, rgba(165, 180, 252, 0.05) 0%, transparent 40%),
        linear-gradient(180deg, #181826 0%, #232338 50%, #181826 100%) !important;
    min-height: 100vh;
}

/* Soft ambient glow at bottom */
.stApp::before {
    content: '';
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    height: 400px;
    background: radial-gradient(ellipse at 50% 100%, rgba(167, 139, 250, 0.06) 0%, rgba(129, 140, 248, 0.03) 50%, transparent 70%);
    pointer-events: none;
    z-index: 0;
}

/* ========================================
   ANIMATIONS
   ======================================== */

/* Keyframes */
@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}

@keyframes fadeInUp {
    from { opacity: 0; transform: translateY(30px); }
    to { opacity: 1; transform: translateY(0); }
}

@keyframes fadeInDown {
    from { opacity: 0; transform: translateY(-30px); }
    to { opacity: 1; transform: translateY(0); }
}

@keyframes fadeInLeft {
    from { opacity: 0; transform: translateX(-30px); }
    to { opacity: 1; transform: translateX(0); }
}

@keyframes fadeInRight {
    from { opacity: 0; transform: translateX(30px); }
    to { opacity: 1; transform: translateX(0); }
}

@keyframes zoomIn {
    from { opacity: 0; transform: scale(0.9); }
    to { opacity: 1; transform: scale(1); }
}

@keyframes float {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-10px); }
}

@keyframes floatRotate {
    0%, 100% { transform: translateY(0) rotate(0deg); }
    50% { transform: translateY(-10px) rotate(2deg); }
}

@keyframes glowPulse {
    0%, 100% { box-shadow: 0 0 20px rgba(167, 139, 250, 0.2); }
    50% { box-shadow: 0 0 40px rgba(167, 139, 250, 0.4); }
}

@keyframes glowPulseStrong {
    0%, 100% { 
        box-shadow: 0 0 20px rgba(167, 139, 250, 0.3), 0 0 40px rgba(167, 139, 250, 0.1);
    }
    50% { 
        box-shadow: 0 0 40px rgba(167, 139, 250, 0.5), 0 0 80px rgba(167, 139, 250, 0.2);
    }
}

@keyframes shimmer {
    0% { background-position: -200% center; }
    100% { background-position: 200% center; }
}

@keyframes bounce {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-5px); }
}

@keyframes rotate {
    from { transform: rotate(0deg); }
    to { transform: rotate(360deg); }
}

@keyframes wave {
    0%, 100% { transform: scale(1); opacity: 0.5; }
    50% { transform: scale(1.2); opacity: 0.8; }
}

@keyframes morph {
    0%, 100% { border-radius: 24px; }
    50% { border-radius: 30px; }
}

@keyframes borderGlow {
    0%, 100% { border-color: rgba(167, 139, 250, 0.2); }
    50% { border-color: rgba(167, 139, 250, 0.5); }
}

@keyframes textGlow {
    0%, 100% { text-shadow: 0 0 10px rgba(167, 139, 250, 0.3); }
    50% { text-shadow: 0 0 20px rgba(167, 139, 250, 0.6), 0 0 30px rgba(167, 139, 250, 0.3); }
}

@keyframes gradientShift {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

@keyframes ripple {
    0% { transform: scale(0); opacity: 0.5; }
    100% { transform: scale(4); opacity: 0; }
}

@keyframes slideInUp {
    0% { transform: translateY(100%); opacity: 0; }
    100% { transform: translateY(0); opacity: 1; }
}

@keyframes heartBeat {
    0% { transform: scale(1); }
    14% { transform: scale(1.1); }
    28% { transform: scale(1); }
    42% { transform: scale(1.1); }
    70% { transform: scale(1); }
}

/* Animation Classes */
.animate-fade-in { animation: fadeIn 0.5s ease-out forwards; }
.animate-fade-in-up { animation: fadeInUp 0.6s ease-out forwards; }
.animate-fade-in-down { animation: fadeInDown 0.6s ease-out forwards; }
.animate-fade-in-left { animation: fadeInLeft 0.6s ease-out forwards; }
.animate-fade-in-right { animation: fadeInRight 0.6s ease-out forwards; }
.animate-zoom-in { animation: zoomIn 0.5s ease-out forwards; }
.animate-float { animation: float 4s ease-in-out infinite; }
.animate-float-rotate { animation: floatRotate 5s ease-in-out infinite; }
.animate-glow-pulse { animation: glowPulse 3s ease-in-out infinite; }
.animate-glow-pulse-strong { animation: glowPulseStrong 2s ease-in-out infinite; }
.animate-shimmer { 
    background: linear-gradient(90deg, transparent, rgba(167, 139, 250, 0.1), transparent);
    background-size: 200% 100%;
    animation: shimmer 3s infinite;
}
.animate-bounce { animation: bounce 1s ease-in-out infinite; }
.animate-rotate { animation: rotate 10s linear infinite; }
.animate-wave { animation: wave 2s ease-in-out infinite; }
.animate-morph { animation: morph 4s ease-in-out infinite; }
.animate-border-glow { animation: borderGlow 2s ease-in-out infinite; }
.animate-text-glow { animation: textGlow 2s ease-in-out infinite; }
.animate-gradient-shift { 
    background-size: 200% 200%;
    animation: gradientShift 5s ease infinite;
}
.animate-heart-beat { animation: heartBeat 1.5s ease-in-out infinite; }

/* Staggered delays */
.delay-1 { animation-delay: 0.1s; }
.delay-2 { animation-delay: 0.2s; }
.delay-3 { animation-delay: 0.3s; }
.delay-4 { animation-delay: 0.4s; }
.delay-5 { animation-delay: 0.5s; }
.delay-6 { animation-delay: 0.6s; }
.delay-7 { animation-delay: 0.7s; }
.delay-8 { animation-delay: 0.8s; }

/* ========================================
   TEXT STYLES
   ======================================== */

h1, h2, h3, h4, h5, h6 {
    color: #FFFFFF !important;
    font-weight: 600;
    letter-spacing: -0.02em;
}

p, span, div {
    color: #94a3b8 !important;
    line-height: 1.6;
}

h1 { color: #FFFFFF !important; font-weight: 700; letter-spacing: -0.03em; }
.subtext { color: #94a3b8 !important; }

/* Gradient text */
.gradient-text {
    background: linear-gradient(135deg, #a78bfa 0%, #c4b5fd 50%, #a78bfa 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    animation: gradientShift 5s ease infinite;
    background-size: 200% 200%;
}

.gradient-text-subtle {
    background: linear-gradient(135deg, #a78bfa 0%, #c4b5fd 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

/* ========================================
   CARDS WITH ANIMATIONS
   ======================================== */

/* Baselass-card, .stCard {
    background: rgba(255, 255, 255, 0.025 glass card */
.g) !important;
    backdrop-filter: blur(20px) !important;
    border: 1px solid rgba(255, 255, 255, 0.06) !important;
    border-radius: 24px !important;
    box-shadow: 
        0 8px 32px rgba(0, 0, 0, 0.2),
        0 0 80px rgba(167, 139, 250, 0.03),
        inset 0 1px 0 rgba(255, 255, 255, 0.04) !important;
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1) !important;
}

/* Card hover effects */
.glass-card:hover, .stCard:hover {
    transform: translateY(-5px);
    border-color: rgba(167, 139, 250, 0.25) !important;
    box-shadow: 
        0 20px 40px rgba(0, 0, 0, 0.3),
        0 0 60px rgba(167, 139, 250, 0.1),
        inset 0 1px 0 rgba(255, 255, 255, 0.08) !important;
}

/* Animated border card */
.card-animated-border {
    position: relative;
    background: rgba(255, 255, 255, 0.025);
    border-radius: 24px;
    overflow: hidden;
}

.card-animated-border::before {
    content: '';
    position: absolute;
    inset: 0;
    border-radius: 24px;
    padding: 1px;
    background: linear-gradient(135deg, rgba(167, 139, 250, 0.3), rgba(139, 92, 246, 0.3), rgba(167, 139, 250, 0.3));
    background-size: 200% 200%;
    animation: gradientShift 3s ease infinite;
    -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
    -webkit-mask-composite: xor;
    mask-composite: exclude;
    pointer-events: none;
}

/* Feature card */
.feature-card-organic {
    background: rgba(255, 255, 255, 0.02);
    border: 1px solid rgba(255, 255, 255, 0.05);
    border-radius: 24px;
    padding: 28px;
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    cursor: pointer;
}

.feature-card-organic:hover {
    background: rgba(255, 255, 255, 0.035);
    border-color: rgba(167, 139, 250, 0.25);
    transform: translateY(-8px) scale(1.02);
    box-shadow: 0 25px 50px rgba(0, 0, 0, 0.25), 0 0 80px rgba(167, 139, 250, 0.12);
}

.feature-card-organic:hover .feature-icon {
    transform: scale(1.15) rotate(5deg);
}

.feature-icon {
    font-size: 40px;
    margin-bottom: 16px;
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    display: inline-block;
}

/* Stats card */
.stats-card-organic {
    background: rgba(255, 255, 255, 0.02);
    backdrop-filter: blur(20px);
    border: 1px solid rgba(255, 255, 255, 0.05);
    border-radius: 24px;
    padding: 24px;
    text-align: center;
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}

.stats-card-organic:hover {
    background: rgba(255, 255, 255, 0.035);
    border-color: rgba(167, 139, 250, 0.25);
    transform: translateY(-5px) scale(1.02);
}

.stats-card-organic:hover .stats-number {
    transform: scale(1.1);
}

.stats-number {
    font-size: 36px;
    font-weight: 700;
    color: #FFFFFF;
    transition: all 0.3s ease;
}

.stats-label {
    font-size: 12px;
    color: #64748b;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    margin-top: 8px;
}

/* Step card */
.step-card-organic {
    background: rgba(255, 255, 255, 0.015);
    border: 1px solid rgba(255, 255, 255, 0.04);
    border-radius: 20px;
    padding: 24px 18px;
    text-align: center;
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}

.step-card-organic:hover {
    background: rgba(167, 139, 250, 0.08);
    border-color: rgba(167, 139, 250, 0.3);
    transform: translateY(-5px);
}

.step-card-organic:hover .step-number {
    transform: scale(1.1) rotate(5deg);
    box-shadow: 0 0 30px rgba(167, 139, 250, 0.4);
}

.step-number {
    width: 48px;
    height: 48px;
    background: linear-gradient(135deg, #a78bfa 0%, #7c3aed 100%);
    border-radius: 14px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    font-size: 18px;
    font-weight: 700;
    color: #0a1628;
    margin-bottom: 16px;
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    box-shadow: 0 4px 15px rgba(167, 139, 250, 0.25);
}

.step-icon {
    font-size: 32px;
    margin-bottom: 12px;
    display: inline-block;
    filter: drop-shadow(0 0 8px rgba(167, 139, 250, 0.4));
    transition: transform 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}

.step-card-organic:hover .step-icon {
    transform: scale(1.15);
    filter: drop-shadow(0 0 15px rgba(167, 139, 250, 0.6));
}

/* ========================================
   BUTTONS WITH ANIMATIONS
   ======================================== */

/* Primary buttons - Organic pill shape */
.stButton > button {
    background: linear-gradient(135deg, #a78bfa 0%, #7c3aed 100%) !important;
    color: #0a1628 !important;
    border: none !important;
    border-radius: 999px !important;
    font-weight: 600 !important;
    font-size: 14px !important;
    padding: 14px 32px !important;
    box-shadow: 
        0 4px 20px rgba(167, 139, 250, 0.3),
        0 0 40px rgba(167, 139, 250, 0.1) !important;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    cursor: pointer;
    position: relative;
    overflow: hidden;
}

.stButton > button::before {
    content: '';
    position: absolute;
    inset: 0;
    background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
    transform: translateX(-100%);
    transition: transform 0.5s ease;
}

.stButton > button:hover::before {
    transform: translateX(100%);
}

.stButton > button:hover {
    transform: translateY(-3px) scale(1.02);
    box-shadow: 
        0 10px 40px rgba(167, 139, 250, 0.4),
        0 0 80px rgba(167, 139, 250, 0.2) !important;
    background: linear-gradient(135deg, #c4b5fd 0%, #a78bfa 100%) !important;
}

.stButton > button:active {
    transform: translateY(-1px) scale(0.98);
}

/* Secondary buttons */
.stButton > button[kind="secondary"] {
    background: rgba(255, 255, 255, 0.05) !important;
    border: 1px solid rgba(255, 255, 255, 0.1) !important;
    color: #e2e8f0 !important;
    border-radius: 999px !important;
    transition: all 0.3s ease !important;
}

.stButton > button[kind="secondary"]:hover {
    background: rgba(255, 255, 255, 0.1) !important;
    border-color: rgba(167, 139, 250, 0.5) !important;
    color: #a78bfa !important;
    transform: translateY(-2px);
    box-shadow: 0 8px 25px rgba(167, 139, 250, 0.15) !important;
}

/* CTA Button Large */
.cta-button-organic {
    display: inline-block;
    background: linear-gradient(135deg, #a78bfa 0%, #7c3aed 100%);
    color: #0a1628;
    font-weight: 600;
    font-size: 16px;
    padding: 18px 48px;
    border-radius: 999px;
    text-decoration: none;
    box-shadow: 0 8px 30px rgba(167, 139, 250, 0.25), 0 0 60px rgba(167, 139, 250, 0.1);
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    cursor: pointer;
    border: none;
    position: relative;
    overflow: hidden;
}

.cta-button-organic::before {
    content: '';
    position: absolute;
    inset: 0;
    background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.3), transparent);
    transform: translateX(-100%);
    transition: transform 0.6s ease;
}

.cta-button-organic:hover {
    transform: translateY(-4px) scale(1.03);
    box-shadow: 0 15px 50px rgba(167, 139, 250, 0.35), 0 0 100px rgba(167, 139, 250, 0.15);
}

.cta-button-organic:hover::before {
    transform: translateX(100%);
}

/* ========================================
   INPUTS WITH ANIMATIONS
   ======================================== */

.stTextInput > div > div,
.stSelectbox > div > div,
.stTextArea > div > textarea,
.stNumberInput > div > input {
    background: rgba(255, 255, 255, 0.025) !important;
    border: 1px solid rgba(255, 255, 255, 0.08) !important;
    border-radius: 14px !important;
    color: #FFFFFF !important;
    padding: 14px 18px !important;
    transition: all 0.3s ease !important;
}

.stTextInput > div > div:focus-within,
.stSelectbox > div > div:focus-within,
.stTextArea > div > textarea:focus {
    border-color: #a78bfa !important;
    box-shadow: 0 0 0 4px rgba(167, 139, 250, 0.15), 0 0 30px rgba(167, 139, 250, 0.1) !important;
    background: rgba(255, 255, 255, 0.04) !important;
    transform: scale(1.01);
}

/* Labels */
label, .stRadio label, .stCheckbox label, .stSelectbox label, .stTextInput label, .stTextArea label {
    color: #64748b !important;
    font-weight: 500 !important;
    font-size: 13px !important;
    transition: color 0.3s ease;
}

label:hover, .stRadio label:hover {
    color: #94a3b8 !important;
}

/* ========================================
   TABS WITH ANIMATIONS
   ======================================== */

.stTabs [data-baseweb="tab-list"] {
    gap: 8px;
    background: transparent;
}

.stTabs [data-baseweb="tab"] {
    background: rgba(255, 255, 255, 0.02) !important;
    border: 1px solid rgba(255, 255, 255, 0.06) !important;
    border-radius: 14px 14px 0 0 !important;
    color: #64748b !important;
    padding: 14px 24px !important;
    font-weight: 500 !important;
    transition: all 0.3s ease !important;
}

.stTabs [data-baseweb="tab"]:hover {
    background: rgba(167, 139, 250, 0.05) !important;
    color: #a78bfa !important;
}

.stTabs [data-baseweb="tab"][aria-selected="true"] {
    background: linear-gradient(135deg, rgba(167, 139, 250, 0.15) 0%, rgba(6, 182, 212, 0.1) 100%) !important;
    border-color: rgba(167, 139, 250, 0.5) !important;
    color: #a78bfa !important;
    box-shadow: 0 0 30px rgba(167, 139, 250, 0.2), inset 0 0 20px rgba(167, 139, 250, 0.05) !important;
}

/* ========================================
   EXPANDERS WITH ANIMATIONS
   ======================================== */

[data-testid="stExpander"] {
    background: rgba(255, 255, 255, 0.015) !important;
    border: 1px solid rgba(255, 255, 255, 0.04) !important;
    border-radius: 20px !important;
    transition: all 0.3s ease !important;
    overflow: hidden;
}

[data-testid="stExpander"]:hover {
    border-color: rgba(167, 139, 250, 0.15) !important;
    box-shadow: 0 0 30px rgba(167, 139, 250, 0.05) !important;
}

.streamlit-expanderHeader {
    background: transparent !important;
    color: #94a3b8 !important;
    border-radius: 20px !important;
    font-weight: 500 !important;
    transition: all 0.3s ease !important;
}

.streamlit-expanderHeader:hover {
    color: #a78bfa !important;
}

/* ========================================
   METRICS WITH ANIMATIONS
   ======================================== */

[data-testid="metric-container"] {
    background: rgba(255, 255, 255, 0.02) !important;
    border: 1px solid rgba(255, 255, 255, 0.06) !important;
    border-radius: 24px !important;
    padding: 24px !important;
    box-shadow: 
        0 4px 24px rgba(0, 0, 0, 0.15),
        0 0 60px rgba(167, 139, 250, 0.04),
        inset 0 1px 0 rgba(255, 255, 255, 0.04) !important;
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1) !important;
}

[data-testid="metric-container"]:hover {
    transform: translateY(-3px);
    border-color: rgba(167, 139, 250, 0.2) !important;
    box-shadow: 
        0 10px 40px rgba(0, 0, 0, 0.2),
        0 0 80px rgba(167, 139, 250, 0.08),
        inset 0 1px 0 rgba(255, 255, 255, 0.06) !important;
}

[data-testid="metric-label"] {
    color: #64748b !important;
    font-size: 12px !important;
    font-weight: 600 !important;
    text-transform: uppercase;
    letter-spacing: 0.06em;
}

[data-testid="metric-value"] {
    color: #FFFFFF !important;
    font-size: 36px !important;
    font-weight: 700 !important;
    letter-spacing: -0.02em;
}

/* ========================================
   PROGRESS BAR ANIMATIONS
   ======================================== */

.stProgress > div > div > div {
    background: linear-gradient(90deg, #a78bfa, #7c3aed, #a78bfa) !important;
    background-size: 200% 100% !important;
    animation: gradientShift 2s ease infinite !important;
    border-radius: 999px !important;
    box-shadow: 0 0 20px rgba(167, 139, 250, 0.5) !important;
}

/* ========================================
   SIDEBAR
   ======================================== */

section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #232338 0%, #181826 100%) !important;
    backdrop-filter: blur(20px) !important;
    border-right: 1px solid rgba(167, 139, 250, 0.15) !important;
}

/* Sidebar elements */
section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3,
section[data-testid="stSidebar"] h4 {
    color: #a78bfa !important;
}

section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] span,
section[data-testid="stSidebar"] div {
    color: #94a3b8 !important;
}

/* Sidebar button animations */
.sidebar-nav-button {
    width: 100%;
    padding: 12px 16px;
    background: rgba(167, 139, 250, 0.05);
    border: 1px solid rgba(167, 139, 250, 0.1);
    border-radius: 12px;
    color: #c4b5fd;
    text-align: left;
    cursor: pointer;
    transition: all 0.3s ease;
    margin-bottom: 6px;
}

.sidebar-nav-button:hover {
    background: rgba(167, 139, 250, 0.12);
    border-color: rgba(167, 139, 250, 0.25);
    color: #a78bfa;
    transform: translateX(5px);
}

.sidebar-nav-button.active {
    background: rgba(167, 139, 250, 0.15);
    border-color: rgba(167, 139, 250, 0.3);
    color: #a78bfa;
}

/* ========================================
   ALERTS/MESSAGES
   ======================================== */

.stSuccess {
    background: rgba(34, 197, 94, 0.1) !important;
    border: 1px solid rgba(34, 197, 94, 0.3) !important;
    border-radius: 14px !important;
    color: #22c55e !important;
    animation: fadeInUp 0.4s ease-out !important;
}

.stInfo {
    background: rgba(167, 139, 250, 0.1) !important;
    border: 1px solid rgba(167, 139, 250, 0.3) !important;
    border-radius: 14px !important;
    color: #a78bfa !important;
    animation: fadeInUp 0.4s ease-out !important;
}

.stWarning {
    background: rgba(251, 191, 36, 0.1) !important;
    border: 1px solid rgba(251, 191, 36, 0.3) !important;
    border-radius: 14px !important;
    color: #fbbf24 !important;
    animation: fadeInUp 0.4s ease-out !important;
}

.stError {
    background: rgba(248, 113, 113, 0.1) !important;
    border: 1px solid rgba(248, 113, 113, 0.3) !important;
    border-radius: 14px !important;
    color: #f87171 !important;
    animation: fadeInUp 0.4s ease-out !important;
}

/* ========================================
   RADIO & CHECKBOX
   ======================================== */

.stRadio > div, .stCheckbox > div {
    color: #94a3b8 !important;
    transition: color 0.3s ease;
}

.stRadio > div:hover, .stCheckbox > div:hover {
    color: #FFFFFF !important;
}

[ data-baseweb="checkbox"] {
    color: #94a3b8 !important;
}

/* Custom checkbox animation */
[data-testid="stCheckbox"] > label > div:first-child {
    transition: all 0.3s ease;
}

[data-testid="stCheckbox"] > label > div:first-child:hover {
    border-color: #a78bfa !important;
    box-shadow: 0 0 10px rgba(167, 139, 250, 0.3) !important;
}

/* ========================================
   DIVIDER
   ======================================== */

hr {
    border: none;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.06), transparent);
    margin: 32px 0;
}

/* ========================================
   MULTISELECT TAGS
   ======================================== */

.stMultiSelect [data-baseweb="tag"] {
    background: linear-gradient(135deg, #a78bfa 0%, #7c3aed 100%) !important;
    color: #0a1628 !important;
    border-radius: 999px !important;
    animation: fadeIn 0.3s ease-out !important;
    transition: all 0.3s ease !important;
}

.stMultiSelect [data-baseweb="tag"]:hover {
    transform: scale(1.05);
    box-shadow: 0 2px 10px rgba(167, 139, 250, 0.3) !important;
}

/* ========================================
   SLIDER
   ======================================== */

.stSlider [data-baseweb="slider"] {
    color: #a78bfa !important;
}

.stSlider [data-testid="stSliderThumbValue"] {
    background: #a78bfa !important;
    color: #0a1628 !important;
}

/* ========================================
   CODE BLOCK
   ======================================== */

.stCodeBlock {
    background: rgba(10, 22, 40, 0.8) !important;
    border: 1px solid rgba(255, 255, 255, 0.06) !important;
    border-radius: 14px !important;
    transition: all 0.3s ease;
}

.stCodeBlock:hover {
    border-color: rgba(167, 139, 250, 0.2) !important;
    box-shadow: 0 0 20px rgba(167, 139, 250, 0.05) !important;
}

/* ========================================
   BADGE & PILL STYLES
   ======================================== */

.badge-pill {
    background: rgba(167, 139, 250, 0.12);
    border: 1px solid rgba(167, 139, 250, 0.25);
    border-radius: 999px;
    padding: 8px 18px;
    font-size: 12px;
    font-weight: 600;
    color: #a78bfa;
    display: inline-block;
    letter-spacing: 0.02em;
    transition: all 0.3s ease;
}

.badge-pill:hover {
    transform: scale(1.05);
    box-shadow: 0 0 20px rgba(167, 139, 250, 0.2);
}

span[data-baseweb="badge"] {
    background: rgba(167, 139, 250, 0.15) !important;
    color: #a78bfa !important;
    border: 1px solid rgba(167, 139, 250, 0.25) !important;
    animation: fadeIn 0.3s ease-out !important;
}

/* ========================================
   HERO SECTION
   ======================================== */

.hero-organic {
    text-align: center;
    padding: 80px 20px;
    position: relative;
}

.hero-title-organic {
    font-size: 64px;
    font-weight: 800;
    letter-spacing: -0.04em;
    line-height: 1.1;
    margin-bottom: 24px;
    animation: fadeInUp 0.8s ease-out;
}

.hero-subtitle-organic {
    font-size: 20px;
    color: #94a3b8;
    max-width: 650px;
    margin: 0 auto 40px;
    line-height: 1.7;
    animation: fadeInUp 0.8s ease-out 0.2s backwards;
}

/* ========================================
   SCROLLBAR
   ======================================== */

::-webkit-scrollbar { width: 6px; height: 6px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: rgba(255, 255, 255, 0.08); border-radius: 3px; transition: background 0.3s ease; }
::-webkit-scrollbar-thumb:hover { background: rgba(255, 255, 255, 0.15); }

html { scroll-behavior: smooth; }

/* ========================================
   PLACEHOLDERS & FOCUS
   ======================================== */

input:focus, textarea:focus, select:focus { 
    outline: none; 
    border-color: #a78bfa !important; 
}

input::placeholder, textarea::placeholder { 
    color: rgba(255, 255, 255, 0.25) !important; 
}

.stNumberInput input[type="number"] { 
    color: #FFFFFF !important; 
}

[data-baseweb="select"] > div > div { 
    background: rgba(15, 39, 68, 0.95) !important; 
    border-color: rgba(255, 255, 255, 0.08) !important; 
}

div[data-baseweb="tooltip"] { 
    background: rgba(15, 39, 68, 0.95) !important; 
    border: 1px solid rgba(255, 255, 255, 0.08) !important; 
    color: #FFFFFF !important; 
}

/* ========================================
   GLOW EFFECTS
   ======================================== */

.glow-border {
    border: 1px solid rgba(167, 139, 250, 0.25);
    box-shadow: 0 0 25px rgba(167, 139, 250, 0.12), inset 0 0 25px rgba(167, 139, 250, 0.03);
    animation: borderGlow 3s ease-in-out infinite;
}

.glow-text {
    animation: textGlow 2s ease-in-out infinite;
}

/* ========================================
   RESPONSIVE
   ======================================== */

@media (max-width: 768px) {
    .hero-title-organic { font-size: 38px; }
    .hero-subtitle-organic { font-size: 16px; }
    .block-container { padding: 1rem !important; }
    
    .feature-card-organic:hover {
        transform: translateY(-4px) scale(1.01);
    }
}

/* ========================================
   HIDE DEFAULT UI
   ======================================== */

#MainMenu { visibility: hidden; }
footer { visibility: hidden; }
.block-container { padding: 2rem 3rem !important; max-width: 1400px !important; }

/* ========================================
   LOADING ANIMATIONS
   ======================================== */

.loading-dots::after {
    content: '';
    animation: dots 1.5s steps(4, end) infinite;
}

@keyframes dots {
    0%, 20% { content: ''; }
    40% { content: '.'; }
    60% { content: '..'; }
    80%, 100% { content: '...'; }
}

/* Spinner */
@keyframes spinner {
    to { transform: rotate(360deg); }
}

.loading-spinner {
    width: 40px;
    height: 40px;
    border: 3px solid rgba(167, 139, 250, 0.2);
    border-top-color: #a78bfa;
    border-radius: 50%;
    animation: spinner 1s linear infinite;
}

/* ========================================
   DASHBOARD GRID ANIMATIONS
   ======================================== */

.dashboard-card {
    opacity: 0;
    animation: fadeInUp 0.5s ease-out forwards;
}

.dashboard-card:nth-child(1) { animation-delay: 0.1s; }
.dashboard-card:nth-child(2) { animation-delay: 0.15s; }
.dashboard-card:nth-child(3) { animation-delay: 0.2s; }
.dashboard-card:nth-child(4) { animation-delay: 0.25s; }
.dashboard-card:nth-child(5) { animation-delay: 0.3s; }
.dashboard-card:nth-child(6) { animation-delay: 0.35s; }
.dashboard-card:nth-child(7) { animation-delay: 0.4s; }
.dashboard-card:nth-child(8) { animation-delay: 0.45s; }
.dashboard-card:nth-child(9) { animation-delay: 0.5s; }

.dashboard-card:hover {
    transform: translateY(-8px) scale(1.02);
    border-color: rgba(167, 139, 250, 0.3) !important;
    box-shadow: 0 25px 50px rgba(0, 0, 0, 0.3), 0 0 40px rgba(167, 139, 250, 0.1) !important;
}

.dashboard-card-icon {
    font-size: 48px;
    margin-bottom: 16px;
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}

.dashboard-card:hover .dashboard-card-icon {
    transform: scale(1.15) rotate(5deg);
}

.dashboard-card-title {
    font-size: 18px;
    font-weight: 600;
    color: #FFFFFF;
    margin-bottom: 8px;
}

.dashboard-card-desc {
    font-size: 14px;
    color: #64748b;
    line-height: 1.5;
}
</style>
""", unsafe_allow_html=True)
