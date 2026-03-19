import React, { useState, createContext } from 'react';
import Landing from './components/Landing';
import Sidebar from './components/Sidebar';
import Profile from './components/Profile';
import Assessment from './components/Assessment';
import Quiz from './components/Quiz';
import LearningPath from './components/LearningPath';
import Courses from './components/Courses';
import Dashboard from './components/Dashboard';
import AICoach from './components/AICoach';
import Prediction from './components/Prediction';
import LearningLog from './components/LearningLog';
import './App.css';

export const AppContext = createContext();

function App() {
  const [step, setStep] = useState(0);
  const [userProfile, setUserProfile] = useState({});
  const [quizBatchScores, setQuizBatchScores] = useState({});
  const [learningPath, setLearningPath] = useState([]);
  const [aiLearningPath, setAiLearningPath] = useState([]);
  const [userLearningPath, setUserLearningPath] = useState([]);
  const [selectedPathType, setSelectedPathType] = useState(null);
  const [dailyLogs, setDailyLogs] = useState([]);
  const [chatHistory, setChatHistory] = useState([]);
  const [assessmentAnswers, setAssessmentAnswers] = useState({});
  const [assessmentPage, setAssessmentPage] = useState(0);
  const [enrolledCourses, setEnrolledCourses] = useState([]);

  const goToStep = (newStep) => {
    setStep(newStep);
    window.scrollTo(0, 0);
  };

  const contextValue = {
    step, setStep: goToStep,
    userProfile, setUserProfile,
    quizBatchScores, setQuizBatchScores,
    learningPath, setLearningPath,
    aiLearningPath, setAiLearningPath,
    userLearningPath, setUserLearningPath,
    selectedPathType, setSelectedPathType,
    dailyLogs, setDailyLogs,
    chatHistory, setChatHistory,
    assessmentAnswers, setAssessmentAnswers,
    assessmentPage, setAssessmentPage,
    enrolledCourses, setEnrolledCourses
  };

  const renderStep = () => {
    switch(step) {
      case 0: return <Landing />;
      case 1: return <Profile />;
      case 2: return <Assessment />;
      case 3: return <Quiz />;
      case 4: return <LearningPath />;
      case 5: return <Courses />;
      case 6: return <Dashboard />;
      case 7: return <AICoach />;
      case 8: return <Prediction />;
      case 9: return <LearningLog />;
      default: return <Dashboard />;
    }
  };

  return (
    <AppContext.Provider value={contextValue}>
      <div className="app">
        {step !== 0 && <Sidebar />}
        <main className={`main-content ${step === 0 ? 'full-width' : ''}`}>
          {renderStep()}
        </main>
      </div>
    </AppContext.Provider>
  );
}

export default App;
