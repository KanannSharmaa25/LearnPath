import React, { useState, useEffect } from 'react';
import { AppContext } from '../App';
import './Prediction.css';

function Prediction() {
  const { setStep, userProfile, quizBatchScores, learningPath, assessmentAnswers } = React.useContext(AppContext);
  const [activeMode, setActiveMode] = useState('smart');
  const [customData, setCustomData] = useState({
    goal: '',
    hoursPerDay: 2,
    experience: 0,
    learningStyle: 'hands-on',
    weeklyDays: 5,
    focusLevel: 'moderate',
    targetRole: '',
    certifications: false,
    projectsPerMonth: 2,
    hasMentor: false,
    targetSalary: '',
    location: '',
  });
  const [prediction, setPrediction] = useState(null);
  const [comparisonScenario, setComparisonScenario] = useState(null);

  const goal = userProfile.goal || '';
  const hours = userProfile.hours || 2;
  const experience = userProfile.experience || 0;
  const techLevel = userProfile.tech || 5;

  useEffect(() => {
    if (activeMode === 'smart' && !prediction) {
      handleSmartPrediction();
    }
  // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [activeMode]);

  const goalEstimates = {
    'web': { 
      baseHours: 800, 
      description: 'Full-Stack Web Developer', 
      roles: ['Frontend Dev', 'Backend Dev', 'Full-Stack Dev'],
      topics: ['HTML/CSS', 'JavaScript', 'React', 'Node.js', 'Databases']
    },
    'data': { 
      baseHours: 1000, 
      description: 'Data Scientist/ML Engineer', 
      roles: ['Data Analyst', 'Data Scientist', 'ML Engineer'],
      topics: ['Python', 'Statistics', 'SQL', 'ML', 'Deep Learning']
    },
    'devops': { 
      baseHours: 600, 
      description: 'DevOps/Cloud Engineer', 
      roles: ['DevOps Engineer', 'Cloud Engineer', 'SRE'],
      topics: ['Linux', 'Docker', 'Kubernetes', 'CI/CD', 'Cloud']
    },
    'mobile': { 
      baseHours: 700, 
      description: 'Mobile Developer', 
      roles: ['iOS Dev', 'Android Dev', 'Cross-Platform Dev'],
      topics: ['Mobile Basics', 'React Native', 'Flutter', 'APIs', 'Firebase']
    },
    'security': { 
      baseHours: 500, 
      description: 'Cybersecurity Specialist', 
      roles: ['Security Analyst', 'Penetration Tester', 'Security Engineer'],
      topics: ['Network Security', 'Ethical Hacking', 'Cryptography', 'Malware Analysis']
    },
    'default': { 
      baseHours: 600, 
      description: 'Software Developer', 
      roles: ['Junior Dev', 'Mid-Level Dev', 'Senior Dev'],
      topics: ['Programming Basics', 'Problem Solving', 'Version Control']
    },
  };

  const detectGoal = (goalText) => {
    const text = goalText.toLowerCase();
    if (text.includes('web') || text.includes('frontend') || text.includes('backend') || text.includes('full-stack') || text.includes('react') || text.includes('javascript')) return 'web';
    if (text.includes('data') || text.includes('ml') || text.includes('ai') || text.includes('machine learning') || text.includes('python')) return 'data';
    if (text.includes('cloud') || text.includes('devops') || text.includes('sre') || text.includes('docker') || text.includes('kubernetes')) return 'devops';
    if (text.includes('mobile') || text.includes('ios') || text.includes('android') || text.includes('react native') || text.includes('flutter')) return 'mobile';
    if (text.includes('security') || text.includes('cyber') || text.includes('penetration') || text.includes('ethical')) return 'security';
    return 'default';
  };

  const calculateQuizReadiness = () => {
    const scores = Object.values(quizBatchScores);
    if (scores.length === 0) return { readiness: 0, avgScore: 0, strongTopics: [], weakTopics: [], topicsCovered: 0 };
    
    const avgScore = Math.round(scores.reduce((acc, s) => acc + s.score, 0) / scores.length);
    const strongTopics = scores.filter(s => s.score >= 80).length;
    const weakTopics = scores.filter(s => s.score < 60).length;
    
    return {
      readiness: Math.min(avgScore + (scores.length * 2), 95),
      avgScore,
      strongTopics,
      weakTopics,
      topicsCovered: scores.length
    };
  };

  const calculateAssessmentInsights = () => {
    if (!assessmentAnswers || Object.keys(assessmentAnswers).length === 0) {
      return {
        learningStyle: 'balanced',
        workStyle: 'independent',
        stressHandling: 'moderate',
        motivation: 'achievement',
        personality: 'explorer'
      };
    }

    const answers = Object.values(assessmentAnswers);
    const counts = {};
    answers.forEach(a => {
      counts[a] = (counts[a] || 0) + 1;
    });

    const learningStyle = counts['hands-on'] > counts['video'] ? 'hands-on' : 
                         counts['video'] > counts['hands-on'] ? 'video' : 'mixed';
    
    const stressHandling = counts['calm'] > counts['stress'] ? 'calm' : 'moderate';
    
    return {
      learningStyle,
      workStyle: counts['group'] > counts['solo'] ? 'collaborative' : 'independent',
      stressHandling,
      motivation: 'achievement',
      personality: 'explorer'
    };
  };

  const calculatePathProgress = () => {
    if (learningPath.length === 0) return { completed: 0, inProgress: 0, remaining: 0, totalHoursCompleted: 0 };
    
    const completed = learningPath.filter(p => p.progress === 100).length;
    const inProgress = learningPath.filter(p => p.progress > 0 && p.progress < 100).length;
    const remaining = learningPath.length - completed - inProgress;
    const totalHoursCompleted = learningPath.reduce((acc, p) => {
      return acc + (p.progress / 100 * 20);
    }, 0);

    return { completed, inProgress, remaining, totalHoursCompleted: Math.round(totalHoursCompleted) };
  };

  const calculateSmartPrediction = () => {
    const goalType = detectGoal(goal);
    const goalInfo = goalEstimates[goalType] || goalEstimates.default;
    let baseHours = goalInfo.baseHours;

    const quizInsights = calculateQuizReadiness();
    const assessmentInsights = calculateAssessmentInsights();
    const pathProgress = calculatePathProgress();

    let learningStyleMultiplier = 1;
    if (assessmentInsights.learningStyle === 'hands-on') learningStyleMultiplier = 0.8;
    else if (assessmentInsights.learningStyle === 'video') learningStyleMultiplier = 0.85;
    else if (assessmentInsights.learningStyle === 'mixed') learningStyleMultiplier = 0.82;

    const experienceReduction = Math.min(experience * 0.12, 0.5);

    let quizBonus = 0;
    if (quizInsights.topicsCovered > 0) {
      quizBonus = (quizInsights.avgScore / 100) * 0.2;
      baseHours = baseHours * (1 - quizBonus);
    }

    const pathDeduction = (pathProgress.completed / learningPath.length) * 0.1;
    baseHours = baseHours * (1 - pathDeduction);

    const stressMultiplier = assessmentInsights.stressHandling === 'calm' ? 0.9 : 1;

    const weeklyHours = hours * 5;
    const adjustedHours = baseHours * learningStyleMultiplier * stressMultiplier * (1 - experienceReduction);
    
    const weeksToCompletion = Math.ceil(adjustedHours / weeklyHours);
    const monthsToCompletion = (weeksToCompletion / 4).toFixed(1);
    
    const today = new Date();
    const completionDate = new Date(today);
    completionDate.setDate(today.getDate() + (weeksToCompletion * 7));

    const totalTopics = goalInfo.topics.length;
    const topicsLearned = pathProgress.completed + Math.round(quizInsights.topicsCovered * 0.5);
    const progressPercent = Math.min(Math.round((topicsLearned / totalTopics) * 100), 95);

    const milestones = [
      { 
        name: 'Foundation Complete', 
        weeks: Math.ceil(weeksToCompletion * 0.25),
        percentage: 25,
        description: 'Core concepts mastered based on your assessment profile',
        skills: goalInfo.topics.slice(0, 2)
      },
      { 
        name: 'Quiz Knowledge Validated', 
        weeks: Math.ceil(weeksToCompletion * 0.4),
        percentage: 40,
        description: 'Topics from quizzes solidified',
        skills: quizInsights.strongTopics > 2 ? ['Strong fundamentals', 'Problem-solving'] : ['Building confidence']
      },
      { 
        name: 'Path Milestone', 
        weeks: Math.ceil(weeksToCompletion * 0.65),
        percentage: 65,
        description: `${pathProgress.completed}/${learningPath.length} path topics complete`,
        skills: ['Advanced patterns', 'Best practices']
      },
      { 
        name: 'Job Ready', 
        weeks: weeksToCompletion,
        percentage: 100,
        description: 'Ready for professional opportunities',
        skills: ['Portfolio ready', 'Interview prepared']
      },
    ];

    const speedUpFactors = [];
    const slowDownFactors = [];

    if (assessmentInsights.learningStyle === 'hands-on') speedUpFactors.push('Your hands-on learning style accelerates project building');
    if (assessmentInsights.stressHandling === 'calm') speedUpFactors.push('You handle pressure well - great for intensive learning');
    if (quizInsights.strongTopics > 2) speedUpFactors.push(`Strong foundation in ${quizInsights.strongTopics} quiz topics`);
    if (pathProgress.completed > 0) speedUpFactors.push(`${pathProgress.completed} topics already started in your learning path`);
    if (techLevel >= 7) speedUpFactors.push('High tech proficiency gives you a head start');

    if (quizInsights.weakTopics > 2) slowDownFactors.push(`${quizInsights.weakTopics} areas need extra practice`);
    if (assessmentInsights.learningStyle === 'video') slowDownFactors.push('Video-based learning is slower than hands-on');
    if (techLevel < 4) slowDownFactors.push('Lower tech level means more foundational work needed');
    if (quizInsights.topicsCovered < 3) slowDownFactors.push('Complete more quizzes for better predictions');
    if (pathProgress.remaining > 3) slowDownFactors.push(`${pathProgress.remaining} path topics still not started`);

    const confidence = Math.min(95, 50 + 
      (quizInsights.topicsCovered * 5) + 
      (pathProgress.completed * 8) + 
      (techLevel * 2) +
      (assessmentInsights.learningStyle === 'hands-on' ? 10 : 0));

    return {
      goalType,
      goalInfo,
      totalHours: Math.round(adjustedHours),
      hoursRemaining: Math.round(adjustedHours - pathProgress.totalHoursCompleted),
      weeksToCompletion,
      monthsToCompletion: parseFloat(monthsToCompletion),
      completionDate: completionDate.toLocaleDateString('en-US', { month: 'long', year: 'numeric' }),
      weeklyHours: Math.round(weeklyHours),
      milestones,
      confidence: Math.round(confidence),
      quizInsights,
      assessmentInsights,
      pathProgress,
      speedUpFactors,
      slowDownFactors,
      progressPercent,
      marketInsights: getMarketInsights(goalType),
      salaryProjection: getSalaryProjection(goalType),
      roleProgression: goalInfo.roles,
      dataSources: {
        profile: { goal, hours, experience, techLevel },
        assessment: assessmentInsights,
        quizzes: quizInsights,
        learningPath: pathProgress
      }
    };
  };

  const getMarketInsights = (goalType) => {
    const insights = {
      'web': { demand: 'Very High', growth: '12%', competition: 'High', tips: ['Build a strong portfolio', 'Learn TypeScript', 'Master one framework deeply'] },
      'data': { demand: 'Very High', growth: '15%', competition: 'Medium', tips: ['Kaggle portfolio is valuable', 'Specialize in one ML domain', 'Build end-to-end projects'] },
      'devops': { demand: 'High', growth: '14%', competition: 'Low', tips: ['Get cloud certifications', 'Build CI/CD pipelines', 'Contribute to open source'] },
      'mobile': { demand: 'High', growth: '10%', competition: 'Medium', tips: ['React Native or Flutter skills', 'Publish apps to stores', 'Build for both iOS and Android'] },
      'security': { demand: 'Very High', growth: '18%', competition: 'Low', tips: ['Get certifications (CompTIA, CISSP)', 'Practice on HackTheBox', 'Build a home lab'] },
      'default': { demand: 'High', growth: '10%', competition: 'High', tips: ['Build projects', 'Contribute to open source', 'Network actively'] },
    };
    return insights[goalType] || insights.default;
  };

  const getSalaryProjection = (goalType) => {
    const baseSalaries = {
      'web': { entry: 55000, mid: 85000, senior: 120000 },
      'data': { entry: 65000, mid: 100000, senior: 150000 },
      'devops': { entry: 70000, mid: 110000, senior: 160000 },
      'mobile': { entry: 60000, mid: 95000, senior: 140000 },
      'security': { entry: 70000, mid: 115000, senior: 170000 },
      'default': { entry: 55000, mid: 85000, senior: 125000 },
    };
    const salaries = baseSalaries[goalType] || baseSalaries.default;
    return {
      entry: salaries.entry,
      mid: salaries.mid,
      senior: salaries.senior,
      currency: 'USD',
    };
  };

  const calculatePrediction = (data, isCustom = false) => {
    const goalType = detectGoal(isCustom ? data.goal : goal);
    const goalInfo = goalEstimates[goalType] || goalEstimates.default;
    let baseHours = goalInfo.baseHours;

    let efficiencyMultiplier = 1;
    switch (data.learningStyle) {
      case 'hands-on': efficiencyMultiplier = 0.8; break;
      case 'video': efficiencyMultiplier = 0.85; break;
      case 'reading': efficiencyMultiplier = 0.9; break;
      case 'mix': efficiencyMultiplier = 0.75; break;
      default: efficiencyMultiplier = 0.85;
    }

    let focusMultiplier = 1;
    switch (data.focusLevel) {
      case 'intense': focusMultiplier = 0.85; break;
      case 'moderate': focusMultiplier = 1; break;
      case 'relaxed': focusMultiplier = 1.2; break;
      default: focusMultiplier = 1;
    }

    const experienceReduction = Math.min(data.experience * 0.12, 0.5);
    const weeklyHours = data.hoursPerDay * data.weeklyDays;
    const adjustedHours = baseHours * efficiencyMultiplier * focusMultiplier * (1 - experienceReduction);

    const weeksToJobReady = Math.ceil(adjustedHours / weeklyHours);
    const monthsToJobReady = (weeksToJobReady / 4).toFixed(1);
    
    const today = new Date();
    const completionDate = new Date(today);
    completionDate.setDate(today.getDate() + (weeksToJobReady * 7));

    const milestones = [
      { name: 'Foundation Mastery', weeks: Math.ceil(weeksToJobReady * 0.2), percentage: 20, description: 'Core concepts and basic skills', skills: ['Fundamentals', 'Basic syntax'] },
      { name: 'Intermediate Proficiency', weeks: Math.ceil(weeksToJobReady * 0.45), percentage: 45, description: 'Building real-world applications', skills: ['Frameworks', 'APIs'] },
      { name: 'Advanced & Portfolio', weeks: Math.ceil(weeksToJobReady * 0.75), percentage: 75, description: 'Complex projects and portfolio', skills: ['Advanced patterns', 'Portfolio'] },
      { name: 'Job Ready', weeks: weeksToJobReady, percentage: 100, description: 'Interview prep and job search', skills: ['Interview prep'] },
    ];

    const speedUpFactors = [];
    const slowDownFactors = [];

    if (data.projectsPerMonth >= 3) speedUpFactors.push('Building 3+ projects monthly');
    if (data.projectsPerMonth < 2) slowDownFactors.push('Only 1-2 projects monthly');
    if (data.hasMentor) speedUpFactors.push('Having a mentor');
    if (data.learningStyle === 'hands-on') speedUpFactors.push('Hands-on learning approach');
    if (data.weeklyDays >= 6) speedUpFactors.push('Consistent 6-7 day schedule');
    if (data.weeklyDays < 5) slowDownFactors.push('Inconsistent study schedule');

    return {
      goalType,
      goalInfo,
      totalHours: Math.round(adjustedHours),
      weeksToCompletion: weeksToJobReady,
      monthsToCompletion: parseFloat(monthsToJobReady),
      completionDate: completionDate.toLocaleDateString('en-US', { month: 'long', year: 'numeric' }),
      weeklyHours: Math.round(weeklyHours),
      milestones,
      experienceYears: data.experience,
      learningStyle: data.learningStyle,
      speedUpFactors,
      slowDownFactors,
      confidence: calculateConfidence(data),
      marketInsights: getMarketInsights(goalType),
      salaryProjection: getSalaryProjection(goalType),
      roleProgression: goalInfo.roles,
    };
  };

  const calculateConfidence = (data) => {
    let score = 70;
    if (data.hoursPerDay >= 2) score += 10;
    if (data.hoursPerDay >= 4) score += 10;
    if (data.weeklyDays >= 5) score += 10;
    if (data.projectsPerMonth >= 3) score += 10;
    if (data.hasMentor) score += 10;
    if (data.learningStyle === 'hands-on' || data.learningStyle === 'mix') score += 10;
    return Math.min(score, 99);
  };

  const handleSmartPrediction = () => {
    const pred = calculateSmartPrediction();
    setPrediction(pred);
  };

  const handleCustomPrediction = () => {
    const pred = calculatePrediction(customData, true);
    setPrediction(pred);
  };

  const handleComparison = () => {
    const scenario1 = calculatePrediction({ ...customData, hoursPerDay: customData.hoursPerDay, weeklyDays: customData.weeklyDays }, true);
    const scenario2 = calculatePrediction({ ...customData, hoursPerDay: customData.hoursPerDay + 1, weeklyDays: Math.min(customData.weeklyDays + 1, 7) }, true);
    setComparisonScenario({ current: scenario1, improved: scenario2 });
  };

  const formatCurrency = (amount) => {
    return new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD', maximumFractionDigits: 0 }).format(amount);
  };

  const quizInsights = calculateQuizReadiness();
  const assessmentInsights = calculateAssessmentInsights();
  const pathProgress = calculatePathProgress();

  return (
    <div className="prediction-page">
      <div className="prediction-header">
        <h2>🔮 AI Learning Predictions</h2>
        <p>Smart timeline predictions based on your profile, assessments, quizzes, and learning path</p>
      </div>

      <div className="mode-tabs">
        <button 
          className={`mode-tab ${activeMode === 'smart' ? 'active' : ''}`}
          onClick={() => { setActiveMode('smart'); setPrediction(null); }}
        >
          🧠 Smart Prediction
        </button>
        <button 
          className={`mode-tab ${activeMode === 'custom' ? 'active' : ''}`}
          onClick={() => { setActiveMode('custom'); setPrediction(null); }}
        >
          🎯 Custom Scenario
        </button>
        <button 
          className={`mode-tab ${activeMode === 'compare' ? 'active' : ''}`}
          onClick={() => { setActiveMode('compare'); setPrediction(null); }}
        >
          ⚖️ Compare
        </button>
      </div>

      {activeMode === 'smart' && (
        <div className="smart-section">
          <div className="data-summary">
            <h3>📊 Your Data Summary</h3>
            <div className="summary-grid">
              <div className="summary-card">
                <div className="summary-icon">👤</div>
                <div className="summary-content">
                  <span className="summary-label">Profile</span>
                  <span className="summary-value">{goal || 'Not set'}</span>
                  <span className="summary-detail">{hours}h/day • {experience} years exp • Level {techLevel}</span>
                </div>
              </div>
              <div className="summary-card">
                <div className="summary-icon">🧠</div>
                <div className="summary-content">
                  <span className="summary-label">Assessment</span>
                  <span className="summary-value">{assessmentInsights.learningStyle} learner</span>
                  <span className="summary-detail">{assessmentInsights.stressHandling} under pressure</span>
                </div>
              </div>
              <div className="summary-card">
                <div className="summary-icon">📝</div>
                <div className="summary-content">
                  <span className="summary-label">Quizzes</span>
                  <span className="summary-value">{quizInsights.topicsCovered} topics tested</span>
                  <span className="summary-detail">Avg: {quizInsights.avgScore}% • {quizInsights.strongTopics} strong</span>
                </div>
              </div>
              <div className="summary-card">
                <div className="summary-icon">🛤️</div>
                <div className="summary-content">
                  <span className="summary-label">Learning Path</span>
                  <span className="summary-value">{pathProgress.completed} completed</span>
                  <span className="summary-detail">{pathProgress.inProgress} in progress • {pathProgress.remaining} remaining</span>
                </div>
              </div>
            </div>
          </div>

          <button className="btn btn-primary btn-full" onClick={handleSmartPrediction}>
            🔮 Generate Smart Prediction
          </button>

          {prediction && (
            <SmartPredictionResult prediction={prediction} formatCurrency={formatCurrency} />
          )}
        </div>
      )}

      {activeMode === 'custom' && (
        <div className="custom-section">
          <div className="custom-form">
            <div className="form-section">
              <h3>🎯 Learning Goals</h3>
              <div className="form-group">
                <label>What do you want to learn?</label>
                <input
                  type="text"
                  value={customData.goal}
                  onChange={(e) => setCustomData({...customData, goal: e.target.value})}
                  placeholder="e.g., Web Development, Data Science, Cloud Engineering"
                />
              </div>
            </div>

            <div className="form-section">
              <h3>⏰ Time Commitment</h3>
              <div className="form-row">
                <div className="form-group">
                  <label>Hours per day</label>
                  <select value={customData.hoursPerDay} onChange={(e) => setCustomData({...customData, hoursPerDay: Number(e.target.value)})}>
                    <option value={0.5}>30 minutes</option>
                    <option value={1}>1 hour</option>
                    <option value={2}>2 hours</option>
                    <option value={3}>3 hours</option>
                    <option value={4}>4 hours</option>
                    <option value={5}>5+ hours</option>
                  </select>
                </div>
                <div className="form-group">
                  <label>Days per week</label>
                  <select value={customData.weeklyDays} onChange={(e) => setCustomData({...customData, weeklyDays: Number(e.target.value)})}>
                    <option value={3}>3 days</option>
                    <option value={4}>4 days</option>
                    <option value={5}>5 days</option>
                    <option value={6}>6 days</option>
                    <option value={7}>7 days</option>
                  </select>
                </div>
              </div>
            </div>

            <div className="form-section">
              <h3>🧠 Learning Style</h3>
              <div className="form-group">
                <label>Preferred learning method</label>
                <div className="radio-group vertical">
                  <label className={customData.learningStyle === 'hands-on' ? 'selected' : ''}>
                    <input type="radio" name="style" value="hands-on" checked={customData.learningStyle === 'hands-on'} onChange={() => setCustomData({...customData, learningStyle: 'hands-on'})} />
                    🛠️ Hands-on Projects (Fastest)
                  </label>
                  <label className={customData.learningStyle === 'mix' ? 'selected' : ''}>
                    <input type="radio" name="style" value="mix" checked={customData.learningStyle === 'mix'} onChange={() => setCustomData({...customData, learningStyle: 'mix'})} />
                    ⚡ Mix of Theory & Practice
                  </label>
                  <label className={customData.learningStyle === 'video' ? 'selected' : ''}>
                    <input type="radio" name="style" value="video" checked={customData.learningStyle === 'video'} onChange={() => setCustomData({...customData, learningStyle: 'video'})} />
                    🎥 Video Tutorials
                  </label>
                  <label className={customData.learningStyle === 'reading' ? 'selected' : ''}>
                    <input type="radio" name="style" value="reading" checked={customData.learningStyle === 'reading'} onChange={() => setCustomData({...customData, learningStyle: 'reading'})} />
                    📖 Reading/Documentation
                  </label>
                </div>
              </div>
            </div>

            <div className="form-section">
              <h3>📈 Experience & Resources</h3>
              <div className="form-row">
                <div className="form-group">
                  <label>Prior experience</label>
                  <select value={customData.experience} onChange={(e) => setCustomData({...customData, experience: Number(e.target.value)})}>
                    <option value={0}>Complete beginner</option>
                    <option value={0.5}>~6 months</option>
                    <option value={1}>1 year</option>
                    <option value={2}>2 years</option>
                    <option value={3}>3+ years</option>
                  </select>
                </div>
                <div className="form-group">
                  <label>Projects per month</label>
                  <select value={customData.projectsPerMonth} onChange={(e) => setCustomData({...customData, projectsPerMonth: Number(e.target.value)})}>
                    <option value={1}>1 project</option>
                    <option value={2}>2 projects</option>
                    <option value={3}>3 projects</option>
                    <option value={4}>4+ projects</option>
                  </select>
                </div>
              </div>
              <div className="form-group">
                <label>Do you have a mentor/teacher?</label>
                <div className="radio-group">
                  <label className={customData.hasMentor ? 'selected' : ''}>
                    <input type="radio" name="mentor" value="yes" checked={customData.hasMentor} onChange={() => setCustomData({...customData, hasMentor: true})} />
                    ✓ Yes
                  </label>
                  <label className={!customData.hasMentor ? 'selected' : ''}>
                    <input type="radio" name="mentor" value="no" checked={!customData.hasMentor} onChange={() => setCustomData({...customData, hasMentor: false})} />
                    ✗ No
                  </label>
                </div>
              </div>
            </div>

            <button className="btn btn-primary btn-full btn-large" onClick={handleCustomPrediction}>
              🔮 Generate Custom Prediction
            </button>
          </div>

          {prediction && (
            <PredictionResult prediction={prediction} formatCurrency={formatCurrency} isCustom={true} />
          )}
        </div>
      )}

      {activeMode === 'compare' && (
        <div className="compare-section">
          <p className="compare-intro">
            Compare two scenarios to see how changes in your commitment affect your timeline.
          </p>

          <div className="compare-form">
            <div className="form-section">
              <h3>⚙️ Your Scenario Settings</h3>
              <div className="form-row">
                <div className="form-group">
                  <label>Hours per day</label>
                  <select value={customData.hoursPerDay} onChange={(e) => setCustomData({...customData, hoursPerDay: Number(e.target.value)})}>
                    <option value={1}>1 hour</option>
                    <option value={2}>2 hours</option>
                    <option value={3}>3 hours</option>
                    <option value={4}>4 hours</option>
                  </select>
                </div>
                <div className="form-group">
                  <label>Days per week</label>
                  <select value={customData.weeklyDays} onChange={(e) => setCustomData({...customData, weeklyDays: Number(e.target.value)})}>
                    <option value={3}>3 days</option>
                    <option value={4}>4 days</option>
                    <option value={5}>5 days</option>
                    <option value={6}>6 days</option>
                  </select>
                </div>
              </div>
              <div className="form-group">
                <label>Learning Goal</label>
                <input
                  type="text"
                  value={customData.goal}
                  onChange={(e) => setCustomData({...customData, goal: e.target.value})}
                  placeholder="e.g., Web Development"
                />
              </div>
            </div>

            <button className="btn btn-secondary btn-full" onClick={handleComparison}>
              ⚖️ Compare Current vs. +1 Hour/Day
            </button>
          </div>

          {comparisonScenario && (
            <div className="comparison-results">
              <ComparisonCard title="📊 Current Plan" prediction={comparisonScenario.current} formatCurrency={formatCurrency} />
              <ComparisonCard title="🚀 With More Time" prediction={comparisonScenario.improved} formatCurrency={formatCurrency} isImproved={true} />
            </div>
          )}
        </div>
      )}

      <div style={{ marginTop: '32px', display: 'flex', gap: '12px' }}>
        <button className="btn btn-secondary" onClick={() => setStep(7)}>💬 AI Coach</button>
        <button className="btn" onClick={() => setStep(6)}>🏠 Dashboard</button>
      </div>
    </div>
  );
}

function SmartPredictionResult({ prediction, formatCurrency }) {
  return (
    <div className="prediction-result smart-result">
      <div className="result-header">
        <h3>🧠 Smart Prediction Results</h3>
        <span className="confidence-badge">
          {prediction.confidence}% Confidence
        </span>
      </div>

      <div className="smart-insights">
        <div className="insight-banner">
          <span className="insight-icon">💡</span>
          <p>This prediction is based on your <strong>{prediction.quizInsights.topicsCovered} quiz scores</strong>, <strong>{prediction.assessmentInsights.learningStyle} learning style</strong>, and <strong>{prediction.pathProgress.completed} completed path topics</strong>.</p>
        </div>
      </div>

      <div className="timeline-hero">
        <div className="timeline-stat">
          <span className="stat-number">{prediction.monthsToCompletion}</span>
          <span className="stat-label">Months to Goal</span>
        </div>
        <div className="timeline-stat">
          <span className="stat-number">{prediction.weeksToCompletion}</span>
          <span className="stat-label">Weeks Total</span>
        </div>
        <div className="timeline-stat highlight">
          <span className="stat-number">{prediction.hoursRemaining}</span>
          <span className="stat-label">Hours Remaining</span>
        </div>
      </div>

      <div className="completion-date">
        🎉 Estimated completion: <strong>{prediction.completionDate}</strong>
      </div>

      <div className="overall-progress">
        <div className="progress-header">
          <span>Overall Progress</span>
          <span>{prediction.progressPercent}%</span>
        </div>
        <div className="progress-bar large">
          <div className="progress-fill" style={{ width: `${prediction.progressPercent}%` }}></div>
        </div>
        <div className="progress-breakdown">
          <span>📚 {prediction.pathProgress.completed} path topics</span>
          <span>📝 {prediction.quizInsights.topicsCovered} quiz topics</span>
          <span>⏱️ {prediction.pathProgress.totalHoursCompleted}h logged</span>
        </div>
      </div>

      <div className="milestones-section">
        <h4>📍 Your Learning Milestones</h4>
        <div className="milestones">
          {prediction.milestones.map((milestone, i) => (
            <div key={i} className="milestone-card">
              <div className="milestone-marker">
                <span className="milestone-number">{i + 1}</span>
                <div className="milestone-line"></div>
              </div>
              <div className="milestone-content">
                <div className="milestone-header">
                  <h5>{milestone.name}</h5>
                  <span className="milestone-weeks">Week {milestone.weeks}</span>
                </div>
                <p>{milestone.description}</p>
                <div className="milestone-progress">
                  <div className="progress-bar">
                    <div className="progress-fill" style={{ width: `${milestone.percentage}%` }}></div>
                  </div>
                  <span className="progress-text">{milestone.percentage}%</span>
                </div>
                {milestone.skills && (
                  <div className="milestone-skills">
                    {milestone.skills.map((skill, j) => (
                      <span key={j} className="skill-tag">{skill}</span>
                    ))}
                  </div>
                )}
              </div>
            </div>
          ))}
        </div>
      </div>

      <div className="insights-grid">
        <div className="insight-card">
          <h4>📈 Market Insights</h4>
          <div className="market-stats">
            <div className="market-stat">
              <span className="stat-label">Demand</span>
              <span className="stat-value demand-high">{prediction.marketInsights.demand}</span>
            </div>
            <div className="market-stat">
              <span className="stat-label">Growth</span>
              <span className="stat-value">{prediction.marketInsights.growth}</span>
            </div>
            <div className="market-stat">
              <span className="stat-label">Competition</span>
              <span className="stat-value">{prediction.marketInsights.competition}</span>
            </div>
          </div>
        </div>

        <div className="insight-card">
          <h4>💰 Salary Projections</h4>
          <div className="salary-tiers">
            <div className="salary-tier entry">
              <span className="tier-label">Entry Level</span>
              <span className="tier-salary">{formatCurrency(prediction.salaryProjection.entry)}</span>
            </div>
            <div className="salary-tier mid">
              <span className="tier-label">Mid Level</span>
              <span className="tier-salary">{formatCurrency(prediction.salaryProjection.mid)}</span>
            </div>
            <div className="salary-tier senior">
              <span className="tier-label">Senior</span>
              <span className="tier-salary">{formatCurrency(prediction.salaryProjection.senior)}</span>
            </div>
          </div>
        </div>
      </div>

      <div className="factors-section">
        <div className="factors-column">
          <h4>✅ Factors Speeding You Up</h4>
          {prediction.speedUpFactors.length > 0 ? (
            <ul className="factors-list speed-up">
              {prediction.speedUpFactors.map((factor, i) => (
                <li key={i}><span className="check">✓</span> {factor}</li>
              ))}
            </ul>
          ) : (
            <p className="no-factors">Complete more quizzes and path topics to speed up!</p>
          )}
        </div>
        <div className="factors-column">
          <h4>⚠️ Areas to Focus</h4>
          {prediction.slowDownFactors.length > 0 ? (
            <ul className="factors-list slow-down">
              {prediction.slowDownFactors.map((factor, i) => (
                <li key={i}><span className="warning">!</span> {factor}</li>
              ))}
            </ul>
          ) : (
            <p className="no-factors success">Looking good! No major concerns.</p>
          )}
        </div>
      </div>

      <div className="role-progression">
        <h4>🎓 Role Progression</h4>
        <div className="roles">
          {prediction.roleProgression.map((role, i) => (
            <div key={i} className="role-card">
              <span className="role-number">{i + 1}</span>
              <span className="role-name">{role}</span>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

function PredictionResult({ prediction, formatCurrency, isCustom }) {
  return (
    <div className="prediction-result">
      <div className="result-header">
        <h3>🎯 Prediction Results</h3>
        <span className="confidence-badge">{prediction.confidence}% Confidence</span>
      </div>

      <div className="timeline-hero">
        <div className="timeline-stat">
          <span className="stat-number">{prediction.monthsToCompletion}</span>
          <span className="stat-label">Months to Goal</span>
        </div>
        <div className="timeline-stat">
          <span className="stat-number">{prediction.weeksToCompletion}</span>
          <span className="stat-label">Weeks Total</span>
        </div>
        <div className="timeline-stat">
          <span className="stat-number">{prediction.totalHours}</span>
          <span className="stat-label">Hours Needed</span>
        </div>
      </div>

      <div className="completion-date">
        🎉 Estimated completion: <strong>{prediction.completionDate}</strong>
      </div>

      <div className="milestones-section">
        <h4>📍 Your Learning Milestones</h4>
        <div className="milestones">
          {prediction.milestones.map((milestone, i) => (
            <div key={i} className="milestone-card">
              <div className="milestone-marker">
                <span className="milestone-number">{i + 1}</span>
                <div className="milestone-line"></div>
              </div>
              <div className="milestone-content">
                <div className="milestone-header">
                  <h5>{milestone.name}</h5>
                  <span className="milestone-weeks">Week {milestone.weeks}</span>
                </div>
                <p>{milestone.description}</p>
                <div className="milestone-progress">
                  <div className="progress-bar">
                    <div className="progress-fill" style={{ width: `${milestone.percentage}%` }}></div>
                  </div>
                  <span className="progress-text">{milestone.percentage}%</span>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>

      <div className="insights-grid">
        <div className="insight-card">
          <h4>📈 Market Insights</h4>
          <div className="market-stats">
            <div className="market-stat">
              <span className="stat-label">Demand</span>
              <span className="stat-value demand-high">{prediction.marketInsights.demand}</span>
            </div>
            <div className="market-stat">
              <span className="stat-label">Growth</span>
              <span className="stat-value">{prediction.marketInsights.growth}</span>
            </div>
            <div className="market-stat">
              <span className="stat-label">Competition</span>
              <span className="stat-value">{prediction.marketInsights.competition}</span>
            </div>
          </div>
        </div>

        <div className="insight-card">
          <h4>💰 Salary Projections</h4>
          <div className="salary-tiers">
            <div className="salary-tier entry"><span className="tier-label">Entry</span><span className="tier-salary">{formatCurrency(prediction.salaryProjection.entry)}</span></div>
            <div className="salary-tier mid"><span className="tier-label">Mid</span><span className="tier-salary">{formatCurrency(prediction.salaryProjection.mid)}</span></div>
            <div className="salary-tier senior"><span className="tier-label">Senior</span><span className="tier-salary">{formatCurrency(prediction.salaryProjection.senior)}</span></div>
          </div>
        </div>
      </div>

      <div className="factors-section">
        <div className="factors-column">
          <h4>✅ Speed Up Factors</h4>
          {prediction.speedUpFactors.length > 0 ? (
            <ul className="factors-list speed-up">
              {prediction.speedUpFactors.map((factor, i) => (<li key={i}><span className="check">✓</span> {factor}</li>))}
            </ul>
          ) : <p className="no-factors">Add more projects and find a mentor!</p>}
        </div>
        <div className="factors-column">
          <h4>⚠️ Slow Down Factors</h4>
          {prediction.slowDownFactors.length > 0 ? (
            <ul className="factors-list slow-down">
              {prediction.slowDownFactors.map((factor, i) => (<li key={i}><span className="warning">!</span> {factor}</li>))}
            </ul>
          ) : <p className="no-factors success">Great! No major slowdowns.</p>}
        </div>
      </div>
    </div>
  );
}

function ComparisonCard({ title, prediction, formatCurrency, isImproved }) {
  return (
    <div className={`comparison-card ${isImproved ? 'improved' : ''}`}>
      <h4>{title}</h4>
      <div className="comparison-stats">
        <div className="comp-stat"><span className="comp-label">Timeline</span><span className="comp-value">{prediction.monthsToCompletion} months</span></div>
        <div className="comp-stat"><span className="comp-label">Weekly Hours</span><span className="comp-value">{prediction.weeklyHours}h/week</span></div>
        <div className="comp-stat"><span className="comp-label">Total Hours</span><span className="comp-value">{prediction.totalHours}h</span></div>
      </div>
    </div>
  );
}

export default Prediction;
