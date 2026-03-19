# course_recommendation_engine.py
# AI-powered course recommendation system

COURSE_DATABASE = {
    "Python Programming": [
        {
            "id": "course_py_1",
            "title": "Python for Everybody",
            "platform": "Coursera",
            "instructor": "Dr. Charles Severance",
            "duration_hours": 30,
            "level": "Beginner",
            "rating": 4.8,
            "students": 2500000,
            "price": "Free with certificate",
            "url": "https://www.coursera.org/learn/python-for-everybody",
            "content": ["Basics", "Data structures", "Databases", "Web scraping"],
            "learning_style": ["Video", "Interactive", "Assignments"],
            "time_commitment": "5-7 hours/week",
            "reviews_highlight": "Great for beginners, clear explanations"
        },
        {
            "id": "course_py_2",
            "title": "Complete Python Bootcamp",
            "platform": "Udemy",
            "instructor": "Jose Portilla",
            "duration_hours": 22,
            "level": "Beginner-Intermediate",
            "rating": 4.6,
            "students": 1500000,
            "price": "$14.99",
            "url": "https://www.udemy.com/course/complete-python-bootcamp/",
            "content": ["Basics", "OOP", "Functional programming", "Web development"],
            "learning_style": ["Video", "Coding projects"],
            "time_commitment": "3-5 hours/week",
            "reviews_highlight": "Comprehensive, lots of projects"
        },
        {
            "id": "course_py_3",
            "title": "Real Python",
            "platform": "Real Python",
            "instructor": "Multiple",
            "duration_hours": 200,
            "level": "Beginner-Advanced",
            "rating": 4.9,
            "students": 500000,
            "price": "$99/month",
            "url": "https://realpython.com/",
            "content": ["Everything from basics to advanced"],
            "learning_style": ["Article", "Video", "Interactive"],
            "time_commitment": "Self-paced",
            "reviews_highlight": "Best reference material, very deep"
        },
        {
            "id": "course_py_4",
            "title": "Python Programming Masterclass",
            "platform": "Udemy",
            "instructor": "Tim Buchalka",
            "duration_hours": 40,
            "level": "Beginner",
            "rating": 4.7,
            "students": 1200000,
            "price": "$14.99",
            "url": "https://www.udemy.com/course/python-the-complete-python-developer-course/",
            "content": ["Basics", "OOP", "Modules", "Lambda functions"],
            "learning_style": ["Video", "Coding exercises"],
            "time_commitment": "5-7 hours/week",
            "reviews_highlight": "Very thorough, great for fundamentals"
        }
    ],
    
    "JavaScript & Web Development": [
        {
            "id": "course_js_1",
            "title": "The Complete JavaScript Course",
            "platform": "Udemy",
            "instructor": "Jonas Schmedtmann",
            "duration_hours": 69,
            "level": "Beginner-Advanced",
            "rating": 4.8,
            "students": 1800000,
            "price": "$14.99",
            "url": "https://www.udemy.com/course/the-complete-javascript-course-2023-from-zero-to-expert/",
            "content": ["Fundamentals", "DOM", "Async", "Projects", "Modern JS"],
            "learning_style": ["Video", "Projects", "Coding exercises"],
            "time_commitment": "10-12 hours/week",
            "reviews_highlight": "Most comprehensive JS course"
        },
        {
            "id": "course_js_2",
            "title": "JavaScript.info",
            "platform": "JavaScript.info",
            "instructor": "Community",
            "duration_hours": 80,
            "level": "Beginner-Intermediate",
            "rating": 4.9,
            "students": 1000000,
            "price": "Free",
            "url": "https://javascript.info/",
            "content": ["All JS fundamentals", "Advanced concepts"],
            "learning_style": ["Interactive", "Articles", "Tasks"],
            "time_commitment": "Self-paced",
            "reviews_highlight": "Best free JS resource, very interactive"
        },
        {
            "id": "course_js_3",
            "title": "Frontend Masters",
            "platform": "Frontend Masters",
            "instructor": "Multiple experts",
            "duration_hours": 500,
            "level": "Intermediate-Advanced",
            "rating": 4.9,
            "students": 200000,
            "price": "$39/month",
            "url": "https://frontendmasters.com/",
            "content": ["JS", "React", "Vue", "Advanced patterns"],
            "learning_style": ["Video", "Live sessions", "Code-along"],
            "time_commitment": "Self-paced",
            "reviews_highlight": "Industry experts, very high quality"
        }
    ],
    
    "React & Modern Frontend": [
        {
            "id": "course_react_1",
            "title": "React - The Complete Guide",
            "platform": "Udemy",
            "instructor": "Maximilian Schwarzmüller",
            "duration_hours": 49,
            "level": "Intermediate",
            "rating": 4.8,
            "students": 1200000,
            "price": "$14.99",
            "url": "https://www.udemy.com/course/react-the-complete-guide-incl-redux/",
            "content": ["React basics", "Hooks", "Redux", "Next.js", "TypeScript"],
            "learning_style": ["Video", "Projects"],
            "time_commitment": "8-10 hours/week",
            "reviews_highlight": "Most comprehensive React course"
        },
        {
            "id": "course_react_2",
            "title": "Scrimba React Course",
            "platform": "Scrimba",
            "instructor": "Bob Ziroll",
            "duration_hours": 25,
            "level": "Beginner-Intermediate",
            "rating": 4.9,
            "students": 300000,
            "price": "Free with Pro",
            "url": "https://scrimba.com/learn/learnreact",
            "content": ["React fundamentals", "Components", "Hooks"],
            "learning_style": ["Interactive", "Video", "Interactive coding"],
            "time_commitment": "5-6 hours/week",
            "reviews_highlight": "Interactive learning, very engaging"
        }
    ],
    
    "Data Structures": [
        {
            "id": "course_ds_1",
            "title": "Algorithms, Part I",
            "platform": "Coursera",
            "instructor": "Robert Sedgewick & Kevin Wayne",
            "duration_hours": 60,
            "level": "Intermediate",
            "rating": 4.8,
            "students": 600000,
            "price": "Free with certificate",
            "url": "https://www.coursera.org/learn/algorithms-part1",
            "content": ["Stacks", "Queues", "Sorting", "Searching", "Graphs"],
            "learning_style": ["Video", "Assignments"],
            "time_commitment": "6-8 hours/week",
            "reviews_highlight": "Academic, rigorous, highly respected"
        },
        {
            "id": "course_ds_2",
            "title": "Data Structures and Algorithms",
            "platform": "Udemy",
            "instructor": "Colt Steele",
            "duration_hours": 20,
            "level": "Beginner-Intermediate",
            "rating": 4.7,
            "students": 400000,
            "price": "$14.99",
            "url": "https://www.udemy.com/course/js-algorithms-and-data-structures-masterclass/",
            "content": ["Arrays", "Objects", "Sorting", "Dynamic programming"],
            "learning_style": ["Video", "Coding exercises"],
            "time_commitment": "4-5 hours/week",
            "reviews_highlight": "Very practical, coding focused"
        }
    ],
    
    "Machine Learning Fundamentals": [
        {
            "id": "course_ml_1",
            "title": "Andrew Ng's Machine Learning Course",
            "platform": "Coursera",
            "instructor": "Andrew Ng",
            "duration_hours": 70,
            "level": "Beginner-Intermediate",
            "rating": 4.9,
            "students": 3000000,
            "price": "Free with certificate",
            "url": "https://www.coursera.org/learn/machine-learning",
            "content": ["Regression", "Classification", "Neural Networks", "Advice for ML"],
            "learning_style": ["Video", "Assignments", "MATLAB"],
            "time_commitment": "7-8 hours/week",
            "reviews_highlight": "The best ML course, from the creator"
        },
        {
            "id": "course_ml_2",
            "title": "Fast.ai - Practical Deep Learning",
            "platform": "Fast.ai",
            "instructor": "Jeremy Howard",
            "duration_hours": 50,
            "level": "Intermediate",
            "rating": 4.8,
            "students": 200000,
            "price": "Free",
            "url": "https://course.fast.ai/",
            "content": ["Deep learning", "Computer vision", "NLP", "Tabular data"],
            "learning_style": ["Video", "Jupyter notebooks", "Top-down approach"],
            "time_commitment": "8-10 hours/week",
            "reviews_highlight": "Practical, top-down approach, very effective"
        },
        {
            "id": "course_ml_3",
            "title": "Machine Learning Specialization",
            "platform": "Coursera",
            "instructor": "Andrew Ng",
            "duration_hours": 150,
            "level": "Beginner-Intermediate",
            "rating": 4.8,
            "students": 500000,
            "price": "$49/month",
            "url": "https://www.coursera.org/specializations/machine-learning-introduction",
            "content": ["Supervised learning", "Unsupervised learning", "Reinforcement learning"],
            "learning_style": ["Video", "Labs", "Quizzes"],
            "time_commitment": "10-12 hours/week",
            "reviews_highlight": "Updated version of classic course, very comprehensive"
        }
    ],
    
    "SQL & Databases": [
        {
            "id": "course_sql_1",
            "title": "SQL Tutorial for Beginners",
            "platform": "Mode Analytics",
            "instructor": "Mode Analytics",
            "duration_hours": 12,
            "level": "Beginner",
            "rating": 4.7,
            "students": 500000,
            "price": "Free",
            "url": "https://mode.com/sql-tutorial/",
            "content": ["SELECT", "WHERE", "JOINs", "Aggregation", "Data analysis"],
            "learning_style": ["Interactive SQL editor", "Tutorials"],
            "time_commitment": "2-3 hours/week",
            "reviews_highlight": "Best free SQL tutorial, interactive"
        },
        {
            "id": "course_sql_2",
            "title": "The Complete SQL Bootcamp",
            "platform": "Udemy",
            "instructor": "Jose Portilla",
            "duration_hours": 9,
            "level": "Beginner",
            "rating": 4.7,
            "students": 1200000,
            "price": "$14.99",
            "url": "https://www.udemy.com/course/the-complete-sql-bootcamp/",
            "content": ["SQL fundamentals", "Joins", "Subqueries", "Window functions"],
            "learning_style": ["Video", "Exercises"],
            "time_commitment": "2-3 hours/week",
            "reviews_highlight": "Comprehensive, covers advanced topics too"
        }
    ],
    
    "System Design": [
        {
            "id": "course_sd_1",
            "title": "Grokking the System Design Interview",
            "platform": "Educative",
            "instructor": "Fahim ul Haq",
            "duration_hours": 40,
            "level": "Advanced",
            "rating": 4.8,
            "students": 100000,
            "price": "$49",
            "url": "https://www.educative.io/courses/grokking-the-system-design-interview",
            "content": ["Scalability", "Load balancing", "Caching", "Databases", "Case studies"],
            "learning_style": ["Interactive lessons", "Visuals", "Code examples"],
            "time_commitment": "6-8 hours/week",
            "reviews_highlight": "Best system design course, very practical"
        },
        {
            "id": "course_sd_2",
            "title": "System Design Primer",
            "platform": "GitHub",
            "instructor": "Donne Martin",
            "duration_hours": 50,
            "level": "Advanced",
            "rating": 4.9,
            "students": 200000,
            "price": "Free",
            "url": "https://github.com/donnemartin/system-design-primer",
            "content": ["All system design concepts", "Scalability principles"],
            "learning_style": ["Reading", "Visuals", "Resources"],
            "time_commitment": "Self-paced",
            "reviews_highlight": "Comprehensive free resource"
        }
    ],

    # ========================================================================
    # DevOps & Cloud
    # ========================================================================
    "DevOps & Cloud Computing": [
        {
            "id": "course_devops_1",
            "title": "AWS Solutions Architect",
            "platform": "Coursera",
            "instructor": "AWS",
            "duration_hours": 60,
            "level": "Intermediate",
            "rating": 4.7,
            "students": 500000,
            "price": "$49/month",
            "url": "https://www.coursera.org/programs/aws-learning",
            "content": ["EC2", "S3", "VPC", "IAM", "Serverless"],
            "learning_style": ["Video", "Labs", "Quizzes"],
            "time_commitment": "5-7 hours/week",
            "reviews_highlight": "Official AWS content, industry recognized"
        },
        {
            "id": "course_devops_2",
            "title": "Docker & Kubernetes Masterclass",
            "platform": "Udemy",
            "instructor": "Bret Fisher",
            "duration_hours": 30,
            "level": "Intermediate",
            "rating": 4.8,
            "students": 200000,
            "price": "$14.99",
            "url": "https://www.udemy.com/course/docker-mastery/",
            "content": ["Docker", "Docker Compose", "Kubernetes", "Swarm"],
            "learning_style": ["Video", "Hands-on labs"],
            "time_commitment": "4-6 hours/week",
            "reviews_highlight": "Very practical, real-world scenarios"
        },
        {
            "id": "course_devops_3",
            "title": "DevOps Bootcamp",
            "platform": "Udemy",
            "instructor": "S上手",
            "duration_hours": 25,
            "level": "Beginner",
            "rating": 4.6,
            "students": 150000,
            "price": "$14.99",
            "url": "https://www.udemy.com/course/devops-bootcamp/",
            "content": ["CI/CD", "Jenkins", "Git", "Docker", "Ansible"],
            "learning_style": ["Video", "Projects"],
            "time_commitment": "3-5 hours/week",
            "reviews_highlight": "Great intro to DevOps"
        }
    ],

    # ========================================================================
    # Cybersecurity
    # ========================================================================
    "Cybersecurity Fundamentals": [
        {
            "id": "course_cyber_1",
            "title": "Cybersecurity Specialization",
            "platform": "Coursera",
            "instructor": "University of Maryland",
            "duration_hours": 40,
            "level": "Intermediate",
            "rating": 4.7,
            "students": 300000,
            "price": "Free with certificate",
            "url": "https://www.coursera.org/specializations/ibm-cybersecurity",
            "content": ["Network security", "Cryptography", "Risk management"],
            "learning_style": ["Video", "Labs", "Assessments"],
            "time_commitment": "4-6 hours/week",
            "reviews_highlight": "Academic approach, very thorough"
        },
        {
            "id": "course_cyber_2",
            "title": "CompTIA Security+",
            "platform": "Udemy",
            "instructor": "Mike Chapple",
            "duration_hours": 20,
            "level": "Beginner",
            "rating": 4.8,
            "students": 100000,
            "price": "$14.99",
            "url": "https://www.udemy.com/course/comptia-security-certification/",
            "content": ["Threats", "Attacks", "Cryptography", "Identity management"],
            "learning_style": ["Video", "Practice tests"],
            "time_commitment": "3-4 hours/week",
            "reviews_highlight": "Best for certification prep"
        }
    ],

    # ========================================================================
    # Data Science
    # ========================================================================
    "Data Science & Analytics": [
        {
            "id": "course_ds_1",
            "title": "IBM Data Science Professional Certificate",
            "platform": "Coursera",
            "instructor": "IBM",
            "duration_hours": 80,
            "level": "Beginner",
            "rating": 4.6,
            "students": 1000000,
            "price": "$39/month",
            "url": "https://www.coursera.org/professional-certificate/ibm-data-science",
            "content": ["Python", "SQL", "Data visualization", "Machine learning"],
            "learning_style": ["Video", "Labs", "Projects"],
            "time_commitment": "10-12 hours/week",
            "reviews_highlight": "Comprehensive, great for career change"
        },
        {
            "id": "course_ds_2",
            "title": "Data Science Masterclass",
            "platform": "Udemy",
            "instructor": "Kirill Eremenko",
            "duration_hours": 44,
            "level": "Beginner",
            "rating": 4.5,
            "students": 800000,
            "price": "$14.99",
            "url": "https://www.udemy.com/course/data-science-and-machine-learning-bootcamp-with-r/",
            "content": ["Python", "Statistics", "Machine learning", "Deep learning"],
            "learning_style": ["Video", "Projects"],
            "time_commitment": "6-8 hours/week",
            "reviews_highlight": "Very hands-on, lots of projects"
        }
    ],

    # ========================================================================
    # Mobile Development
    # ========================================================================
    "Mobile App Development": [
        {
            "id": "course_mobile_1",
            "title": "Flutter & Dart - The Complete Guide",
            "platform": "Udemy",
            "instructor": "Academind",
            "duration_hours": 42,
            "level": "Beginner",
            "rating": 4.7,
            "students": 300000,
            "price": "$14.99",
            "url": "https://www.udemy.com/course/flutter-dart-the-complete-guide/",
            "content": ["Dart", "Flutter", "iOS", "Android", "Firebase"],
            "learning_style": ["Video", "Projects"],
            "time_commitment": "5-7 hours/week",
            "reviews_highlight": "Best cross-platform course"
        },
        {
            "id": "course_mobile_2",
            "title": "iOS & Swift - The Complete Developer",
            "platform": "Udemy",
            "instructor": "Dr. Angela Yu",
            "duration_hours": 60,
            "level": "Beginner",
            "rating": 4.8,
            "students": 200000,
            "price": "$14.99",
            "url": "https://www.udemy.com/course/ios-13-app-development-bootcamp/",
            "content": ["Swift", "SwiftUI", "Xcode", "iOS development"],
            "learning_style": ["Video", "Projects"],
            "time_commitment": "8-10 hours/week",
            "reviews_highlight": "Best for iOS beginners"
        }
    ],

    # ========================================================================
    # UI/UX Design
    # ========================================================================
    "UI/UX Design": [
        {
            "id": "course_uiux_1",
            "title": "Google UX Design Certificate",
            "platform": "Coursera",
            "instructor": "Google",
            "duration_hours": 90,
            "level": "Beginner",
            "rating": 4.8,
            "students": 500000,
            "price": "$39/month",
            "url": "https://www.coursera.org/professional-certificate/google-ux-design",
            "content": ["UX research", "Wireframing", "Prototyping", "Usability testing"],
            "learning_style": ["Video", "Hands-on projects"],
            "time_commitment": "10-12 hours/week",
            "reviews_highlight": "Industry recognized, great portfolio projects"
        },
        {
            "id": "course_uiux_2",
            "title": "UI/UX Design Masterclass",
            "platform": "Udemy",
            "instructor": "Gary Simon",
            "duration_hours": 25,
            "level": "Beginner",
            "rating": 4.7,
            "students": 150000,
            "price": "$14.99",
            "url": "https://www.udemy.com/course/ui-ux-design-course/",
            "content": ["Figma", "Design principles", "User research", "Prototyping"],
            "learning_style": ["Video", "Design projects"],
            "time_commitment": "3-5 hours/week",
            "reviews_highlight": "Practical, focuses on Figma"
        }
    ],

    # ========================================================================
    # AI & Machine Learning
    # ========================================================================
    "Artificial Intelligence": [
        {
            "id": "course_ai_1",
            "title": "AI For Everyone",
            "platform": "Coursera",
            "instructor": "Andrew Ng",
            "duration_hours": 8,
            "level": "Beginner",
            "rating": 4.8,
            "students": 2000000,
            "price": "Free with certificate",
            "url": "https://www.coursera.org/learn/ai-for-everyone",
            "content": ["AI concepts", "Machine learning", "Deep learning", "AI strategy"],
            "learning_style": ["Video", "Quizzes"],
            "time_commitment": "2-3 hours/week",
            "reviews_highlight": "Best intro to AI for non-technical"
        },
        {
            "id": "course_ai_2",
            "title": "Deep Learning.AI TensorFlow Developer",
            "platform": "Coursera",
            "instructor": "Laurence Moroney",
            "duration_hours": 40,
            "level": "Intermediate",
            "rating": 4.7,
            "students": 400000,
            "price": "$49/month",
            "url": "https://www.coursera.org/professional-certificates/tensorflow-in-practice",
            "content": ["TensorFlow", "Neural networks", "CNNs", "NLP"],
            "learning_style": ["Video", "Coding exercises"],
            "time_commitment": "5-7 hours/week",
            "reviews_highlight": "Hands-on with TensorFlow"
        }
    ],

    # ========================================================================
    # Blockchain
    # ========================================================================
    "Blockchain & Cryptocurrency": [
        {
            "id": "course_blockchain_1",
            "title": "Blockchain Specialization",
            "platform": "Coursera",
            "instructor": "University at Buffalo",
            "duration_hours": 40,
            "level": "Intermediate",
            "rating": 4.6,
            "students": 200000,
            "price": "Free with certificate",
            "url": "https://www.coursera.org/specializations/blockchain",
            "content": ["Smart contracts", "Solidity", "Ethereum", "DApps"],
            "learning_style": ["Video", "Projects"],
            "time_commitment": "4-6 hours/week",
            "reviews_highlight": "Academic approach, very thorough"
        },
        {
            "id": "course_blockchain_2",
            "title": "Ethereum & Solidity Bootcamp",
            "platform": "Udemy",
            "instructor": "Stephen Grider",
            "duration_hours": 30,
            "level": "Intermediate",
            "rating": 4.7,
            "students": 100000,
            "price": "$14.99",
            "url": "https://www.udemy.com/course/ethereum-and-solidity-the-complete-developers-guide/",
            "content": ["Solidity", "Smart contracts", "Web3", "Truffle"],
            "learning_style": ["Video", "Projects"],
            "time_commitment": "4-6 hours/week",
            "reviews_highlight": "Best practical blockchain course"
        }
    ],

    # ========================================================================
    # Product Management
    # ========================================================================
    "Product Management": [
        {
            "id": "course_pm_1",
            "title": "Product Management Certificate",
            "platform": "Coursera",
            "instructor": "Berklee College",
            "duration_hours": 30,
            "level": "Beginner",
            "rating": 4.7,
            "students": 150000,
            "price": "$49/month",
            "url": "https://www.coursera.org/professional-certificate/product-management",
            "content": ["Product strategy", "Roadmapping", "User research", "Analytics"],
            "learning_style": ["Video", "Projects"],
            "time_commitment": "4-6 hours/week",
            "reviews_highlight": "Comprehensive PM foundation"
        },
        {
            "id": "course_pm_2",
            "title": "Product Management Masterclass",
            "platform": "Udemy",
            "instructor": "Justin R. Russel",
            "duration_hours": 20,
            "level": "Beginner",
            "rating": 4.6,
            "students": 100000,
            "price": "$14.99",
            "url": "https://www.udemy.com/course/product-management-masterclass/",
            "content": ["Product discovery", "Agile", "Stakeholder management"],
            "learning_style": ["Video", "Case studies"],
            "time_commitment": "3-4 hours/week",
            "reviews_highlight": "Practical, real-world examples"
        }
    ],

    # ========================================================================
    # Business Fundamentals
    # ========================================================================
    "Business Fundamentals": [
        {
            "id": "course_biz_1",
            "title": "Business Foundations",
            "platform": "Coursera",
            "instructor": "Wharton",
            "duration_hours": 35,
            "level": "Beginner",
            "rating": 4.8,
            "students": 1000000,
            "price": "Free with certificate",
            "url": "https://www.coursera.org/specializations/wharton-business-foundations",
            "content": ["Marketing", "Finance", "Operations", "People management"],
            "learning_style": ["Video", "Case studies", "Assessments"],
            "time_commitment": "4-6 hours/week",
            "reviews_highlight": "Top-tier business education"
        },
        {
            "id": "course_biz_2",
            "title": "Entrepreneurship Specialization",
            "platform": "Coursera",
            "instructor": "University of Pennsylvania",
            "duration_hours": 40,
            "level": "Beginner",
            "rating": 4.7,
            "students": 400000,
            "price": "Free with certificate",
            "url": "https://www.coursera.org/specializations/wharton-entrepreneurship",
            "content": ["Business models", "Pitching", "Funding", "Growth"],
            "learning_style": ["Video", "Projects"],
            "time_commitment": "5-7 hours/week",
            "reviews_highlight": "Great for aspiring entrepreneurs"
        }
    ],

    # ========================================================================
    # Marketing
    # ========================================================================
    "Marketing Fundamentals": [
        {
            "id": "course_mkt_1",
            "title": "Digital Marketing Specialization",
            "platform": "Coursera",
            "instructor": "University of Illinois",
            "duration_hours": 40,
            "level": "Beginner",
            "rating": 4.6,
            "students": 600000,
            "price": "Free with certificate",
            "url": "https://www.coursera.org/specializations/digital-marketing",
            "content": ["SEO", "Social media", "Analytics", "Content marketing"],
            "learning_style": ["Video", "Projects"],
            "time_commitment": "5-7 hours/week",
            "reviews_highlight": "Comprehensive digital marketing"
        },
        {
            "id": "course_mkt_2",
            "title": "Marketing Analytics Course",
            "platform": "Udemy",
            "instructor": "Anton Voroni",
            "duration_hours": 15,
            "level": "Beginner",
            "rating": 4.5,
            "students": 80000,
            "price": "$14.99",
            "url": "https://www.udemy.com/course/marketing-analytics-course/",
            "content": ["Google Analytics", "Data analysis", "ROI", "Metrics"],
            "learning_style": ["Video", "Hands-on"],
            "time_commitment": "2-3 hours/week",
            "reviews_highlight": "Practical analytics skills"
        }
    ],

    # ========================================================================
    # Finance & Accounting
    # ========================================================================
    "Finance & Accounting": [
        {
            "id": "course_fin_1",
            "title": "Finance Specialization",
            "platform": "Coursera",
            "instructor": "University of Michigan",
            "duration_hours": 45,
            "level": "Beginner",
            "rating": 4.7,
            "students": 500000,
            "price": "Free with certificate",
            "url": "https://www.coursera.org/specializations/finance-fundamentals",
            "content": ["Financial analysis", "Valuation", "Corporate finance"],
            "learning_style": ["Video", "Exercises"],
            "time_commitment": "5-7 hours/week",
            "reviews_highlight": "Strong foundation in finance"
        },
        {
            "id": "course_fin_2",
            "title": "Accounting Masterclass",
            "platform": "Udemy",
            "instructor": "Irwin T. David",
            "duration_hours": 25,
            "level": "Beginner",
            "rating": 4.6,
            "students": 150000,
            "price": "$14.99",
            "url": "https://www.udemy.com/course/accounting-masterclass/",
            "content": ["Bookkeeping", "Financial statements", "T-accounts"],
            "learning_style": ["Video", "Examples"],
            "time_commitment": "3-4 hours/week",
            "reviews_highlight": "Clear explanations"
        }
    ],

    # ========================================================================
    # Leadership & Management
    # ========================================================================
    "Leadership & Management": [
        {
            "id": "course_lead_1",
            "title": "Leadership Specialization",
            "platform": "Coursera",
            "instructor": "University of Michigan",
            "duration_hours": 30,
            "level": "Intermediate",
            "rating": 4.8,
            "students": 400000,
            "price": "Free with certificate",
            "url": "https://www.coursera.org/specializations/leadership-skills",
            "content": ["Leadership", "Communication", "Team building", "Influence"],
            "learning_style": ["Video", "Peer assessments"],
            "time_commitment": "4-5 hours/week",
            "reviews_highlight": "Transformative leadership training"
        },
        {
            "id": "course_lead_2",
            "title": "Management Skills Masterclass",
            "platform": "Udemy",
            "instructor": "Chris Croft",
            "duration_hours": 18,
            "level": "Beginner",
            "rating": 4.7,
            "students": 200000,
            "price": "$14.99",
            "url": "https://www.udemy.com/course/management-skills-course/",
            "content": ["Time management", "Delegation", "Conflict resolution"],
            "learning_style": ["Video", "Exercises"],
            "time_commitment": "2-3 hours/week",
            "reviews_highlight": "Practical and actionable"
        }
    ],

    # ========================================================================
    # Project Management
    # ========================================================================
    "Project Management": [
        {
            "id": "course_proj_1",
            "title": "PMP Certification",
            "platform": "Coursera",
            "instructor": "PMI",
            "duration_hours": 60,
            "level": "Advanced",
            "rating": 4.7,
            "students": 300000,
            "price": "$99/month",
            "url": "https://www.coursera.org/programs/pmp-certification",
            "content": ["PMBOK", "Agile", "Scrum", "Risk management"],
            "learning_style": ["Video", "Practice tests"],
            "time_commitment": "8-10 hours/week",
            "reviews_highlight": "Best for PMP certification"
        },
        {
            "id": "course_proj_2",
            "title": "Project Management Bootcamp",
            "platform": "Udemy",
            "instructor": "Jose Portilla",
            "duration_hours": 20,
            "level": "Beginner",
            "rating": 4.6,
            "students": 250000,
            "price": "$14.99",
            "url": "https://www.udemy.com/course/project-management-bootcamp/",
            "content": ["Agile", "Scrum", "Kanban", "Tools"],
            "learning_style": ["Video", "Projects"],
            "time_commitment": "3-5 hours/week",
            "reviews_highlight": "Great intro to PM"
        }
    ],

    # ========================================================================
    # Data Engineering
    # ========================================================================
    "Data Engineering": [
        {
            "id": "course_de_1",
            "title": "IBM Data Engineering Professional Certificate",
            "platform": "Coursera",
            "instructor": "IBM",
            "duration_hours": 70,
            "level": "Intermediate",
            "rating": 4.6,
            "students": 300000,
            "price": "$39/month",
            "url": "https://www.coursera.org/professional-certificate/ibm-data-engineering",
            "content": ["Python", "SQL", "Spark", "Hadoop", "ETL"],
            "learning_style": ["Video", "Labs"],
            "time_commitment": "8-10 hours/week",
            "reviews_highlight": "Comprehensive data engineering path"
        },
        {
            "id": "course_de_2",
            "title": "Data Engineering on GCP",
            "platform": "Udemy",
            "instructor": "Google Cloud",
            "duration_hours": 30,
            "level": "Advanced",
            "rating": 4.7,
            "students": 100000,
            "price": "$14.99",
            "url": "https://www.udemy.com/course/data-engineering-gcp/",
            "content": ["BigQuery", "Dataflow", "Dataproc", "Datafusion"],
            "learning_style": ["Video", "Hands-on labs"],
            "time_commitment": "4-6 hours/week",
            "reviews_highlight": "Practical GCP skills"
        }
    ],

    # ========================================================================
    # Natural Language Processing
    # ========================================================================
    "Natural Language Processing": [
        {
            "id": "course_nlp_1",
            "title": "Natural Language Processing Specialization",
            "platform": "Coursera",
            "instructor": "DeepLearning.AI",
            "duration_hours": 40,
            "level": "Advanced",
            "rating": 4.7,
            "students": 200000,
            "price": "$49/month",
            "url": "https://www.coursera.org/specializations/natural-language-processing",
            "content": ["Sentiment analysis", "Transformers", "Attention models"],
            "learning_style": ["Video", "Coding assignments"],
            "time_commitment": "5-7 hours/week",
            "reviews_highlight": "Best NLP course by Andrew Ng's team"
        },
        {
            "id": "course_nlp_2",
            "title": "NLP with Python",
            "platform": "Udemy",
            "instructor": "Jose Portilla",
            "duration_hours": 22,
            "level": "Intermediate",
            "rating": 4.6,
            "students": 150000,
            "price": "$14.99",
            "url": "https://www.udemy.com/course/nlp-natural-language-processing-with-python/",
            "content": ["NLTK", "Spacy", "Text classification", "Word embeddings"],
            "learning_style": ["Video", "Projects"],
            "time_commitment": "3-5 hours/week",
            "reviews_highlight": "Hands-on with Python libraries"
        }
    ],

    # ========================================================================
    # Linux & Operating Systems
    # ========================================================================
    "Linux/Unix Fundamentals": [
        {
            "id": "course_linux_1",
            "title": "Linux Masterclass",
            "platform": "Udemy",
            "instructor": "Scott Simpson",
            "duration_hours": 20,
            "level": "Beginner",
            "rating": 4.7,
            "students": 300000,
            "price": "$14.99",
            "url": "https://www.udemy.com/course/linux-command-line-basics/",
            "content": ["Command line", "Bash scripting", "File management"],
            "learning_style": ["Video", "Exercises"],
            "time_commitment": "3-4 hours/week",
            "reviews_highlight": "Perfect for Linux beginners"
        },
        {
            "id": "course_linux_2",
            "title": "CompTIA Linux+",
            "platform": "Udemy",
            "instructor": "Jason Cannon",
            "duration_hours": 25,
            "level": "Intermediate",
            "rating": 4.6,
            "students": 100000,
            "price": "$14.99",
            "url": "https://www.udemy.com/course/comptia-linux/",
            "content": ["System administration", "Security", "Troubleshooting"],
            "learning_style": ["Video", "Lab exercises"],
            "time_commitment": "4-5 hours/week",
            "reviews_highlight": "Best for Linux+ certification"
        }
    ],

    # ========================================================================
    # Version Control & Git
    # ========================================================================
    "Version Control (Git)": [
        {
            "id": "course_git_1",
            "title": "Git Complete",
            "platform": "Udemy",
            "instructor": "Jason Taylor",
            "duration_hours": 10,
            "level": "Beginner",
            "rating": 4.7,
            "students": 400000,
            "price": "$14.99",
            "url": "https://www.udemy.com/course/git-complete/",
            "content": ["Git basics", "Branching", "Merging", "GitHub"],
            "learning_style": ["Video", "Hands-on"],
            "time_commitment": "2-3 hours/week",
            "reviews_highlight": "Best practical Git course"
        },
        {
            "id": "course_git_2",
            "title": "Git & GitHub Bootcamp",
            "platform": "Udemy",
            "instructor": "Colt Steele",
            "duration_hours": 15,
            "level": "Beginner",
            "rating": 4.8,
            "students": 250000,
            "price": "$14.99",
            "url": "https://www.udemy.com/course/git-and-github-bootcamp/",
            "content": ["Version control", "Collaboration", "Open source"],
            "learning_style": ["Video", "Projects"],
            "time_commitment": "2-4 hours/week",
            "reviews_highlight": "Great for collaboration skills"
        }
    ],

    # ========================================================================
    # Communication Skills
    # ========================================================================
    "Communication Skills": [
        {
            "id": "course_comm_1",
            "title": "Business Communication",
            "platform": "Coursera",
            "instructor": "University of Colorado",
            "duration_hours": 25,
            "level": "Beginner",
            "rating": 4.7,
            "students": 300000,
            "price": "Free with certificate",
            "url": "https://www.coursera.org/learn/business-communication",
            "content": ["Writing", "Presentation", "Email", "Meetings"],
            "learning_style": ["Video", "Assignments"],
            "time_commitment": "3-4 hours/week",
            "reviews_highlight": "Professional communication skills"
        },
        {
            "id": "course_comm_2",
            "title": "Public Speaking Masterclass",
            "platform": "Udemy",
            "instructor": "Chris Harpham",
            "duration_hours": 8,
            "level": "Beginner",
            "rating": 4.6,
            "students": 200000,
            "price": "$14.99",
            "url": "https://www.udemy.com/course/public-speaking-presentation-skills/",
            "content": ["Presentations", "Overcoming fear", "Body language"],
            "learning_style": ["Video", "Practice"],
            "time_commitment": "1-2 hours/week",
            "reviews_highlight": "Builds confidence"
        }
    ],

    # ========================================================================
    # Economics
    # ========================================================================
    "Economics Basics": [
        {
            "id": "course_econ_1",
            "title": "Economics Principles",
            "platform": "Coursera",
            "instructor": "University of Michigan",
            "duration_hours": 30,
            "level": "Beginner",
            "rating": 4.7,
            "students": 500000,
            "price": "Free with certificate",
            "url": "https://www.coursera.org/learn/principles-of-economics",
            "content": ["Microeconomics", "Macroeconomics", "Supply and demand"],
            "learning_style": ["Video", "Exercises"],
            "time_commitment": "4-5 hours/week",
            "reviews_highlight": "Excellent foundation in economics"
        },
        {
            "id": "course_econ_2",
            "title": "Finance & Economics for Everyone",
            "platform": "Udemy",
            "instructor": "Sean Ross",
            "duration_hours": 12,
            "level": "Beginner",
            "rating": 4.5,
            "students": 50000,
            "price": "$14.99",
            "url": "https://www.udemy.com/course/finance-economics/",
            "content": ["Economic indicators", "Markets", "Investment basics"],
            "learning_style": ["Video"],
            "time_commitment": "2-3 hours/week",
            "reviews_highlight": "Accessible to everyone"
        }
    ],

    # ========================================================================
    # Human Resources
    # ========================================================================
    "Human Resources": [
        {
            "id": "course_hr_1",
            "title": "HR Fundamentals",
            "platform": "Coursera",
            "instructor": "UC Irvine",
            "duration_hours": 25,
            "level": "Beginner",
            "rating": 4.6,
            "students": 150000,
            "price": "Free with certificate",
            "url": "https://www.coursera.org/learn/human-resources",
            "content": ["Recruitment", "Compensation", "Employee relations"],
            "learning_style": ["Video", "Case studies"],
            "time_commitment": "3-4 hours/week",
            "reviews_highlight": "Comprehensive HR intro"
        },
        {
            "id": "course_hr_2",
            "title": "HR Management Masterclass",
            "platform": "Udemy",
            "instructor": "SHRM-CP Instructor",
            "duration_hours": 20,
            "level": "Intermediate",
            "rating": 4.7,
            "students": 80000,
            "price": "$14.99",
            "url": "https://www.udemy.com/course/hr-management-course/",
            "content": ["Strategic HR", "Compliance", "Performance management"],
            "learning_style": ["Video", "Quizzes"],
            "time_commitment": "3-5 hours/week",
            "reviews_highlight": "Practical HR skills"
        }
    ],

    # ========================================================================
    # Agile & Scrum
    # ========================================================================
    "Agile & Scrum Methodology": [
        {
            "id": "course_agile_1",
            "title": "Agile Project Management",
            "platform": "Coursera",
            "instructor": "University of Colorado",
            "duration_hours": 30,
            "level": "Beginner",
            "rating": 4.7,
            "students": 400000,
            "price": "Free with certificate",
            "url": "https://www.coursera.org/learn/agile-project-management",
            "content": ["Scrum", "Kanban", "Sprints", "User stories"],
            "learning_style": ["Video", "Projects"],
            "time_commitment": "4-5 hours/week",
            "reviews_highlight": "Best intro to Agile"
        },
        {
            "id": "course_agile_2",
            "title": "Scrum Master Certification",
            "platform": "Udemy",
            "instructor": "Jose Portilla",
            "duration_hours": 15,
            "level": "Beginner",
            "rating": 4.8,
            "students": 300000,
            "price": "$14.99",
            "url": "https://www.udemy.com/course/scrum-master-certification/",
            "content": ["Scrum roles", "Sprint planning", "Retrospectives"],
            "learning_style": ["Video", "Practice tests"],
            "time_commitment": "2-4 hours/week",
            "reviews_highlight": "Best for CSM certification prep"
        }
    ],

    # ========================================================================
    # Software Architecture
    # ========================================================================
    "Software Architecture": [
        {
            "id": "course_sa_1",
            "title": "Software Architecture Essentials",
            "platform": "Coursera",
            "instructor": "University of Alberta",
            "duration_hours": 35,
            "level": "Advanced",
            "rating": 4.7,
            "students": 150000,
            "price": "$49/month",
            "url": "https://www.coursera.org/learn/software-architecture",
            "content": ["Design patterns", "Microservices", "Clean architecture"],
            "learning_style": ["Video", "Case studies"],
            "time_commitment": "5-6 hours/week",
            "reviews_highlight": "Comprehensive architecture knowledge"
        },
        {
            "id": "course_sa_2",
            "title": "Enterprise Architecture Masterclass",
            "platform": "Udemy",
            "instructor": "IT Expert",
            "duration_hours": 25,
            "level": "Advanced",
            "rating": 4.6,
            "students": 50000,
            "price": "$14.99",
            "url": "https://www.udemy.com/course/enterprise-architecture/",
            "content": ["TOGAF", "Enterprise patterns", "Architecture frameworks"],
            "learning_style": ["Video", "Diagrams"],
            "time_commitment": "4-5 hours/week",
            "reviews_highlight": "Best for enterprise architects"
        }
    ],

    # ========================================================================
    # API Design
    # ========================================================================
    "API Design": [
        {
            "id": "course_api_1",
            "title": "API Design Masterclass",
            "platform": "Udemy",
            "instructor": "Eliostruyf",
            "duration_hours": 12,
            "level": "Intermediate",
            "rating": 4.6,
            "students": 80000,
            "price": "$14.99",
            "url": "https://www.udemy.com/course/api-design/",
            "content": ["REST", "GraphQL", "Best practices", "Documentation"],
            "learning_style": ["Video", "Projects"],
            "time_commitment": "2-3 hours/week",
            "reviews_highlight": "Practical API design"
        },
        {
            "id": "course_api_2",
            "title": "Building APIs with Node.js",
            "platform": "Coursera",
            "instructor": "Amazon Web Services",
            "duration_hours": 20,
            "level": "Intermediate",
            "rating": 4.7,
            "students": 100000,
            "price": "$49/month",
            "url": "https://www.coursera.org/learn/building-apis-node-js",
            "content": ["Express", "RESTful design", "Authentication"],
            "learning_style": ["Video", "Coding labs"],
            "time_commitment": "3-4 hours/week",
            "reviews_highlight": "Hands-on API development"
        }
    ],

    # ========================================================================
    # Technical Writing
    # ========================================================================
    "Technical Writing": [
        {
            "id": "course_tw_1",
            "title": "Technical Writing Masterclass",
            "platform": "Udemy",
            "instructor": "Patrick H. Winston",
            "duration_hours": 10,
            "level": "Beginner",
            "rating": 4.7,
            "students": 100000,
            "price": "$14.99",
            "url": "https://www.udemy.com/course/technical-writing/",
            "content": ["Documentation", "Manuals", "Clear writing"],
            "learning_style": ["Video", "Exercises"],
            "time_commitment": "2-3 hours/week",
            "reviews_highlight": "Write clearly and effectively"
        },
        {
            "id": "course_tw_2",
            "title": "API Documentation Masterclass",
            "platform": "Udemy",
            "instructor": "Tom Wiesing",
            "duration_hours": 8,
            "level": "Intermediate",
            "rating": 4.6,
            "students": 30000,
            "price": "$14.99",
            "url": "https://www.udemy.com/course/api-documentation/",
            "content": ["Swagger", "OpenAPI", "Redoc", "Developer docs"],
            "learning_style": ["Video", "Templates"],
            "time_commitment": "1-2 hours/week",
            "reviews_highlight": "Best for API docs"
        }
    ],

    # ========================================================================
    # Data Visualization
    # ========================================================================
    "Data Visualization": [
        {
            "id": "course_dv_1",
            "title": "Data Visualization with Tableau",
            "platform": "Coursera",
            "instructor": "UC Irvine",
            "duration_hours": 30,
            "level": "Beginner",
            "rating": 4.7,
            "students": 400000,
            "price": "Free with certificate",
            "url": "https://www.coursera.org/learn/data-visualization-tableau",
            "content": ["Tableau", "Dashboards", "Charts", "Storytelling"],
            "learning_style": ["Video", "Hands-on"],
            "time_commitment": "4-5 hours/week",
            "reviews_highlight": "Industry standard viz tool"
        },
        {
            "id": "course_dv_2",
            "title": "Python for Data Visualization",
            "platform": "Udemy",
            "instructor": "Kirill Eremenko",
            "duration_hours": 18,
            "level": "Intermediate",
            "rating": 4.6,
            "students": 200000,
            "price": "$14.99",
            "url": "https://www.udemy.com/course/python-for-data-visualization/",
            "content": ["Matplotlib", "Seaborn", "Plotly", "Interactive charts"],
            "learning_style": ["Video", "Projects"],
            "time_commitment": "3-4 hours/week",
            "reviews_highlight": "Python viz libraries mastery"
        }
    ],

    # ========================================================================
    # Big Data
    # ========================================================================
    "Big Data Fundamentals": [
        {
            "id": "course_bigdata_1",
            "title": "Big Data Specialization",
            "platform": "Coursera",
            "instructor": "UC San Diego",
            "duration_hours": 50,
            "level": "Intermediate",
            "rating": 4.6,
            "students": 300000,
            "price": "Free with certificate",
            "url": "https://www.coursera.org/specializations/big-data",
            "content": ["Hadoop", "Spark", "NoSQL", "Data lakes"],
            "learning_style": ["Video", "Labs"],
            "time_commitment": "6-8 hours/week",
            "reviews_highlight": "Comprehensive big data intro"
        },
        {
            "id": "course_bigdata_2",
            "title": "Spark & Hadoop Masterclass",
            "platform": "Udemy",
            "instructor": "Frank Kane",
            "duration_hours": 20,
            "level": "Intermediate",
            "rating": 4.7,
            "students": 100000,
            "price": "$14.99",
            "url": "https://www.udemy.com/course/spark-and-hadoop/",
            "content": ["PySpark", "Spark SQL", "Data processing"],
            "learning_style": ["Video", "Projects"],
            "time_commitment": "3-5 hours/week",
            "reviews_highlight": "Hands-on big data"
        }
    ],

    # ========================================================================
    # IoT
    # ========================================================================
    "Internet of Things (IoT)": [
        {
            "id": "course_iot_1",
            "title": "IoT Specialization",
            "platform": "Coursera",
            "instructor": "University of California",
            "duration_hours": 40,
            "level": "Intermediate",
            "rating": 4.6,
            "students": 200000,
            "price": "Free with certificate",
            "url": "https://www.coursera.org/specializations/internet-of-things",
            "content": ["Sensors", "IoT protocols", "Cloud integration"],
            "learning_style": ["Video", "Hardware projects"],
            "time_commitment": "5-7 hours/week",
            "reviews_highlight": "Complete IoT foundation"
        },
        {
            "id": "course_iot_2",
            "title": "Arduino for Beginners",
            "platform": "Udemy",
            "instructor": "Educational Engineering",
            "duration_hours": 15,
            "level": "Beginner",
            "rating": 4.5,
            "students": 150000,
            "price": "$14.99",
            "url": "https://www.udemy.com/course/arduino-for-beginners/",
            "content": ["Arduino", "Sensors", "Programming", "Projects"],
            "learning_style": ["Video", "Hardware labs"],
            "time_commitment": "2-3 hours/week",
            "reviews_highlight": "Best hardware intro"
        }
    ],

    # ========================================================================
    # Game Development
    # ========================================================================
    "Game Development": [
        {
            "id": "course_game_1",
            "title": "Game Development with Unity",
            "platform": "Coursera",
            "instructor": "Michigan State University",
            "duration_hours": 50,
            "level": "Beginner",
            "rating": 4.7,
            "students": 300000,
            "price": "Free with certificate",
            "url": "https://www.coursera.org/specializations/game-development",
            "content": ["Unity", "C#", "3D games", "2D games"],
            "learning_style": ["Video", "Projects"],
            "time_commitment": "6-8 hours/week",
            "reviews_highlight": "Complete game dev path"
        },
        {
            "id": "course_game_2",
            "title": "Unreal Engine Masterclass",
            "platform": "Udemy",
            "instructor": "Ben Tristem",
            "duration_hours": 35,
            "level": "Beginner",
            "rating": 4.6,
            "students": 200000,
            "price": "$14.99",
            "url": "https://www.udemy.com/course/unreal-engine-course/",
            "content": ["Unreal", "Blueprints", "Game physics", "VR"],
            "learning_style": ["Video", "Projects"],
            "time_commitment": "5-7 hours/week",
            "reviews_highlight": "Best for 3D games"
        }
    ],

    # ========================================================================
    # Computer Networking
    # ========================================================================
    "Computer Networking": [
        {
            "id": "course_net_1",
            "title": "Computer Networking Basics",
            "platform": "Coursera",
            "instructor": "Google",
            "duration_hours": 25,
            "level": "Beginner",
            "rating": 4.8,
            "students": 500000,
            "price": "Free with certificate",
            "url": "https://www.coursera.org/learn/computer-networking",
            "content": ["TCP/IP", "DNS", "HTTP", "Network security"],
            "learning_style": ["Video", "Labs"],
            "time_commitment": "3-4 hours/week",
            "reviews_highlight": "Best networking intro by Google"
        },
        {
            "id": "course_net_2",
            "title": "CompTIA Network+",
            "platform": "Udemy",
            "instructor": "Mike Chapple",
            "duration_hours": 30,
            "level": "Intermediate",
            "rating": 4.7,
            "students": 150000,
            "price": "$14.99",
            "url": "https://www.udemy.com/course/comptia-network-plus/",
            "content": ["Network+", "Subnetting", "Routing", "Security"],
            "learning_style": ["Video", "Practice tests"],
            "time_commitment": "4-5 hours/week",
            "reviews_highlight": "Best for certification"
        }
    ],

    # ========================================================================
    # UX Research
    # ========================================================================
    "UX Research & Testing": [
        {
            "id": "course_ux_1",
            "title": "UX Research Specialization",
            "platform": "Coursera",
            "instructor": "University of Michigan",
            "duration_hours": 30,
            "level": "Beginner",
            "rating": 4.7,
            "students": 200000,
            "price": "Free with certificate",
            "url": "https://www.coursera.org/specializations/ux-research",
            "content": ["User interviews", "Surveys", "Usability testing", "Analysis"],
            "learning_style": ["Video", "Projects"],
            "time_commitment": "4-5 hours/week",
            "reviews_highlight": "Research-driven UX"
        },
        {
            "id": "course_ux_2",
            "title": "UX Research Masterclass",
            "platform": "Udemy",
            "instructor": "Joe Natoli",
            "duration_hours": 12,
            "level": "Beginner",
            "rating": 4.6,
            "students": 50000,
            "price": "$14.99",
            "url": "https://www.udemy.com/course/ux-research/",
            "content": ["Research methods", "User testing", "Reporting"],
            "learning_style": ["Video", "Templates"],
            "time_commitment": "2-3 hours/week",
            "reviews_highlight": "Practical research skills"
        }
    ],

    # ========================================================================
    # Cloud Architecture
    # ========================================================================
    "Cloud Architecture": [
        {
            "id": "course_cloud_1",
            "title": "Cloud Architecture Professional",
            "platform": "Coursera",
            "instructor": "Google Cloud",
            "duration_hours": 50,
            "level": "Advanced",
            "rating": 4.7,
            "students": 300000,
            "price": "$49/month",
            "url": "https://www.coursera.org/professional-certificate/cloud-architecture-gcp",
            "content": ["GCP", "Design patterns", "Cost optimization", "Security"],
            "learning_style": ["Video", "Labs", "Qwiklabs"],
            "time_commitment": "6-8 hours/week",
            "reviews_highlight": "Best GCP architecture course"
        },
        {
            "id": "course_cloud_2",
            "title": "AWS Solutions Architect Masterclass",
            "platform": "Udemy",
            "instructor": "Frank Kane",
            "duration_hours": 25,
            "level": "Advanced",
            "rating": 4.8,
            "students": 200000,
            "price": "$14.99",
            "url": "https://www.udemy.com/course/aws-solutions-architect/",
            "content": ["AWS", "EC2", "S3", "VPC", "Serverless"],
            "learning_style": ["Video", "Practice exams"],
            "time_commitment": "4-5 hours/week",
            "reviews_highlight": "Best for AWS cert prep"
        }
    ],

    # ========================================================================
    # Quality Assurance
    # ========================================================================
    "Quality Assurance & Testing": [
        {
            "id": "course_qa_1",
            "title": "QA Automation Testing",
            "platform": "Coursera",
            "instructor": "University of Minnesota",
            "duration_hours": 35,
            "level": "Intermediate",
            "rating": 4.6,
            "students": 200000,
            "price": "Free with certificate",
            "url": "https://www.coursera.org/specializations/automation-testing",
            "content": ["Selenium", "JUnit", "Test automation", "CI/CD"],
            "learning_style": ["Video", "Projects"],
            "time_commitment": "4-6 hours/week",
            "reviews_highlight": "Complete automation testing"
        },
        {
            "id": "course_qa_2",
            "title": "Manual Testing Masterclass",
            "platform": "Udemy",
            "instructor": "Raghavendra K.",
            "duration_hours": 20,
            "level": "Beginner",
            "rating": 4.5,
            "students": 150000,
            "price": "$14.99",
            "url": "https://www.udemy.com/course/manual-testing-complete/",
            "content": ["Test cases", "Bug reporting", "Test plans", "Agile testing"],
            "learning_style": ["Video", "Templates"],
            "time_commitment": "3-4 hours/week",
            "reviews_highlight": "Best manual testing intro"
        }
    ],

    # ========================================================================
    # Sales
    # ========================================================================
    "Sales Fundamentals": [
        {
            "id": "course_sales_1",
            "title": "Sales Training Masterclass",
            "platform": "Udemy",
            "instructor": "Grant Cardone",
            "duration_hours": 20,
            "level": "Beginner",
            "rating": 4.7,
            "students": 500000,
            "price": "$14.99",
            "url": "https://www.udemy.com/course/sales-training-program/",
            "content": ["Closing techniques", "Prospecting", "Cold calling"],
            "learning_style": ["Video", "Action plans"],
            "time_commitment": "3-4 hours/week",
            "reviews_highlight": "Best for sales skills"
        },
        {
            "id": "course_sales_2",
            "title": "B2B Sales Masterclass",
            "platform": "Coursera",
            "instructor": "HubSpot",
            "duration_hours": 15,
            "level": "Beginner",
            "rating": 4.6,
            "students": 100000,
            "price": "Free with certificate",
            "url": "https://www.coursera.org/learn/b2b-sales",
            "content": ["B2B selling", "Lead generation", "CRM"],
            "learning_style": ["Video", "Exercises"],
            "time_commitment": "2-3 hours/week",
            "reviews_highlight": "Modern B2B techniques"
        }
    ]

}

def recommend_courses(skill_name, profile=None, budget=None):
    """
    Recommend courses for a given skill
    
    Args:
        skill_name: Name of the skill to learn
        profile: User profile for personalization
        budget: Max budget for courses
    
    Returns:
        List of recommended courses with scoring
    """
    
    courses = COURSE_DATABASE.get(skill_name, [])
    
    if not courses:
        return {
            "skill": skill_name,
            "status": "No courses in database yet",
            "recommendation": "We're adding more courses. Check back soon!"
        }
    
    # Score courses based on profile
    scored_courses = []
    
    for course in courses:
        score = 100
        reasons = []
        
        # Price matching
        if budget:
            if "Free" in course["price"]:
                score += 20
                reasons.append("Free option within budget")
            elif budget >= 100:
                reasons.append("Within your budget")
            elif budget < 20 and course["price"] == "$14.99":
                score -= 10
                reasons.append("May exceed budget")
        
        # Learning style matching
        if profile and "preferred_format" in profile:
            preferred = profile["preferred_format"]
            if any(fmt.lower() in [x.lower() for x in course["learning_style"]] for fmt in preferred):
                score += 15
                reasons.append("Matches your preferred learning style")
        
        # Duration matching
        if profile and "daily_hours" in profile:
            daily_hours = profile["daily_hours"]
            course_weeks = course["duration_hours"] / (daily_hours * 7)
            if 4 <= course_weeks <= 12:
                score += 10
                reasons.append("Good duration for your pace")
            elif course_weeks > 12:
                reasons.append("Longer course - more time needed")
        
        # Rating
        score += course["rating"] * 5
        reasons.append(f"Highly rated ({course['rating']}/5)")
        
        scored_courses.append({
            **course,
            "score": score,
            "recommendation_reasons": reasons,
            "estimated_weeks": course["duration_hours"] / (profile.get("daily_hours", 2) * 7) if profile else None
        })
    
    # Sort by score
    scored_courses.sort(key=lambda x: x["score"], reverse=True)
    
    return {
        "skill": skill_name,
        "total_courses_found": len(scored_courses),
        "top_recommendations": scored_courses[:3],
        "all_courses": scored_courses,
        "recommendation_summary": f"Found {len(scored_courses)} courses. Top choice: {scored_courses[0]['title']} on {scored_courses[0]['platform']}"
    }

def get_all_courses_for_skill(skill_name, profile=None, budget=None):
    """
    Get courses for a skill with fuzzy matching.
    If exact match not found, tries partial match.
    If still no match, returns all available courses.
    """
    # Try exact match first
    courses = COURSE_DATABASE.get(skill_name, [])
    
    # If no exact match, try partial match
    if not courses:
        skill_lower = skill_name.lower()
        for key in COURSE_DATABASE.keys():
            if skill_lower in key.lower() or key.lower() in skill_lower:
                courses = COURSE_DATABASE[key]
                break
    
    # If still no match, return all courses
    if not courses:
        all_courses = []
        for cat_courses in COURSE_DATABASE.values():
            all_courses.extend(cat_courses)
        courses = all_courses
    
    # Score courses based on profile
    scored_courses = []
    
    for course in courses:
        score = 100
        reasons = []
        
        # Price matching
        if budget:
            if "Free" in course["price"]:
                score += 20
                reasons.append("Free option within budget")
            elif budget >= 100:
                reasons.append("Within your budget")
            elif budget < 20 and course["price"] == "$14.99":
                score -= 10
                reasons.append("May exceed budget")
        
        # Learning style matching
        if profile and "preferred_format" in profile:
            preferred = profile["preferred_format"]
            if any(fmt.lower() in [x.lower() for x in course["learning_style"]] for fmt in preferred):
                score += 15
                reasons.append("Matches your preferred learning style")
        
        # Duration matching
        if profile and "daily_hours" in profile:
            daily_hours = profile["daily_hours"]
            course_weeks = course["duration_hours"] / (daily_hours * 7)
            if 4 <= course_weeks <= 12:
                score += 10
                reasons.append("Good duration for your pace")
            elif course_weeks > 12:
                reasons.append("Longer course - more time needed")
        
        # Rating
        score += course["rating"] * 5
        reasons.append(f"Highly rated ({course['rating']}/5)")
        
        scored_courses.append({
            **course,
            "score": score,
            "recommendation_reasons": reasons,
            "estimated_weeks": course["duration_hours"] / (profile.get("daily_hours", 2) * 7) if profile else None
        })
    
    # Sort by score
    scored_courses.sort(key=lambda x: x["score"], reverse=True)
    
    return {
        "skill": skill_name,
        "total_courses_found": len(scored_courses),
        "top_recommendations": scored_courses[:6],
        "all_courses": scored_courses,
        "recommendation_summary": f"Found {len(scored_courses)} courses across all categories. Top choice: {scored_courses[0]['title']} on {scored_courses[0]['platform']}"
    }

def get_course(course_id):
    """Get detailed information about a specific course"""
    for courses in COURSE_DATABASE.values():
        for course in courses:
            if course["id"] == course_id:
                return course
    return None

def filter_courses(skill_name, filters=None):
    """
    Filter courses by criteria
    
    Args:
        skill_name: Skill name
        filters: {
            "price_max": 50,
            "level": "Beginner",
            "platform": "Udemy",
            "duration_max_hours": 30,
            "min_rating": 4.5
        }
    """
    courses = COURSE_DATABASE.get(skill_name, [])
    
    if not filters:
        return courses
    
    filtered = courses
    
    # Filter by level
    if "level" in filters:
        filtered = [c for c in filtered if filters["level"].lower() in c["level"].lower()]
    
    # Filter by platform
    if "platform" in filters:
        filtered = [c for c in filtered if c["platform"] == filters["platform"]]
    
    # Filter by price
    if "price_max" in filters:
        filtered = [c for c in filtered if (
            "Free" in c["price"] or 
            float(c["price"].replace("$", "").split("/")[0]) <= filters["price_max"]
        )]
    
    # Filter by duration
    if "duration_max_hours" in filters:
        filtered = [c for c in filtered if c["duration_hours"] <= filters["duration_max_hours"]]
    
    # Filter by rating
    if "min_rating" in filters:
        filtered = [c for c in filtered if c["rating"] >= filters["min_rating"]]
    
    return filtered
