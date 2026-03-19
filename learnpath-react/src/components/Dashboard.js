import React, { useState, useEffect } from 'react';
import { AppContext } from '../App';
import './Dashboard.css';

function Dashboard() {
  const { setStep, userProfile, quizBatchScores, learningPath, dailyLogs, enrolledCourses } = React.useContext(AppContext);
  const [animatedStats, setAnimatedStats] = useState({ quizzes: 0, score: 0, progress: 0, hours: 0 });
  const [isLoaded, setIsLoaded] = useState(false);
  
  const name = userProfile.name || 'Learner';
  const hour = new Date().getHours();
  const greeting = hour < 12 ? 'Good morning' : hour < 17 ? 'Good afternoon' : 'Good evening';
  
  const quizCount = Object.keys(quizBatchScores).length;
  let avgScore = 0;
  if (quizCount > 0) {
    const total = Object.values(quizBatchScores).reduce((sum, s) => sum + s.score, 0);
    avgScore = Math.round(total / quizCount);
  }
  
  const completed = learningPath.filter(p => p.progress === 100).length;
  const totalHours = dailyLogs.reduce((sum, log) => sum + log.hours, 0);
  const pathProgress = learningPath.length > 0 ? Math.round((completed / learningPath.length) * 100) : 0;

  useEffect(() => {
    setIsLoaded(true);
    animateNumbers();
  }, []);

  const animateNumbers = () => {
    const duration = 1500;
    const steps = 60;
    const interval = duration / steps;
    let step = 0;
    
    const timer = setInterval(() => {
      step++;
      const progress = step / steps;
      
      setAnimatedStats({
        quizzes: Math.round(quizCount * progress),
        score: Math.round(avgScore * progress),
        progress: Math.round(pathProgress * progress),
        hours: Math.round(totalHours * progress)
      });
      
      if (step >= steps) clearInterval(timer);
    }, interval);
  };

  const getMotivationalQuote = () => {
    const quotes = [
      "Every expert was once a beginner! 🌱",
      "Small progress is still progress! 📈",
      "You're doing amazing! Keep going! ⭐",
      "Consistency is the key to success! 🔑",
      "Learning is a superpower! 💪",
      "Today's effort is tomorrow's success! 🏆",
    ];
    return quotes[Math.floor(Math.random() * quotes.length)];
  };

  const getTimeIcon = () => {
    if (hour < 12) return '🌅';
    if (hour < 17) return '☀️';
    return '🌙';
  };

  const actions = [
    { icon: "📝", title: "Take Quiz", desc: "Test knowledge", step: 3, color: 'purple' },
    { icon: "🛤️", title: "Learning Path", desc: "Your roadmap", step: 4, color: 'blue' },
    { icon: "📚", title: "Courses", desc: "Browse catalog", step: 5, color: 'green' },
    { icon: "🤖", title: "AI Coach", desc: "Get guidance", step: 7, color: 'orange' },
    { icon: "🔮", title: "Predictions", desc: "See timeline", step: 8, color: 'pink' },
  ];

  return (
    <div className={`dashboard-page ${isLoaded ? 'loaded' : ''}`}>
      <div className="dashboard-header">
        <div className="greeting-section">
          <div className="time-icon">{getTimeIcon()}</div>
          <div className="greeting-content">
            <h1>{greeting}, {name}! 👋</h1>
            <p className="motivation-quote">{getMotivationalQuote()}</p>
          </div>
        </div>
        <div className="header-decoration">
          <div className="floating-shapes">
            <span className="shape shape-1">✨</span>
            <span className="shape shape-2">📚</span>
            <span className="shape shape-3">🎯</span>
          </div>
        </div>
      </div>

      <div className="stats-section">
        <div className="stats-header">
          <h2>📊 Your Dashboard</h2>
          <p>Track your learning journey</p>
        </div>
        
        <div className="stats-grid">
          <div className="stat-card stat-1">
            <div className="stat-glow"></div>
            <div className="stat-icon-wrapper">
              <span className="stat-icon">📝</span>
            </div>
            <div className="stat-number">{animatedStats.quizzes}</div>
            <div className="stat-label">Quizzes Taken</div>
            <div className="stat-decoration"></div>
          </div>
          
          <div className="stat-card stat-2">
            <div className="stat-glow"></div>
            <div className="stat-icon-wrapper">
              <span className="stat-icon">🎯</span>
            </div>
            <div className="stat-number">{animatedStats.score}%</div>
            <div className="stat-label">Average Score</div>
            <div className="stat-decoration"></div>
          </div>
          
          <div className="stat-card stat-3">
            <div className="stat-glow"></div>
            <div className="stat-icon-wrapper">
              <span className="stat-icon">📚</span>
            </div>
            <div className="stat-number">{animatedStats.progress}%</div>
            <div className="stat-label">Path Progress</div>
            <div className="stat-decoration"></div>
          </div>
          
          <div className="stat-card stat-4">
            <div className="stat-glow"></div>
            <div className="stat-icon-wrapper">
              <span className="stat-icon">⏱️</span>
            </div>
            <div className="stat-number">{animatedStats.hours}h</div>
            <div className="stat-label">Hours Logged</div>
            <div className="stat-decoration"></div>
          </div>
        </div>
      </div>

      <div className="quick-actions-section">
        <h2>⚡ Quick Actions</h2>
        <div className="actions-grid">
          {actions.map((action, i) => (
            <div 
              key={i} 
              className={`action-card action-${action.color}`}
              onClick={() => setStep(action.step)}
              style={{ animationDelay: `${i * 0.1}s` }}
            >
              <div className="action-icon">{action.icon}</div>
              <div className="action-content">
                <h3>{action.title}</h3>
                <p>{action.desc}</p>
              </div>
              <div className="action-arrow">→</div>
            </div>
          ))}
        </div>
      </div>

      <div className="main-content-grid">
        <div className="content-card progress-card">
          <div className="card-header">
            <h3>📈 Learning Progress</h3>
            <span className="card-badge">{completed}/{learningPath.length} complete</span>
          </div>
          
          {learningPath.length > 0 ? (
            <div className="progress-list">
              {learningPath.slice(0, 5).map((item, i) => (
                <div key={i} className="progress-item" style={{ animationDelay: `${i * 0.1}s` }}>
                  <div className="progress-icon">{item.icon}</div>
                  <div className="progress-info">
                    <div className="progress-title">{item.title}</div>
                    <div className="progress-bar-wrapper">
                      <div className="progress-bar">
                        <div 
                          className="progress-fill" 
                          style={{ width: `${item.progress}%` }}
                        ></div>
                      </div>
                      <span className="progress-percent">{item.progress}%</span>
                    </div>
                  </div>
                  <div className={`progress-status ${item.progress === 100 ? 'completed' : item.progress > 0 ? 'in-progress' : 'not-started'}`}>
                    {item.progress === 100 ? '✓' : item.progress > 0 ? '⟳' : '○'}
                  </div>
                </div>
              ))}
            </div>
          ) : (
            <div className="empty-state">
              <span className="empty-icon">🛤️</span>
              <p>Complete your assessment to see your personalized learning path!</p>
              <button className="btn" onClick={() => setStep(2)}>Start Assessment</button>
            </div>
          )}
          
          {learningPath.length > 5 && (
            <button className="btn btn-secondary btn-full" style={{ marginTop: '16px' }} onClick={() => setStep(4)}>
              View Full Path →
            </button>
          )}
        </div>

        <div className="content-card activity-card">
          <div className="card-header">
            <h3>📋 Recent Activity</h3>
            <button className="add-btn" onClick={() => setStep(9)}>+</button>
          </div>
          
          {dailyLogs.length > 0 ? (
            <div className="activity-list">
              {dailyLogs.slice(-5).reverse().map((log, i) => (
                <div key={i} className="activity-item" style={{ animationDelay: `${i * 0.1}s` }}>
                  <div className="activity-icon">📖</div>
                  <div className="activity-content">
                    <div className="activity-title">{log.topic}</div>
                    <div className="activity-meta">
                      <span>{log.date}</span>
                      <span className="separator">•</span>
                      <span>{log.hours} hours</span>
                    </div>
                  </div>
                </div>
              ))}
            </div>
          ) : (
            <div className="empty-state small">
              <span className="empty-icon">📊</span>
              <p>Start logging your learning activities!</p>
            </div>
          )}
          
          <button className="btn btn-gradient btn-full" style={{ marginTop: '16px' }} onClick={() => setStep(9)}>
            📝 Log Today's Learning
          </button>
        </div>
      </div>

      <div className="secondary-content-grid">
        <div className="content-card profile-card">
          <div className="card-header">
            <h3>👤 Your Profile</h3>
            <button className="edit-btn" onClick={() => setStep(1)}>✏️</button>
          </div>
          
          <div className="profile-grid">
            <div className="profile-item">
              <span className="profile-icon">🎯</span>
              <div className="profile-info">
                <span className="profile-label">Goal</span>
                <span className="profile-value">{userProfile.goal || 'Not set'}</span>
              </div>
            </div>
            
            <div className="profile-item">
              <span className="profile-icon">⏰</span>
              <div className="profile-info">
                <span className="profile-label">Daily Hours</span>
                <span className="profile-value">{userProfile.hours || 2}h</span>
              </div>
            </div>
            
            <div className="profile-item">
              <span className="profile-icon">📊</span>
              <div className="profile-info">
                <span className="profile-label">Tech Level</span>
                <span className="profile-value">{userProfile.tech || 5}/10</span>
              </div>
            </div>
            
            <div className="profile-item">
              <span className="profile-icon">🏆</span>
              <div className="profile-info">
                <span className="profile-label">Experience</span>
                <span className="profile-value">{userProfile.experience || 0} years</span>
              </div>
            </div>
          </div>
          
          {enrolledCourses.length > 0 && (
            <div className="enrolled-courses">
              <h4>📚 Enrolled Courses ({enrolledCourses.length})</h4>
              <div className="course-tags">
                {enrolledCourses.slice(0, 3).map((course, i) => (
                  <span key={i} className="course-tag">{course.split(' ')[0]}</span>
                ))}
                {enrolledCourses.length > 3 && (
                  <span className="course-tag more">+{enrolledCourses.length - 3}</span>
                )}
              </div>
            </div>
          )}
        </div>

        <div className="content-card quiz-score-card">
          <div className="card-header">
            <h3>🏅 Quiz Performance</h3>
          </div>
          
          {quizCount > 0 ? (
            <div className="quiz-scores">
              <div className="score-overview">
                <div className="score-circle">
                  <svg viewBox="0 0 100 100">
                    <circle cx="50" cy="50" r="45" className="score-bg" />
                    <circle 
                      cx="50" cy="50" r="45" 
                      className="score-progress"
                      style={{ 
                        strokeDasharray: `${(avgScore / 100) * 283} 283`,
                      }}
                    />
                  </svg>
                  <div className="score-value">
                    <span className="score-number">{avgScore}</span>
                    <span className="score-percent">%</span>
                  </div>
                </div>
                <p>Overall Performance</p>
              </div>
              
              <div className="score-topics">
                {Object.entries(quizBatchScores).slice(0, 4).map(([topic, data], i) => (
                  <div key={i} className="score-topic">
                    <span className="topic-name">{topic.replace(/_/g, ' ')}</span>
                    <div className="topic-bar">
                      <div className="topic-fill" style={{ width: `${data.score}%` }}></div>
                    </div>
                    <span className="topic-score">{data.score}%</span>
                  </div>
                ))}
              </div>
            </div>
          ) : (
            <div className="empty-state small">
              <span className="empty-icon">📝</span>
              <p>Take quizzes to see your performance here!</p>
              <button className="btn" onClick={() => setStep(3)}>Take Quiz</button>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

export default Dashboard;
