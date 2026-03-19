import React, { useState } from 'react';
import { AppContext } from '../App';

function Assessment() {
  const { setStep, assessmentAnswers, setAssessmentAnswers, assessmentPage, setAssessmentPage } = React.useContext(AppContext);
  const [showWarning, setShowWarning] = useState(false);

  const questions = [
    {
      title: "Background & Education",
      questions: [
        { q: "What is your highest level of education?", opts: ["High School", "Some College", "Associate's", "Bachelor's", "Master's", "PhD"] },
        { q: "How would you describe your technical background?", opts: ["None - complete beginner", "Self-taught basics", "Formal education in tech", "Professional experience", "Advanced/expert level"] },
        { q: "How long have you been learning programming?", opts: ["Just started", "Less than 6 months", "6-12 months", "1-2 years", "More than 2 years"] },
        { q: "Have you completed any online courses before?", opts: ["Never", "1-2 courses", "3-5 courses", "6-10 courses", "More than 10 courses"] },
        { q: "How would you rate your problem-solving skills?", opts: ["Beginner", "Below Average", "Average", "Good", "Excellent"] },
        { q: "Do you have any professional work experience in tech?", opts: ["No, never worked in tech", "Internship experience", "1-2 years", "3-5 years", "5+ years"] },
        { q: "What best describes your learning environment?", opts: ["Quiet home office", "Coffee shop/cafe", "Library", "Co-working space", "Varies frequently"] },
        { q: "How many programming languages have you used?", opts: ["None", "1 language", "2-3 languages", "4-5 languages", "6+ languages"] },
        { q: "Have you contributed to any open source projects?", opts: ["Never", "Once or twice", "Occasionally", "Regularly", "I'm a maintainer"] },
        { q: "What is your primary reason for learning tech?", opts: ["Career change", "Career advancement", "Personal interest", "Startup/business", "Academic pursuit"] },
      ]
    },
    {
      title: "Work Under Pressure & Deadlines",
      questions: [
        { q: "How do you handle tight deadlines?", opts: ["Get stressed and make mistakes", "Struggle but deliver", "Manage okay", "Work well under pressure", "Thrive in deadlines"] },
        { q: "When facing a difficult problem, you typically:", opts: ["Give up quickly", "Try for 10 mins then quit", "Persist for hours", "Take breaks and persist", "Enjoy the challenge"] },
        { q: "How do you react to unexpected changes in requirements?", opts: ["Very frustrated", "Somewhat frustrated", "Neutral", "Adapt reasonably", "Embrace change"] },
        { q: "Do you prefer working alone or in teams?", opts: ["Always alone", "Prefer alone", "No preference", "Prefer teams", "Always in teams"] },
        { q: "How do you handle criticism of your code/work?", opts: ["Take it personally", "Feel defensive", "Consider it objectively", "Appreciate feedback", "Seek criticism"] },
        { q: "When stuck on a bug, you usually:", opts: ["Ask immediately", "Search online for 30 min", "Struggle for hours", "Take a break then solve", "Enjoy debugging"] },
        { q: "How would you rate your time management?", opts: ["Poor", "Below average", "Average", "Good", "Excellent"] },
        { q: "Do you prefer structured guidance or freedom?", opts: ["Fully structured", "Mostly structured", "Mix of both", "Mostly freedom", "Complete freedom"] },
        { q: "How do you stay focused during long coding sessions?", opts: ["Can't focus long", "Struggle to focus", "Can focus with effort", "Stay focused easily", "Deep focus state"] },
        { q: "When given a complex task, you:", opts: ["Feel overwhelmed", "Feel anxious", "Plan then execute", "Break into parts", "Dive right in"] },
      ]
    },
    {
      title: "Psychology & Personality",
      questions: [
        { q: "How do you prefer to receive feedback?", opts: ["Written only", "Written preferred", "No preference", "Face to face", "Video call"] },
        { q: "When learning something new, you prefer:", opts: ["Video tutorials", "Written tutorials", "Hands-on practice", "Mix of all", "Building projects"] },
        { q: "How do you handle failure?", opts: ["Give up entirely", "Feel discouraged", "Try again with changes", "Learn from failure", "Use failure as motivation"] },
        { q: "Are you more of a generalist or specialist?", opts: ["Fully generalist", "More generalist", "Balanced", "More specialist", "Fully specialist"] },
        { q: "How do you prefer to plan your learning?", opts: ["Detailed schedule", "Weekly goals", "Monthly goals", "Loose direction", "No plan at all"] },
        { q: "Do you enjoy competitive environments?", opts: ["Strongly dislike", "Somewhat dislike", "Neutral", "Somewhat enjoy", "Love competition"] },
        { q: "How often do you review and reflect on your progress?", opts: ["Never", "Rarely", "Sometimes", "Often", "Always"] },
        { q: "What motivates you most?", opts: ["Money", "Recognition", "Learning itself", "Helping others", "Problem solving"] },
        { q: "How do you handle ambiguity?", opts: ["Very uncomfortable", "Somewhat uncomfortable", "Neutral", "Comfortable", "Thrives in ambiguity"] },
        { q: "Do you prefer working on one thing or multiple things?", opts: ["Single task only", "Prefer single task", "Mix of both", "Prefer multiple", "Many things at once"] },
      ]
    },
    {
      title: "Interests & Goals",
      questions: [
        { q: "What interests you most in tech?", opts: ["Building websites", "Data science/AI", "Cloud/DevOps", "Mobile development", "Cybersecurity"] },
        { q: "What's your primary learning goal?", opts: ["Get a job in tech", "Switch careers", "Get promoted", "Build projects", "Explore technologies"] },
        { q: "What's your expected timeline to see results?", opts: ["Immediately", "Within 1 month", "3-6 months", "Within a year", "Patient, no rush"] },
        { q: "How important is earning potential in your choices?", opts: ["Top priority", "Important", "Somewhat important", "Not very important", "Not important"] },
        { q: "Do you prefer learning alone or in community?", opts: ["Alone", "With mentor", "In group", "Mix of approaches", "Online forums"] },
        { q: "What's your ideal learning environment?", opts: ["Quiet/focused", "Collaborative", "Flexible", "Structured", "Coffee shop vibes"] },
        { q: "How do you feel about videos vs reading?", opts: ["Prefer videos", "Prefer reading", "Mix of both", "Depends on topic", "Hands-on practice"] },
        { q: "What type of learner are you?", opts: ["Visual", "Auditory", "Reading/Writing", "Kinesthetic", "Multimodal"] },
        { q: "What rewards keep you motivated?", opts: ["Career advancement", "Money", "Recognition", "Personal satisfaction", "Knowledge itself"] },
        { q: "Where do you see yourself in 2 years?", opts: ["Working as developer", "Running business", "In leadership role", "Freelancing", "Still exploring"] },
      ]
    },
    {
      title: "Time Management & Productivity",
      questions: [
        { q: "How many hours per day can you realistically commit?", opts: ["Less than 1 hour", "1-2 hours", "2-4 hours", "4-6 hours", "More than 6 hours"] },
        { q: "When do you prefer to learn?", opts: ["Early morning", "Morning", "Afternoon", "Evening", "Flexible/varies"] },
        { q: "How often do you meet your self-set learning goals?", opts: ["Almost never", "Rarely", "About half", "Most of the time", "Almost always"] },
        { q: "What's your biggest obstacle to consistent learning?", opts: ["Lack of time", "Procrastination", "Lack of motivation", "Too many resources", "No clear direction"] },
        { q: "How do you stay accountable?", opts: ["Don't track", "Journal/app", "Tell others", "Join community", "Hire coach"] },
        { q: "How do you handle learning when tired after work?", opts: ["Push through", "Take nap then study", "Skip that day", "Switch to light activities", "Use caffeine"] },
        { q: "What's your best time management technique?", opts: ["Time blocking", "Pomodoro", "To-do lists", "No specific technique", "Flexible approach"] },
        { q: "How do you deal with distractions?", opts: ["Use focus apps", "Embrace them", "Dedicated space", "Listen to music", "Struggle with them"] },
        { q: "When you miss a learning session, you:", opts: ["Catch up next day", "Skip and continue", "Feel guilty", "Modify schedule", "Not a big deal"] },
        { q: "How do you maintain work-life-learning balance?", opts: ["Strict boundaries", "Flexible approach", "Learning is hobby", "Struggle to balance", "Make it priority"] },
      ]
    },
    {
      title: "Technical Background & Skills",
      questions: [
        { q: "How would you rate your programming knowledge?", opts: ["Expert - complex systems", "Advanced - full apps", "Intermediate - fundamentals", "Beginner - just starting", "None - complete beginner"] },
        { q: "Which technologies are you most comfortable with?", opts: ["Python", "JavaScript", "Java", "C/C++", "Go/Rust"] },
        { q: "Have you built complete projects before?", opts: ["Yes, professionally", "Yes, personal", "Started but didn't finish", "No but have ideas", "No, never tried"] },
        { q: "What's your debugging approach?", opts: ["Professional tools", "Print statements", "Research online", "Ask for help", "Trial and error"] },
        { q: "How comfortable are you with command line?", opts: ["Expert - daily use", "Comfortable", "Basic - occasional", "Uncomfortable", "Never used"] },
        { q: "Have you contributed to open source?", opts: ["Yes, regularly", "Yes, few times", "No, but want to", "No, not interested", "Working on it"] },
        { q: "How do you typically solve new problems?", opts: ["Search docs", "Google/Stack Overflow", "Video tutorials", "Ask communities", "Trial and error"] },
        { q: "What's your experience with version control?", opts: ["Git expert", "Comfortable", "Basic knowledge", "Heard of it", "Never used"] },
      ]
    }
  ];

  const totalPages = questions.length;
  const currentQuestions = questions[assessmentPage].questions;

  const handleAnswer = (index, answer) => {
    setAssessmentAnswers({ ...assessmentAnswers, [`${assessmentPage}_${index}`]: answer });
  };

  const goNext = () => {
    const currentPageQuestions = questions[assessmentPage].questions;
    const answeredCount = currentPageQuestions.filter((_, i) => assessmentAnswers[`${assessmentPage}_${i}`]).length;
    
    if (answeredCount < currentPageQuestions.length) {
      setShowWarning(true);
      setTimeout(() => setShowWarning(false), 3000);
      return;
    }
    
    if (assessmentPage < totalPages - 1) {
      setAssessmentPage(assessmentPage + 1);
      setShowWarning(false);
    } else {
      setStep(3);
    }
  };

  const goPrev = () => {
    if (assessmentPage > 0) {
      setAssessmentPage(assessmentPage - 1);
    }
  };

  const clearAnswers = () => {
    setAssessmentAnswers({});
  };

  return (
    <div className="assessment-page">
      <h2>🧠 Smart Assessment</h2>
      <p style={{ marginBottom: '24px' }}>Answer these questions to help us understand your psychology, learning style, and work habits.</p>

      <div className="progress-bar" style={{ marginBottom: '8px' }}>
        <div className="fill" style={{ width: `${((assessmentPage + 1) / totalPages) * 100}%` }}></div>
      </div>
      <p style={{ marginBottom: '24px' }}>Page {assessmentPage + 1} of {totalPages} — {questions[assessmentPage].title}</p>

      {showWarning && (
        <div className="warning-message">
          ⚠️ Please answer all questions on this page before proceeding.
        </div>
      )}

      <div className="card">
        {currentQuestions.map((question, qIndex) => (
          <div key={qIndex} style={{ marginBottom: '24px' }}>
            <p style={{ fontWeight: '600', marginBottom: '12px' }}>{qIndex + 1}. {question.q}</p>
            <div className="radio-group">
              {question.opts.map((opt, oIndex) => (
                <label 
                  key={oIndex} 
                  className={`radio-option ${assessmentAnswers[`${assessmentPage}_${qIndex}`] === opt ? 'selected' : ''}`}
                  onClick={() => handleAnswer(qIndex, opt)}
                >
                  {opt}
                </label>
              ))}
            </div>
          </div>
        ))}
      </div>

      <div className="flex gap-2" style={{ marginTop: '24px' }}>
        <button className="btn btn-secondary" onClick={goPrev} disabled={assessmentPage === 0}>
          ← Previous
        </button>
        <button className="btn btn-secondary" onClick={clearAnswers}>
          Clear All
        </button>
        <button className="btn" onClick={goNext} style={{ marginLeft: 'auto' }}>
          {assessmentPage < totalPages - 1 ? 'Next →' : 'Finish ✓'}
        </button>
      </div>
    </div>
  );
}

export default Assessment;
