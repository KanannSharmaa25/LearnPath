import React, { useState, useEffect, useRef } from 'react';
import { AppContext } from '../App';
import './Landing.css';

function Landing() {
  const { setStep } = React.useContext(AppContext);
  const [isLoaded, setIsLoaded] = useState(false);
  const [counters, setCounters] = useState({ learners: 0, questions: 0, success: 0 });
  const featuresRef = useRef(null);
  const stepsRef = useRef(null);

  useEffect(() => {
    setIsLoaded(true);
    animateCounters();
  }, []);

  const animateCounters = () => {
    const duration = 2000;
    const steps = 60;
    const interval = duration / steps;
    let step = 0;
    
    const timer = setInterval(() => {
      step++;
      const progress = step / steps;
      setCounters({
        learners: Math.round(50000 * progress),
        questions: Math.round(200 * progress),
        success: Math.round(95 * progress),
      });
      if (step >= steps) clearInterval(timer);
    }, interval);
  };

  const handleStartJourney = () => {
    setStep(1);
  };

  const features = [
    { icon: "🧠", title: "Psychology Assessment", desc: "Understand how you learn best", color: "purple" },
    { icon: "📝", title: "Knowledge Quizzes", desc: "Test skills across 20+ topics", color: "blue" },
    { icon: "🛤️", title: "AI Learning Path", desc: "Personalized roadmap for you", color: "green" },
    { icon: "📚", title: "Curated Courses", desc: "Best resources matched to you", color: "orange" },
    { icon: "💬", title: "AI Coach", desc: "24/7 guidance and support", color: "pink" },
    { icon: "🔮", title: "Smart Predictions", desc: "AI-powered timeline estimates", color: "cyan" },
  ];

  const stats = [
    { icon: "👥", value: counters.learners, suffix: "+", label: "Active Learners" },
    { icon: "📚", value: counters.questions, suffix: "+", label: "Quiz Questions" },
    { icon: "🎯", value: counters.success, suffix: "%", label: "Success Rate" },
  ];

  const steps = [
    { num: "1", icon: "👤", title: "Create Profile", desc: "Tell us about yourself" },
    { num: "2", icon: "🧠", title: "Take Assessment", desc: "Psychology-based analysis" },
    { num: "3", icon: "📝", title: "Take Quizzes", desc: "Test your knowledge" },
    { num: "4", icon: "🛤️", title: "Get Your Path", desc: "AI creates your roadmap" },
    { num: "5", icon: "🚀", title: "Start Learning", desc: "Follow your path" },
  ];

  return (
    <div className={`landing ${isLoaded ? 'loaded' : ''}`}>
      <div className="landing-bg">
        <div className="bg-gradient"></div>
        <div className="bg-shapes">
          <div className="shape shape-1"></div>
          <div className="shape shape-2"></div>
          <div className="shape shape-3"></div>
        </div>
        <div className="particles">
          {[...Array(30)].map((_, i) => (
            <div key={i} className="particle" style={{
              left: `${Math.random() * 100}%`,
              top: `${Math.random() * 100}%`,
              animationDelay: `${Math.random() * 8}s`,
              animationDuration: `${8 + Math.random() * 6}s`,
              fontSize: `${12 + Math.random() * 16}px`,
            }}>
              {['✨', '⭐', '📚', '💡', '🎯'][Math.floor(Math.random() * 5)]}
            </div>
          ))}
        </div>
      </div>

      <div className="landing-content">
        <section className="hero">
          <div className="hero-badge animate-badge">
            <span className="badge-dot"></span>
            <span>AI-Powered Learning Platform</span>
          </div>
          
          <h1 className="hero-title">
            <span className="title-accent animate-title-1">Learn</span>
            <span className="animate-title-2">Path</span>
          </h1>
          
          <p className="hero-subtitle animate-subtitle">
            Discover your unique learning style through psychology-driven assessments.
            Get a personalized roadmap designed just for your brain.
          </p>
          
          <div className="hero-tags animate-tags">
            <span className="tag animate-tag-1">🧠 Psychology-Based</span>
            <span className="tag animate-tag-2">✨ AI-Powered</span>
            <span className="tag animate-tag-3">📊 Data-Driven</span>
          </div>
          
          <button className="btn-primary animate-btn" onClick={handleStartJourney}>
            <span className="btn-text">Start Your Journey</span>
            <span className="btn-icon">→</span>
            <span className="btn-glow"></span>
          </button>
          
          <p className="hero-note animate-note">Free forever • No credit card • Instant access</p>
        </section>

        <section className="stats-section animate-stats">
          {stats.map((s, i) => (
            <div key={i} className="stat-card" style={{ animationDelay: `${i * 0.15}s` }}>
              <div className="stat-glow"></div>
              <span className="stat-icon">{s.icon}</span>
              <div className="stat-value">
                {s.value.toLocaleString()}{s.suffix}
              </div>
              <div className="stat-label">{s.label}</div>
            </div>
          ))}
        </section>

        <section className="features" ref={featuresRef}>
          <h2 className="section-title animate-section-title">
            <span className="title-decoration">✨</span>
            Everything You Need to Succeed
          </h2>
          <div className="features-grid">
            {features.map((f, i) => (
              <div key={i} className="feature-card" style={{ animationDelay: `${i * 0.1}s` }}>
                <div className="feature-shimmer"></div>
                <div className="feature-icon-wrapper">
                  <span className="feature-icon">{f.icon}</span>
                  <div className="feature-icon-glow"></div>
                </div>
                <h3>{f.title}</h3>
                <p>{f.desc}</p>
                <div className="feature-border"></div>
              </div>
            ))}
          </div>
        </section>

        <section className="how-it-works" ref={stepsRef}>
          <h2 className="section-title animate-section-title">
            <span className="title-decoration">🚀</span>
            How It Works
          </h2>
          <div className="steps-container">
            <div className="steps-line"></div>
            <div className="steps-row">
              {steps.map((s, i) => (
                <div key={i} className="step-card" style={{ animationDelay: `${i * 0.15}s` }}>
                  <div className="step-connector"></div>
                  <div className="step-num">{s.num}</div>
                  <div className="step-icon-wrapper">
                    <span className="step-icon">{s.icon}</span>
                  </div>
                  <h4>{s.title}</h4>
                  <p>{s.desc}</p>
                  <div className="step-glow"></div>
                </div>
              ))}
            </div>
          </div>
        </section>

        <section className="cta">
          <div className="cta-box">
            <div className="cta-decoration">
              <span className="deco">✨</span>
              <span className="deco">🎓</span>
              <span className="deco">🚀</span>
            </div>
            <h2 className="animate-cta-title">Ready to Transform Your Learning?</h2>
            <p className="animate-cta-text">Join thousands of learners on their journey to success</p>
            <button className="btn-primary btn-large animate-cta-btn" onClick={handleStartJourney}>
              <span className="btn-text">Get Started Free</span>
              <span className="btn-icon">🚀</span>
              <span className="btn-glow"></span>
            </button>
          </div>
        </section>
      </div>
    </div>
  );
}

export default Landing;
