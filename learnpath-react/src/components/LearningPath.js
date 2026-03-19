import React, { useState } from 'react';
import { AppContext } from '../App';
import './LearningPath.css';

function LearningPath() {
  const { setStep, userProfile, quizBatchScores, learningPath, setLearningPath, aiLearningPath, setAiLearningPath, userLearningPath, setUserLearningPath, setSelectedPathType } = React.useContext(AppContext);
  const [activeTab, setActiveTab] = useState('analysis');
  const [userDescription, setUserDescription] = useState('');
  const [preferredTopics, setPreferredTopics] = useState([]);
  const [selectedFinalPath, setSelectedFinalPath] = useState(null);
  
  // New custom path options
  const [learningPace, setLearningPace] = useState('moderate');
  const [learningStyle, setLearningStyle] = useState('hands-on');
  const [timeline, setTimeline] = useState('3-6-months');
  const [certificationGoals, setCertificationGoals] = useState([]);
  const [projectIdeas, setProjectIdeas] = useState('');
  const [priorityOrder, setPriorityOrder] = useState([]);
  const [specificSkills, setSpecificSkills] = useState('');

  const weakAreas = [];
  const strongAreas = [];
  
  Object.entries(quizBatchScores).forEach(([topic, data]) => {
    if (data.score < 70) {
      weakAreas.push({ name: topic.replace(/_/g, ' ').replace(/\b\w/g, l => l.toUpperCase()), score: data.score });
    } else {
      strongAreas.push({ name: topic.replace(/_/g, ' ').replace(/\b\w/g, l => l.toUpperCase()), score: data.score });
    }
  });

  const generateAiPath = () => {
    const path = [];
    const goal = userProfile.goal || '';
    const experience = userProfile.experience || 0;

    if (experience < 1) {
      path.push({ title: "Programming Basics", duration: "3 weeks", icon: "💻", level: "Beginner", reason: "Build strong foundation" });
    }

    if (goal.toLowerCase().includes('web') || goal.toLowerCase().includes('project')) {
      path.push({ title: "HTML & CSS Fundamentals", duration: "2 weeks", icon: "🎨", level: "Beginner", reason: "Web development foundation" });
      path.push({ title: "JavaScript Essentials", duration: "4 weeks", icon: "⚡", level: "Beginner", reason: "Interactive web development" });
      path.push({ title: "React Framework", duration: "5 weeks", icon: "⚛️", level: "Intermediate", reason: "Modern frontend development" });
      path.push({ title: "Backend Development", duration: "4 weeks", icon: "🔗", level: "Intermediate", reason: "Full-stack capability" });
    } else if (goal.toLowerCase().includes('data') || goal.toLowerCase().includes('ai') || goal.toLowerCase().includes('ml')) {
      path.push({ title: "Python Programming", duration: "4 weeks", icon: "🐍", level: "Beginner", reason: "Primary language for data/ML" });
      path.push({ title: "Statistics & Mathematics", duration: "4 weeks", icon: "📊", level: "Intermediate", reason: "Essential for data science" });
      path.push({ title: "Machine Learning Fundamentals", duration: "6 weeks", icon: "🤖", level: "Intermediate", reason: "Core ML concepts" });
      path.push({ title: "Deep Learning", duration: "6 weeks", icon: "🧠", level: "Advanced", reason: "Advanced AI techniques" });
    } else if (goal.toLowerCase().includes('cloud') || goal.toLowerCase().includes('devops')) {
      path.push({ title: "Linux Fundamentals", duration: "3 weeks", icon: "🐧", level: "Beginner", reason: "Server management basics" });
      path.push({ title: "Docker & Containers", duration: "3 weeks", icon: "📦", level: "Intermediate", reason: "Modern deployment" });
      path.push({ title: "Kubernetes", duration: "4 weeks", icon: "☸️", level: "Intermediate", reason: "Container orchestration" });
      path.push({ title: "CI/CD Pipelines", duration: "3 weeks", icon: "🔄", level: "Intermediate", reason: "Automation skills" });
    } else {
      path.push({ title: "Python Fundamentals", duration: "4 weeks", icon: "🐍", level: "Beginner", reason: "Versatile programming" });
      path.push({ title: "Data Structures", duration: "4 weeks", icon: "🏗️", level: "Intermediate", reason: "Problem-solving skills" });
      path.push({ title: "Web Development", duration: "6 weeks", icon: "🌐", level: "Intermediate", reason: "Practical applications" });
    }

    weakAreas.forEach(area => {
      path.unshift({ title: `${area.name} Refresher`, duration: "2 weeks", icon: "📚", level: "Beginner", reason: `Boost score (currently ${area.score}%)` });
    });

    setAiLearningPath(path.map(p => ({ ...p, progress: 0, status: 'Not Started' })));
    setActiveTab('ai');
  };

  const generateUserPath = () => {
    const path = [];
    
    // Calculate duration multiplier based on pace
    const paceMultiplier = learningPace === 'intensive' ? 0.7 : learningPace === 'relaxed' ? 1.5 : 1;
    
    const topicMap = {
      "Web Development": { 
        title: "Web Development", 
        icon: "🌐", 
        level: "Beginner", 
        duration: `${Math.round(6 * paceMultiplier)} weeks`,
        reason: "Full-stack web development" 
      },
      "Mobile Development": { 
        title: "Mobile App Development", 
        icon: "📱", 
        level: "Intermediate", 
        duration: `${Math.round(5 * paceMultiplier)} weeks`,
        reason: "iOS and Android development" 
      },
      "Data Science": { 
        title: "Data Science", 
        icon: "📊", 
        level: "Intermediate", 
        duration: `${Math.round(8 * paceMultiplier)} weeks`,
        reason: "Data analysis and visualization" 
      },
      "Machine Learning": { 
        title: "Machine Learning", 
        icon: "🤖", 
        level: "Advanced", 
        duration: `${Math.round(10 * paceMultiplier)} weeks`,
        reason: "ML algorithms and models" 
      },
      "Cloud/DevOps": { 
        title: "Cloud & DevOps", 
        icon: "☁️", 
        level: "Intermediate", 
        duration: `${Math.round(6 * paceMultiplier)} weeks`,
        reason: "Cloud infrastructure and deployment" 
      },
      "Backend Development": { 
        title: "Backend Development", 
        icon: "🔗", 
        level: "Intermediate", 
        duration: `${Math.round(5 * paceMultiplier)} weeks`,
        reason: "Server-side programming and APIs" 
      },
      "Frontend Development": { 
        title: "Frontend Development", 
        icon: "🎨", 
        level: "Beginner", 
        duration: `${Math.round(4 * paceMultiplier)} weeks`,
        reason: "User interface and UX" 
      },
      "UI/UX Design": { 
        title: "UI/UX Design", 
        icon: "✨", 
        level: "Intermediate", 
        duration: `${Math.round(4 * paceMultiplier)} weeks`,
        reason: "Design thinking and prototyping" 
      },
      "Cybersecurity": { 
        title: "Cybersecurity", 
        icon: "🔒", 
        level: "Advanced", 
        duration: `${Math.round(8 * paceMultiplier)} weeks`,
        reason: "Security fundamentals and testing" 
      },
      "Blockchain": { 
        title: "Blockchain Development", 
        icon: "⛓️", 
        level: "Intermediate", 
        duration: `${Math.round(6 * paceMultiplier)} weeks`,
        reason: "Smart contracts and Web3" 
      },
    };

    // Sort by priority order if set
    let sortedTopics = [...preferredTopics];
    if (priorityOrder.length > 0) {
      sortedTopics = priorityOrder.filter(t => preferredTopics.includes(t));
      preferredTopics.filter(t => !priorityOrder.includes(t)).forEach(t => sortedTopics.push(t));
    }

    sortedTopics.forEach(topic => {
      if (topicMap[topic]) {
        const item = { ...topicMap[topic], reason: "Based on your preferences" };
        
        // Add project idea context
        if (projectIdeas) {
          item.project = projectIdeas;
        }
        
        path.push(item);
      }
    });

    // Add fundamentals if experience is low
    if (path.length > 0 && (userProfile.experience || 0) < 1) {
      path.unshift({ 
        title: "Programming Fundamentals", 
        icon: "💻", 
        level: "Beginner", 
        duration: `${Math.round(3 * paceMultiplier)} weeks`,
        reason: "Essential foundation before specialized topics"
      });
    }

    // Add certification prep if selected
    if (certificationGoals.length > 0) {
      certificationGoals.forEach(cert => {
        path.push({
          title: `${cert} Certification Prep`,
          icon: "🏆",
          level: "Intermediate",
          duration: `${Math.round(4 * paceMultiplier)} weeks`,
          reason: `Prepare for ${cert} certification exam`
        });
      });
    }

    if (path.length === 0) {
      path.push({ 
        title: "Python Fundamentals", 
        icon: "🐍", 
        level: "Beginner", 
        duration: `${Math.round(4 * paceMultiplier)} weeks`,
        reason: "Build your foundation"
      });
    }

    setUserLearningPath(path.map(p => ({ ...p, progress: 0, status: 'Not Started' })));
    setActiveTab('user');
  };

  const useAiPath = () => {
    setLearningPath(aiLearningPath);
    setSelectedPathType('ai');
    setSelectedFinalPath('ai');
  };

  const useUserPath = () => {
    setLearningPath(userLearningPath);
    setSelectedPathType('user');
    setSelectedFinalPath('user');
  };

  const combinePaths = () => {
    const combined = [...aiLearningPath.slice(0, 3), ...userLearningPath.slice(0, 3)];
    const unique = combined.filter((item, index, self) => 
      index === self.findIndex(t => t.title === item.title)
    );
    setLearningPath(unique);
    setSelectedPathType('combined');
    setSelectedFinalPath('combined');
  };

  const allTopics = [
    "Web Development", "Mobile Development", "Data Science", "Machine Learning", 
    "Cloud/DevOps", "Backend Development", "Frontend Development", "UI/UX Design",
    "Cybersecurity", "Blockchain"
  ];

  const certifications = [
    "AWS Certified", "Google Cloud", "Microsoft Azure", 
    "CompTIA Security+", "Certified Kubernetes", "Scrum Master",
    "Python Institute", "Meta Frontend", "TensorFlow Developer"
  ];

  const toggleTopic = (topic) => {
    if (preferredTopics.includes(topic)) {
      setPreferredTopics(preferredTopics.filter(t => t !== topic));
      setPriorityOrder(priorityOrder.filter(t => t !== topic));
    } else {
      setPreferredTopics([...preferredTopics, topic]);
      setPriorityOrder([...priorityOrder, topic]);
    }
  };

  const toggleCert = (cert) => {
    if (certificationGoals.includes(cert)) {
      setCertificationGoals(certificationGoals.filter(c => c !== cert));
    } else {
      setCertificationGoals([...certificationGoals, cert]);
    }
  };

  const timelineOptions = {
    '1-month': { label: '1 Month', desc: 'Crash course intensive' },
    '3-months': { label: '3 Months', desc: 'Focused learning' },
    '3-6-months': { label: '3-6 Months', desc: 'Standard pace' },
    '6-12-months': { label: '6-12 Months', desc: 'Comprehensive' },
    '12-plus': { label: '12+ Months', desc: 'Deep dive & mastery' },
  };

  const paceOptions = {
    'intensive': { label: '🚀 Intensive', desc: '8+ hours daily' },
    'moderate': { label: '⚖️ Moderate', desc: '4-6 hours daily' },
    'relaxed': { label: '🐢 Relaxed', desc: '1-3 hours daily' },
    'weekend': { label: '📅 Weekend Only', desc: 'Weekend focus' },
  };

  const styleOptions = {
    'hands-on': { label: '🛠️ Hands-on Projects', desc: 'Learn by building' },
    'theory': { label: '📖 Theory First', desc: 'Concepts then practice' },
    'mix': { label: '⚡ Mix of Both', desc: 'Balanced approach' },
    'video': { label: '🎥 Video Tutorials', desc: 'Visual learning' },
  };

  return (
    <div className="learning-path-page">
      <h2>🛤️ Create Your Learning Path</h2>
      <p style={{ marginBottom: '32px' }}>Compare AI-generated path with your custom path or create your own personalized journey.</p>

      <div className="tabs">
        <button className={`tab ${activeTab === 'analysis' ? 'active' : ''}`} onClick={() => setActiveTab('analysis')}>
          📊 Analysis
        </button>
        <button className={`tab ${activeTab === 'ai' ? 'active' : ''}`} onClick={() => setActiveTab('ai')}>
          🤖 AI Path
        </button>
        <button className={`tab ${activeTab === 'user' ? 'active' : ''}`} onClick={() => setActiveTab('user')}>
          ✏️ Custom Path
        </button>
        <button className={`tab ${activeTab === 'compare' ? 'active' : ''}`} onClick={() => setActiveTab('compare')}>
          ⚖️ Compare
        </button>
      </div>

      {activeTab === 'analysis' && (
        <div>
          <div className="grid-2">
            <div className="card">
              <h3>💪 Strong Areas</h3>
              {strongAreas.length > 0 ? (
                strongAreas.map((area, i) => (
                  <div key={i} className="strength-item">
                    <span className="strength-name">{area.name}</span>
                    <span className="strength-score success">{area.score}%</span>
                  </div>
                ))
              ) : (
                <p className="alert alert-info">Complete quizzes to see strong areas!</p>
              )}
            </div>
            <div className="card">
              <h3>📈 Areas to Improve</h3>
              {weakAreas.length > 0 ? (
                weakAreas.map((area, i) => (
                  <div key={i} className="strength-item">
                    <span className="strength-name">{area.name}</span>
                    <span className="strength-score warning">{area.score}%</span>
                  </div>
                ))
              ) : (
                <p className="alert alert-success">Great job! No weak areas detected.</p>
              )}
            </div>
          </div>

          <div className="card" style={{ marginTop: '24px' }}>
            <h3>📋 Quick Profile Insights</h3>
            <div className="insights-grid">
              <div className="insight-item">
                <span className="insight-icon">🎯</span>
                <div>
                  <span className="insight-label">Goal</span>
                  <span className="insight-value">{userProfile.goal || 'Not set'}</span>
                </div>
              </div>
              <div className="insight-item">
                <span className="insight-icon">⏰</span>
                <div>
                  <span className="insight-label">Daily Hours</span>
                  <span className="insight-value">{userProfile.hours || 2}h</span>
                </div>
              </div>
              <div className="insight-item">
                <span className="insight-icon">🏆</span>
                <div>
                  <span className="insight-label">Experience</span>
                  <span className="insight-value">{userProfile.experience || 0} years</span>
                </div>
              </div>
              <div className="insight-item">
                <span className="insight-icon">📊</span>
                <div>
                  <span className="insight-label">Tech Level</span>
                  <span className="insight-value">{userProfile.tech || 5}/10</span>
                </div>
              </div>
            </div>
          </div>

          <button className="btn btn-full" style={{ marginTop: '24px' }} onClick={generateAiPath}>
            🤖 Generate AI Learning Path
          </button>
        </div>
      )}

      {activeTab === 'ai' && (
        <div>
          {aiLearningPath.length === 0 ? (
            <p className="alert alert-info">Generate your AI path from the Analysis tab first!</p>
          ) : (
            <>
              <p style={{ marginBottom: '16px', color: '#6b7280' }}>Based on your assessment scores and profile, here are AI's recommendations:</p>
              {aiLearningPath.map((item, i) => (
                <div key={i} className="path-card">
                  <div className="path-card-header">
                    <span className="path-number">{i + 1}</span>
                    <span className="path-icon">{item.icon}</span>
                    <div className="path-info">
                      <h4>{item.title}</h4>
                      <div className="path-meta">
                        <span className="path-level">{item.level}</span>
                        <span className="path-duration">{item.duration}</span>
                      </div>
                    </div>
                  </div>
                  <p className="path-reason">💡 {item.reason}</p>
                </div>
              ))}
              <button className="btn btn-full" style={{ marginTop: '24px' }} onClick={useAiPath}>
                ✅ Use This AI Path
              </button>
            </>
          )}
        </div>
      )}

      {activeTab === 'user' && (
        <div>
          <div className="custom-path-builder">
            
            <div className="card">
              <h3>🎯 Describe Your Goals</h3>
              <div className="input-field">
                <label>What do you want to achieve?</label>
                <textarea 
                  value={userDescription}
                  onChange={(e) => setUserDescription(e.target.value)}
                  placeholder="I want to become a full-stack developer focusing on Python for backend and React for frontend, eventually getting an AWS certification..."
                />
              </div>
            </div>

            <div className="card" style={{ marginTop: '24px' }}>
              <h3>⏱️ Timeline & Pace</h3>
              <div className="option-cards">
                {Object.entries(timelineOptions).map(([key, opt]) => (
                  <div 
                    key={key}
                    className={`option-card ${timeline === key ? 'selected' : ''}`}
                    onClick={() => setTimeline(key)}
                  >
                    <span className="option-label">{opt.label}</span>
                    <span className="option-desc">{opt.desc}</span>
                  </div>
                ))}
              </div>
              
              <div className="option-cards" style={{ marginTop: '16px' }}>
                {Object.entries(paceOptions).map(([key, opt]) => (
                  <div 
                    key={key}
                    className={`option-card ${learningPace === key ? 'selected' : ''}`}
                    onClick={() => setLearningPace(key)}
                  >
                    <span className="option-label">{opt.label}</span>
                    <span className="option-desc">{opt.desc}</span>
                  </div>
                ))}
              </div>
            </div>

            <div className="card" style={{ marginTop: '24px' }}>
              <h3>📚 Topics You Want to Learn</h3>
              <p style={{ color: '#6b7280', marginBottom: '16px' }}>Select topics and drag to prioritize order:</p>
              <div className="topics-grid">
                {allTopics.map(topic => (
                  <div 
                    key={topic}
                    className={`topic-chip ${preferredTopics.includes(topic) ? 'selected' : ''}`}
                    onClick={() => toggleTopic(topic)}
                  >
                    {preferredTopics.includes(topic) && (
                      <span className="topic-priority">{preferredTopics.indexOf(topic) + 1}</span>
                    )}
                    {topic}
                  </div>
                ))}
              </div>
            </div>

            <div className="card" style={{ marginTop: '24px' }}>
              <h3>🛠️ Learning Style</h3>
              <div className="option-cards">
                {Object.entries(styleOptions).map(([key, opt]) => (
                  <div 
                    key={key}
                    className={`option-card ${learningStyle === key ? 'selected' : ''}`}
                    onClick={() => setLearningStyle(key)}
                  >
                    <span className="option-label">{opt.label}</span>
                    <span className="option-desc">{opt.desc}</span>
                  </div>
                ))}
              </div>
              
              <div className="input-field" style={{ marginTop: '16px' }}>
                <label>Any specific skills you want to master?</label>
                <input 
                  type="text"
                  value={specificSkills}
                  onChange={(e) => setSpecificSkills(e.target.value)}
                  placeholder="e.g., TypeScript, Docker, TensorFlow, Figma..."
                />
              </div>
            </div>

            <div className="card" style={{ marginTop: '24px' }}>
              <h3>🏆 Certification Goals</h3>
              <p style={{ color: '#6b7280', marginBottom: '16px' }}>Select certifications you want to achieve:</p>
              <div className="topics-grid">
                {certifications.map(cert => (
                  <div 
                    key={cert}
                    className={`topic-chip ${certificationGoals.includes(cert) ? 'selected' : ''}`}
                    onClick={() => toggleCert(cert)}
                  >
                    {cert}
                  </div>
                ))}
              </div>
            </div>

            <div className="card" style={{ marginTop: '24px' }}>
              <h3>💡 Project Ideas</h3>
              <div className="input-field">
                <label>What projects do you want to build?</label>
                <textarea 
                  value={projectIdeas}
                  onChange={(e) => setProjectIdeas(e.target.value)}
                  placeholder="e.g., E-commerce website, Todo app with React, Machine learning model for price prediction..."
                />
              </div>
            </div>

            <button className="btn btn-full btn-gradient" style={{ marginTop: '24px' }} onClick={generateUserPath}>
              ✨ Generate My Custom Path
            </button>
          </div>

          {userLearningPath.length > 0 && (
            <div style={{ marginTop: '32px' }}>
              <h3>Your Custom Path Preview</h3>
              {userLearningPath.map((item, i) => (
                <div key={i} className="path-card">
                  <div className="path-card-header">
                    <span className="path-number">{i + 1}</span>
                    <span className="path-icon">{item.icon}</span>
                    <div className="path-info">
                      <h4>{item.title}</h4>
                      <div className="path-meta">
                        <span className="path-level">{item.level}</span>
                        <span className="path-duration">{item.duration}</span>
                      </div>
                    </div>
                  </div>
                  <p className="path-reason">💡 {item.reason}</p>
                </div>
              ))}
              <button className="btn btn-full" style={{ marginTop: '24px' }} onClick={useUserPath}>
                ✅ Use This Custom Path
              </button>
            </div>
          )}
        </div>
      )}

      {activeTab === 'compare' && (
        <div>
          <div className="comparison-grid">
            <div className="card comparison-card ai">
              <div className="comparison-header">
                <span className="comparison-icon">🤖</span>
                <h3>AI-Generated Path</h3>
              </div>
              {aiLearningPath.length > 0 ? (
                <>
                  <div className="comparison-stats">
                    <span><strong>{aiLearningPath.length}</strong> Topics</span>
                    <span><strong>{aiLearningPath.reduce((acc, p) => acc + parseInt(p.duration), 0)}</strong> Weeks</span>
                  </div>
                  <div className="comparison-pros-cons">
                    <div className="pros">
                      <h4>✅ Pros</h4>
                      <ul>
                        <li>Based on quiz results</li>
                        <li>Addresses weak areas</li>
                        <li>Optimized for your goals</li>
                        <li>Evidence-based</li>
                      </ul>
                    </div>
                    <div className="cons">
                      <h4>⚠️ Cons</h4>
                      <ul>
                        <li>Generic approach</li>
                        <li>May not match preferences</li>
                      </ul>
                    </div>
                  </div>
                </>
              ) : (
                <p className="alert alert-info">AI path not generated yet</p>
              )}
            </div>

            <div className="card comparison-card user">
              <div className="comparison-header">
                <span className="comparison-icon">✏️</span>
                <h3>Your Custom Path</h3>
              </div>
              {userLearningPath.length > 0 ? (
                <>
                  <div className="comparison-stats">
                    <span><strong>{userLearningPath.length}</strong> Topics</span>
                    <span><strong>{userLearningPath.reduce((acc, p) => acc + parseInt(p.duration), 0)}</strong> Weeks</span>
                  </div>
                  <div className="comparison-pros-cons">
                    <div className="pros">
                      <h4>✅ Pros</h4>
                      <ul>
                        <li>Matches your preferences</li>
                        <li>You chose the focus areas</li>
                        <li>Personalized approach</li>
                      </ul>
                    </div>
                    <div className="cons">
                      <h4>⚠️ Cons</h4>
                      <ul>
                        <li>May have knowledge gaps</li>
                        <li>Not optimized for weaknesses</li>
                      </ul>
                    </div>
                  </div>
                </>
              ) : (
                <p className="alert alert-info">Custom path not created yet</p>
              )}
            </div>
          </div>

          <div className="card recommendation-card" style={{ marginTop: '24px' }}>
            <h3>💡 AI Recommendations</h3>
            <div className="recommendations">
              {selectedFinalPath === 'ai' && <div className="selected-badge ai-selected">✅ AI path selected as your final learning journey!</div>}
              {selectedFinalPath === 'user' && <div className="selected-badge user-selected">✅ Custom path selected as your final learning journey!</div>}
              {selectedFinalPath === 'combined' && <div className="selected-badge combined-selected">✅ Combined path selected - best of both worlds!</div>}
              {!selectedFinalPath && (
                <>
                  <p>Based on your profile:</p>
                  {weakAreas.length > 2 && <p>⚠️ You have {weakAreas.length} areas to improve. Consider combining paths to address both strengths and weaknesses.</p>}
                  {userProfile.hours < 2 && <p>⏱️ With limited time, focus on fewer topics with deeper learning rather than broad coverage.</p>}
                  {certificationGoals.length > 0 && <p>🏆 Your certification goals add {certificationGoals.length * 4} weeks to your path.</p>}
                </>
              )}
            </div>
          </div>

          <div className="selection-buttons" style={{ marginTop: '24px' }}>
            <button className="btn btn-ai" onClick={useAiPath} disabled={aiLearningPath.length === 0}>
              🤖 Use AI Path
            </button>
            <button className="btn btn-user" onClick={useUserPath} disabled={userLearningPath.length === 0}>
              ✏️ Use Custom Path
            </button>
            <button className="btn btn-combine" onClick={combinePaths} disabled={aiLearningPath.length === 0 || userLearningPath.length === 0}>
              🔄 Combine Both
            </button>
          </div>
        </div>
      )}

      {learningPath.length > 0 && (
        <div style={{ marginTop: '32px' }}>
          <h3>📚 Your Selected Learning Path</h3>
          {learningPath.map((item, i) => (
            <div key={i} className="path-card selected">
              <div className="path-card-header">
                <span className="path-number">{i + 1}</span>
                <span className="path-icon">{item.icon}</span>
                <div className="path-info">
                  <h4>{item.title}</h4>
                  <div className="path-meta">
                    <span className="path-level">{item.level}</span>
                    <span className="path-duration">{item.duration}</span>
                  </div>
                </div>
              </div>
              <p className="path-reason">💡 {item.reason}</p>
            </div>
          ))}
        </div>
      )}

      <div className="divider" style={{ marginTop: '32px' }}></div>
      <div className="flex gap-2">
        <button className="btn btn-secondary" onClick={() => setStep(5)}>📚 Browse Courses</button>
        <button className="btn" onClick={() => setStep(6)}>🏠 Back to Dashboard</button>
      </div>
    </div>
  );
}

export default LearningPath;
