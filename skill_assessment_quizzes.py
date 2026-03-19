# skill_assessment_quizzes.py
# Comprehensive skill assessment quizzes

SKILL_ASSESSMENT_QUIZZES = {
    
    # ========================================================================
    # PROGRAMMING FUNDAMENTALS QUIZ
    # ========================================================================
    "programming_fundamentals": {
        "title": "Programming Fundamentals",
        "description": "Assess your programming knowledge",
        "time_limit": 10,  # minutes
        "difficulty": "Beginner-Intermediate",
        "questions": [
            {
                "id": "prog_1",
                "question": "What is a variable?",
                "options": [
                    "A name that stores a value in memory",
                    "A type of programming language",
                    "A function that changes",
                    "A mathematical constant"
                ],
                "correct": 0,
                "explanation": "A variable is a named location in memory that holds a value"
            },
            {
                "id": "prog_2",
                "question": "What does a loop do?",
                "options": [
                    "Creates an error",
                    "Repeats code multiple times",
                    "Stores data",
                    "Defines a function"
                ],
                "correct": 1,
                "explanation": "Loops execute a block of code multiple times"
            },
            {
                "id": "prog_3",
                "question": "What is a function?",
                "options": [
                    "A variable that stores numbers",
                    "Reusable block of code that performs a task",
                    "A type of data",
                    "A programming error"
                ],
                "correct": 1,
                "explanation": "Functions are reusable blocks of code for specific tasks"
            },
            {
                "id": "prog_4",
                "question": "What is debugging?",
                "options": [
                    "Writing code",
                    "Finding and fixing errors",
                    "Running a program",
                    "Creating variables"
                ],
                "correct": 1,
                "explanation": "Debugging is the process of finding and fixing bugs/errors"
            },
            {
                "id": "prog_5",
                "question": "What is an array/list?",
                "options": [
                    "A single value",
                    "An ordered collection of values",
                    "A function definition",
                    "A type of error"
                ],
                "correct": 1,
                "explanation": "Arrays/lists store multiple values in an ordered sequence"
            }
                ,
                {
                    "id": "prog_6",
                    "question": "What is a conditional statement?",
                    "options": [
                        "A loop that repeats",
                        "A statement that executes code based on a condition",
                        "A way to store data",
                        "A type of function"
                    ],
                    "correct": 1,
                    "explanation": "Conditionals let you branch logic based on true/false checks"
                },
                {
                    "id": "prog_7",
                    "question": "What's the purpose of comments in code?",
                    "options": [
                        "Execute faster",
                        "Document and explain code",
                        "Encrypt code",
                        "Store variables"
                    ],
                    "correct": 1,
                    "explanation": "Comments help explain and document code for humans"
                },
                {
                    "id": "prog_8",
                    "question": "What is code refactoring?",
                    "options": [
                        "Deleting code",
                        "Changing code structure without changing behavior",
                        "Running code faster",
                        "Creating new features only"
                    ],
                    "correct": 1,
                    "explanation": "Refactoring improves code structure while keeping functionality"
                }
        ]
    },

    # ========================================================================
    # PROBLEM SOLVING & LOGIC QUIZ
    # ========================================================================
    "problem_solving": {
        "title": "Problem Solving & Logic",
        "description": "Test your logical reasoning",
        "time_limit": 15,
        "difficulty": "Intermediate",
        "questions": [
            {
                "id": "logic_1",
                "question": "When solving a problem, what's the first step?",
                "options": [
                    "Start coding immediately",
                    "Understand the problem",
                    "Copy from StackOverflow",
                    "Ask someone else"
                ],
                "correct": 1,
                "explanation": "Understanding the problem is crucial before solving it"
            },
            {
                "id": "logic_2",
                "question": "What's algorithmic complexity?",
                "options": [
                    "How hard it is to understand",
                    "How much time and space an algorithm needs",
                    "The number of lines of code",
                    "The programming language used"
                ],
                "correct": 1,
                "explanation": "Complexity measures time and space efficiency"
            },
            {
                "id": "logic_3",
                "question": "If a task has 2 subtasks (each 5 mins), total time is?",
                "options": [
                    "5 minutes",
                    "10 minutes",
                    "2.5 minutes",
                    "20 minutes"
                ],
                "correct": 1,
                "explanation": "5 + 5 = 10 minutes total"
            },
            {
                "id": "logic_4",
                "question": "What's the benefit of breaking problems into smaller parts?",
                "options": [
                    "Wastes more time",
                    "Makes problems easier to solve",
                    "Confuses the solution",
                    "Reduces code quality"
                ],
                "correct": 1,
                "explanation": "Decomposition makes complex problems manageable"
            },
            {
                "id": "logic_5",
                "question": "What's edge case handling?",
                "options": [
                    "Using the edge of your desk",
                    "Testing unusual/extreme inputs",
                    "A programming error",
                    "A type of variable"
                ],
                "correct": 1,
                "explanation": "Edge cases are unusual but valid inputs that should be tested"
            }
                ,
                {
                    "id": "logic_6",
                    "question": "What's heuristic approach mean?",
                    "options": [
                        "Exact solution always",
                        "Rule-of-thumb approach to find a good solution",
                        "A formal proof",
                        "Copying code"
                    ],
                    "correct": 1,
                    "explanation": "Heuristics are practical approaches that yield good solutions"
                },
                {
                    "id": "logic_7",
                    "question": "What's greedy algorithm approach?",
                    "options": [
                        "Considering all possibilities",
                        "Making the locally optimal choice at each step",
                        "Random selection",
                        "Backtracking always"
                    ],
                    "correct": 1,
                    "explanation": "Greedy algorithms make locally optimal choices hoping for global optimum"
                },
                {
                    "id": "logic_8",
                    "question": "Why write pseudocode before coding?",
                    "options": [
                        "To avoid documentation",
                        "To plan logic in plain language",
                        "To test performance",
                        "To compile it"
                    ],
                    "correct": 1,
                    "explanation": "Pseudocode helps design solutions without syntax concerns"
                }
        ]
    },

    # ========================================================================
    # DATA STRUCTURES QUIZ
    # ========================================================================
    "data_structures": {
        "title": "Data Structures",
        "description": "Understand common data structures",
        "time_limit": 12,
        "difficulty": "Intermediate",
        "questions": [
            {
                "id": "ds_1",
                "question": "What's the main advantage of a Hash Map?",
                "options": [
                    "Always sorted",
                    "Fast lookups",
                    "Small memory",
                    "Easy to visualize"
                ],
                "correct": 1,
                "explanation": "Hash maps provide O(1) lookup time"
            },
            {
                "id": "ds_2",
                "question": "What's a linked list?",
                "options": [
                    "A list on the web",
                    "Elements connected by pointers/references",
                    "A type of array",
                    "A database structure"
                ],
                "correct": 1,
                "explanation": "Linked lists connect nodes through references"
            },
            {
                "id": "ds_3",
                "question": "Stack follows which principle?",
                "options": [
                    "First In First Out (FIFO)",
                    "Last In First Out (LIFO)",
                    "Random order",
                    "Sorted order"
                ],
                "correct": 1,
                "explanation": "Stacks follow LIFO principle"
            },
            {
                "id": "ds_4",
                "question": "Queue follows which principle?",
                "options": [
                    "LIFO",
                    "FIFO",
                    "Random",
                    "Sorted"
                ],
                "correct": 1,
                "explanation": "Queues follow FIFO principle"
            },
            {
                "id": "ds_5",
                "question": "What's a tree data structure used for?",
                "options": [
                    "Growing plants",
                    "Hierarchical data organization",
                    "Storing strings",
                    "Random storage"
                ],
                "correct": 1,
                "explanation": "Trees represent hierarchical relationships"
            }
            ,
            {
                "id": "ds_6",
                "question": "What's a graph used to model?",
                "options": [
                    "Hierarchies",
                    "Pairs of connected entities (nodes/edges)",
                    "Linear arrays",
                    "Sorted lists"
                ],
                "correct": 1,
                "explanation": "Graphs model relationships between entities"
            },
            {
                "id": "ds_7",
                "question": "What's amortized analysis?",
                "options": [
                    "Worst-case only",
                    "Average cost over sequence of operations",
                    "Space complexity",
                    "A sorting algorithm"
                ],
                "correct": 1,
                "explanation": "Amortized analysis spreads cost across operations"
            },
            {
                "id": "ds_8",
                "question": "What's a priority queue used for?",
                "options": [
                    "Random access",
                    "Retrieving highest-priority element efficiently",
                    "Sorting strings",
                    "Storing characters"
                ],
                "correct": 1,
                "explanation": "Priority queues return highest (or lowest) priority elements efficiently"
            }
        ]
    },

    # ========================================================================
    # WEB DEVELOPMENT QUIZ
    # ========================================================================
    "web_development": {
        "title": "Web Development Basics",
        "description": "Test your web development knowledge",
        "time_limit": 12,
        "difficulty": "Intermediate",
        "questions": [
            {
                "id": "web_1",
                "question": "What does HTML do?",
                "options": [
                    "Styles the website",
                    "Structures web content",
                    "Creates interactivity",
                    "Stores data"
                ],
                "correct": 1,
                "explanation": "HTML provides structure to web pages"
            },
            {
                "id": "web_2",
                "question": "What's the role of CSS?",
                "options": [
                    "Structures content",
                    "Styles and layouts",
                    "Creates logic",
                    "Stores databases"
                ],
                "correct": 1,
                "explanation": "CSS handles styling and layout"
            },
            {
                "id": "web_3",
                "question": "What's JavaScript primarily used for?",
                "options": [
                    "Server storage",
                    "Client-side interactivity",
                    "Database management",
                    "Styling"
                ],
                "correct": 1,
                "explanation": "JavaScript adds interactivity to web pages"
            },
            {
                "id": "web_4",
                "question": "What's a REST API?",
                "options": [
                    "A way to take breaks",
                    "A method for server-client communication",
                    "A type of database",
                    "A styling framework"
                ],
                "correct": 1,
                "explanation": "REST APIs enable server-client communication"
            },
            {
                "id": "web_5",
                "question": "What's responsive design?",
                "options": [
                    "Quick website loading",
                    "Works on all device sizes",
                    "Uses many colors",
                    "Requires JavaScript"
                ],
                "correct": 1,
                "explanation": "Responsive design adapts to different screen sizes"
            }
            ,
            {
                "id": "web_6",
                "question": "What is the DOM?",
                "options": [
                    "A styling library",
                    "Document Object Model representing HTML structure",
                    "A database",
                    "A server"
                ],
                "correct": 1,
                "explanation": "DOM is the structured representation of the page"
            },
            {
                "id": "web_7",
                "question": "What does AJAX allow?",
                "options": [
                    "Synchronous page reloads",
                    "Background server requests without full reload",
                    "CSS animations",
                    "Python execution in browser"
                ],
                "correct": 1,
                "explanation": "AJAX enables asynchronous server communication in pages"
            },
            {
                "id": "web_8",
                "question": "What's accessibility in web design?",
                "options": [
                    "Using many colors",
                    "Designing for users with diverse abilities",
                    "Faster load times",
                    "SEO only"
                ],
                "correct": 1,
                "explanation": "Accessibility ensures websites work for people with disabilities"
            }
        ]
    },

    # ========================================================================
    # DATABASES & SQL QUIZ
    # ========================================================================
    "databases": {
        "title": "Databases & SQL",
        "description": "Test your database knowledge",
        "time_limit": 12,
        "difficulty": "Intermediate",
        "questions": [
            {
                "id": "db_1",
                "question": "What's SQL primarily used for?",
                "options": [
                    "Website styling",
                    "Querying and managing data",
                    "Building apps",
                    "Creating graphics"
                ],
                "correct": 1,
                "explanation": "SQL is the language for database queries"
            },
            {
                "id": "db_2",
                "question": "What's a primary key?",
                "options": [
                    "The first column",
                    "Uniquely identifies each row",
                    "A password",
                    "A type of index"
                ],
                "correct": 1,
                "explanation": "Primary keys uniquely identify records"
            },
            {
                "id": "db_3",
                "question": "What's normalization in databases?",
                "options": [
                    "Making data normal",
                    "Organizing data to reduce redundancy",
                    "Encrypting data",
                    "Backing up data"
                ],
                "correct": 1,
                "explanation": "Normalization eliminates data redundancy"
            },
            {
                "id": "db_4",
                "question": "What's a JOIN in SQL?",
                "options": [
                    "Combining rows from multiple tables",
                    "Creating new tables",
                    "Deleting data",
                    "A type of error"
                ],
                "correct": 1,
                "explanation": "JOINs combine data from multiple tables"
            },
            {
                "id": "db_5",
                "question": "What's an index in a database?",
                "options": [
                    "A table of contents",
                    "A structure for faster searches",
                    "A backup method",
                    "A type of table"
                ],
                "correct": 1,
                "explanation": "Indexes speed up database queries"
            }
            ,
            {
                "id": "db_6",
                "question": "What's ACID in databases?",
                "options": [
                    "A chemical",
                    "Set of transactional properties (Atomicity, Consistency, Isolation, Durability)",
                    "Indexing type",
                    "Compression method"
                ],
                "correct": 1,
                "explanation": "ACID describes reliable transaction properties"
            },
            {
                "id": "db_7",
                "question": "What is denormalization used for?",
                "options": [
                    "Reducing redundancy",
                    "Improving read performance by duplicating data",
                    "Encrypting data",
                    "Backing up data"
                ],
                "correct": 1,
                "explanation": "Denormalization trades redundancy for faster reads"
            },
            {
                "id": "db_8",
                "question": "What's a transaction log?",
                "options": [
                    "A user log",
                    "Record of database changes for recovery",
                    "A performance metric",
                    "A query"
                ],
                "correct": 1,
                "explanation": "Transaction logs help recover and audit database changes"
            }
        ]
    },

    # ========================================================================
    # PYTHON BASICS QUIZ
    # ========================================================================
    "python_basics": {
        "title": "Python Basics",
        "description": "Test your Python knowledge",
        "time_limit": 10,
        "difficulty": "Beginner",
        "questions": [
            {
                "id": "py_1",
                "question": "What's Python primarily known for?",
                "options": [
                    "Web design",
                    "Readability and simplicity",
                    "Gaming",
                    "Graphics"
                ],
                "correct": 1,
                "explanation": "Python is known for clean, readable syntax"
            },
            {
                "id": "py_2",
                "question": "What's a Python virtual environment?",
                "options": [
                    "A computer in the cloud",
                    "Isolated Python setup for projects",
                    "A game",
                    "A type of file"
                ],
                "correct": 1,
                "explanation": "Virtual environments isolate project dependencies"
            },
            {
                "id": "py_3",
                "question": "What does 'pip' do?",
                "options": [
                    "Installs Python",
                    "Manages Python packages",
                    "Edits code",
                    "Runs programs"
                ],
                "correct": 1,
                "explanation": "pip is the Python package manager"
            },
            {
                "id": "py_4",
                "question": "What's a Python decorator?",
                "options": [
                    "A visual element",
                    "Modifies functions or classes",
                    "A type of loop",
                    "A string type"
                ],
                "correct": 1,
                "explanation": "Decorators modify function or class behavior"
            },
            {
                "id": "py_5",
                "question": "What's list comprehension?",
                "options": [
                    "Understanding lists",
                    "Concise way to create lists",
                    "A reading technique",
                    "A type of loop"
                ],
                "correct": 1,
                "explanation": "List comprehensions create lists concisely"
            }
            ,
            {
                "id": "py_6",
                "question": "What's a dictionary in Python?",
                "options": [
                    "An ordered sequence",
                    "Key-value mapping",
                    "A list of functions",
                    "A loop"
                ],
                "correct": 1,
                "explanation": "Dictionaries map keys to values"
            },
            {
                "id": "py_7",
                "question": "What's exception handling used for?",
                "options": [
                    "Optimizing speed",
                    "Handling runtime errors gracefully",
                    "Formatting strings",
                    "Declaring variables"
                ],
                "correct": 1,
                "explanation": "Try/except blocks handle errors at runtime"
            },
            {
                "id": "py_8",
                "question": "What is a module in Python?",
                "options": [
                    "A function",
                    "A file containing Python definitions and statements",
                    "A data type",
                    "A package manager"
                ],
                "correct": 1,
                "explanation": "Modules group related code in files"
            }
        ]
    },

    # ========================================================================
    # MATH & ALGORITHMS QUIZ
    # ========================================================================
    "math_algorithms": {
        "title": "Math & Algorithms",
        "description": "Test mathematical and algorithmic thinking",
        "time_limit": 15,
        "difficulty": "Intermediate-Advanced",
        "questions": [
            {
                "id": "math_1",
                "question": "What's Big O notation used for?",
                "options": [
                    "Email notation",
                    "Measuring algorithm efficiency",
                    "Mathematical operations",
                    "Sorting data"
                ],
                "correct": 1,
                "explanation": "Big O describes algorithmic time/space complexity"
            },
            {
                "id": "math_2",
                "question": "What's O(n) complexity?",
                "options": [
                    "Constant time",
                    "Linear time with input size",
                    "Quadratic time",
                    "Exponential time"
                ],
                "correct": 1,
                "explanation": "O(n) means execution time grows linearly with input"
            },
            {
                "id": "math_3",
                "question": "What's recursion?",
                "options": [
                    "A loop",
                    "Function calling itself",
                    "A data structure",
                    "A sorting method"
                ],
                "correct": 1,
                "explanation": "Recursion is when a function calls itself"
            },
            {
                "id": "math_4",
                "question": "What's a binary search?",
                "options": [
                    "Searching for 0s and 1s",
                    "Dividing search space in half repeatedly",
                    "Random searching",
                    "Sorting data"
                ],
                "correct": 1,
                "explanation": "Binary search efficiently finds items in sorted data"
            },
            {
                "id": "math_5",
                "question": "What does 'sorting' do?",
                "options": [
                    "Arranges data in order",
                    "Deletes data",
                    "Encrypts data",
                    "Compresses data"
                ],
                "correct": 1,
                "explanation": "Sorting arranges elements in a specific order"
            }
            ,
            {
                "id": "math_6",
                "question": "What's the median of [1,2,3,4,5]?",
                "options": [
                    "2",
                    "3",
                    "4",
                    "5"
                ],
                "correct": 1,
                "explanation": "Median is the middle value"
            },
            {
                "id": "math_7",
                "question": "What's dynamic programming used for?",
                "options": [
                    "Greedy choices",
                    "Breaking problems into overlapping subproblems and caching",
                    "Sorting data",
                    "Compiling code"
                ],
                "correct": 1,
                "explanation": "Dynamic programming uses memoization for optimal substructure problems"
            },
            {
                "id": "ux_5",
                "question": "What is a persona in UX design?",
                "options": [
                    "A character in a game",
                    "Fictional representation of target user",
                    "A design pattern",
                    "A testing method"
                ],
                "correct": 1,
                "explanation": "Personas are fictional characters representing user types"
            }
        ]
    },

    # ========================================================================
    # NATURAL LANGUAGE PROCESSING
    # ========================================================================
    "nlp": {
        "title": "Natural Language Processing",
        "description": "Test your NLP knowledge",
        "time_limit": 10,
        "difficulty": "Advanced",
        "questions": [
            {
                "id": "nlp_1",
                "question": "What is tokenization in NLP?",
                "options": [
                    "Converting text to tokens",
                    "Breaking text into smaller units",
                    "Translating languages",
                    "Generating text"
                ],
                "correct": 1,
                "explanation": "Tokenization breaks text into words, sentences, or subwords"
            },
            {
                "id": "nlp_2",
                "question": "What is sentiment analysis?",
                "options": [
                    "Analyzing grammar",
                    "Determining emotional tone of text",
                    "Translating text",
                    "Summarizing text"
                ],
                "correct": 1,
                "explanation": "Sentiment analysis identifies opinions and emotions in text"
            },
            {
                "id": "nlp_3",
                "question": "What is a word embedding?",
                "options": [
                    "Text formatting",
                    "Dense vector representation of words",
                    "Word count",
                    "Grammar check"
                ],
                "correct": 1,
                "explanation": "Word embeddings represent words as numerical vectors"
            },
            {
                "id": "nlp_4",
                "question": "What is Named Entity Recognition (NER)?",
                "options": [
                    "Naming variables",
                    "Identifying entities like persons, organizations",
                    "Creating new words",
                    "Translating names"
                ],
                "correct": 1,
                "explanation": "NER identifies and classifies named entities in text"
            },
            {
                "id": "nlp_5",
                "question": "What is a transformer model?",
                "options": [
                    "Power grid component",
                    "Architecture using self-attention",
                    "Data conversion tool",
                    "Text format"
                ],
                "correct": 1,
                "explanation": "Transformers use self-attention mechanisms for NLP tasks"
            }
        ]
    },

    # ========================================================================
    # DOCKER & KUBERNETES
    # ========================================================================
    "docker_kubernetes": {
        "title": "Docker & Kubernetes",
        "description": "Test your container knowledge",
        "time_limit": 10,
        "difficulty": "Intermediate",
        "questions": [
            {
                "id": "dk_1",
                "question": "What is a Docker container?",
                "options": [
                    "Physical shipping container",
                    "Lightweight executable package",
                    "Virtual machine",
                    "Storage unit"
                ],
                "correct": 1,
                "explanation": "Containers package application with its dependencies"
            },
            {
                "id": "dk_2",
                "question": "What is a Dockerfile?",
                "options": [
                    "Container runtime",
                    "Script to build container images",
                    "Container registry",
                    "Orchestration tool"
                ],
                "correct": 1,
                "explanation": "Dockerfile contains instructions to build a container image"
            },
            {
                "id": "dk_3",
                "question": "What is Kubernetes?",
                "options": [
                    "Container orchestration platform",
                    "Programming language",
                    "Database system",
                    "Web server"
                ],
                "correct": 0,
                "explanation": "Kubernetes automates container deployment and management"
            },
            {
                "id": "dk_4",
                "question": "What is a Kubernetes pod?",
                "options": [
                    "Storage unit",
                    "Smallest deployable unit",
                    "Network protocol",
                    "Container registry"
                ],
                "correct": 1,
                "explanation": "A pod is the smallest deployable unit in Kubernetes"
            },
            {
                "id": "dk_5",
                "question": "What is container orchestration?",
                "options": [
                    "Playing music",
                    "Managing containerized applications",
                    "Building containers",
                    "Container storage"
                ],
                "correct": 1,
                "explanation": "Orchestration automates deployment and scaling of containers"
            }
        ]
    },

    # ========================================================================
    # SOFTWARE ARCHITECTURE
    # ========================================================================
    "software_architecture": {
        "title": "Software Architecture",
        "description": "Test your architecture knowledge",
        "time_limit": 10,
        "difficulty": "Advanced",
        "questions": [
            {
                "id": "sa_1",
                "question": "What is microservices architecture?",
                "options": [
                    "Small code files",
                    "Application broken into small services",
                    "Monolithic design",
                    "Single function programs"
                ],
                "correct": 1,
                "explanation": "Microservices divide app into independently deployable services"
            },
            {
                "id": "sa_2",
                "question": "What is the SOLID principle?",
                "options": [
                    "Solid state storage",
                    "Design principles for OOP",
                    "Code thickness",
                    "Architecture pattern"
                ],
                "correct": 1,
                "explanation": "SOLID is five design principles for maintainable code"
            },
            {
                "id": "sa_3",
                "question": "What is a REST API?",
                "options": [
                    "State transfer architectural style",
                    "Database system",
                    "Programming language",
                    "Web browser"
                ],
                "correct": 0,
                "explanation": "REST is an architectural style for web services"
            },
            {
                "id": "sa_4",
                "question": "What is event-driven architecture?",
                "options": [
                    "Streaming video",
                    "System responding to events",
                    "Sequential processing",
                    "Batch processing"
                ],
                "correct": 1,
                "explanation": "Event-driven architecture responds to events or messages"
            },
            {
                "id": "sa_5",
                "question": "What is a design pattern?",
                "options": [
                    "Drawing tool",
                    "Reusable solution to common problems",
                    "Code format",
                    "Testing method"
                ],
                "correct": 1,
                "explanation": "Design patterns are reusable solutions to recurring problems"
            }
        ]
    },

    # ========================================================================
    # TECHNICAL WRITING
    # ========================================================================
    "technical_writing": {
        "title": "Technical Writing",
        "description": "Test your technical writing knowledge",
        "time_limit": 10,
        "difficulty": "Beginner",
        "questions": [
            {
                "id": "tw_1",
                "question": "What is documentation?",
                "options": [
                    "Public records",
                    "Written explanation of technical information",
                    "Code only",
                    "Marketing material"
                ],
                "correct": 1,
                "explanation": "Documentation provides written guidance about a product or system"
            },
            {
                "id": "tw_2",
                "question": "What is a README file?",
                "options": [
                    "Reading book",
                    "Document explaining a project",
                    "Code file",
                    "Database"
                ],
                "correct": 1,
                "explanation": "README introduces and explains a project"
            },
            {
                "id": "tw_3",
                "question": "What is API documentation?",
                "options": [
                    "Historical records",
                    "Description of how to use an API",
                    "Code implementation",
                    "Test cases"
                ],
                "correct": 1,
                "explanation": "API docs explain how to use application programming interfaces"
            },
            {
                "id": "tw_4",
                "question": "What is the purpose of comments in code?",
                "options": [
                    "Make code run",
                    "Explain code for developers",
                    "Increase speed",
                    "Hide code"
                ],
                "correct": 1,
                "explanation": "Comments explain code functionality to developers"
            },
            {
                "id": "tw_5",
                "question": "What is a style guide?",
                "options": [
                    "Fashion guide",
                    "Document with writing standards",
                    "Code compiler",
                    "Testing tool"
                ],
                "correct": 1,
                "explanation": "Style guides define consistent writing and formatting rules"
            }
        ]
    },

    # ========================================================================
    # DATA VISUALIZATION
    # ========================================================================
    "data_visualization": {
        "title": "Data Visualization",
        "description": "Test your data viz knowledge",
        "time_limit": 10,
        "difficulty": "Intermediate",
        "questions": [
            {
                "id": "dv_1",
                "question": "What is a bar chart used for?",
                "options": [
                    "Showing trends over time",
                    "Comparing categories",
                    "Displaying distributions",
                    "Network relationships"
                ],
                "correct": 1,
                "explanation": "Bar charts compare values across different categories"
            },
            {
                "id": "dv_2",
                "question": "What is a scatter plot?",
                "options": [
                    "Random dots",
                    "Showing relationship between two variables",
                    "Timeline display",
                    "Pie chart variant"
                ],
                "correct": 1,
                "explanation": "Scatter plots show correlation between two variables"
            },
            {
                "id": "dv_3",
                "question": "When should you use a pie chart?",
                "options": [
                    "For large datasets",
                    "Showing parts of a whole",
                    "Comparing trends",
                    "Time series data"
                ],
                "correct": 1,
                "explanation": "Pie charts show proportions or percentages of a whole"
            },
            {
                "id": "dv_4",
                "question": "What is a heat map?",
                "options": [
                    "Temperature display",
                    "Color-coded matrix showing values",
                    "Weather chart",
                    "Network diagram"
                ],
                "correct": 1,
                "explanation": "Heat maps use color to represent values in a matrix"
            },
            {
                "id": "dv_5",
                "question": "What is dashboard design?",
                "options": [
                    "Car dashboard",
                    "Visual display of key metrics",
                    "Database query",
                    "Code editor"
                ],
                "correct": 1,
                "explanation": "Dashboards present key metrics in an organized view"
            }
        ]
    },

    # ========================================================================
    # API DESIGN
    # ========================================================================
    "api_design": {
        "title": "API Design",
        "description": "Test your API design knowledge",
        "time_limit": 10,
        "difficulty": "Intermediate",
        "questions": [
            {
                "id": "api_1",
                "question": "What does API stand for?",
                "options": [
                    "Application Programming Interface",
                    "Advanced Program Integration",
                    "Automated Protocol Interface",
                    "Application Process Integration"
                ],
                "correct": 0,
                "explanation": "API defines how software components interact"
            },
            {
                "id": "api_2",
                "question": "What are HTTP methods?",
                "options": [
                    "Programming languages",
                    "Verbs for API operations",
                    "Data formats",
                    "Security protocols"
                ],
                "correct": 1,
                "explanation": "HTTP methods like GET, POST define operations"
            },
            {
                "id": "api_3",
                "question": "What is JSON?",
                "options": [
                    "Programming language",
                    "Lightweight data interchange format",
                    "Database",
                    "Operating system"
                ],
                "correct": 1,
                "explanation": "JSON is a common data format for APIs"
            },
            {
                "id": "api_4",
                "question": "What is authentication?",
                "options": [
                    "Authorization",
                    "Verifying user identity",
                    "Data encryption",
                    "Network protocol"
                ],
                "correct": 1,
                "explanation": "Authentication verifies who a user is"
            },
            {
                "id": "api_5",
                "question": "What is rate limiting?",
                "options": [
                    "Speed control",
                    "Controlling API request frequency",
                    "Data compression",
                    "Error handling"
                ],
                "correct": 1,
                "explanation": "Rate limiting prevents abuse by limiting requests"
            }
        ]
    },

    # ========================================================================
    # LINUX/UNIX
    # ========================================================================
    "linux_unix": {
        "title": "Linux/Unix Fundamentals",
        "description": "Test your Linux knowledge",
        "time_limit": 10,
        "difficulty": "Beginner",
        "questions": [
            {
                "id": "lu_1",
                "question": "What is the Linux kernel?",
                "options": [
                    "Graphical interface",
                    "Core of the operating system",
                    "Application program",
                    "File manager"
                ],
                "correct": 1,
                "explanation": "Kernel is the core component of Linux OS"
            },
            {
                "id": "lu_2",
                "question": "What does the ls command do?",
                "options": [
                    "Lists files",
                    "Deletes files",
                    "Creates files",
                    "Edits files"
                ],
                "correct": 0,
                "explanation": "ls lists directory contents"
            },
            {
                "id": "lu_3",
                "question": "What is a shell?",
                "options": [
                    "Outer covering",
                    "Command-line interpreter",
                    "File system",
                    "Network protocol"
                ],
                "correct": 1,
                "explanation": "Shell is a command-line interface to interact with OS"
            },
            {
                "id": "lu_4",
                "question": "What does chmod do?",
                "options": [
                    "Change mode",
                    "Modifies file permissions",
                    "Creates directory",
                    "Deletes files"
                ],
                "correct": 1,
                "explanation": "chmod changes file read/write/execute permissions"
            },
            {
                "id": "lu_5",
                "question": "What is sudo?",
                "options": [
                    "Super user do",
                    "Execute command as root",
                    "File transfer",
                    "Text editor"
                ],
                "correct": 1,
                "explanation": "sudo allows elevated privileges for commands"
            }
        ]
    },

    # ========================================================================
    # MICROSERVICES
    # ========================================================================
    "microservices": {
        "title": "Microservices Architecture",
        "description": "Test your microservices knowledge",
        "time_limit": 10,
        "difficulty": "Advanced",
        "questions": [
            {
                "id": "ms_1",
                "question": "What is service discovery?",
                "options": [
                    "Finding services automatically",
                    "Web search",
                    "DNS lookup",
                    "Network scan"
                ],
                "correct": 0,
                "explanation": "Service discovery lets services find each other"
            },
            {
                "id": "ms_2",
                "question": "What is API gateway?",
                "options": [
                    "Door hardware",
                    "Entry point for microservices",
                    "Network router",
                    "Database"
                ],
                "correct": 1,
                "explanation": "API gateway routes requests to microservices"
            },
            {
                "id": "ms_3",
                "question": "What is containerization?",
                "options": [
                    "Shipping containers",
                    "Packaging apps in containers",
                    "Data storage",
                    "Network config"
                ],
                "correct": 1,
                "explanation": "Containerization packages apps with dependencies"
            },
            {
                "id": "ms_4",
                "question": "What is CI/CD?",
                "options": [
                    "Continuous Integration/Deployment",
                    "Code library",
                    "Version control",
                    "Database system"
                ],
                "correct": 0,
                "explanation": "CI/CD automates building, testing, and deployment"
            },
            {
                "id": "ms_5",
                "question": "What is distributed tracing?",
                "options": [
                    "GPS tracking",
                    "Following requests across services",
                    "Network monitoring",
                    "Log analysis"
                ],
                "correct": 1,
                "explanation": "Distributed tracing tracks requests through microservices"
            }
        ]
    },

    # ========================================================================
    # CLOUD COMPUTING
    # ========================================================================
    "cloud_computing": {
        "title": "Cloud Computing",
        "description": "Test your cloud computing knowledge",
        "time_limit": 10,
        "difficulty": "Intermediate",
        "questions": [
            {
                "id": "cc_1",
                "question": "What is IaaS?",
                "options": [
                    "Internet as a Service",
                    "Infrastructure as a Service",
                    "Integration as a Service",
                    "Image as a Service"
                ],
                "correct": 1,
                "explanation": "IaaS provides virtualized computing resources"
            },
            {
                "id": "cc_2",
                "question": "What is SaaS?",
                "options": [
                    "Software as a Service",
                    "Storage as a Service",
                    "Security as a Service",
                    "Server as a Service"
                ],
                "correct": 0,
                "explanation": "SaaS delivers software over the internet"
            },
            {
                "id": "cc_3",
                "question": "What is serverless computing?",
                "options": [
                    "No servers involved",
                    "Computing without server management",
                    "Offline computing",
                    "Dedicated servers"
                ],
                "correct": 1,
                "explanation": "Serverless runs code without managing servers"
            },
            {
                "id": "cc_4",
                "question": "What is a virtual machine?",
                "options": [
                    "Computer simulation",
                    "Emulated computer system",
                    "Physical computer",
                    "Network device"
                ],
                "correct": 1,
                "explanation": "VM is an emulated computer running on physical hardware"
            },
            {
                "id": "cc_5",
                "question": "What is auto-scaling?",
                "options": [
                    "Automatic resizing",
                    "Automatically adjusting resources",
                    "Manual scaling",
                    "Fixed resources"
                ],
                "correct": 1,
                "explanation": "Auto-scaling adjusts resources based on demand"
            }
        ]
    },

    # ========================================================================
    # VERSION CONTROL
    # ========================================================================
    "version_control": {
        "title": "Version Control (Git)",
        "description": "Test your Git knowledge",
        "time_limit": 10,
        "difficulty": "Beginner",
        "questions": [
            {
                "id": "vc_1",
                "question": "What is Git?",
                "options": [
                    "A programming language",
                    "Distributed version control system",
                    "Database",
                    "Web browser"
                ],
                "correct": 1,
                "explanation": "Git tracks changes in source code"
            },
            {
                "id": "vc_2",
                "question": "What is a commit?",
                "options": [
                    "Sending email",
                    "Saving changes to repository",
                    "Deleting files",
                    "Creating branch"
                ],
                "correct": 1,
                "explanation": "Commit saves changes to repository history"
            },
            {
                "id": "vc_3",
                "question": "What is a branch?",
                "options": [
                    "Tree part",
                    "Parallel version of code",
                    "File folder",
                    "Code comment"
                ],
                "correct": 1,
                "explanation": "Branch allows parallel development"
            },
            {
                "id": "vc_4",
                "question": "What does merge do?",
                "options": [
                    "Combines branches",
                    "Deletes code",
                    "Creates backup",
                    "Deploys code"
                ],
                "correct": 0,
                "explanation": "Merge combines changes from different branches"
            },
            {
                "id": "vc_5",
                "question": "What is a pull request?",
                "options": [
                    "Downloading files",
                    "Proposing changes for review",
                    "Sending email",
                    "Uploading code"
                ],
                "correct": 1,
                "explanation": "Pull request proposes and reviews code changes"
            }
        ]
    },

    # ========================================================================
    # BIG DATA
    # ========================================================================
    "big_data": {
        "title": "Big Data Fundamentals",
        "description": "Test your big data knowledge",
        "time_limit": 10,
        "difficulty": "Advanced",
        "questions": [
            {
                "id": "bd_1",
                "question": "What is Hadoop?",
                "options": [
                    "Elephant",
                    "Big data processing framework",
                    "Programming language",
                    "Database"
                ],
                "correct": 1,
                "explanation": "Hadoop processes large datasets across clusters"
            },
            {
                "id": "bd_2",
                "question": "What is Spark?",
                "options": [
                    "Fire",
                    "Big data processing engine",
                    "Database",
                    "Network tool"
                ],
                "correct": 1,
                "explanation": "Spark is fast big data processing engine"
            },
            {
                "id": "bd_3",
                "question": "What is data lake?",
                "options": [
                    "Natural water body",
                    "Centralized data storage",
                    "Data visualization",
                    "Network storage"
                ],
                "correct": 1,
                "explanation": "Data lake stores raw data in native format"
            },
            {
                "id": "bd_4",
                "question": "What is ETL?",
                "options": [
                    "Easy Tech Language",
                    "Extract, Transform, Load",
                    "Error Trapping Logic",
                    "External Transfer Link"
                ],
                "correct": 1,
                "explanation": "ETL extracts, transforms, and loads data"
            },
            {
                "id": "bd_5",
                "question": "What is MapReduce?",
                "options": [
                    "Navigation tool",
                    "Programming model for processing data",
                    "Database query",
                    "Network protocol"
                ],
                "correct": 1,
                "explanation": "MapReduce processes data in parallel"
            }
        ]
    },

    # ========================================================================
    # BUSINESS FUNDAMENTALS
    # ========================================================================
    "business_fundamentals": {
        "title": "Business Fundamentals",
        "description": "Test your business knowledge",
        "time_limit": 10,
        "difficulty": "Beginner",
        "questions": [
            {
                "id": "bf_1",
                "question": "What is a business model?",
                "options": [
                    "Company logo",
                    "Plan for generating revenue",
                    "Office layout",
                    "Employee schedule"
                ],
                "correct": 1,
                "explanation": "Business model describes how a company creates and delivers value"
            },
            {
                "id": "bf_2",
                "question": "What is ROI?",
                "options": [
                    "Return on Investment",
                    "Rate of Interest",
                    "Revenue of Industry",
                    "Risk of Investment"
                ],
                "correct": 0,
                "explanation": "ROI measures the profitability of an investment"
            },
            {
                "id": "bf_3",
                "question": "What is a startup?",
                "options": [
                    "Small business",
                    "Newly formed company seeking growth",
                    "Chain store",
                    "Government office"
                ],
                "correct": 1,
                "explanation": "Startup is a company in early stages seeking rapid growth"
            },
            {
                "id": "bf_4",
                "question": "What is bootstrapping in business?",
                "options": [
                    "Using bootstrap software",
                    "Self-funding without external investment",
                    "Hiring temporary staff",
                    "Outsourcing work"
                ],
                "correct": 1,
                "explanation": "Bootstrapping means growing with personal savings and revenue"
            },
            {
                "id": "bf_5",
                "question": "What is a pivot in business?",
                "options": [
                    "Turning around",
                    "Changing business strategy",
                    "Hiring new CEO",
                    "Opening new office"
                ],
                "correct": 1,
                "explanation": "Pivot means fundamentally changing business direction"
            }
        ]
    },

    # ========================================================================
    # MARKETING FUNDAMENTALS
    # ========================================================================
    "marketing_fundamentals": {
        "title": "Marketing Fundamentals",
        "description": "Test your marketing knowledge",
        "time_limit": 10,
        "difficulty": "Beginner",
        "questions": [
            {
                "id": "mk_1",
                "question": "What is a target audience?",
                "options": [
                    "Everyone",
                    "Specific group of potential customers",
                    "Competitors",
                    "Shareholders"
                ],
                "correct": 1,
                "explanation": "Target audience is the specific group you're marketing to"
            },
            {
                "id": "mk_2",
                "question": "What is brand awareness?",
                "options": [
                    "Company debt",
                    "How well people know your brand",
                    "Brand colors",
                    "Employee names"
                ],
                "correct": 1,
                "explanation": "Brand awareness measures recognition of your brand"
            },
            {
                "id": "mk_3",
                "question": "What is SEO?",
                "options": [
                    "Search Engine Optimization",
                    "Social Enterprise Online",
                    "Sales Executive Office",
                    "Standard Enterprise Operations"
                ],
                "correct": 0,
                "explanation": "SEO improves website visibility in search results"
            },
            {
                "id": "mk_4",
                "question": "What is content marketing?",
                "options": [
                    "Writing books",
                    "Creating valuable content to attract customers",
                    "Selling products",
                    "Advertising on TV"
                ],
                "correct": 1,
                "explanation": "Content marketing attracts audiences through valuable content"
            },
            {
                "id": "mk_5",
                "question": "What is a call-to-action (CTA)?",
                "options": [
                    "Phone call",
                    "Prompt encouraging action",
                    "Business meeting",
                    "Customer service"
                ],
                "correct": 1,
                "explanation": "CTA prompts users to take a specific action"
            }
        ]
    },

    # ========================================================================
    # FINANCE & ACCOUNTING
    # ========================================================================
    "finance_accounting": {
        "title": "Finance & Accounting",
        "description": "Test your finance knowledge",
        "time_limit": 10,
        "difficulty": "Intermediate",
        "questions": [
            {
                "id": "fa_1",
                "question": "What is a balance sheet?",
                "options": [
                    "Gym equipment",
                    "Financial statement showing assets and liabilities",
                    "Employee schedule",
                    "Marketing plan"
                ],
                "correct": 1,
                "explanation": "Balance sheet shows financial position at a point in time"
            },
            {
                "id": "fa_2",
                "question": "What is cash flow?",
                "options": [
                    "Water flow",
                    "Money moving in and out of business",
                    "Employee salary",
                    "Bank interest"
                ],
                "correct": 1,
                "explanation": "Cash flow tracks money entering and leaving a business"
            },
            {
                "id": "fa_3",
                "question": "What is profit margin?",
                "options": [
                    "Store discount",
                    "Percentage of revenue kept as profit",
                    "Tax rate",
                    "Employee bonus"
                ],
                "correct": 1,
                "explanation": "Profit margin shows profitability as a percentage of revenue"
            },
            {
                "id": "fa_4",
                "question": "What is equity?",
                "options": [
                    "Equality",
                    "Ownership value in a company",
                    "Debt",
                    "Salary"
                ],
                "correct": 1,
                "explanation": "Equity represents ownership stake in a business"
            },
            {
                "id": "fa_5",
                "question": "What is a budget?",
                "options": [
                    "Expense report",
                    "Plan for managing money",
                    "Tax form",
                    "Invoice"
                ],
                "correct": 1,
                "explanation": "Budget is a plan for income and expenses"
            }
        ]
    },

    # ========================================================================
    # LEADERSHIP & MANAGEMENT
    # ========================================================================
    "leadership_management": {
        "title": "Leadership & Management",
        "description": "Test your leadership knowledge",
        "time_limit": 10,
        "difficulty": "Intermediate",
        "questions": [
            {
                "id": "lm_1",
                "question": "What is leadership?",
                "options": [
                    "Being in charge",
                    "Influencing and guiding others",
                    "Managing files",
                    "Giving orders"
                ],
                "correct": 1,
                "explanation": "Leadership is inspiring and guiding others toward goals"
            },
            {
                "id": "lm_2",
                "question": "What is delegation?",
                "options": [
                    "Removing employees",
                    "Assigning tasks to others",
                    "Holding meetings",
                    "Firing staff"
                ],
                "correct": 1,
                "explanation": "Delegation assigns responsibility to team members"
            },
            {
                "id": "lm_3",
                "question": "What is emotional intelligence?",
                "options": [
                    "Being emotional",
                    "Understanding and managing emotions",
                    "High IQ",
                    "Technical skills"
                ],
                "correct": 1,
                "explanation": "EQ is the ability to understand and manage emotions"
            },
            {
                "id": "lm_4",
                "question": "What is a team?",
                "options": [
                    "Group of people working toward common goal",
                    "Sports group",
                    "Company department only",
                    "Individual workers"
                ],
                "correct": 0,
                "explanation": "Team is a collaborative group working toward shared goals"
            },
            {
                "id": "lm_5",
                "question": "What is conflict resolution?",
                "options": [
                    "Ending disagreements",
                    "Solving disputes between parties",
                    "Firing employees",
                    "Avoiding problems"
                ],
                "correct": 1,
                "explanation": "Conflict resolution addresses and solves disagreements"
            }
        ]
    },

    # ========================================================================
    # ENTREPRENEURSHIP
    # ========================================================================
    "entrepreneurship": {
        "title": "Entrepreneurship",
        "description": "Test your entrepreneurship knowledge",
        "time_limit": 10,
        "difficulty": "Intermediate",
        "questions": [
            {
                "id": "en_1",
                "question": "What is an entrepreneur?",
                "options": [
                    "Business employee",
                    "Person who starts and runs a business",
                    "Investor",
                    "Manager"
                ],
                "correct": 1,
                "explanation": "Entrepreneur creates and operates a new business"
            },
            {
                "id": "en_2",
                "question": "What is venture capital?",
                "options": [
                    "Bank loan",
                    "Investment in startups",
                    "Government grant",
                    "Personal savings"
                ],
                "correct": 1,
                "explanation": "Venture capital funds early-stage companies"
            },
            {
                "id": "en_3",
                "question": "What is a business plan?",
                "options": [
                    "Resume",
                    "Written document outlining business goals",
                    "Invoice",
                    "Meeting notes"
                ],
                "correct": 1,
                "explanation": "Business plan outlines objectives and strategy"
            },
            {
                "id": "en_4",
                "question": "What is market research?",
                "options": [
                    "Google search",
                    "Gathering information about market and customers",
                    "Marketplace location",
                    "Sales report"
                ],
                "correct": 1,
                "explanation": "Market research gathers insights about customers and competition"
            },
            {
                "id": "en_5",
                "question": "What is scalability?",
                "options": [
                    "Business size",
                    "Ability to grow without major changes",
                    "Cost reduction",
                    "Staff hiring"
                ],
                "correct": 1,
                "explanation": "Scalability is ability to handle growth efficiently"
            }
        ]
    },

    # ========================================================================
    # SALES
    # ========================================================================
    "sales": {
        "title": "Sales Fundamentals",
        "description": "Test your sales knowledge",
        "time_limit": 10,
        "difficulty": "Beginner",
        "questions": [
            {
                "id": "sl_1",
                "question": "What is a sales funnel?",
                "options": [
                    "Kitchen tool",
                    "Process from prospect to customer",
                    "Sales report",
                    "Product inventory"
                ],
                "correct": 1,
                "explanation": "Sales funnel shows customer journey to purchase"
            },
            {
                "id": "sl_2",
                "question": "What is a lead?",
                "options": [
                    "Metal object",
                    "Potential customer",
                    "Sales manager",
                    "Product feature"
                ],
                "correct": 1,
                "explanation": "Lead is a potential interested customer"
            },
            {
                "id": "sl_3",
                "question": "What is cold calling?",
                "options": [
                    "Calling in winter",
                    "Contacting potential customers unexpectedly",
                    "Calling friends",
                    "Customer support"
                ],
                "correct": 1,
                "explanation": "Cold calling is contacting prospects without prior contact"
            },
            {
                "id": "sl_4",
                "question": "What is upselling?",
                "options": [
                    "Selling upstairs",
                    "Encouraging customers to buy more",
                    "Returning products",
                    "Firing clients"
                ],
                "correct": 1,
                "explanation": "Upselling encourages customers to purchase higher-value items"
            },
            {
                "id": "sl_5",
                "question": "What is a value proposition?",
                "options": [
                    "Mathematical statement",
                    "Reason customers should choose you",
                    "Product price",
                    "Company mission"
                ],
                "correct": 1,
                "explanation": "Value proposition explains unique value to customers"
            }
        ]
    },

    # ========================================================================
    # PROJECT MANAGEMENT
    # ========================================================================
    "project_management": {
        "title": "Project Management",
        "description": "Test your PM knowledge",
        "time_limit": 10,
        "difficulty": "Intermediate",
        "questions": [
            {
                "id": "pm_1",
                "question": "What is a project scope?",
                "options": [
                    "Project size",
                    "Defined boundaries and deliverables",
                    "Project budget",
                    "Timeline"
                ],
                "correct": 1,
                "explanation": "Scope defines what's included in a project"
            },
            {
                "id": "pm_2",
                "question": "What is a milestone?",
                "options": [
                    "Stone marker",
                    "Significant project checkpoint",
                    "Final deadline",
                    "Budget review"
                ],
                "correct": 1,
                "explanation": "Milestone is a major achievement point in a project"
            },
            {
                "id": "pm_3",
                "question": "What is risk management?",
                "options": [
                    "Avoiding danger",
                    "Identifying and addressing potential problems",
                    "Security guard",
                    "Insurance"
                ],
                "correct": 1,
                "explanation": "Risk management identifies and mitigates potential issues"
            },
            {
                "id": "pm_4",
                "question": "What is a stakeholder?",
                "options": [
                    "Building owner",
                    "Person with interest in the project",
                    "Project manager",
                    "Customer only"
                ],
                "correct": 1,
                "explanation": "Stakeholder is anyone affected by or interested in the project"
            },
            {
                "id": "pm_5",
                "question": "What is a Gantt chart?",
                "options": [
                    "Bar chart showing project schedule",
                    "Pie chart",
                    "Org chart",
                    "Flowchart"
                ],
                "correct": 0,
                "explanation": "Gantt chart visualizes project timeline and tasks"
            }
        ]
    },

    # ========================================================================
    # COMMUNICATION SKILLS
    # ========================================================================
    "communication_skills": {
        "title": "Communication Skills",
        "description": "Test your communication knowledge",
        "time_limit": 10,
        "difficulty": "Beginner",
        "questions": [
            {
                "id": "cs_1",
                "question": "What is active listening?",
                "options": [
                    "Loud hearing",
                    "Fully focusing on the speaker",
                    "Speaking first",
                    "Taking notes only"
                ],
                "correct": 1,
                "explanation": "Active listening gives full attention and responds thoughtfully"
            },
            {
                "id": "cs_2",
                "question": "What is nonverbal communication?",
                "options": [
                    "Phone calls",
                    "Body language and gestures",
                    "Written emails",
                    "Meetings"
                ],
                "correct": 1,
                "explanation": "Nonverbal communication uses body language, not words"
            },
            {
                "id": "cs_3",
                "question": "What is feedback?",
                "options": [
                    "Food delivery",
                    "Constructive response to improve performance",
                    "Criticism only",
                    "Annual review"
                ],
                "correct": 1,
                "explanation": "Feedback provides helpful information to improve"
            },
            {
                "id": "cs_4",
                "question": "What is public speaking?",
                "options": [
                    "Talking to friends",
                    "Presenting to an audience",
                    "Teaching class",
                    "Phone conversation"
                ],
                "correct": 1,
                "explanation": "Public speaking is presenting to a group of people"
            },
            {
                "id": "cs_5",
                "question": "What is clarity in communication?",
                "options": [
                    "Speaking loudly",
                    "Being clear and easy to understand",
                    "Using big words",
                    "Fast talking"
                ],
                "correct": 1,
                "explanation": "Clarity means communicating ideas simply and clearly"
            }
        ]
    },

    # ========================================================================
    # HUMAN RESOURCES
    # ========================================================================
    "human_resources": {
        "title": "Human Resources",
        "description": "Test your HR knowledge",
        "time_limit": 10,
        "difficulty": "Intermediate",
        "questions": [
            {
                "id": "hr_1",
                "question": "What is recruitment?",
                "options": [
                    "Hiring new employees",
                    "Firing employees",
                    "Training",
                    "Payroll"
                ],
                "correct": 0,
                "explanation": "Recruitment is finding and hiring qualified candidates"
            },
            {
                "id": "hr_2",
                "question": "What is onboarding?",
                "options": [
                    "Boarding a plane",
                    "Integrating new employees",
                    "Performance review",
                    "Layoffs"
                ],
                "correct": 1,
                "explanation": "Onboarding helps new employees adjust to the organization"
            },
            {
                "id": "hr_3",
                "question": "What is employee engagement?",
                "options": [
                    "Keeping employees busy",
                    "Employee commitment to organization",
                    "Scheduling shifts",
                    "Payroll management"
                ],
                "correct": 1,
                "explanation": "Engagement measures employee dedication and involvement"
            },
            {
                "id": "hr_4",
                "question": "What is performance appraisal?",
                "options": [
                    "Appraising property",
                    "Evaluating employee performance",
                    "Salary negotiation",
                    "Job interview"
                ],
                "correct": 1,
                "explanation": "Performance appraisal assesses employee work"
            },
            {
                "id": "hr_5",
                "question": "What is workplace diversity?",
                "options": [
                    "Many office locations",
                    "Variety in employee backgrounds",
                    "Different products",
                    "Multiple teams"
                ],
                "correct": 1,
                "explanation": "Diversity includes varied backgrounds and perspectives"
            }
        ]
    },

    # ========================================================================
    # ECONOMICS
    # ========================================================================
    "economics": {
        "title": "Economics Basics",
        "description": "Test your economics knowledge",
        "time_limit": 10,
        "difficulty": "Beginner",
        "questions": [
            {
                "id": "ec_1",
                "question": "What is supply and demand?",
                "options": [
                    "Providing food",
                    "Relationship between product availability and desire",
                    "Business inventory",
                    "Price setting"
                ],
                "correct": 1,
                "explanation": "Supply and demand determines prices and quantities"
            },
            {
                "id": "ec_2",
                "question": "What is inflation?",
                "options": [
                    "Balloons",
                    "Rising prices over time",
                    "Economic growth",
                    "Stock market"
                ],
                "correct": 1,
                "explanation": "Inflation is the increase in prices over time"
            },
            {
                "id": "ec_3",
                "question": "What is GDP?",
                "options": [
                    "Government Department Program",
                    "Gross Domestic Product",
                    "General Data Protocol",
                    "Gold Deposit Price"
                ],
                "correct": 1,
                "explanation": "GDP measures total economic output of a country"
            },
            {
                "id": "ec_4",
                "question": "What is a market economy?",
                "options": [
                    "Shopping center",
                    "System driven by supply and demand",
                    "Government control",
                    "Planned economy"
                ],
                "correct": 1,
                "explanation": "Market economy is based on private decisions"
            },
            {
                "id": "ec_5",
                "question": "What is unemployment rate?",
                "options": [
                    "Job openings",
                    "Percentage of people without jobs",
                    "Job growth",
                    "Salary level"
                ],
                "correct": 1,
                "explanation": "Unemployment rate shows labor force without employment"
            }
        ]
    },

    # ========================================================================
    # DIGITAL MARKETING
    # ========================================================================
    "digital_marketing": {
        "title": "Digital Marketing",
        "description": "Test your digital marketing knowledge",
        "time_limit": 10,
        "difficulty": "Intermediate",
        "questions": [
            {
                "id": "dm_1",
                "question": "What is PPC advertising?",
                "options": [
                    "Pay Per Click",
                    "Price Per Customer",
                    "Public Press Coverage",
                    "Product Price Comparison"
                ],
                "correct": 0,
                "explanation": "PPC is paying for each ad click"
            },
            {
                "id": "dm_2",
                "question": "What is social media marketing?",
                "options": [
                    "Marketing on social platforms",
                    "Selling social media accounts",
                    "Traditional advertising",
                    "Cold calling"
                ],
                "correct": 0,
                "explanation": "Social media marketing uses platforms to reach audiences"
            },
            {
                "id": "dm_3",
                "question": "What is email marketing?",
                "options": [
                    "Writing emails",
                    "Marketing via email campaigns",
                    "Sending letters",
                    "Customer service"
                ],
                "correct": 1,
                "explanation": "Email marketing sends promotional messages to subscribers"
            },
            {
                "id": "dm_4",
                "question": "What is influencer marketing?",
                "options": [
                    "Political influence",
                    "Partnering with popular personalities",
                    "Sales promotion",
                    "TV advertising"
                ],
                "correct": 1,
                "explanation": "Influencer marketing uses popular people to promote brands"
            },
            {
                "id": "dm_5",
                "question": "What is analytics in marketing?",
                "options": [
                    "Data analysis for marketing decisions",
                    "Math only",
                    "Survey creation",
                    "Writing reports"
                ],
                "correct": 0,
                "explanation": "Analytics measures and analyzes marketing performance"
            }
        ]
    },

}

# Get a specific quiz by ID
def get_quiz(quiz_id):
    """Returns a specific quiz by ID"""
    return SKILL_ASSESSMENT_QUIZZES.get(quiz_id)

# Get all available quizzes
def get_all_quizzes():
    """Returns all available quizzes"""
    return {
        quiz_id: {
            "title": quiz_data["title"],
            "description": quiz_data["description"],
            "difficulty": quiz_data["difficulty"],
            "time_limit": quiz_data["time_limit"],
            "question_count": len(quiz_data["questions"])
        }
        for quiz_id, quiz_data in SKILL_ASSESSMENT_QUIZZES.items()
    }

# Calculate quiz score
def calculate_quiz_score(quiz_id, answers):
    """
    Calculate score for a quiz
    answers: dict like {question_id: selected_option_index}
    """
    quiz = get_quiz(quiz_id)
    if not quiz:
        return None
    
    score = 0
    total = len(quiz["questions"])
    
    for question in quiz["questions"]:
        if question["id"] in answers:
            if answers[question["id"]] == question["correct"]:
                score += 1
    
    percentage = (score / total * 100) if total > 0 else 0
    return {
        "score": score,
        "total": total,
        "percentage": percentage,
        "passed": percentage >= 70
    }
