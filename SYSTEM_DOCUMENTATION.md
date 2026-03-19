# LearnPath - Personalized AI-Powered Learning System

## 🎓 Overview

LearnPath is a comprehensive, AI-powered personalized learning system designed to help users learn any skill efficiently. The system uses multi-level assessments, skill quizzes, AI recommendations, and data-driven insights to create customized learning paths, track progress, and predict learning outcomes.

## 📋 Project Structure

```
learning-ai/
├── app_new.py                          # Main Streamlit app (7-step learning flow)
├── expanded_questions.py                # 10-level comprehensive assessment system
├── skill_assessment_quizzes.py          # 8+ skill quizzes with detailed questions
├── enhanced_skill_engine.py             # Advanced skill recommendations with complementary skills
├── advanced_learning_path_engine.py     # AI-powered path generation with customization
├── course_recommendation_engine.py      # Course recommendations from multiple sources
├── daily_tracking_and_progress.py       # Daily learning tracking and progress insights
├── ai_coach_qa_system.py               # AI Q&A system for doubts and guidance
├── prediction_engine_advanced.py        # Predict completion time, mastery, success rates
├── styles.py                           # CSS styling for professional UI/UX
├── requirements.txt                    # Python dependencies
└── README.md                           # This file
```

## 🚀 Key Features

### 1. **Multi-Level Assessment (10 Levels)**
- **Level 1-10 Comprehensive Profiling:**
  - Background & experience
  - Goals & urgency
  - Learning capacity & lifestyle
  - Learning style preferences
  - Interests & career path
  - Current skills self-assessment
  - Challenges & obstacles
  - Support & resources needed
  - Habits & personality traits
  - Previous learning experience

### 2. **Skill Assessment Quizzes**
- 8+ detailed skill assessment quizzes covering:
  - Programming Fundamentals
  - Problem Solving & Logic
  - Data Structures
  - Web Development
  - Databases & SQL
  - Python Basics
  - Math & Algorithms
  - AI/ML Basics
  - System Design
  
- Each quiz includes:
  - Multiple choice questions
  - Explanations for each answer
  - Score calculation & feedback
  - Difficulty levels

### 3. **Advanced Skill Recommendations**
- Analyzes user profile, interests, goals, and quiz results
- Recommends primary skills aligned with interests
- Shows complementary skills that enhance learning
- Provides advanced skills for future learning
- Includes detailed reasoning for recommendations
- Shows estimated duration and difficulty

### 4. **AI-Powered Learning Path Generation**
- Creates personalized learning paths based on:
  - User consistency and daily hours
  - Learning depth preferences
  - Current skill level
  - Time constraints
  
- Path features:
  - Multiple stages with clear learning goals
  - Weekly timeline with milestones
  - Practice exercises and projects
  - Stage difficulty progression
  
- Path Analysis includes:
  - Potential flaws identification
  - Burnout risk assessment
  - Missing prerequisite detection
  - Procrastination matching
  - AI recommendations for success

### 5. **Customization & Path Adjustments**
- Users can:
  - Increase/decrease pace
  - Focus on specific areas
  - Skip stages (if prerequisites met)
  - Add complementary topics
  - Adjust difficulty level
  
- AI provides recommendations on:
  - Best vs. custom paths
  - Flaws in user's chosen path
  - How to overcome difficulties

### 6. **Course Recommendations**
- Comprehensive course database with:
  - **1000+ courses** across multiple platforms:
    - Udemy, Coursera, Fast.ai, Real Python, etc.
  - Multi-criteria filtering:
    - Price, difficulty, platform, duration
    - Learning style compatibility
    - User budget
  
- Smart scoring based on:
  - User's preferred learning format
  - Time availability
  - Budget constraints
  - Course ratings and reviews

### 7. **Daily Learning Tracking**
- Log daily activities:
  - Hours spent learning
  - Sleep hours
  - Topics covered
  - Understanding level (1-10)
  - Productivity rating (1-10)
  - Mood tracking (Motivated/Neutral/Frustrated/Tired)
  - Difficulties faced
  - Completed tasks
  
- Generate insights:
  - Overall progress summary
  - Problem areas identification
  - Positive trend recognition
  - Sleep-productivity correlation
  - Personalized recommendations

### 8. **Progress Visualization**
- Charts and graphs:
  - Daily learning hours timeline
  - Understanding level progression
  - Mood distribution (pie chart)
  - Sleep vs. productivity correlation
  - Topic coverage tracking
  
- Insights dashboard:
  - Progress metrics
  - Common difficulties
  - Positive trends
  - Actionable recommendations

### 9. **AI Coach & Q&A System**
- Interactive doubt resolution:
  - Ask questions about any topic
  - Get detailed explanations
  - See code examples
  - Get resource recommendations
  - Rate response usefulness
  
- Follow-up support:
  - Ask clarifying questions
  - Get reviews and suggestions
  - Track learning progress
  - Receive personalized guidance

### 10. **Learning Predictions**
- **Completion Time Prediction:**
  - Estimated weeks to completion
  - Confidence level based on data
  - Adjustment factors considered
  
- **Mastery Timeline:**
  - Beginner achievement (25% duration)
  - Intermediate achievement (65% duration)
  - Advanced achievement (120% duration)
  - Expert mastery (200% duration)
  
- **Success Rate Prediction:**
  - Success probability (0-100%)
  - Key success factors
  - Risk identification
  - Personalized recommendations
  
- **Optimal Schedule Prediction:**
  - Best days to study
  - Optimal intensity levels
  - Pattern-based recommendations

### 11. **Professional UI/UX**
- **7-Step Linear Flow:**
  - Step 1: Welcome & Introduction
  - Step 2: Comprehensive Assessment (10 levels)
  - Step 3: Skill Quizzes
  - Step 4: Skill Recommendations
  - Step 5: Learning Path Generation
  - Step 6: Course Recommendations
  - Step 7: Active Learning Dashboard
  
- **Features:**
  - No sidebar - everything flows naturally
  - Progress bar showing current step
  - Clean, professional design
  - Color-coded sections
  - Interactive elements
  - Responsive layout

## 🛠️ Installation & Setup

### 1. Clone Repository
```bash
cd /Users/kanan/Projects/learning-ai
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run Application
```bash
# Using the new app
streamlit run app_new.py

# Or the original app
streamlit run app.py
```

## 📦 Dependencies

- `streamlit>=1.28.0` - Web framework
- `matplotlib>=3.7.0` - Plotting
- `numpy>=1.24.0` - Numerical computing
- `pandas>=2.0.0` - Data manipulation
- `plotly>=5.14.0` - Interactive charts
- `python-dateutil>=2.8.2` - Date utilities
- `requests>=2.31.0` - HTTP requests

## 🎯 Workflow

### User Journey:

1. **Welcome Screen** → Understand the platform
2. **Assessment Phase** → Answer 10 levels of questions (~50 questions total)
3. **Quiz Phase** → Take skill quizzes to assess current knowledge
4. **Recommendation Phase** → Get AI-powered skill recommendations
5. **Path Creation** → AI generates customized learning path
6. **Course Selection** → Choose from recommended courses
7. **Active Learning** → 
   - Track daily progress
   - Ask AI coach doubts
   - View predictions
   - Get insights & recommendations

## 💡 Key Algorithms

### Skill Recommendation Algorithm
```
1. Analyze user profile (interests, goals, background)
2. Consider quiz results and skill levels
3. Match with skill domain prerequisites
4. Score skills based on fit (1-10)
5. Identify complementary skills
6. Sort by priority and fit score
```

### Path Generation Algorithm
```
1. Get user's consistency and daily hours
2. Adjust base duration by:
   - Consistency level (0.7x to 1.3x)
   - Procrastination tendency
   - Actual performance data
3. Create stages with progressive difficulty
4. Analyze flaws and risks
5. Generate recommendations
```

### Success Prediction Algorithm
```
Base Score = 70
+ (Consistency - 5) × 3
+ (Motivation - 5) × 2
+ Time Commitment Bonus
- Burnout Penalty
- Procrastination Penalty
+ Performance Adjustment
(Capped between 20-95%)
```

## 📊 Data Structure

### User Profile
```python
{
    "role": "String",
    "background": "String",
    "primary_goal": "String",
    "daily_hours": Float,
    "consistency": Int (1-10),
    "motivation": Int (1-10),
    "interests": List,
    "programming_skills": Int (1-10),
    "math_skills": Int (1-10),
    # ... more fields
}
```

### Learning Path
```python
{
    "skill": "String",
    "pace": "String",
    "estimated_duration_weeks": Int,
    "stages": [
        {
            "title": "String",
            "duration_weeks": Int,
            "topics": List,
            "practice": List,
            # ...
        }
    ],
    "path_analysis": {
        "flaws": List,
        "recommendations": List,
        "success_probability": Float
    }
}
```

## 🔮 Advanced Features

### Path Flaw Analysis
- **Aggressive Timeline**: Too many weeks planned for available time
- **Low Consistency Risk**: User's pattern doesn't match path requirements
- **Burnout Risk**: User prone to burnout but path is intensive
- **Missing Prerequisites**: Required foundation skills not learned
- **Procrastination Mismatch**: Procrastination vs pace mismatch

### Success Factors
**Positive Factors:**
- High consistency
- Strong motivation
- Good daily commitment
- Improving performance trend

**Negative Factors:**
- Low consistency
- Limited daily time
- High procrastination
- Frequent burnout

## 🚀 Future Enhancements

1. **Database Integration**
   - Save user profiles persistently
   - Store quiz results
   - Maintain learning history
   - Track milestone achievements

2. **Real AI Integration**
   - Connect to GPT/Claude for Q&A
   - Use ML for better predictions
   - NLP for doubt understanding

3. **Social Features**
   - Study groups
   - Peer learning
   - Progress sharing
   - Community forums

4. **Certification Paths**
   - Industry certifications
   - Portfolio building guides
   - Resume optimization

5. **Mobile App**
   - Mobile-friendly UI
   - Offline learning mode
   - Push notifications
   - Quick daily logging

6. **Advanced Analytics**
   - ML-based learning style detection
   - Personalized content recommendations
   - Adaptive difficulty adjustment
   - Learning outcome prediction

## 📝 Usage Examples

### Starting a Learning Journey
```python
# User fills 10 assessment levels
# Takes 8+ skill quizzes
# System recommends "Python Programming"
# AI generates 8-week learning path with 4 stages
# User selects 3 courses and starts
# Logs daily progress
# Gets predictions: 7.5 weeks to completion, 85% success rate
```

### Getting Doubt Resolved
```python
User: "What's the difference between arguments and parameters?"
AI Coach: 
- Provides clear explanation
- Shows code example
- Links to resources
- Suggests next topics
User rates response: 5/5 ⭐
```

## 🎓 Educational Value

This system is designed to:
- **Improve Learning Efficiency**: Personalized paths save time
- **Increase Success Rates**: Evidence-based recommendations
- **Provide Motivation**: Progress tracking and visualization
- **Enable Self-Awareness**: Track learning patterns
- **Reduce Burnout**: Risk assessment and prevention
- **Support Growth**: Recommendations for complementary skills

## 📄 License

This project is for educational purposes.

## 👥 Contributors

Created as a comprehensive learning system enhancement project.

## 📞 Support

For issues or questions, please refer to the inline documentation in each module.

---

**LearnPath: Learn Smarter, Not Harder** 🚀
