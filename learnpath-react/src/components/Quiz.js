import React, { useState } from 'react';
import { AppContext } from '../App';

function Quiz() {
  const { setStep, quizBatchScores, setQuizBatchScores } = React.useContext(AppContext);
  const [selectedTopic, setSelectedTopic] = useState(null);
  const [, setCurrentBatch] = useState(0);
  const [submitted, setSubmitted] = useState(false);
  const [answers, setAnswers] = useState({});
  const [showWarning, setShowWarning] = useState(false);

  const QUIZZES = {
    programming_fundamentals: {
      title: "Programming Fundamentals",
      icon: "💻",
      description: "Variables, loops, functions, debugging",
      questions: [
        { q: "What is a variable?", opts: ["A name that stores a value", "A type of language", "A function", "A mathematical constant"] },
        { q: "What does a loop do?", opts: ["Creates an error", "Repeats code", "Stores data", "Defines a function"] },
        { q: "What is a function?", opts: ["A variable", "Reusable block of code", "A type of data", "A programming error"] },
        { q: "What is debugging?", opts: ["Writing code", "Finding and fixing errors", "Running code", "Creating variables"] },
        { q: "What is an array?", opts: ["A single value", "An ordered collection", "A function", "A type of error"] },
        { q: "What is a conditional?", opts: ["A loop", "Code based on condition", "Storing data", "A type of function"] },
        { q: "Comments in code are for:", opts: ["Execute faster", "Document and explain", "Encrypt code", "Store variables"] },
        { q: "What is refactoring?", opts: ["Deleting code", "Changing structure", "Running faster", "New features only"] },
        { q: "What is an algorithm?", opts: ["A language", "Step-by-step instructions", "Data structure", "Software bug"] },
        { q: "OOP stands for:", opts: ["Only One Process", "Object-Oriented Programming", "Open Output Program", "Ordered Operations"] },
      ],
      correct: [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    },
    problem_solving: {
      title: "Problem Solving & Logic",
      icon: "🧩",
      description: "Logical reasoning and decomposition",
      questions: [
        { q: "First step in solving a problem?", opts: ["Start coding", "Understand the problem", "Copy from internet", "Ask someone"] },
        { q: "Algorithm complexity measures:", opts: ["How hard", "Time and space needed", "Lines of code", "Language used"] },
        { q: "Breaking problems helps because:", opts: ["Wastes time", "Makes easier", "Confuses solution", "Reduces quality"] },
        { q: "Edge case handling means:", opts: ["Using desk edge", "Testing extreme inputs", "Programming error", "Type of variable"] },
        { q: "Greedy algorithm approach:", opts: ["All possibilities", "Locally optimal choice", "Random selection", "Backtracking"] },
        { q: "Pseudocode is used to:", opts: ["Avoid documentation", "Plan logic", "Test performance", "Compile it"] },
        { q: "Recursion is:", opts: ["A loop", "Function calling itself", "Data structure", "Sorting method"] },
        { q: "Big O notation is for:", opts: ["Email", "Measuring efficiency", "Math operations", "Sorting data"] },
        { q: "Heuristic approach means:", opts: ["Exact solution", "Rule-of-thumb approach", "Formal proof", "Copying code"] },
        { q: "Why write tests?", opts: ["Waste time", "Find bugs early", "Slow down development", "Required by law"] },
      ],
      correct: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    },
    data_structures: {
      title: "Data Structures",
      icon: "🏗️",
      description: "Arrays, lists, trees, graphs",
      questions: [
        { q: "Hash Map advantage:", opts: ["Always sorted", "Fast lookups", "Small memory", "Easy to visualize"] },
        { q: "Linked list is:", opts: ["List on web", "Elements connected by pointers", "Type of array", "Database structure"] },
        { q: "Stack follows:", opts: ["FIFO", "LIFO", "Random order", "Sorted order"] },
        { q: "Queue follows:", opts: ["LIFO", "FIFO", "Random", "Sorted"] },
        { q: "Tree data structure used for:", opts: ["Growing plants", "Hierarchical data", "Storing strings", "Random storage"] },
        { q: "Graph models:", opts: ["Hierarchies", "Connected entities (nodes/edges)", "Linear arrays", "Sorted lists"] },
        { q: "Priority queue retrieves:", opts: ["Random element", "Highest-priority element", "First element", "Last element"] },
        { q: "Array lookup by index is:", opts: ["O(n)", "O(1)", "O(log n)", "O(n²)"] },
        { q: "LIFO is used by:", opts: ["Queue", "Stack", "Array", "Tree"] },
        { q: "Binary search time complexity:", opts: ["O(n)", "O(1)", "O(log n)", "O(n²)"] },
      ],
      correct: [1, 1, 1, 1, 1, 1, 1, 1, 1, 2]
    },
    web_development: {
      title: "Web Development",
      icon: "🌐",
      description: "HTML, CSS, JavaScript, APIs",
      questions: [
        { q: "HTML does:", opts: ["Styles website", "Structures content", "Creates interactivity", "Stores data"] },
        { q: "CSS role:", opts: ["Structures content", "Styles and layouts", "Creates logic", "Stores databases"] },
        { q: "JavaScript used for:", opts: ["Server storage", "Client-side interactivity", "Database management", "Styling"] },
        { q: "REST API is:", opts: ["A way to take breaks", "Server-client communication", "Database type", "Styling framework"] },
        { q: "Responsive design:", opts: ["Quick loading", "Works on all devices", "Many colors", "Requires JS"] },
        { q: "DOM stands for:", opts: ["Design Object Model", "Document Object Model", "Data Object Model", "Digital Output Model"] },
        { q: "AJAX allows:", opts: ["Synchronous reloads", "Background requests", "CSS animations", "Python in browser"] },
        { q: "Accessibility means:", opts: ["Many colors", "Designing for all abilities", "Faster load", "SEO only"] },
        { q: "CDN stands for:", opts: ["Content Delivery Network", "Coding Development Network", "Central Database", "Client Data"] },
        { q: "API stands for:", opts: ["Application Programming Interface", "Automated Program", "Advanced Protocol", "Application Process"] },
      ],
      correct: [1, 1, 1, 1, 1, 1, 1, 1, 0, 0]
    },
    databases: {
      title: "Databases & SQL",
      icon: "🗄️",
      description: "SQL, NoSQL, data modeling",
      questions: [
        { q: "SQL is used for:", opts: ["Website styling", "Querying data", "Building apps", "Creating graphics"] },
        { q: "Primary key:", opts: ["First column", "Uniquely identifies row", "Password", "A type of index"] },
        { q: "Database normalization:", opts: ["Making data normal", "Reduce redundancy", "Encrypt data", "Backup data"] },
        { q: "SQL JOIN:", opts: ["Combining rows", "Creating tables", "Deleting data", "A type of error"] },
        { q: "Database index:", opts: ["Table of contents", "Structure for faster searches", "Backup method", "A type of table"] },
        { q: "ACID properties:", opts: ["Chemical element", "Transactional properties", "Indexing type", "Compression method"] },
        { q: "Denormalization:", opts: ["Reducing redundancy", "Improving read performance", "Encrypting data", "Backing up"] },
        { q: "Transaction log:", opts: ["User log", "Record of changes", "Performance metric", "A query"] },
        { q: "Foreign key:", opts: ["Key outside DB", "References primary key", "User auth key", "Encryption key"] },
        { q: "NoSQL databases best for:", opts: ["Structured data", "Unstructured data", "Large enterprises", "Offline apps"] },
      ],
      correct: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    },
    python_basics: {
      title: "Python Basics",
      icon: "🐍",
      description: "Python syntax, functions, data types",
      questions: [
        { q: "Python known for:", opts: ["Web design", "Readability and simplicity", "Gaming", "Graphics"] },
        { q: "Python virtual environment:", opts: ["Computer in cloud", "Isolated Python setup", "A game", "A type of file"] },
        { q: "pip does:", opts: ["Installs Python", "Manages packages", "Edits code", "Runs programs"] },
        { q: "Python decorator:", opts: ["Visual element", "Modifies functions", "A type of loop", "String type"] },
        { q: "List comprehension:", opts: ["Understanding lists", "Concise way to create lists", "Reading technique", "A type of loop"] },
        { q: "Python dictionary:", opts: ["Ordered sequence", "Key-value mapping", "List of functions", "A loop"] },
        { q: "Exception handling:", opts: ["Optimizing speed", "Handling errors gracefully", "Formatting strings", "Declaring variables"] },
        { q: "Python module:", opts: ["A function", "Python definitions file", "A data type", "Package manager"] },
        { q: "'self' refers to:", opts: ["The class", "Current instance", "Global variable", "A parameter"] },
        { q: "None in Python:", opts: ["Zero", "Empty string", "Null value", "False"] },
      ],
      correct: [1, 1, 1, 1, 1, 1, 1, 1, 1, 2]
    },
    cloud_computing: {
      title: "Cloud Computing",
      icon: "☁️",
      description: "AWS, Azure, cloud services",
      questions: [
        { q: "IaaS stands for:", opts: ["Internet as Service", "Infrastructure as Service", "Integration as Service", "Image as Service"] },
        { q: "SaaS stands for:", opts: ["Software as Service", "Storage as Service", "System as Service", "Server as Service"] },
        { q: "PaaS stands for:", opts: ["Platform as Service", "Programming as Service", "Process as Service", "Private as Service"] },
        { q: "Serverless computing:", opts: ["No servers exist", "Auto scaling compute", "Free computing", "Offline computing"] },
        { q: "Auto-scaling:", opts: ["Auto compilation", "Adjusting resources", "Auto-saving files", "Auto testing"] },
        { q: "VPC stands for:", opts: ["Very Private Computer", "Virtual Private Cloud", "Virtual Process", "Verified Program"] },
        { q: "Load balancing:", opts: ["Weighing components", "Distributing traffic", "Balancing code", "Measuring weight"] },
        { q: "Cloud region:", opts: ["Country border", "Geographic area with zones", "A state", "Server room"] },
        { q: "Edge computing:", opts: ["Computing at edges", "Computing with edges", "Border computing", "Side computing"] },
        { q: "Cloud migration:", opts: ["Moving to sky", "Transferring to cloud", "Cloudy weather", "Data backup"] },
      ],
      correct: [1, 0, 0, 1, 1, 0, 1, 1, 0, 1]
    },
    devops: {
      title: "DevOps & CI/CD",
      icon: "🔄",
      description: "CI/CD pipelines, Docker, Kubernetes",
      questions: [
        { q: "Docker container:", opts: ["Shipping container", "Lightweight package", "Virtual machine", "Storage unit"] },
        { q: "Dockerfile:", opts: ["Container runtime", "Script to build images", "Container registry", "Orchestration tool"] },
        { q: "Kubernetes:", opts: ["Container orchestration", "Programming language", "Database system", "Web server"] },
        { q: "Kubernetes pod:", opts: ["Storage unit", "Smallest deployable unit", "Network protocol", "Container registry"] },
        { q: "Container orchestration:", opts: ["Playing music", "Managing containers", "Building containers", "Container storage"] },
        { q: "CI/CD:", opts: ["Continuous Integration", "Code library", "Version control", "Database system"] },
        { q: "Git:", opts: ["Programming language", "Version control system", "Database", "Operating system"] },
        { q: "git merge:", opts: ["Deletes branches", "Combines changes", "Creates repo", "Uploads code"] },
        { q: "Docker image:", opts: ["Running container", "Template to create containers", "Container logs", "Network config"] },
        { q: "Container registry:", opts: ["Container storage", "Repository for images", "Container network", "Monitoring"] },
      ],
      correct: [1, 1, 0, 1, 1, 0, 1, 1, 1, 1]
    },
    javascript: {
      title: "JavaScript",
      icon: "⚡",
      description: "ES6+, async/await, DOM manipulation",
      questions: [
        { q: "let vs var:", opts: ["Same scope", "Block vs function scope", "Global vs local", "No difference"] },
        { q: "arrow function syntax:", opts: ["function =", "() =>", "->", "::"] },
        { q: "Promise represents:", opts: ["Data type", "Async operation result", "Error", "Variable"] },
        { q: "async/await:", opts: ["Error handling", "Make async code sync-looking", "Loop", "Data type"] },
        { q: "map() returns:", opts: ["Same length array", "Original array", "Number", "Object"] },
        { q: "destructuring:", opts: ["Creating objects", "Extract array/object values", "Delete values", "Sort array"] },
        { q: "spread operator (...):", opts: ["Math operation", "Expand elements", "Exception handling", "Loop"] },
        { q: "null vs undefined:", opts: ["Same thing", "Assigned vs unassigned", "Both errors", "Same type"] },
        { q: "closure:", opts: ["End of function", "Function with access to outer scope", "Loop", "Error"] },
        { q: "event loop:", opts: ["Drawing graphics", "Process events in queue", "Start program", "End loop"] },
      ],
      correct: [1, 1, 1, 1, 0, 1, 1, 1, 1, 1]
    },
    react: {
      title: "React",
      icon: "⚛️",
      description: "Components, hooks, state management",
      questions: [
        { q: "React component must:", opts: ["Return JSX", "Be class", "Have CSS", "Use jQuery"] },
        { q: "useState hook:", opts: ["HTTP requests", "Manage state", "Router", "Style"] },
        { q: "props:", opts: ["Local data", "Parent to child data", "State", "Style"] },
        { q: "useEffect:", opts: ["Render UI", "Handle side effects", "Create components", "Define routes"] },
        { q: "controlled component:", opts: ["Fast component", "State controls input", "Large component", "Memoized"] },
        { q: "React.Fragment:", opts: ["Error boundary", "Group elements without DOM node", "Component type", "Hook"] },
        { q: "useMemo:", opts: ["Fetch data", "Memoize expensive calculation", "State management", "Routing"] },
        { q: "React.memo:", opts: ["Error handling", "Prevent unnecessary re-renders", "Memory management", "Data fetching"] },
        { q: "Context API:", opts: ["Styling", "Share data across components", "Routing", "Animation"] },
        { q: "Virtual DOM:", opts: ["Actual DOM", "Lightweight copy for performance", "Browser feature", "CSS"] },
      ],
      correct: [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    },
    machine_learning: {
      title: "Machine Learning",
      icon: "🤖",
      description: "ML algorithms, neural networks, evaluation",
      questions: [
        { q: "Supervised learning:", opts: ["No labels", "With labeled data", "With images", "Unsupervised"] },
        { q: "Linear regression used for:", opts: ["Classification", "Continuous value prediction", "Clustering", "Image recognition"] },
        { q: "Overfitting:", opts: ["Model too simple", "Model memorizes training data", "Not enough data", "Good performance"] },
        { q: "Cross-validation:", opts: ["Training only", "Testing model generalization", "Data cleaning", "Feature selection"] },
        { q: "Neural network layer:", opts: ["Single neuron", "Group of neurons", "Data row", "Output"] },
        { q: "Gradient descent:", opts: ["Increase error", "Minimize error iteratively", "Static optimization", "Random guessing"] },
        { q: "CNN primarily used for:", opts: ["Text", "Images", "Audio", "Video games"] },
        { q: "Random Forest is:", opts: ["Single tree", "Ensemble of trees", "Linear model", "Neural network"] },
        { q: "Feature scaling:", opts: ["Select features", "Normalize feature ranges", "Remove features", "Create features"] },
        { q: "Bias in ML:", opts: ["Model variance", "Systematic error from assumptions", "Data size", "Training speed"] },
      ],
      correct: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    },
    data_science: {
      title: "Data Science",
      icon: "📊",
      description: "Pandas, NumPy, data analysis",
      questions: [
        { q: "Pandas DataFrame:", opts: ["Single value", "2D labeled data structure", "Plot library", "Web framework"] },
        { q: "NumPy used for:", opts: ["Web apps", "Numerical computing", "Image editing", "Database"] },
        { q: "Data cleaning:", opts: ["Build models", "Handle missing/invalid data", "Deploy models", "Write docs"] },
        { q: "EDA:", opts: ["Error handling", "Explore and understand data", "Model training", "Deployment"] },
        { q: "Matplotlib used for:", opts: ["Database", "Data visualization", "Machine learning", "Web scraping"] },
        { q: "Correlation measures:", opts: ["Model accuracy", "Relationship between variables", "Data size", "Computation speed"] },
        { q: "Feature engineering:", opts: ["Remove all features", "Create new features from data", "Delete data", "Train model"] },
        { q: "Normal distribution:", opts: ["Linear pattern", "Bell curve probability distribution", "Random noise", "Outlier"] },
        { q: "Pivot table:", opts: ["Database query", "Summarize data by categories", "Machine learning", "Data cleaning"] },
        { q: "Data normalization:", opts: ["Delete data", "Scale to similar ranges", "Add more data", "Sort data"] },
      ],
      correct: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    },
    git_github: {
      title: "Git & GitHub",
      icon: "🔀",
      description: "Version control, branches, collaboration",
      questions: [
        { q: "git clone:", opts: ["Delete repository", "Copy repository locally", "Create branch", "Push changes"] },
        { q: "git branch:", opts: ["Main code only", "Independent line of development", "Delete code", "Merge files"] },
        { q: "git checkout:", opts: ["Travel through time", "Switch branches or restore files", "Delete branch", "Push code"] },
        { q: "git pull:", opts: ["Upload local changes", "Fetch and merge remote changes", "Delete files", "Create repo"] },
        { q: "git push:", opts: ["Download changes", "Upload local commits", "Delete repository", "Create branch"] },
        { q: "Merge conflict:", opts: ["Git error", "Changes cannot be merged automatically", "Branch created", "Code works"] },
        { q: "Pull request:", opts: ["Request code deletion", "Propose changes to repository", "Download repo", "Create branch"] },
        { q: "git rebase:", opts: ["Delete commits", "Reapply commits on new base", "Merge branches", "Push code"] },
        { q: ".gitignore:", opts: ["Git documentation", "Files to ignore in version control", "Git command", "Repository"] },
        { q: "git stash:", opts: ["Delete code", "Temporarily save changes", "Create branch", "Push commits"] },
      ],
      correct: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    },
    cybersecurity: {
      title: "Cybersecurity",
      icon: "🔒",
      description: "Security principles, threats, best practices",
      questions: [
        { q: "Phishing:", opts: ["Fishing sport", "Deceptive communication to steal data", "Encryption", "Network protocol"] },
        { q: "SQL injection:", opts: ["Database backup", "Insert malicious SQL code", "Data visualization", "Network speed test"] },
        { q: "HTTPS provides:", opts: ["Faster loading", "Encrypted communication", "More features", "Better design"] },
        { q: "Two-factor authentication:", opts: ["Two passwords", "Two-step verification", "Double login", "Backup login"] },
        { q: "Encryption:", opts: ["Delete data", "Convert data to secure format", "Compress data", "Duplicate data"] },
        { q: "Firewall:", opts: ["Coding tool", "Network security barrier", "Database", "Web browser"] },
        { q: "Malware:", opts: ["Good software", "Malicious software", "Database system", "Network protocol"] },
        { q: "Zero-day vulnerability:", opts: ["Fixed bug", "Unknown exploited vulnerability", "Security update", "Password"] },
        { q: "Penetration testing:", opts: ["Load testing", "Ethical hacking to find vulnerabilities", "Unit testing", "Design review"] },
        { q: "Principle of least privilege:", opts: ["Admin access for all", "Minimum necessary access rights", "Full access", "No access"] },
      ],
      correct: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    },
    testing: {
      title: "Software Testing",
      icon: "🧪",
      description: "Unit tests, integration tests, TDD",
      questions: [
        { q: "Unit test:", opts: ["Test entire system", "Test individual components", "Test performance", "Test design"] },
        { q: "Integration test:", opts: ["Test single function", "Test component interactions", "Test design", "Test database"] },
        { q: "TDD:", opts: ["Test during deployment", "Test-driven development", "Track data", "Type definitions"] },
        { q: "Mock object:", opts: ["Real production object", "Simulated object for testing", "Deleted object", "Backup object"] },
        { q: "Assertion:", opts: ["Guess", "Verify expected condition", "Skip test", "Create test"] },
        { q: "Test coverage:", opts: ["Code comments", "Percentage of code tested", "Test speed", "Test count only"] },
        { q: "Regression test:", opts: ["New feature test", "Ensure existing features still work", "Performance test", "Security test"] },
        { q: "End-to-end test:", opts: ["Test single function", "Test complete user flow", "Test database", "Test design"] },
        { q: "CI in testing:", opts: ["Code inspection", "Run tests automatically on changes", "Manual testing", "User testing"] },
        { q: "Bug report should include:", opts: ["Just the error", "Steps to reproduce, expected/actual behavior", "Only screenshots", "Developer info"] },
      ],
      correct: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    },
    system_design: {
      title: "System Design",
      icon: "🏗️",
      description: "Architecture, scalability, APIs",
      questions: [
        { q: "Horizontal scaling:", opts: ["Add more servers", "Add CPU to server", "Add memory", "Add disk space"] },
        { q: "Vertical scaling:", opts: ["Add more machines", "Add more resources to machine", "Add network", "Add database"] },
        { q: "Load balancer:", opts: ["Balance database", "Distribute traffic across servers", "Balance code", "Load data"] },
        { q: "Caching:", opts: ["Store all data", "Store frequently accessed data", "Delete data", "Encrypt data"] },
        { q: "CDN:", opts: ["Code delivery", "Deliver content from edge servers", "Content database", "Copy data"] },
        { q: "Microservices:", opts: ["Single large application", "Small independent services", "Microscopic code", "Database service"] },
        { q: "API gateway:", opts: ["Database interface", "Single entry point for clients", "Network switch", "Code gateway"] },
        { q: "Message queue:", opts: ["Email system", "Async communication between services", "Code queue", "Data storage"] },
        { q: "Database replication:", opts: ["Delete backup", "Copy database across servers", "Database encryption", "Database migration"] },
        { q: "CAP theorem:", opts: ["Programming language", "Consistency, Availability, Partition tolerance", "Code design", "API design"] },
      ],
      correct: [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    },
    networking: {
      title: "Networking",
      icon: "🌐",
      description: "HTTP, TCP/IP, protocols",
      questions: [
        { q: "HTTP methods GET/POST:", opts: ["Same thing", "Retrieve data / Send data", "Delete / Create", "Connect / Disconnect"] },
        { q: "TCP:", opts: ["Connectionless protocol", "Connection-oriented reliable delivery", "Fast delivery", "Unreliable"] },
        { q: "IP address:", opts: ["Software", "Unique device identifier", "Network name", "Website"] },
        { q: "DNS:", opts: ["Database", "Domain name to IP translation", "Network device", "Code language"] },
        { q: "Firewall:", opts: ["Web browser", "Network security device", "Programming tool", "Database"] },
        { q: "API endpoint:", opts: ["Database", "Specific URL for API communication", "Server location", "Code function"] },
        { q: "WebSocket provides:", opts: ["One-way communication", "Bidirectional persistent connection", "File transfer", "Email"] },
        { q: "HTTP status codes 4xx:", opts: ["Success", "Client errors", "Server errors", "Redirect"] },
        { q: "Latency:", opts: ["Bandwidth", "Delay in communication", "Packet loss", "Connection type"] },
        { q: "Bandwidth:", opts: ["Delay", "Data transfer capacity", "Network type", "Connection speed"] },
      ],
      correct: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    },
    ui_ux_design: {
      title: "UI/UX Design",
      icon: "🎨",
      description: "User interface, experience, accessibility",
      questions: [
        { q: "UI design focuses on:", opts: ["Backend", "Visual elements and interactivity", "Database", "Server"] },
        { q: "UX design focuses on:", opts: ["Colors only", "Overall user experience", "Code only", "Marketing"] },
        { q: "Wireframe:", opts: ["Final design", "Basic layout sketch", "Code", "Database"] },
        { q: "Prototyping:", opts: ["Final product", "Testable preliminary version", "Documentation", "Deployment"] },
        { q: "Accessibility (a11y):", opts: ["Making money", "Designing for all abilities", "Speed optimization", "Code quality"] },
        { q: "Color contrast ratio:", opts: ["Design preference", "Text readability measure", "Image size", "Font choice"] },
        { q: "Mobile-first design:", opts: ["Desktop first", "Design for mobile first", "Ignore mobile", "Mobile only"] },
        { q: "User persona:", opts: ["Real user", "Fictional user representation", "System user", "Admin"] },
        { q: "Usability testing:", opts: ["Load testing", "Test with real users", "Security testing", "Code testing"] },
        { q: "Design system:", opts: ["Random designs", "Collection of reusable components", "Single component", "Code only"] },
      ],
      correct: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    },
    agile_scrum: {
      title: "Agile & Scrum",
      icon: "📋",
      description: "Agile methodology, sprints, ceremonies",
      questions: [
        { q: "Agile emphasizes:", opts: ["Big upfront planning", "Iterative development", "Waterfall approach", "Documentation over code"] },
        { q: "Sprint:", opts: ["Long project", "Time-boxed iteration", "Bug fix", "Meeting"] },
        { q: "Daily standup:", opts: ["Weekly meeting", "Daily brief status sync", "Sprint planning", "Retrospective"] },
        { q: "Product backlog:", opts: ["Completed work", "Prioritized list of work", "Current sprint", "Team list"] },
        { q: "Sprint planning:", opts: ["Daily meeting", "Plan sprint goals and tasks", "Code review", "Demo"] },
        { q: "Scrum roles:", opts: ["Only developers", "Product Owner, Scrum Master, Team", "Managers only", "No roles"] },
        { q: "Definition of Done:", opts: ["Feature works", "Shared criteria for completion", "Code written", "Test passing"] },
        { q: "Retrospective:", opts: ["Plan next sprint", "Reflect on past sprint", "Daily meeting", "Sprint demo"] },
        { q: "User story:", opts: ["Technical description", "User-focused requirement", "Bug report", "Code snippet"] },
        { q: "Velocity:", opts: ["Speed of development", "Story points completed per sprint", "Bug count", "Meeting hours"] },
      ],
      correct: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    },
  };

  const topics = Object.keys(QUIZZES);

  const handleAnswer = (index, answer) => {
    setAnswers({ ...answers, [index]: answer });
  };

  const submitBatch = () => {
    if (!selectedTopic) return;
    const quiz = QUIZZES[selectedTopic];
    
    const answeredCount = Object.keys(answers).length;
    if (answeredCount < quiz.questions.length) {
      setShowWarning(true);
      setTimeout(() => setShowWarning(false), 3000);
      return;
    }
    
    let correct = 0;
    for (let i = 0; i < quiz.questions.length; i++) {
      if (answers[i] === quiz.questions[i].opts[quiz.correct[i]]) {
        correct++;
      }
    }
    const score = Math.round((correct / quiz.questions.length) * 100);
    setQuizBatchScores({ ...quizBatchScores, [selectedTopic]: { correct, total: quiz.questions.length, score } });
    setSubmitted(true);
    setShowWarning(false);
  };

  const resetQuiz = () => {
    setSelectedTopic(null);
    setAnswers({});
    setSubmitted(false);
    setCurrentBatch(0);
  };

  if (selectedTopic && !submitted) {
    const quiz = QUIZZES[selectedTopic];
    const answeredCount = Object.keys(answers).length;
    return (
      <div className="quiz-page">
        <h2>{quiz.icon} {quiz.title}</h2>
        <p style={{ marginBottom: '8px' }}>Questions {1} to {quiz.questions.length}</p>
        <p style={{ marginBottom: '16px', color: '#6b7280', fontSize: '14px' }}>
          Answered: {answeredCount}/{quiz.questions.length}
        </p>

        {showWarning && (
          <div className="warning-message">
            ⚠️ Please answer all questions before submitting.
          </div>
        )}

        <div className="card">
          {quiz.questions.map((question, index) => (
            <div key={index} style={{ marginBottom: '24px' }}>
              <p style={{ fontWeight: '600', marginBottom: '12px' }}>Q{index + 1}. {question.q}</p>
              <div className="radio-group">
                {question.opts.map((opt, oIndex) => (
                  <label 
                    key={oIndex}
                    className={`radio-option ${answers[index] === opt ? 'selected' : ''}`}
                    onClick={() => handleAnswer(index, opt)}
                  >
                    {opt}
                  </label>
                ))}
              </div>
            </div>
          ))}
        </div>

        <div className="flex gap-2" style={{ marginTop: '24px' }}>
          <button className="btn btn-secondary" onClick={resetQuiz}>← Back to Topics</button>
          <button className="btn" onClick={submitBatch} style={{ marginLeft: 'auto' }}>Submit Quiz ✓</button>
        </div>
      </div>
    );
  }

  if (submitted) {
    const score = quizBatchScores[selectedTopic];
    return (
      <div className="quiz-page">
        <h2>Quiz Results</h2>
        <div className="card">
          <h3>{QUIZZES[selectedTopic].icon} {QUIZZES[selectedTopic].title}</h3>
          <p style={{ fontSize: '24px', margin: '16px 0' }}>
            <strong>{score.correct}/{score.total}</strong> correct ({score.score}%)
          </p>
          <button className="btn btn-full" onClick={resetQuiz}>Take Another Quiz</button>
        </div>
        
        <h3 style={{ marginTop: '32px' }}>Quiz Topics</h3>
        <div className="grid-3" style={{ marginTop: '16px' }}>
          {topics.map(topic => (
            <div key={topic} className="card" style={{ textAlign: 'center' }}>
              <h4>{QUIZZES[topic].icon}</h4>
              <p>{QUIZZES[topic].title}</p>
              {quizBatchScores[topic] ? (
                <p style={{ color: '#8b5cf6', fontWeight: '600' }}>{quizBatchScores[topic].score}%</p>
              ) : (
                <button className="btn" onClick={() => { setSelectedTopic(topic); setSubmitted(false); setAnswers({}); }}>
                  Start Quiz
                </button>
              )}
            </div>
          ))}
        </div>

        <button className="btn btn-secondary" style={{ marginTop: '32px' }} onClick={() => setStep(4)}>
          Generate Learning Path →
        </button>
      </div>
    );
  }

  return (
    <div className="quiz-page">
      <h2>📋 Knowledge Quiz</h2>
      <p style={{ marginBottom: '32px' }}>Test your knowledge across different topics.</p>

      <div className="grid-3">
        {topics.map(topic => (
          <div key={topic} className="card" style={{ textAlign: 'center' }}>
            <div style={{ fontSize: '48px', marginBottom: '12px' }}>{QUIZZES[topic].icon}</div>
            <h4>{QUIZZES[topic].title}</h4>
            <p style={{ fontSize: '14px', color: '#6b7280' }}>{QUIZZES[topic].description}</p>
            <p style={{ color: '#8b5cf6', fontSize: '12px' }}>{QUIZZES[topic].questions.length} questions</p>
            {quizBatchScores[topic] ? (
              <div style={{ marginTop: '12px' }}>
                <span className="alert alert-success" style={{ display: 'inline-block' }}>
                  Completed: {quizBatchScores[topic].score}%
                </span>
              </div>
            ) : (
              <button className="btn" style={{ marginTop: '12px' }} onClick={() => setSelectedTopic(topic)}>
                Start Quiz
              </button>
            )}
          </div>
        ))}
      </div>

      <button className="btn btn-secondary" style={{ marginTop: '32px' }} onClick={() => setStep(4)}>
        Skip to Learning Path →
      </button>
    </div>
  );
}

export default Quiz;
