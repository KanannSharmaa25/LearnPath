import React, { useState } from 'react';
import { AppContext } from '../App';

function LearningLog() {
  const { setStep, dailyLogs, setDailyLogs } = React.useContext(AppContext);
  const [formData, setFormData] = useState({
    topic: '',
    type: 'Watching tutorials/videos',
    hours: 1,
    difficulty: 'Medium',
    resource: '',
    mood: '🙂 Good',
    notes: '',
    nextTopics: '',
    completed: false,
    newConcept: false,
    struggled: false
  });

  const learningTypes = [
    "Watching tutorials/videos",
    "Reading documentation/articles",
    "Taking a course",
    "Building a project",
    "Practice exercises",
    "Code review",
    "Reading books",
    "Other"
  ];

  const moods = ["😊 Great", "🙂 Good", "😐 Okay", "😕 Struggled", "😤 Frustrated"];
  const difficulties = ["Easy", "Medium", "Hard"];
  const topicTags = [
    "Python", "JavaScript", "Web Dev", "React", "Data Science", 
    "Machine Learning", "Databases", "APIs", "Git/GitHub", 
    "Cloud", "DevOps", "Mobile", "UI/UX", "Algorithms"
  ];
  const [selectedTags, setSelectedTags] = useState([]);

  const toggleTag = (tag) => {
    if (selectedTags.includes(tag)) {
      setSelectedTags(selectedTags.filter(t => t !== tag));
    } else {
      setSelectedTags([...selectedTags, tag]);
    }
  };

  const handleSubmit = () => {
    const logEntry = {
      ...formData,
      date: new Date().toISOString().split('T')[0],
      tags: selectedTags,
      timestamp: new Date().toISOString()
    };
    
    setDailyLogs([...dailyLogs, logEntry]);
    setStep(6);
  };

  const handleChange = (field, value) => {
    setFormData({ ...formData, [field]: value });
  };

  return (
    <div className="learning-log-page">
      <h2>📊 Log Your Learning Journey</h2>
      <p style={{ marginBottom: '32px' }}>Track your daily learning activities, progress, and reflections.</p>

      <div className="card">
        <h3>📚 Learning Details</h3>
        <div className="grid-2">
          <div className="input-field">
            <label>What did you learn?</label>
            <input 
              type="text" 
              value={formData.topic}
              onChange={(e) => handleChange('topic', e.target.value)}
              placeholder="e.g., Python functions, React hooks..."
            />
          </div>
          <div className="input-field">
            <label>Learning Type</label>
            <select value={formData.type} onChange={(e) => handleChange('type', e.target.value)}>
              {learningTypes.map(type => (
                <option key={type}>{type}</option>
              ))}
            </select>
          </div>
        </div>
        <div className="grid-2">
          <div className="input-field">
            <label>Hours spent: {formData.hours}</label>
            <input 
              type="range" 
              min="0.5" 
              max="12" 
              step="0.5"
              value={formData.hours}
              onChange={(e) => handleChange('hours', parseFloat(e.target.value))}
            />
          </div>
          <div className="input-field">
            <label>Difficulty</label>
            <div className="radio-group">
              {difficulties.map(d => (
                <label 
                  key={d}
                  className={`radio-option ${formData.difficulty === d ? 'selected' : ''}`}
                  onClick={() => handleChange('difficulty', d)}
                >
                  {d}
                </label>
              ))}
            </div>
          </div>
        </div>
        <div className="input-field">
          <label>Resource Used (optional)</label>
          <input 
            type="text" 
            value={formData.resource}
            onChange={(e) => handleChange('resource', e.target.value)}
            placeholder="e.g., Udemy Course, YouTube, Official Docs..."
          />
        </div>
      </div>

      <div className="card" style={{ marginTop: '24px' }}>
        <h3>🎯 Progress & Achievements</h3>
        <div className="grid-2">
          <div className="input-field">
            <label>Topics Covered</label>
            <div className="checkbox-group">
              {topicTags.map(tag => (
                <label 
                  key={tag}
                  className={`checkbox-option ${selectedTags.includes(tag) ? 'selected' : ''}`}
                  onClick={() => toggleTag(tag)}
                >
                  <input type="checkbox" checked={selectedTags.includes(tag)} readOnly />
                  {tag}
                </label>
              ))}
            </div>
          </div>
          <div>
            <div className="input-field">
              <label>How did you feel?</label>
              <select value={formData.mood} onChange={(e) => handleChange('mood', e.target.value)}>
                {moods.map(mood => (
                  <option key={mood}>{mood}</option>
                ))}
              </select>
            </div>
            <div className="input-field">
              <label style={{ marginTop: '16px', display: 'block' }}>Achievements</label>
              <label className={`checkbox-option ${formData.completed ? 'selected' : ''}`} onClick={() => handleChange('completed', !formData.completed)}>
                <input type="checkbox" checked={formData.completed} readOnly />
                Completed a milestone/sub-goal
              </label>
              <label className={`checkbox-option ${formData.newConcept ? 'selected' : ''}`} onClick={() => handleChange('newConcept', !formData.newConcept)}>
                <input type="checkbox" checked={formData.newConcept} readOnly />
                Learned something new
              </label>
              <label className={`checkbox-option ${formData.struggled ? 'selected' : ''}`} onClick={() => handleChange('struggled', !formData.struggled)}>
                <input type="checkbox" checked={formData.struggled} readOnly />
                Struggled with something
              </label>
            </div>
          </div>
        </div>
        <div className="input-field">
          <label>Quick notes (optional)</label>
          <textarea 
            value={formData.notes}
            onChange={(e) => handleChange('notes', e.target.value)}
            placeholder="Any thoughts, questions, or key takeaways..."
          />
        </div>
      </div>

      <div className="card" style={{ marginTop: '24px' }}>
        <h3>🔮 Tomorrow's Plan</h3>
        <div className="grid-2">
          <div className="input-field">
            <label>What will you learn next?</label>
            <input 
              type="text" 
              value={formData.nextTopics}
              onChange={(e) => handleChange('nextTopics', e.target.value)}
              placeholder="e.g., Python decorators, API routes..."
            />
          </div>
        </div>
      </div>

      <button className="btn btn-full" style={{ marginTop: '32px' }} onClick={handleSubmit}>
        💾 Save Log
      </button>

      {dailyLogs.length > 0 && (
        <div style={{ marginTop: '48px' }}>
          <h3>📜 Recent Logs</h3>
          {dailyLogs.slice(-5).reverse().map((log, i) => (
            <div key={i} className="card">
              <h4>📅 {log.date} - {log.topic}</h4>
              <p><strong>Type:</strong> {log.type}</p>
              <p><strong>Hours:</strong> {log.hours}</p>
              <p><strong>Difficulty:</strong> {log.difficulty}</p>
              <p><strong>Mood:</strong> {log.mood}</p>
              {log.tags && log.tags.length > 0 && <p><strong>Tags:</strong> {log.tags.join(', ')}</p>}
              {log.notes && <p><strong>Notes:</strong> {log.notes}</p>}
            </div>
          ))}
        </div>
      )}

      <button className="btn btn-secondary btn-full" style={{ marginTop: '32px' }} onClick={() => setStep(6)}>
        🏠 Back to Dashboard
      </button>
    </div>
  );
}

export default LearningLog;
