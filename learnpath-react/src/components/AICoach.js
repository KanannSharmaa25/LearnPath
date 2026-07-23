import React, { useState, useRef, useEffect } from 'react';
import { AppContext } from '../App';
import './AICoach.css';
import generateCoachResponse from '../utils/generateCoachResponse';
import ChatMessages from './ChatMessages';

function AICoach() {
  const { userProfile, chatHistory, setChatHistory, learningPath, quizBatchScores, enrolledCourses } = React.useContext(AppContext);
  const [input, setInput] = useState('');
  const [isTyping, setIsTyping] = useState(false);
  const chatEndRef = useRef(null);
  const goal = userProfile.goal || '';
  const hours = userProfile.hours || 2;
  const experience = userProfile.experience || 0;

  const getContext = () => {
    const pathTopic = learningPath.length > 0 ? learningPath[0]?.title : null;
    const quizScores = Object.entries(quizBatchScores);
    const weakAreas = quizScores.filter(([_, data]) => data.score < 70).map(([topic]) => topic);
    const strongAreas = quizScores.filter(([_, data]) => data.score >= 70).map(([topic]) => topic);
    
    return {
      pathTopic,
      quizScores,
      weakAreas,
      strongAreas,
      enrolledCount: enrolledCourses.length,
      learningPathLength: learningPath.length
    };
  };

  getContext();

  const suggested = [
    { icon: '📅', text: 'How should I structure my daily study schedule?', category: 'planning' },
    { icon: '💪', text: 'I\'m feeling overwhelmed, what should I do?', category: 'motivation' },
    { icon: '🎯', text: 'What\'s the fastest way to reach my goal?', category: 'strategy' },
    { icon: '📝', text: 'How do I practice what I learn effectively?', category: 'methods' },
    { icon: '🔍', text: 'How do I know if I\'m improving?', category: 'progress' },
    { icon: '💻', text: 'What projects should I build?', category: 'projects' },
    { icon: '⏸️', text: 'Should I take breaks while studying?', category: 'wellness' },
    { icon: '🎓', text: 'How do I prepare for technical interviews?', category: 'career' },
  ];

  const generateResponse = (question) =>
    generateCoachResponse(question, {
      ctx: getContext(),
      goal,
      hours,
      experience,
      enrolledCourses,
    });

  const handleAsk = () => {
    if (!input.trim()) return;
    
    const userMessage = { role: 'user', content: input, timestamp: Date.now() };
    setChatHistory([...chatHistory, userMessage]);
    setInput('');
    
    setIsTyping(true);
    setTimeout(() => {
      const response = generateResponse(input);
      const assistantMessage = { role: 'assistant', content: response, timestamp: Date.now() };
      setChatHistory(prev => [...prev, assistantMessage]);
      setIsTyping(false);
    }, 800 + Math.random() * 500);
  };

  const handleSuggested = (text) => {
    setInput(text);
  };

  const clearChat = () => {
    setChatHistory([]);
  };

  useEffect(() => {
    chatEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [chatHistory]);

  return (
    <div className="ai-coach-page">
      <div className="coach-header">
        <div className="coach-avatar">🤖</div>
        <div className="coach-info">
          <h2>AI Learning Coach</h2>
          <p>Personalized guidance based on your profile and progress</p>
        </div>
      </div>

      <div className="quick-actions">
        <span className="actions-label">Quick Actions:</span>
        <button className="quick-action" onClick={() => handleSuggested("What's the fastest way to reach my goal?")}>
          🎯 Goal Strategy
        </button>
        <button className="quick-action" onClick={() => handleSuggested("How should I structure my daily study schedule?")}>
          📅 Study Plan
        </button>
        <button className="quick-action" onClick={() => handleSuggested("What projects should I build?")}>
          💻 Projects
        </button>
        <button className="quick-action" onClick={() => handleSuggested("I'm feeling overwhelmed, what should I do?")}>
          💪 Motivation
        </button>
      </div>

      <div className="suggested-questions">
        <h3>💡 Common Questions</h3>
        <div className="suggested-grid">
          {suggested.map((q, i) => (
            <button key={i} className="suggested-btn" onClick={() => handleSuggested(q.text)}>
              <span>{q.icon}</span>
              <span>{q.text}</span>
            </button>
          ))}
        </div>
      </div>

      <div className="input-section">
        <div className="input-wrapper">
          <input 
            type="text" 
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Ask me anything about learning..."
            onKeyPress={(e) => e.key === 'Enter' && handleAsk()}
          />
          <button className="send-btn" onClick={handleAsk} disabled={!input.trim()}>
            <svg viewBox="0 0 24 24" fill="currentColor">
              <path d="M2.01 21L23 12 2.01 3 2 10l15 2-15 2z"/>
            </svg>
          </button>
        </div>
      </div>

      {chatHistory.length > 0 && (
        <ChatMessages
          chatHistory={chatHistory}
          isTyping={isTyping}
          clearChat={clearChat}
          chatEndRef={chatEndRef}
        />
      )}

      <div className="coach-footer">
        <p>💡 Tip: Ask about study schedules, motivation, projects, interview prep, or any learning topic!</p>
      </div>
    </div>
  );
}

export default AICoach;