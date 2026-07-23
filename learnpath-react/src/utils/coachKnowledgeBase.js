// Static advice content for the AI Coach, keyed by learning track.
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

export default knowledgeBase;