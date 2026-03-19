# 🏗️ LearnPath - Technical Architecture

## System Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│                         STREAMLIT UI LAYER                           │
│  (7-Step Frontend with Step-by-Step Flow, No Sidebar)               │
└────────────────┬────────────────────────────────────────────────────┘
                 │
┌────────────────┴────────────────────────────────────────────────────┐
│                      CORE LOGIC MODULES                              │
│                                                                       │
│  ├─ Assessment Engine (expanded_questions.py)                       │
│  ├─ Quiz System (skill_assessment_quizzes.py)                       │
│  ├─ Skill Recommender (enhanced_skill_engine.py)                    │
│  ├─ Path Generator (advanced_learning_path_engine.py)               │
│  ├─ Course Finder (course_recommendation_engine.py)                 │
│  ├─ Progress Tracker (daily_tracking_and_progress.py)               │
│  ├─ AI Coach (ai_coach_qa_system.py)                                │
│  └─ Prediction Engine (prediction_engine_advanced.py)               │
└────────────────┬────────────────────────────────────────────────────┘
                 │
┌────────────────┴────────────────────────────────────────────────────┐
│                    DATA LAYER (SESSION STATE)                        │
│                                                                       │
│  - user_profile (dict)                                              │
│  - quiz_results (dict)                                              │
│  - selected_skill (dict)                                            │
│  - learning_path (dict)                                             │
│  - tracker (DailyLearningTracker object)                            │
│  - ai_coach (AICoach object)                                        │
└────────────────┬────────────────────────────────────────────────────┘
                 │
┌────────────────┴────────────────────────────────────────────────────┐
│               PERSISTENT DATA (Ready for DB)                         │
│                                                                       │
│  └─ Database Integration Point                                      │
│     (JSON/SQL ready - not yet implemented)                          │
└─────────────────────────────────────────────────────────────────────┘
```

## Module Breakdown

### 1. **expanded_questions.py** - Assessment Engine
**Purpose:** Comprehensive 10-level user profiling

**Key Classes:**
- `EXPANDED_ASSESSMENT_LEVELS` (dict) - 10 assessment levels

**Functions:**
- `get_all_questions_flat()` - Flatten all questions
- `get_total_questions_count()` - Get total questions

**Data Structure:**
```python
{
  "level_X_name": {
    "title": str,
    "icon": str,
    "description": str,
    "questions": [
      {
        "key": str,
        "question": str,
        "type": "slider|single|multi",
        "options": list (if single/multi)
      }
    ]
  }
}
```

**Output:**
- User profile dictionary with 50+ attributes

---

### 2. **skill_assessment_quizzes.py** - Quiz System
**Purpose:** Assess user knowledge across multiple domains

**Key Classes:**
- `SKILL_ASSESSMENT_QUIZZES` (dict) - 8+ skill quizzes

**Functions:**
- `get_all_quizzes()` - List available quizzes
- `calculate_quiz_score(quiz_id, answers)` - Score calculation
- `get_quiz(quiz_id)` - Get specific quiz

**Quiz Database:**
- Programming Fundamentals
- Problem Solving & Logic
- Data Structures
- Web Development
- Databases & SQL
- Python Basics
- Math & Algorithms
- AI/ML Basics
- System Design

**Output:**
```python
{
  "score": int,
  "total": int,
  "percentage": float,
  "passed": bool
}
```

---

### 3. **enhanced_skill_engine.py** - Skill Recommender
**Purpose:** Intelligent skill recommendations with complementary suggestions

**Key Classes:**
- `COMPREHENSIVE_SKILLS` (dict) - Skill database organized by category

**Functions:**
- `recommend_skills_enhanced(profile, quiz_results)` - Generate recommendations
- `get_skill_by_name(skill_name)` - Look up skill
- `suggest_learning_sequence(profile, selected_skill)` - Path planning
- `get_learning_path_for_skill(skill_name)` - Get path for skill

**Skill Categories:**
- Meta (Learning, Problem Solving, Communication)
- Programming (Python, JavaScript, etc.)
- Data (SQL, Analysis, Statistics)
- AI/ML (ML, Deep Learning, NLP, Vision)
- Frontend (HTML/CSS, React, UI/UX)
- Backend (Node.js, Django, APIs, DevOps)
- Advanced (System Design, Performance, Security)

**Output:**
```python
{
  "primary_skills": [...],
  "complementary_skills": [...],
  "advanced_skills": [...],
  "reasoning": str,
  "total_recommendations": int
}
```

---

### 4. **advanced_learning_path_engine.py** - Path Generator
**Purpose:** AI-powered learning path generation with customization

**Key Classes:**
- `LearningPathGenerator` - Main path generation class

**Methods:**
- `generate_base_path()` - Create base learning path
- `customize_path(customization)` - Apply customizations
- `analyze_path_flaws()` - Identify issues & risks
- `get_recommendations_vs_custom(user_custom_path)` - Compare paths

**Path Structure:**
```python
{
  "skill": str,
  "pace": str,  # Fast/Balanced/Slow
  "estimated_duration_weeks": int,
  "stages": [
    {
      "title": str,
      "duration_weeks": int,
      "learn": list,
      "practice": list,
      "milestone": str
    }
  ],
  "timeline": [...],
  "milestones": [...],
  "path_analysis": {
    "flaws": [...],
    "warnings": [...],
    "recommendations": [...]
  }
}
```

**Flaw Analysis Identifies:**
- Aggressive timeline
- Low consistency risk
- Burnout potential
- Missing prerequisites
- Procrastination mismatch

---

### 5. **course_recommendation_engine.py** - Course Finder
**Purpose:** Curate and recommend courses from multiple platforms

**Key Classes:**
- `COURSE_DATABASE` (dict) - Comprehensive course database

**Functions:**
- `recommend_courses(skill_name, profile, budget)` - Get recommendations
- `get_course(course_id)` - Get course details
- `filter_courses(skill_name, filters)` - Filter by criteria

**Course Data Structure:**
```python
{
  "id": str,
  "title": str,
  "platform": str,  # Udemy, Coursera, etc.
  "instructor": str,
  "duration_hours": int,
  "level": str,
  "rating": float,
  "students": int,
  "price": str,
  "content": list,
  "learning_style": list,
  "time_commitment": str,
  "reviews_highlight": str
}
```

**Platforms Covered:**
- Udemy
- Coursera
- Real Python
- Fast.ai
- Scrimba
- Educative
- Mode Analytics
- GitHub

---

### 6. **daily_tracking_and_progress.py** - Progress Tracker
**Purpose:** Track daily learning and generate insights

**Key Classes:**
- `DailyLearningTracker` - Main tracking class
- `ProgressVisualizer` - Generate chart data

**Methods:**
- `log_daily_activity(activity_data)` - Record daily log
- `get_progress_summary()` - Overall summary
- `identify_problem_areas()` - Find struggles
- `get_insights_and_patterns()` - Generate insights
- `get_chart_data_*()` - Chart data generators

**Daily Log Structure:**
```python
{
  "date": str,
  "hours_spent": float,
  "sleep_hours": int,
  "topics_covered": list,
  "understanding_level": int (1-10),
  "difficulty_faced": str,
  "completed_tasks": list,
  "mood": str,
  "productivity_rating": int (1-10),
  "environment": str,
  "notes": str
}
```

**Insights Generated:**
- Progress summary (hours, days, averages)
- Problem areas (low understanding, recurring difficulties)
- Positive trends (improvement, high productivity)
- Recommendations (personalized actions)

---

### 7. **ai_coach_qa_system.py** - AI Coach
**Purpose:** Answer doubts and provide guidance

**Key Classes:**
- `AICoach` - Main coaching class
- `InteractiveQASession` - Interactive Q&A

**Methods:**
- `ask_doubt(doubt_data)` - Process doubt
- `rate_response(doubt_id, satisfaction_rating)` - Rate response
- `get_review_and_suggestions(doubt_id)` - Get review

**Doubt Structure:**
```python
{
  "id": int,
  "topic": str,
  "doubt_text": str,
  "context": str,
  "difficulty_level": str,
  "status": str,
  "ai_response": {
    "main_answer": str,
    "explanation": str,
    "examples": str,
    "resources": list,
    "follow_up_suggestion": str
  },
  "user_satisfaction": int (1-5)
}
```

---

### 8. **prediction_engine_advanced.py** - Prediction Engine
**Purpose:** Predict learning outcomes with high accuracy

**Key Classes:**
- `LearningPredictorAdvanced` - Main predictor class

**Methods:**
- `predict_completion_time()` - When will complete
- `predict_mastery_timeline()` - Mastery progression
- `predict_success_rate()` - Success probability
- `predict_optimal_learning_schedule()` - Best study times
- `generate_prediction_report()` - Full report

**Prediction Outputs:**

**Completion Time:**
```python
{
  "estimated_completion_weeks": float,
  "estimated_completion_date": str,
  "confidence_percentage": float,
  "factors": {
    "consistency_adjustment": float,
    "procrastination_adjustment": float,
    "actual_performance_adjustment": float
  }
}
```

**Success Rate:**
```python
{
  "success_probability_percentage": float (0-100),
  "success_rating": str,  # Very High / High / Medium / Low
  "key_factors": {
    "positive": list,
    "negative": list,
    "neutral": list
  }
}
```

---

## Algorithm Specifications

### 1. Skill Recommendation Algorithm
```
Input: user_profile, quiz_results
Process:
  1. Always recommend top 2 meta skills
  2. Check interests and goals for programming skills
  3. Check for data/analytics interests
  4. Check for AI/ML interests
  5. Check for frontend/fullstack interests
  6. Score each skill (1-10 fit score)
  7. Find complementary skills
  8. Sort by priority and fit
Output: Ranked list with reasoning
```

### 2. Learning Path Duration Calculation
```
base_duration = skill.estimated_weeks
consistency_factor = consistency / 5  (range: 0.2 to 2.0)

if procrastination >= 8:
  procrastination_penalty = 1.3
elif procrastination <= 2:
  procrastination_penalty = 0.9
else:
  procrastination_penalty = 1.0

adjusted_duration = base_duration × 
                   (procrastination_penalty / consistency_factor) × 
                   performance_multiplier
```

### 3. Success Rate Calculation
```
score = 70
score += (consistency - 5) × 3
score += (motivation - 5) × 2
if daily_hours >= 3: score += 5
if daily_hours < 1: score -= 10

if burnout == "Often": score -= 15
if burnout == "Rarely": score += 10

score -= (procrastination - 5) × 2
score = max(20, min(95, score))  # Cap between 20-95%
```

---

## Data Flow

### User Assessment Flow
```
User Input (10 levels)
    ↓
Profile Dictionary (50+ attributes)
    ↓
Quiz Results (8+ quizzes)
    ↓
Combined Profile Data
    ↓
Skill Recommendation
```

### Learning Path Generation Flow
```
Selected Skill + User Profile
    ↓
Base Path Generation (stages, timeline, milestones)
    ↓
Path Analysis (flaws, warnings, risks)
    ↓
Success Probability Calculation
    ↓
Final Learning Path with Analysis
```

### Daily Progress Flow
```
Daily Log Entry
    ↓
Progress Summary Update
    ↓
Problem Area Detection
    ↓
Positive Trend Recognition
    ↓
Insight Generation
    ↓
Recommendation Generation
```

---

## Integration Points (Database Ready)

### Ready for SQL/NoSQL Integration

**User Profile Table:**
```sql
CREATE TABLE users (
  user_id PRIMARY KEY,
  profile_data JSON,
  created_at TIMESTAMP,
  updated_at TIMESTAMP
)
```

**Learning Path Table:**
```sql
CREATE TABLE learning_paths (
  path_id PRIMARY KEY,
  user_id FOREIGN KEY,
  skill_name TEXT,
  created_date DATE,
  completion_date DATE,
  status ENUM
)
```

**Daily Logs Table:**
```sql
CREATE TABLE daily_logs (
  log_id PRIMARY KEY,
  user_id FOREIGN KEY,
  path_id FOREIGN KEY,
  log_date DATE,
  hours_spent FLOAT,
  understanding_level INT,
  mood TEXT,
  data JSON
)
```

---

## Performance Considerations

**Current Implementation:**
- All data in session state (fast, no DB overhead)
- In-memory calculations
- No external API calls
- Ready for production caching

**Optimization Opportunities:**
- Cache skill recommendations
- Pre-compute common paths
- Batch prediction calculations
- Database indexing on user_id, dates

---

## Extensibility

### Easy to Add:

1. **New Quizzes** - Add to `SKILL_ASSESSMENT_QUIZZES`
2. **New Skills** - Add to `COMPREHENSIVE_SKILLS`
3. **New Courses** - Add to `COURSE_DATABASE`
4. **Custom Algorithms** - Extend prediction engine
5. **New Visualizations** - Add to `ProgressVisualizer`

### API Integration Ready:
- LLM integration for AI Coach
- Real course data APIs
- Calendar integration
- Email notification hooks
- Analytics platforms

---

## Quality Assurance

**Validation Points:**
- Assessment responses (min/max values)
- Quiz answer ranges
- Profile field validation
- Duration calculations
- Success probability bounds (20-95%)

**Error Handling:**
- Missing data fallbacks
- Invalid input rejection
- Graceful degradation
- Informative error messages

---

## Security Considerations

**Current (Local):**
- No external data transmission
- Session-based storage
- No authentication needed for demo

**When Integrating Database:**
- User authentication required
- Data encryption at rest
- HTTPS for all connections
- Regular backups
- GDPR compliance

---

## Testing Checklist

- [ ] All 10 assessment levels complete
- [ ] All 8+ quizzes scoreable
- [ ] Skill recommendations accurate
- [ ] Path generation non-breaking
- [ ] Flaw analysis identifies real risks
- [ ] Course recommendations relevant
- [ ] Daily logging works
- [ ] Predictions reasonable
- [ ] UI step flow smooth
- [ ] No data loss on back button

---

This architecture is production-ready for local deployment and easily extensible for enterprise integration.
