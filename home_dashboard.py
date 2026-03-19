# home_dashboard.py
# Animated home page with feature cards and dashboard

import streamlit as st
st.markdown("""
<style>
[data-testid="stAppViewContainer"]{
background:#0f0a1f;
}
</style>
""", unsafe_allow_html=True)

def render_feature_card(icon, title, description, index=0, step=0, feature_name=None):
    """Render an animated clickable feature card with enhanced styling"""
    card_html = f"""
    <style>
        @keyframes fadeInUp {{
            from {{
                opacity: 0;
                transform: translateY(30px);
            }}
            to {{
                opacity: 1;
                transform: translateY(0);
            }}
        }}

        @keyframes glow {{
            0%, 100% {{
                box-shadow: 0 15px 40px rgba(25,118,210,0.1), inset 0 0 0 1px rgba(25,118,210,0.2);
            }}
            50% {{
                box-shadow: 0 15px 40px rgba(25,118,210,0.25), inset 0 0 0 1px rgba(25,118,210,0.4);
            }}
        }}

        @keyframes pulse {{
            0% {{ transform: scale(1); }}
            50% {{ transform: scale(1.05); }}
            100% {{ transform: scale(1); }}
        }}

        @keyframes shimmer {{
            0% {{ background-position: -1000px 0; }}
            100% {{ background-position: 1000px 0; }}
        }}

        .feature-card-{index} {{
            animation: fadeInUp 0.6s ease-out {index * 0.12}s both;
        }}

        .feature-card {{
            background: linear-gradient(135deg, #E8F4FF 0%, #F0F9FF 100%);
            border-radius: 18px;
            padding: 32px 28px;
            margin: 15px 0;
            box-shadow: 0 12px 35px rgba(25,118,210,0.12);
            cursor: pointer;
            transition: all 0.5s cubic-bezier(0.34, 1.56, 0.64, 1);
            border: 1.5px solid rgba(25,118,210,0.15);
            position: relative;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            height: 240px;
        }}

        .feature-card:hover {{
            transform: translateY(-14px) scale(1.03);
            box-shadow: 0 30px 70px rgba(25,118,210,0.2);
            border-color: rgba(25,118,210,0.4);
            background: linear-gradient(135deg, #D4E8FF 0%, #E8F6FF 100%);
        }}

        .feature-card::before {{
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.4), transparent);
            transition: left 0.6s ease-out;
        }}

        .feature-card:hover::before {{
            left: 100%;
        }}

        .feature-icon {{
            font-size: 64px;
            margin-bottom: 18px;
            display: inline-block;
            transition: transform 0.4s ease-out;
        }}

        .feature-card:hover .feature-icon {{
            transform: scale(1.15) rotate(5deg);
        }}

        .feature-title {{
            color: #0D47A1;
            font-size: 26px;
            font-weight: 700;
            margin-bottom: 14px;
            letter-spacing: -0.5px;
        }}

        .feature-description {{
            color: #1565C0;
            font-size: 15px;
            line-height: 1.7;
            flex-grow: 1;
            overflow: hidden;
            font-weight: 500;
        }}
    </style>

    <div class="feature-card feature-card-{index}" id="card-{index}">
        <div class="feature-icon">{icon}</div>
        <div class="feature-title">{title}</div>
        <div class="feature-description">{description}</div>
    </div>
    """
    return card_html


def render_animated_header():
    """Render animated header with premium gradient and animations"""
    header_html = """
    <style>
        @keyframes slideInDown {{
            from {{
                opacity: 0;
                transform: translateY(-40px);
            }}
            to {{
                opacity: 1;
                transform: translateY(0);
            }}
        }}

        @keyframes float {{
            0%, 100% {{
                transform: translateY(0px);
            }}
            50% {{
                transform: translateY(-8px);
            }}
        }}

        @keyframes titleGlow {{
            0%, 100% {{
                text-shadow: 0 0 20px rgba(255,255,255,0.3);
            }}
            50% {{
                text-shadow: 0 0 40px rgba(255,255,255,0.6), 0 0 60px rgba(255,200,124,0.4);
            }}
        }}

        .hero-header {{
            animation: slideInDown 0.8s ease-out;
            background: linear-gradient(135deg, #1976D2 0%, #1565C0 50%, #0D47A1 100%);
            border-radius: 24px;
            padding: 70px 50px;
            text-align: center;
            color: #FFFFFF;
            margin-bottom: 70px;
            box-shadow: 0 20px 50px rgba(25,118,210,0.25);
            position: relative;
            overflow: hidden;
        }}

        .hero-header::before {{
            content: '';
            position: absolute;
            top: -50%;
            right: -10%;
            width: 400px;
            height: 400px;
            background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 70%);
            border-radius: 50%;
            animation: float 4s ease-in-out infinite;
        }}

        .hero-header::after {{
            content: '';
            position: absolute;
            bottom: -30%;
            left: -5%;
            width: 350px;
            height: 350px;
            background: radial-gradient(circle, rgba(255,255,255,0.08) 0%, transparent 70%);
            border-radius: 50%;
            animation: float 5s ease-in-out infinite reverse;
        }}

        .hero-title {{
            font-size: 80px;
            font-weight: 800;
            margin-bottom: 15px;
            color: #FFFFFF;
            position: relative;
            z-index: 1;
            letter-spacing: -1px;
            animation: titleGlow 3s ease-in-out infinite;
        }}

        .hero-description {{
            font-size: 20px;
            color: rgba(255,255,255,0.95);
            max-width: 700px;
            margin: 0 auto;
            line-height: 1.8;
            position: relative;
            z-index: 1;
            font-weight: 500;
        }}
    </style>

    <div class="hero-header">
        <div class="hero-title">🎓 LearnPath</div>
        <div class="hero-description">
            AI-powered personalized learning paths tailored to your goals, style, and pace.
        </div>
    </div>
    """
    return header_html


def show_home_dashboard():
    """Main home dashboard with premium animations and clickable cards"""

    # Add custom CSS for better overall styling
    st.markdown("""
    <style>
        .dashboard-container {
            padding: 20px 0;
        }
        
        [data-testid="stMainBlockContainer"] {
            padding-top: 1rem;
        }
    </style>
    """, unsafe_allow_html=True)

    # Display animated header
    st.markdown(render_animated_header(), unsafe_allow_html=True)

    # Features data mapped to steps
    features = [
        {"icon": "📋", "title": "Profile Setup", "description": "Create your profile to get personalized learning recommendations.", "step": 1, "key": "profile"},
        {"icon": "📝", "title": "Smart Assessment", "description": "Take a comprehensive assessment to understand your background and goals.", "step": 2, "key": "assessment"},
        {"icon": "🧪", "title": "Skill Quizzes", "description": "Test your knowledge across multiple domains.", "step": 3, "key": "quizzes"},
        {"icon": "🎯", "title": "Learning Paths", "description": "Get personalized AI-generated learning paths.", "step": 4, "key": "paths"},
        {"icon": "📚", "title": "Curated Courses", "description": "Browse courses matched to your learning needs.", "step": 5, "key": "courses"},
        {"icon": "📊", "title": "Progress Dashboard", "description": "Log daily learning and track your progress.", "step": 6, "key": "dashboard"},
        {"icon": "🤖", "title": "AI Coach", "description": "Ask questions and get instant guidance.", "step": 6, "key": "coach", "feature": "coach"},
        {"icon": "🔮", "title": "Learning Predictions", "description": "Get AI predictions on completion time and success.", "step": 6, "key": "predictions", "feature": "predictions"},
    ]

    # Use a responsive 2-column layout with better spacing
    cols = st.columns([1, 1], gap="large")
    
    for idx, feature in enumerate(features):
        col_idx = idx % 2
        with cols[col_idx]:
            # Render the animated card HTML
            card_html = render_feature_card(
                feature["icon"], feature["title"], feature["description"], idx, feature["step"]
            )
            st.markdown(card_html, unsafe_allow_html=True)
            
            # Add invisible button for navigation (positioned over the card)
            if st.button("", key=f"btn_{feature['key']}", use_container_width=True, help=f"Navigate to {feature['title']}"):
                st.session_state.current_step = feature["step"]
                if feature.get("feature"):
                    st.query_params["feature"] = feature["feature"]
                else:
                    # clear query params
                    st.query_params.clear()
                st.rerun()
