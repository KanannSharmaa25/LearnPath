import React, { useState, useRef, useEffect } from 'react';
import { AppContext } from '../App';
import './AICoach.css';

function AICoach() {
  const { userProfile, chatHistory, setChatHistory, learningPath, quizBatchScores, enrolledCourses } = React.useContext(AppContext);
  const [input, setInput] = useState('');
  const [isTyping, setIsTyping] = useState(false);
  const chatEndRef = useRef(null);
  const goal = userProfile.goal || '';
  const hours = userProfile.hours || 2;
  const experience = userProfile.experience || 0;

  const knowledgeBase = {
    web: {
      topics: ['HTML', 'CSS', 'JavaScript', 'React', 'Vue.js', 'Node.js', 'TypeScript', 'Next.js'],
      advice: `For web development, focus on these core areas:

**Frontend Foundation:**
- HTML5 semantic structure
- CSS3 (Flexbox, Grid, animations)
- JavaScript ES6+ fundamentals

**Framework Mastery:**
- Pick React or Vue.js and master it
- Learn state management (Redux, Vuex)
- Understand component lifecycle

**Backend Essentials:**
- Node.js or Python
- REST/GraphQL APIs
- Database basics (SQL + NoSQL)`
    },
    data: {
      topics: ['Python', 'SQL', 'Pandas', 'NumPy', 'Machine Learning', 'Visualization', 'Statistics'],
      advice: `For data science, here's your roadmap:

**Math Foundation:**
- Linear algebra basics
- Statistics & probability
- Calculus fundamentals

**Programming:**
- Python (focus on data libraries)
- SQL for data querying

**Core Skills:**
- Pandas for data manipulation
- NumPy for numerical computing
- Matplotlib/Seaborn for visualization

**ML/AI:**
- Scikit-learn for ML basics
- TensorFlow or PyTorch`
    },
    devops: {
      topics: ['Linux', 'Docker', 'Kubernetes', 'CI/CD', 'Cloud', 'Git'],
      advice: `For DevOps/Cloud, build these skills:

**Foundation:**
- Linux administration
- Shell scripting (Bash)
- Git version control

**Containerization:**
- Docker fundamentals
- Docker Compose

**Orchestration:**
- Kubernetes basics
- Helm charts

**Cloud Platforms:**
- AWS or GCP or Azure`
    },
    mobile: {
      topics: ['React Native', 'Flutter', 'iOS', 'Android', 'Firebase'],
      advice: `For mobile development:

**Cross-Platform (Recommended):**
- React Native or Flutter
- JavaScript/Dart fundamentals

**Key Skills:**
- State management
- Navigation
- API integration

**Backend Integration:**
- Firebase
- REST APIs`
    }
  };

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

  const generateResponse = (question) => {
    const q = question.toLowerCase();
    const ctx = getContext();
    
    if (q.includes('motivation') || q.includes('overwhelm') || q.includes('burnout') || q.includes('tired')) {
      const tips = [
        "Take a step back - learning is a marathon, not a sprint!",
        "Try the Pomodoro technique: 25 min focus, 5 min break.",
        "Celebrate small wins - every completed topic is progress!",
        "Connect with others on the same journey.",
        "Remember why you started. Your goal is achievable!",
        "A bad day of learning is still better than no learning."
      ];
      return `Feeling overwhelmed is completely normal! Here's what's helped many learners:

**Immediate Actions:**
- Take a 10-minute walk outside
- Review what you've already learned (you'll be surprised!)
- Break your current task into smaller pieces

**Long-term Strategy:**
- ${tips.slice(0, 3).join('\n- ')}

**Remember:**
You have ${hours} hours daily - that's ${hours * 30} hours monthly! Consistency beats intensity. ${ctx.pathTopic ? `Your next topic: ${ctx.pathTopic}` : ''}`;
    }

    if (q.includes('schedule') || q.includes('plan') || q.includes('organize') || q.includes('structure') || q.includes('daily')) {
      const schedule = hours < 2 ? `
**Limited Time (${hours}h/day):**
- 10 min: Review previous material
- ${Math.floor(hours * 60 * 0.7)} min: Learn new concepts
- ${Math.floor(hours * 60 * 0.2)} min: Practice exercises
- 10 min: Take notes for tomorrow` : hours < 4 ? `
**Moderate Time (${hours}h/day):**
- 15 min: Morning review
- ${Math.floor(hours * 60 * 0.5)} min: Deep focus learning
- 30 min: Project work
- ${Math.floor(hours * 60 * 0.15)} min: Review & reflect
- 15 min: Preview tomorrow` : `
**Intensive Schedule (${hours}h/day):**
- Rotate between: Theory → Practice → Projects
- Take a 10-min break every 90 minutes
- Include light review sessions
- Dedicate 1 day/week for projects only`;
      
      return `Here's an optimal schedule for ${hours} hours daily:

${schedule}

**Pro Tips:**
- Study hardest topics when you're most alert
- Learn theory in the morning, practice in the afternoon
- Never skip the review step - it's crucial for retention!`;
    }

    if (q.includes('improve') || q.includes('progress') || q.includes('better') || q.includes('faster')) {
      let response = `Based on your current progress:\n`;
      
      if (ctx.quizScores.length > 0) {
        response += `\n**Your Strengths (${ctx.strongAreas.length} topics):**\n`;
        ctx.strongAreas.forEach(area => response += `✓ ${area.replace(/_/g, ' ')}\n`);
        
        if (ctx.weakAreas.length > 0) {
          response += `\n**Focus Areas (${ctx.weakAreas.length} topics):**\n`;
          ctx.weakAreas.forEach(area => response += `⚠ ${area.replace(/_/g, ' ')} - needs more practice\n`);
        }
      } else {
        response += `\n- Complete quizzes to get personalized improvement tips!\n`;
      }
      
      response += `\n**General Improvement Tips:**
- Teach others (pretend you're explaining to a beginner)
- Build projects that challenge you
- Review mistakes, not just successes
- Space out your learning (don't cram!)`;
      
      return response;
    }

    if (q.includes('project') || q.includes('build') || q.includes('portfolio')) {
      let response = `Great question! Projects are the best way to learn.\n\n`;
      
      if (goal.toLowerCase().includes('web') || goal.toLowerCase().includes('project')) {
        response += knowledgeBase.web.advice;
      } else if (goal.toLowerCase().includes('data') || goal.toLowerCase().includes('ai') || goal.toLowerCase().includes('ml')) {
        response += knowledgeBase.data.advice;
      } else if (goal.toLowerCase().includes('cloud') || goal.toLowerCase().includes('devops')) {
        response += knowledgeBase.devops.advice;
      } else if (goal.toLowerCase().includes('mobile')) {
        response += knowledgeBase.mobile.advice;
      } else {
        response += `**Beginner Projects:**
1. Todo list app
2. Quiz/trivia game
3. Weather app
4. Personal portfolio site

**Intermediate Projects:**
1. Blog with CMS
2. E-commerce basic store
3. Social media dashboard
4. Recipe manager

**Key Tips:**
- Don't copy tutorials blindly
- Add your own features
- Deploy everything
- Write about your process`;
      }
      
      return response;
    }

    if (q.includes('quiz') || q.includes('test') || q.includes('assess')) {
      if (ctx.quizScores.length > 0) {
        const avgScore = Math.round(
          ctx.quizScores.reduce((acc, [_, data]) => acc + data.score, 0) / ctx.quizScores.length
        );
        return `You've completed ${ctx.quizScores.length} topic quizzes!

**Your Average Score:** ${avgScore}%

${ctx.weakAreas.length > 0 ? `**Areas to Review:**\n${ctx.weakAreas.map(a => `- ${a.replace(/_/g, ' ')}`).join('\n')}\n` : ''}

**Recommendation:**
${avgScore >= 80 ? 'Great job! You have a solid foundation. Move on to more advanced topics or start building projects.' : avgScore >= 60 ? 'Good progress! Focus on weak areas, then continue building.' : 'Keep studying the fundamentals before moving forward. Practice more problems in these areas.'}

Want me to suggest specific topics for your next quiz?`;
      }
      return `Quizzes help identify what you know and what needs more work!

**Tips:**
- Take quizzes after studying each topic
- Review explanations for wrong answers
- Retake quizzes after reviewing
- Don't stress about perfect scores - focus on learning!`;
    }

    if (q.includes('python')) {
      return `Python is excellent for beginners! Here's your roadmap:

**Week 1-2: Basics**
- Variables, data types
- Control flow (if/else, loops)
- Functions

**Week 3-4: Intermediate**
- Lists, dictionaries, sets
- File handling
- Error handling

**Week 5-6: Advanced**
- OOP concepts
- Modules and packages
- List comprehensions

**Week 7+: Projects**
- Build a calculator
- Create a web scraper
- Make a simple game

**Resources:** Official docs, Automate the Boring Stuff, Python Crash Course`;
    }

    if (q.includes('javascript') || q.includes('js')) {
      return `JavaScript is essential for web development!

**Core Concepts:**
- Variables (let, const, var)
- Functions and arrow functions
- Arrays and objects
- DOM manipulation

**ES6+ Features:**
- Template literals
- Destructuring
- Spread operator
- Async/await

**Practice:**
- Build an interactive form
- Create a weather app
- Make a to-do list

**Tip:** Master vanilla JS before frameworks!`;
    }

    if (q.includes('react') || q.includes('vue') || q.includes('angular') || q.includes('framework')) {
      const framework = q.includes('react') ? 'React' : q.includes('vue') ? 'Vue.js' : 'Angular';
      return `Learning ${framework}? Here's what to focus on:

**Basics:**
- Components
- Props and state
- Event handling

**Intermediate:**
- Hooks (useState, useEffect)
- Context API
- Routing

**Advanced:**
- State management (Redux/Zustand)
- Performance optimization
- Testing

**Projects:**
1. Blog app
2. E-commerce cart
3. Social media dashboard

**Tip:** Build real projects to solidify your understanding!`;
    }

    if (q.includes('interview') || q.includes('job') || q.includes('career') || q.includes('hire')) {
      return `Preparing for tech roles? Here's your checklist:

**For All Roles:**
- Data structures & algorithms basics
- Problem-solving practice
- Project portfolio
- Behavioral questions

**Web Developer:**
- Build 3-5 impressive projects
- Know HTML/CSS/JS deeply
- Understand HTTP, APIs, responsive design

**Data/ML:**
- Statistics fundamentals
- SQL and Python
- ML algorithms intuition
- Portfolio projects

**DevOps:**
- Docker, Kubernetes
- CI/CD pipelines
- Cloud platforms basics

**Interview Tips:**
- Explain your thought process
- Practice out loud
- Review your projects deeply
- Prepare 3-5 stories for behaviors`;
    }

    if (q.includes('break') || q.includes('rest') || q.includes('wellness') || q.includes('health')) {
      return `Taking breaks is essential for learning! 🧠

**The Science:**
- Brain consolidates learning during rest
- Short breaks improve focus
- Sleep is crucial for memory

**Recommended Schedule:**
- 25 min work + 5 min break (Pomodoro)
- Longer break every 2-3 hours
- 7-8 hours sleep daily

**Break Activities:**
- Walk outside
- Stretch or exercise
- Listen to music
- Nap (15-20 min max)

**Red Flags:**
- headaches
- Eye strain
- Feeling exhausted
- Loss of motivation

Take care of yourself! Learning is a journey, not a race.`;
    }

    if (q.includes('course') || q.includes('enroll') || q.includes('resource') || q.includes('learn')) {
      const enrolled = enrolledCourses.length;
      return enrolled > 0 
        ? `You have ${enrolled} course(s) enrolled!\n\n**Your Enrolled Courses:**\n${enrolledCourses.map(c => `- ${c}`).join('\n')}\n\n**Tips:**
- Focus on one course at a time
- Take notes while watching
- Code along, don't just watch
- Complete all exercises

Need help deciding which to start with?`
        : `Looking for learning resources? Here's my recommendation:

**Structured Courses:**
- Udemy (sales often)
- Coursera/EdX
- freeCodeCamp
- The Odin Project (free!)

**Practice Platforms:**
- LeetCode (algorithms)
- freeCodeCamp challenges
- Project Euler

**Documentation:**
- Official docs are your best friend
- MDN for web
- Read the actual source code!

Start with one course, complete it, then move to the next!`;
    }

    if (q.includes('error') || q.includes('bug') || q.includes('stuck') || q.includes('debug')) {
      return `Everyone gets stuck! Here's how to debug:

**Step 1: Read the Error**
- Read it completely
- Identify the file and line number

**Step 2: Google Smart**
- Paste the exact error message
- Add your programming language
- Check Stack Overflow answers

**Step 3: Debug Techniques**
- console.log() everything
- Use a debugger
- Simplify the problem
- Rubber duck debugging

**Step 4: Ask for Help**
- Describe what you expected
- Show what happened
- Share your code (not screenshots!)

**Remember:**
Asking questions is a skill, not weakness!`;
    }

    if (q.includes('time') || q.includes('how long') || q.includes('weeks') || q.includes('months')) {
      const baseTime = experience < 1 ? '6-12 months' : experience < 3 ? '3-6 months' : '1-3 months';
      return `Time to ${goal || 'professional level'} depends on:

**Your Background:** ${experience} years
**Daily Commitment:** ${hours} hours

**Estimated Timeline:** ${baseTime}

**Factors That Speed Up Learning:**
✓ Building projects daily
✓ Teaching others
✓ Code reviews
✓ Consistent practice

**Factors That Slow You Down:**
✗ Tutorial hell (watching without doing)
✗ Skipping fundamentals
✗ Long gaps between study sessions
✗ Perfectionism

Focus on progress, not perfection!`;
    }

    if (q.includes('beginner') || q.includes('start') || q.includes('where')) {
      return `Starting your ${goal || 'tech'} journey? Here's your starting point:

**For Complete Beginners:**
1. Don't try to learn everything at once
2. Pick ONE language/stack and stick with it
3. Follow ONE course to completion
4. Build ONE project from scratch
5. Celebrate every small win!

**Daily Routine:**
- 30 min learning new concept
- 30 min practicing exercises
- 60 min building project

**Mindset:**
- You WILL feel lost at first (normal!)
- Struggle means you're learning
- Mistakes are your best teachers

You've got this! 🚀`;
    }

    if (q.includes('certificate') || q.includes('certification')) {
      return `Certifications can boost your career! Here's my advice:

**High-Value Certifications:**
- AWS/GCP/Azure Cloud
- Google Data Analytics
- AWS Developer
- Kubernetes (CKA)
- PMP (for managers)

**Tips:**
- Don't buy certs just for the badge
- Get hands-on experience first
- Use practice exams
- Don't rush - understand the concepts

**Free Alternatives:**
- freeCodeCamp certifications
- Google's learning path badges
- Coursera audit mode (still learn!)

Certifications + Projects + Skills = Job Ready!`;
    }

    if (q.includes('english') || q.includes('foreign') || q.includes('non-english')) {
      return `Great question! Here are resources by language:

**For English Learners:**
- Almost all major courses available
- YouTube tutorials
- Stack Overflow

**For Non-Native Speakers:**
- Many courses have subtitles
- Search for your language + 'programming'
- Join communities in your language
- Use translation tools when needed

**Tips:**
- Technical vocabulary takes time
- Practice reading documentation
- Watch at 0.75x speed if needed
- Don't let language stop you!`;
    }

    return `Great question! Based on your profile:

**Your Goal:** ${goal || 'Not specified'}
**Daily Time:** ${hours} hours
**Experience:** ${experience} year(s)

${ctx.pathTopic ? `**Your Next Topic:** ${ctx.pathTopic}\n` : ''}
${ctx.quizScores.length > 0 ? `**Quizzes Completed:** ${ctx.quizScores.length}\n` : ''}
${ctx.enrolledCount > 0 ? `**Courses Enrolled:** ${ctx.enrolledCount}\n` : ''}

**My Top Advice:**
1. Consistency beats intensity
2. Build projects, not just tutorials
3. Take breaks and rest well
4. Join communities and ask questions
5. Track your progress

What specific area would you like to dive deeper into?`;
  };

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
        <div className="chat-history">
          <div className="chat-header">
            <h3>Conversation</h3>
            <button className="clear-btn" onClick={clearChat}>
              🗑️ Clear Chat
            </button>
          </div>
          
          <div className="messages">
            {chatHistory.map((msg, i) => (
              <div key={i} className={`message ${msg.role}`}>
                <div className="message-avatar">
                  {msg.role === 'user' ? '👤' : '🤖'}
                </div>
                <div className="message-content">
                  <div className="message-role">
                    {msg.role === 'user' ? 'You' : 'AI Coach'}
                  </div>
                  <div className="message-text">
                    {msg.content.split('\n').map((line, j) => (
                      <div key={j}>{line}</div>
                    ))}
                  </div>
                </div>
              </div>
            ))}
            
            {isTyping && (
              <div className="message assistant typing">
                <div className="message-avatar">🤖</div>
                <div className="message-content">
                  <div className="message-role">AI Coach</div>
                  <div className="message-text typing-indicator">
                    <span></span>
                    <span></span>
                    <span></span>
                  </div>
                </div>
              </div>
            )}
            
            <div ref={chatEndRef} />
          </div>
        </div>
      )}

      <div className="coach-footer">
        <p>💡 Tip: Ask about study schedules, motivation, projects, interview prep, or any learning topic!</p>
      </div>
    </div>
  );
}

export default AICoach;
