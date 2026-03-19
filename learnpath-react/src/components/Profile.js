import React, { useState } from 'react';
import { AppContext } from '../App';

function Profile() {
  const { setStep, userProfile, setUserProfile } = React.useContext(AppContext);
  const [formData, setFormData] = useState({
    name: userProfile.name || '',
    email: userProfile.email || '',
    age: userProfile.age || '18-24',
    gender: userProfile.gender || 'Prefer not to say',
    education: userProfile.education || 'High School',
    field: userProfile.field || 'Computer Science',
    role: userProfile.role || 'Student',
    experience: userProfile.experience || 0,
    goal: userProfile.goal || 'Get a job in tech',
    style: userProfile.style || ['Visual'],
    hours: userProfile.hours || 2,
    tech: userProfile.tech || 5,
    workEnv: userProfile.workEnv || 'Remote',
    schedule: userProfile.schedule || ['Flexible'],
    commute: userProfile.commute || 30,
    interest: userProfile.interest || 'Web Development',
    currentSkills: userProfile.currentSkills || [],
    certifications: userProfile.certifications || 'None',
    stress: userProfile.stress || 5,
    motivation: userProfile.motivation || 'Career growth',
    constraints: userProfile.constraints || []
  });

  const learningStyles = ['Visual', 'Auditory', 'Reading/Writing', 'Kinesthetic', 'Social', 'Solitary'];
  const skillOptions = ['Python', 'JavaScript', 'HTML/CSS', 'SQL', 'Java', 'None yet'];
  const handleSubmit = () => {
    setUserProfile(formData);
    setStep(2);
  };

  const handleChange = (field, value) => {
    setFormData({ ...formData, [field]: value });
  };

  const toggleArrayItem = (field, item) => {
    const current = formData[field];
    if (current.includes(item)) {
      handleChange(field, current.filter(i => i !== item));
    } else {
      handleChange(field, [...current, item]);
    }
  };

  return (
    <div className="profile-page">
      <h2>👤 Create Your Profile</h2>
      <p style={{ marginBottom: '32px' }}>Tell us about yourself so we can personalize your learning experience.</p>

      <div className="grid-3">
        <div className="card">
          <h3>Personal Info</h3>
          <div className="input-field">
            <label>Full Name</label>
            <input 
              type="text" 
              value={formData.name} 
              onChange={(e) => handleChange('name', e.target.value)}
              placeholder="Enter your name"
            />
          </div>
          <div className="input-field">
            <label>Email (optional)</label>
            <input 
              type="email" 
              value={formData.email} 
              onChange={(e) => handleChange('email', e.target.value)}
              placeholder="your@email.com"
            />
          </div>
          <div className="input-field">
            <label>Age Range</label>
            <select value={formData.age} onChange={(e) => handleChange('age', e.target.value)}>
              <option>Under 18</option>
              <option>18-24</option>
              <option>25-34</option>
              <option>35-44</option>
              <option>45-54</option>
              <option>55+</option>
            </select>
          </div>
        </div>

        <div className="card">
          <h3>Background</h3>
          <div className="input-field">
            <label>Education Level</label>
            <select value={formData.education} onChange={(e) => handleChange('education', e.target.value)}>
              <option>High School</option>
              <option>Some College</option>
              <option>Associate's</option>
              <option>Bachelor's</option>
              <option>Master's</option>
              <option>PhD</option>
            </select>
          </div>
          <div className="input-field">
            <label>Field of Study</label>
            <select value={formData.field} onChange={(e) => handleChange('field', e.target.value)}>
              <option>Computer Science</option>
              <option>Engineering</option>
              <option>Business</option>
              <option>Arts & Design</option>
              <option>Mathematics</option>
              <option>Science</option>
              <option>Other</option>
            </select>
          </div>
          <div className="input-field">
            <label>Current Role</label>
            <select value={formData.role} onChange={(e) => handleChange('role', e.target.value)}>
              <option>Student</option>
              <option>Employed Full-time</option>
              <option>Employed Part-time</option>
              <option>Freelancer</option>
              <option>Career Switcher</option>
              <option>Unemployed</option>
            </select>
          </div>
          <div className="input-field">
            <label>Years of Experience: {formData.experience}</label>
            <input 
              type="range" 
              min="0" 
              max="20" 
              value={formData.experience}
              onChange={(e) => handleChange('experience', parseInt(e.target.value))}
            />
          </div>
        </div>

        <div className="card">
          <h3>Learning Preferences</h3>
          <div className="input-field">
            <label>Primary Goal</label>
            <select value={formData.goal} onChange={(e) => handleChange('goal', e.target.value)}>
              <option>Get a job in tech</option>
              <option>Switch careers</option>
              <option>Advance in current role</option>
              <option>Build personal projects</option>
              <option>Start a business</option>
              <option>Personal growth</option>
            </select>
          </div>
          <div className="input-field">
            <label>Learning Style</label>
            <div className="checkbox-group">
              {learningStyles.map(style => (
                <label key={style} className={`checkbox-option ${formData.style.includes(style) ? 'selected' : ''}`}>
                  <input 
                    type="checkbox" 
                    checked={formData.style.includes(style)}
                    onChange={() => toggleArrayItem('style', style)}
                  />
                  {style}
                </label>
              ))}
            </div>
          </div>
          <div className="input-field">
            <label>Daily Learning Hours: {formData.hours}</label>
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
            <label>Tech Comfort Level: {formData.tech}/10</label>
            <input 
              type="range" 
              min="1" 
              max="10" 
              value={formData.tech}
              onChange={(e) => handleChange('tech', parseInt(e.target.value))}
            />
          </div>
        </div>
      </div>

      <div className="divider"></div>

      <h3>Additional Details</h3>
      <div className="grid-3" style={{ marginTop: '24px' }}>
        <div className="card">
          <h4>Work & Schedule</h4>
          <div className="input-field">
            <label>Work Environment</label>
            <select value={formData.workEnv} onChange={(e) => handleChange('workEnv', e.target.value)}>
              <option>Remote</option>
              <option>Office</option>
              <option>Hybrid</option>
              <option>Field Work</option>
            </select>
          </div>
          <div className="input-field">
            <label>Tech Interest</label>
            <select value={formData.interest} onChange={(e) => handleChange('interest', e.target.value)}>
              <option>Web Development</option>
              <option>Mobile Development</option>
              <option>Data Science/ML</option>
              <option>Cloud/DevOps</option>
              <option>Cybersecurity</option>
              <option>UI/UX Design</option>
            </select>
          </div>
        </div>

        <div className="card">
          <h4>Career & Skills</h4>
          <div className="input-field">
            <label>Current Skills</label>
            <div className="checkbox-group">
              {skillOptions.map(skill => (
                <label key={skill} className={`checkbox-option ${formData.currentSkills.includes(skill) ? 'selected' : ''}`}>
                  <input 
                    type="checkbox" 
                    checked={formData.currentSkills.includes(skill)}
                    onChange={() => toggleArrayItem('currentSkills', skill)}
                  />
                  {skill}
                </label>
              ))}
            </div>
          </div>
        </div>

        <div className="card">
          <h4>Lifestyle & Motivation</h4>
          <div className="input-field">
            <label>Stress Tolerance: {formData.stress}/10</label>
            <input 
              type="range" 
              min="1" 
              max="10" 
              value={formData.stress}
              onChange={(e) => handleChange('stress', parseInt(e.target.value))}
            />
          </div>
          <div className="input-field">
            <label>Motivation Source</label>
            <select value={formData.motivation} onChange={(e) => handleChange('motivation', e.target.value)}>
              <option>Career growth</option>
              <option>Money/Financial</option>
              <option>Passion for tech</option>
              <option>Problem solving</option>
              <option>Recognition</option>
            </select>
          </div>
        </div>
      </div>

      <div className="divider"></div>

      <button className="btn btn-full" onClick={handleSubmit}>
        Save & Continue
      </button>
    </div>
  );
}

export default Profile;
