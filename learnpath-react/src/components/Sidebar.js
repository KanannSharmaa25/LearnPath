import React from 'react';
import { AppContext } from '../App';
import './Sidebar.css';

function Sidebar() {
  const { step, setStep, userProfile, learningPath, quizBatchScores } = React.useContext(AppContext);
  
  const navItems = [
    { icon: "🏠", label: "Dashboard", num: 6, desc: "Overview & stats" },
    { icon: "👤", label: "Profile", num: 1, desc: "Your info" },
    { icon: "📝", label: "Assessment", num: 2, desc: "Psychology quiz" },
    { icon: "📋", label: "Quizzes", num: 3, desc: "Knowledge tests" },
    { icon: "🛤️", label: "Learning Path", num: 4, desc: "Your roadmap" },
    { icon: "📚", label: "Courses", num: 5, desc: "Recommendations" },
    { icon: "🤖", label: "AI Coach", num: 7, desc: "Get guidance" },
    { icon: "🔮", label: "Predictions", num: 8, desc: "Timeline & career" },
    { icon: "📊", label: "Progress", num: 9, desc: "Track journey" },
  ];

  const completedCount = learningPath.filter(p => p.progress === 100).length;
  const quizCount = Object.keys(quizBatchScores).length;

  return (
    <aside className="sidebar">
      <div className="sidebar-header">
        <div className="logo">
          <span className="logo-icon">🎓</span>
          <div className="logo-text">
            <span className="logo-title">LearnPath</span>
            <span className="logo-subtitle">AI Learning</span>
          </div>
        </div>
      </div>

      <div className="sidebar-stats">
        <div className="stat-item">
          <span className="stat-number">{quizCount}</span>
          <span className="stat-label">Quizzes</span>
        </div>
        <div className="stat-divider"></div>
        <div className="stat-item">
          <span className="stat-number">{completedCount}</span>
          <span className="stat-label">Completed</span>
        </div>
        <div className="stat-divider"></div>
        <div className="stat-item">
          <span className="stat-number">{learningPath.length}</span>
          <span className="stat-label">Topics</span>
        </div>
      </div>

      <div className="sidebar-section-title">Menu</div>
      
      <nav className="sidebar-nav">
        {navItems.map((item) => (
          <button
            key={item.num}
            className={`nav-btn ${step === item.num ? 'active' : ''}`}
            onClick={() => setStep(item.num)}
          >
            <span className="nav-icon">{item.icon}</span>
            <div className="nav-content">
              <span className="nav-label">{item.label}</span>
              <span className="nav-desc">{item.desc}</span>
            </div>
            {step === item.num && <span className="active-indicator"></span>}
          </button>
        ))}
      </nav>

      <div className="sidebar-footer">
        <div className="user-card">
          <div className="user-avatar">
            {userProfile.name ? userProfile.name.charAt(0).toUpperCase() : '👤'}
          </div>
          <div className="user-info">
            <span className="user-name">{userProfile.name || 'Guest'}</span>
            <span className="user-goal">{userProfile.goal || 'Set your goal'}</span>
          </div>
        </div>
      </div>
    </aside>
  );
}

export default Sidebar;
