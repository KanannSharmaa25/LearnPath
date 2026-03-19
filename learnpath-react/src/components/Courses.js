import React, { useState } from 'react';
import { AppContext } from '../App';
import './Courses.css';

function Courses() {
  const { setStep, userProfile, enrolledCourses, setEnrolledCourses } = React.useContext(AppContext);
  const goal = userProfile.goal || '';
  const [filter, setFilter] = useState('all');
  const [showEnrolled, setShowEnrolled] = useState(false);

  const allCourses = [
    {
      title: "Complete Python Developer",
      provider: "Zero to Mastery",
      duration: "30+ hours",
      level: "Beginner",
      price: "$$",
      rating: 4.8,
      icon: "🐍",
      category: "backend",
      tags: ["Python", "Backend", "Projects"],
      description: "Master Python from zero to hero. Build 12+ projects including web apps, APIs, and automation scripts.",
      skills: ["Python", "Django", "Flask", "APIs"]
    },
    {
      title: "The Web Developer Bootcamp",
      provider: "Colt Steele",
      duration: "60+ hours",
      level: "Beginner",
      price: "$$",
      rating: 4.7,
      icon: "🌐",
      category: "frontend",
      tags: ["HTML", "CSS", "JavaScript", "Node.js"],
      description: "The only course you need to learn web development. Covers frontend and backend with real projects.",
      skills: ["HTML", "CSS", "JavaScript", "Node.js", "MongoDB"]
    },
    {
      title: "Machine Learning A-Z",
      provider: "Kirill Eremenko",
      duration: "44+ hours",
      level: "Intermediate",
      price: "$$$",
      rating: 4.5,
      icon: "🤖",
      category: "data",
      tags: ["ML", "Data Science", "Python"],
      description: "Learn to create Machine Learning algorithms in Python and R from industry experts.",
      skills: ["Python", "R", "ML Algorithms", "Data Visualization"]
    },
    {
      title: "Docker & Kubernetes",
      provider: "Bret Fisher",
      duration: "25+ hours",
      level: "Intermediate",
      price: "$$",
      rating: 4.8,
      icon: "📦",
      category: "devops",
      tags: ["Docker", "Kubernetes", "DevOps"],
      description: "Master containerization with Docker and orchestration with Kubernetes for modern deployment.",
      skills: ["Docker", "Kubernetes", "Docker Compose", "Helm"]
    },
    {
      title: "Algorithms & Data Structures",
      provider: "Stephen Grider",
      duration: "20+ hours",
      level: "Intermediate",
      price: "$$",
      rating: 4.6,
      icon: "🏗️",
      category: "programming",
      tags: ["Algorithms", "Interviews", "Problem Solving"],
      description: "Ace technical interviews with hands-on practice on common data structures and algorithms.",
      skills: ["Big O", "Arrays", "Trees", "Graphs", "Dynamic Programming"]
    },
    {
      title: "React - The Complete Guide",
      provider: "Academind",
      duration: "50+ hours",
      level: "Intermediate",
      price: "$$",
      rating: 4.7,
      icon: "⚛️",
      category: "frontend",
      tags: ["React", "JavaScript", "Frontend"],
      description: "Dive deep into React 18 with hooks, Redux, React Router, and Next.js framework.",
      skills: ["React", "Redux", "Hooks", "Next.js", "TypeScript"]
    },
    {
      title: "SQL for Data Science",
      provider: "Mosh Hamedani",
      duration: "8+ hours",
      level: "Beginner",
      price: "$",
      rating: 4.5,
      icon: "🗄️",
      category: "data",
      tags: ["SQL", "Databases", "Data Science"],
      description: "Master SQL for data analysis with hands-on exercises and real-world datasets.",
      skills: ["SQL", "PostgreSQL", "MySQL", "Data Analysis"]
    },
    {
      title: "AWS Certified Developer",
      provider: "Stephane Maarek",
      duration: "35+ hours",
      level: "Advanced",
      price: "$$",
      rating: 4.7,
      icon: "☁️",
      category: "devops",
      tags: ["AWS", "Cloud", "Certification"],
      description: "Prepare for AWS Developer Associate certification with hands-on labs and practice exams.",
      skills: ["AWS", "Lambda", "DynamoDB", "S3", "CloudFormation"]
    },
    {
      title: "TypeScript Complete Guide",
      provider: "Maximilian Schwarzmüller",
      duration: "25+ hours",
      level: "Intermediate",
      price: "$$",
      rating: 4.8,
      icon: "📘",
      category: "frontend",
      tags: ["TypeScript", "JavaScript", "Frontend"],
      description: "Master TypeScript with real-world projects and advanced type system features.",
      skills: ["TypeScript", "React", "Node.js", "Advanced Types"]
    },
    {
      title: "Node.js Backend Development",
      provider: "Andrew Mead",
      duration: "40+ hours",
      level: "Intermediate",
      price: "$$",
      rating: 4.6,
      icon: "🟢",
      category: "backend",
      tags: ["Node.js", "Backend", "Express"],
      description: "Build production-ready APIs and backends with Node.js, Express, and MongoDB.",
      skills: ["Node.js", "Express", "MongoDB", "REST APIs", "Authentication"]
    },
    {
      title: "Deep Learning Specialization",
      provider: "Andrew Ng",
      duration: "3 months",
      level: "Advanced",
      price: "$$$",
      rating: 4.9,
      icon: "🧠",
      category: "data",
      tags: ["Deep Learning", "AI", "Neural Networks"],
      description: "Master deep learning fundamentals from the pioneer of AI education.",
      skills: ["Neural Networks", "CNN", "RNN", "Transformers", "TensorFlow"]
    },
    {
      title: "Cybersecurity Fundamentals",
      provider: "IBM",
      duration: "20+ hours",
      level: "Beginner",
      price: "$",
      rating: 4.6,
      icon: "🔒",
      category: "security",
      tags: ["Security", "Ethical Hacking", "Networking"],
      description: "Learn cybersecurity basics, threat detection, and security best practices.",
      skills: ["Network Security", "Penetration Testing", "SIEM", "Firewalls"]
    },
    {
      title: "Git & GitHub Complete Guide",
      provider: "Academind",
      duration: "6+ hours",
      level: "Beginner",
      price: "$",
      rating: 4.7,
      icon: "🔀",
      category: "devops",
      tags: ["Git", "GitHub", "Version Control"],
      description: "Master version control with Git and GitHub for professional development workflows.",
      skills: ["Git", "GitHub", "Branching", "Merging", "CI/CD"]
    },
    {
      title: "Flutter & Dart Complete",
      provider: "Dr. Angela Yu",
      duration: "45+ hours",
      level: "Intermediate",
      price: "$$",
      rating: 4.8,
      icon: "📱",
      category: "mobile",
      tags: ["Flutter", "Dart", "Mobile"],
      description: "Build iOS and Android apps with a single codebase using Flutter framework.",
      skills: ["Flutter", "Dart", "Firebase", "State Management"]
    },
    {
      title: "React Native Complete",
      provider: "Stephen Grider",
      duration: "25+ hours",
      level: "Intermediate",
      price: "$$",
      rating: 4.5,
      icon: "📲",
      category: "mobile",
      tags: ["React Native", "JavaScript", "Mobile"],
      description: "Build cross-platform mobile apps with React Native and JavaScript.",
      skills: ["React Native", "Redux", "Navigation", "APIs", "Deployment"]
    },
    {
      title: "GraphQL Bootcamp",
      provider: "Stephen Grider",
      duration: "12+ hours",
      level: "Intermediate",
      price: "$$",
      rating: 4.6,
      icon: "🔗",
      category: "backend",
      tags: ["GraphQL", "Apollo", "Backend"],
      description: "Master GraphQL for building efficient and flexible APIs.",
      skills: ["GraphQL", "Apollo", "Node.js", "React", "Schema Design"]
    },
    {
      title: "UI/UX Design Masterclass",
      provider: "Gary Simon",
      duration: "30+ hours",
      level: "Beginner",
      price: "$$",
      rating: 4.7,
      icon: "🎨",
      category: "design",
      tags: ["UI", "UX", "Figma", "Design"],
      description: "Learn modern UI/UX design from scratch with Figma and design principles.",
      skills: ["Figma", "Prototyping", "User Research", "Design Systems"]
    },
    {
      title: "MongoDB Complete Guide",
      provider: "Maximilian Schwarzmüller",
      duration: "15+ hours",
      level: "Intermediate",
      price: "$$",
      rating: 4.6,
      icon: "🍃",
      category: "backend",
      tags: ["MongoDB", "NoSQL", "Backend"],
      description: "Master MongoDB for building modern database-driven applications.",
      skills: ["MongoDB", "Aggregation", "Indexing", "Mongoose"]
    },
    {
      title: "PostgreSQL Mastery",
      provider: "Brian Wakham",
      duration: "18+ hours",
      level: "Intermediate",
      price: "$$",
      rating: 4.7,
      icon: "🐘",
      category: "data",
      tags: ["PostgreSQL", "SQL", "Databases"],
      description: "Advanced PostgreSQL for data professionals and backend developers.",
      skills: ["PostgreSQL", "Advanced SQL", "Performance", "Backup"]
    },
    {
      title: "Kubernetes for Developers",
      provider: "William Boyd",
      duration: "22+ hours",
      level: "Advanced",
      price: "$$",
      rating: 4.8,
      icon: "☸️",
      category: "devops",
      tags: ["Kubernetes", "Cloud", "DevOps"],
      description: "Deploy, scale, and manage containerized applications with Kubernetes.",
      skills: ["Kubernetes", "Helm", "Ingress", "Services", "Monitoring"]
    },
    {
      title: "Vue.js Complete Guide",
      provider: "Maximilian Schwarzmüller",
      duration: "35+ hours",
      level: "Intermediate",
      price: "$$",
      rating: 4.7,
      icon: "💚",
      category: "frontend",
      tags: ["Vue.js", "JavaScript", "Frontend"],
      description: "Build modern web apps with Vue.js 3, Composition API, and Nuxt.js.",
      skills: ["Vue.js", "Vuex", "Vue Router", "Nuxt.js", "Composition API"]
    },
    {
      title: "Data Visualization with Python",
      provider: "Jose Portilla",
      duration: "16+ hours",
      level: "Intermediate",
      price: "$$",
      rating: 4.6,
      icon: "📊",
      category: "data",
      tags: ["Python", "Visualization", "Data Science"],
      description: "Create stunning visualizations with Matplotlib, Seaborn, and Plotly.",
      skills: ["Matplotlib", "Seaborn", "Plotly", "Pandas", "Tableau"]
    },
    {
      title: "Linux Administration",
      provider: "Jason Cannon",
      duration: "20+ hours",
      level: "Beginner",
      price: "$",
      rating: 4.7,
      icon: "🐧",
      category: "devops",
      tags: ["Linux", "Server", "DevOps"],
      description: "Master Linux command line and system administration basics.",
      skills: ["Linux", "Bash", "Shell Scripting", "SSH", "Systemd"]
    },
    {
      title: "Go Programming Language",
      provider: "Todd McLeod",
      duration: "30+ hours",
      level: "Intermediate",
      price: "$$",
      rating: 4.6,
      icon: "🔵",
      category: "backend",
      tags: ["Go", "Backend", "Concurrency"],
      description: "Learn Go programming for building fast, reliable, and efficient software.",
      skills: ["Go", "Goroutines", "Channels", "Web Services", "Testing"]
    },
  ];

  const categories = [
    { id: 'all', label: 'All Courses', icon: '📚' },
    { id: 'frontend', label: 'Frontend', icon: '🎨' },
    { id: 'backend', label: 'Backend', icon: '⚙️' },
    { id: 'data', label: 'Data & ML', icon: '📊' },
    { id: 'devops', label: 'DevOps', icon: '🔄' },
    { id: 'mobile', label: 'Mobile', icon: '📱' },
    { id: 'security', label: 'Security', icon: '🔒' },
    { id: 'design', label: 'Design', icon: '✨' },
  ];

  const toggleEnroll = (courseTitle) => {
    if (enrolledCourses.includes(courseTitle)) {
      setEnrolledCourses(enrolledCourses.filter(c => c !== courseTitle));
    } else {
      setEnrolledCourses([...enrolledCourses, courseTitle]);
    }
  };

  const isEnrolled = (courseTitle) => enrolledCourses.includes(courseTitle);

  let filteredCourses = allCourses;
  if (filter !== 'all') {
    filteredCourses = allCourses.filter(c => c.category === filter);
  } else if (goal.toLowerCase().includes('web') || goal.toLowerCase().includes('project')) {
    filteredCourses = allCourses.filter(c => c.tags.some(t => ["HTML", "CSS", "JavaScript", "React", "Frontend", "Vue.js"].includes(t)));
  } else if (goal.toLowerCase().includes('data') || goal.toLowerCase().includes('ai') || goal.toLowerCase().includes('ml')) {
    filteredCourses = allCourses.filter(c => c.tags.some(t => ["ML", "Data Science", "SQL", "Python", "Deep Learning", "Visualization"].includes(t)));
  } else if (goal.toLowerCase().includes('cloud') || goal.toLowerCase().includes('devops')) {
    filteredCourses = allCourses.filter(c => c.tags.some(t => ["Docker", "Kubernetes", "AWS", "Cloud", "Linux", "Git"].includes(t)));
  }

  const enrolledCourseDetails = allCourses.filter(c => enrolledCourses.includes(c.title));

  return (
    <div className="courses-page">
      <h2>📚 Curated Courses</h2>
      
      <div className="courses-header">
        <div className="category-tabs">
          {categories.map(cat => (
            <button
              key={cat.id}
              className={`category-tab ${filter === cat.id ? 'active' : ''}`}
              onClick={() => { setFilter(cat.id); setShowEnrolled(false); }}
            >
              <span>{cat.icon}</span>
              <span>{cat.label}</span>
            </button>
          ))}
        </div>
        
        <button 
          className={`enrolled-toggle ${showEnrolled ? 'active' : ''}`}
          onClick={() => setShowEnrolled(!showEnrolled)}
        >
          📋 My Enrollments ({enrolledCourses.length})
        </button>
      </div>

      {showEnrolled ? (
        <div>
          {enrolledCourseDetails.length > 0 ? (
            <>
              <p style={{ marginBottom: '24px' }}>You have enrolled in {enrolledCourseDetails.length} course(s)</p>
              <div className="grid-2">
                {enrolledCourseDetails.map((course, i) => (
                  <CourseCard 
                    key={i} 
                    course={course} 
                    enrolled={true}
                    onEnroll={() => toggleEnroll(course.title)}
                  />
                ))}
              </div>
            </>
          ) : (
            <div className="empty-state">
              <span style={{ fontSize: '64px' }}>📚</span>
              <h3>No Enrollments Yet</h3>
              <p>Browse courses and click "Enroll" to add them to your learning plan.</p>
              <button className="btn" onClick={() => setShowEnrolled(false)}>Browse Courses</button>
            </div>
          )}
        </div>
      ) : (
        <>
          <p style={{ marginBottom: '24px', color: '#6b7280' }}>
            Showing {filteredCourses.length} courses 
            {filter === 'all' && goal && ` recommended for your goal: ${goal}`}
          </p>
          <div className="grid-2">
            {filteredCourses.map((course, i) => (
              <CourseCard 
                key={i} 
                course={course} 
                enrolled={isEnrolled(course.title)}
                onEnroll={() => toggleEnroll(course.title)}
              />
            ))}
          </div>
        </>
      )}

      <div style={{ marginTop: '32px', display: 'flex', gap: '12px' }}>
        <button className="btn btn-secondary" onClick={() => setStep(4)}>← Learning Path</button>
        <button className="btn" onClick={() => setStep(6)}>🏠 Dashboard</button>
      </div>
    </div>
  );
}

function CourseCard({ course, enrolled, onEnroll }) {
  const [expanded, setExpanded] = useState(false);

  return (
    <div className={`course-card ${enrolled ? 'enrolled' : ''}`}>
      <div className="course-header">
        <span style={{ fontSize: '36px' }}>{course.icon}</span>
        <div className="course-meta">
          <h4>{course.title}</h4>
          <span className="provider">{course.provider}</span>
        </div>
        {enrolled && <span className="enrolled-badge">✓ Enrolled</span>}
      </div>
      
      <p className="course-description">{course.description}</p>
      
      <div className="course-stats">
        <span className="stat">⏱️ {course.duration}</span>
        <span className="stat">📊 {course.level}</span>
        <span className="stat">💰 {course.price}</span>
        <span className="stat">⭐ {course.rating}</span>
      </div>
      
      <div className="course-skills">
        <span className="skills-label">Skills you'll gain:</span>
        <div className="skills-list">
          {course.skills.slice(0, expanded ? undefined : 4).map((skill, i) => (
            <span key={i} className="skill-tag">{skill}</span>
          ))}
          {course.skills.length > 4 && (
            <button className="expand-btn" onClick={() => setExpanded(!expanded)}>
              {expanded ? 'Show less' : `+${course.skills.length - 4} more`}
            </button>
          )}
        </div>
      </div>
      
      <div className="course-tags">
        {course.tags.map((tag, j) => (
          <span key={j} className="tag">{tag}</span>
        ))}
      </div>
      
      <button 
        className={`enroll-btn ${enrolled ? 'enrolled' : ''}`}
        onClick={onEnroll}
      >
        {enrolled ? (
          <>
            <span>✓ Enrolled</span>
            <span className="remove-text">Click to unenroll</span>
          </>
        ) : (
          <>
            <span>📚 Enroll in Course</span>
          </>
        )}
      </button>
    </div>
  );
}

export default Courses;
