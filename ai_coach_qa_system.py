# ai_coach_qa_system.py
# AI-powered doubt asking and coaching system

from datetime import datetime
import random

class AICoach:
    """AI Coach for answering doubts and providing guidance"""
    
    def __init__(self, user_profile, learning_path):
        self.user_profile = user_profile
        self.learning_path = learning_path
        self.conversation_history = []
        self.doubts_database = []
    
    def ask_doubt(self, doubt_data):
        """User asks a doubt"""
        doubt_entry = {
            "id": len(self.doubts_database) + 1,
            "timestamp": datetime.now().isoformat(),
            "topic": doubt_data.get("topic", "General"),
            "doubt_text": doubt_data.get("doubt", ""),
            "context": doubt_data.get("context", ""),
            "difficulty_level": doubt_data.get("difficulty_level", "Unknown"),
            "related_topics": doubt_data.get("related_topics", []),
            "status": "pending",
            "ai_response": None,
            "user_satisfaction": None,
            "follow_up_questions": []
        }
        
        self.doubts_database.append(doubt_entry)
        
        # Generate AI response
        response = self._generate_response(doubt_entry)
        doubt_entry["ai_response"] = response
        doubt_entry["status"] = "answered"
        
        # Add to conversation history
        self.conversation_history.append({"role": "user", "content": doubt_data.get("doubt", ""), "topic": doubt_data.get("topic", "General")})
        self.conversation_history.append({"role": "assistant", "content": response.get("main_answer", ""), "topic": doubt_data.get("topic", "General")})
        
        return doubt_entry
    
    def _generate_response(self, doubt_entry):
        """Generate intelligent AI response"""
        doubt_text = doubt_entry["doubt_text"].lower()
        topic = doubt_entry["topic"]
        difficulty = doubt_entry.get("difficulty_level", "Beginner")
        
        # Find matching topic
        category = self._find_category(doubt_text + " " + topic)
        
        if category:
            answer = self._get_answer_for_topic(doubt_text, category)
            return {
                "main_answer": answer,
                "explanation": self._get_explanation(category),
                "examples": self._get_examples(category),
                "resources": self._get_resources(category),
                "follow_up_suggestion": self._get_follow_up(category, difficulty),
                "confidence_score": 0.9,
                "category": category
            }
        
        # Generic response
        return {
            "main_answer": self._get_generic_answer(doubt_text, topic),
            "explanation": "This is an important concept. Let me explain...",
            "examples": "Try practicing with examples from official documentation.",
            "resources": [{"title": "Official Documentation", "url": "https://google.com"}],
            "follow_up_suggestion": "Could you be more specific about what you want to learn?",
            "confidence_score": 0.5,
            "category": "general"
        }
    
    def _find_category(self, text):
        """Find best matching category"""
        text_lower = text.lower()
        
        # Programming topics
        prog_keywords = {
            "python": ["python", "py", "django", "flask", "pandas", "numpy", "pip"],
            "javascript": ["javascript", "js", "react", "node", "vue", "angular", "frontend", "dom"],
            "java": ["java", "spring", "android"],
            "html": ["html", "css", "web", "frontend", "responsive", "flexbox", "grid"],
            "sql": ["sql", "mysql", "postgresql", "mongodb", "database", "nosql", "query"],
            "data_science": ["data science", "machine learning", "ml", "ai", "deep learning", "tensorflow", "pandas", "analytics", "neural"],
            "devops": ["devops", "docker", "kubernetes", "aws", "cloud", "ci", "cd", "jenkins", "git", "linux"],
            "algorithms": ["algorithm", "data structure", "complexity", "big o", "sorting", "searching", "tree", "graph"],
            # Business topics
            "business": ["business", "startup", "entrepreneur", "business plan", "revenue", "profit", "pivot"],
            "marketing": ["marketing", "seo", "social media", "brand", "content", "digital", "advertising"],
            "finance": ["finance", "accounting", "budget", "investment", "roi", "cash flow", "balance sheet"],
            "management": ["management", "leadership", "team", "project", "agile", "scrum", "strategy"],
            "product": ["product", "roadmap", "user research", "mvp", "feature", "prioritization"],
            "communication": ["communication", "presentation", "public speaking", "writing", "email", "meeting"],
            "career": ["career", "resume", "interview", "job", "salary", "promotion"]
        }
        
        for cat, keywords in prog_keywords.items():
            for kw in keywords:
                if kw in text_lower:
                    return cat
        
        return None
    
    def _get_answer_for_topic(self, doubt_text, category):
        """Get answer for specific topic"""
        answers = {
            "python": {
                "variable": "Variables are containers for storing data. In Python, you don't declare types - Python infers them automatically.",
                "function": "Functions are reusable code blocks. Use 'def' keyword: def greet(name): return f'Hello {name}!'",
                "list": "Lists are ordered, mutable collections: numbers = [1, 2, 3]. They can hold mixed types.",
                "dictionary": "Dictionaries store key-value pairs: person = {'name': 'John', 'age': 25}. Fast lookups by key.",
                "class": "Classes are blueprints for objects. Define attributes and methods to create instances.",
                "loop": "Loops repeat code. Use 'for i in range(5):' for count, 'while' for conditional repetition.",
                "import": "Use 'import module' or 'from module import function'. Python standard library has many built-ins.",
                "error": "Common errors: SyntaxError (grammar), NameError (undefined), TypeError (wrong type), IndexError (out of bounds).",
                "default": "Python is a high-level language known for readability. It's versatile: web dev, data science, AI, automation."
            },
            "javascript": {
                "variable": "Use 'let' for changeable variables, 'const' for constants. Avoid 'var' in modern JS.",
                "function": "Functions can use 'function' keyword or arrow syntax: const add = (a, b) => a + b;",
                "array": "Arrays have methods like map(), filter(), reduce(): numbers.map(x => x * 2).",
                "dom": "DOM represents HTML as objects. Use document.getElementById() or querySelector() to select elements.",
                "async": "Use async/await for async operations. Promises handle callbacks: fetch(url).then(res => res.json()).",
                "event": "Events are user actions. Use element.addEventListener('click', handler) to respond.",
                "default": "JavaScript makes web pages interactive. It runs in browsers and server-side with Node.js."
            },
            "html": {
                "default": "HTML structures web content with elements like <div>, <p>, <span>. Every element has opening and closing tags.",
                "css": "CSS styles elements. Use classes (.class), IDs (#id), or element selectors. Try Flexbox or Grid for layouts.",
                "flexbox": "Flexbox is for one-dimensional layouts. display: flex; justify-content: center; aligns items.",
                "responsive": "Use media queries: @media (max-width: 768px) { .column { width: 100%; } }"
            },
            "sql": {
                "select": "SELECT retrieves data: SELECT * FROM users WHERE age > 18 ORDER BY name;",
                "join": "JOINs combine tables: INNER JOIN (matching), LEFT JOIN (all left + matching right).",
                "index": "Indexes speed up queries but slow down writes. Add on frequently filtered columns.",
                "default": "SQL manages relational databases. Use queries to insert, update, delete, and retrieve data."
            },
            "data_science": {
                "default": "Data Science extracts insights from data using statistics, programming, and domain knowledge.",
                "machine learning": "ML algorithms learn patterns. Types: Supervised (labeled data), Unsupervised (clustering), Reinforcement.",
                "neural network": "Neural networks have layers of neurons that process data. Deep learning uses many layers.",
                "overfitting": "Overfitting means memorizing training data. Combat with: more data, regularization, cross-validation."
            },
            "devops": {
                "docker": "Docker containers package apps with dependencies. Use Dockerfile to define image, docker run to start.",
                "kubernetes": "Kubernetes orchestrates containers. Pods are smallest units. Deployments manage replicas.",
                "git": "Git tracks changes: git add, git commit, git push, git pull, git merge. Branch for features.",
                "ci_cd": "CI merges code frequently. CD automates deployment. Tools: Jenkins, GitHub Actions, GitLab CI.",
                "default": "DevOps combines development and operations. Goal: faster, more reliable software delivery."
            },
            "algorithms": {
                "big o": "Big O: O(1) constant, O(log n) logarithmic, O(n) linear, O(n log n) linearithmic, O(n²) quadratic.",
                "recursion": "Recursion is a function calling itself. Needs base case (stop condition) and recursive case (progress).",
                "sorting": "Common sorts: O(n²) - Bubble, Selection, Insertion. O(n log n) - Merge, Quick, Heap.",
                "default": "Algorithms are step-by-step procedures. Data structures organize data. Time/Space complexity measures efficiency."
            },
            "business": {
                "business model": "Business model describes how you create value: Subscription, Marketplace, SaaS, etc.",
                "pivot": "Pivot = change business direction based on feedback or market conditions.",
                "default": "Business involves creating value through products/services. Key: understand customers, solve problems."
            },
            "marketing": {
                "seo": "SEO improves search rankings. Use keywords in content, build backlinks, optimize page speed.",
                "funnel": "Marketing funnel: Awareness -> Interest -> Consideration -> Intent -> Purchase -> Retention.",
                "content": "Content marketing attracts audiences with valuable content: Blog, Video, Podcast, E-book.",
                "default": "Marketing promotes products to attract/retain customers. Digital: SEO, social media, email, paid ads."
            },
            "finance": {
                "balance sheet": "Balance sheet: Assets = Liabilities + Equity. Shows financial position at a point in time.",
                "roi": "ROI = (Revenue - Cost) / Cost × 100%. Measures return relative to investment.",
                "cash flow": "Cash flow tracks money in/out. Operating (business), Investing (assets), Financing (debt/equity).",
                "default": "Finance manages money: budgeting, investing, raising capital. Accounting tracks transactions."
            },
            "management": {
                "agile": "Agile values: Individuals over processes, Working software over documentation, Collaboration over contracts.",
                "scrum": "Scrum: Roles (PO, SM, Team), Events (Sprint, Planning, Daily, Review, Retro), Artifacts.",
                "delegation": "Delegate by sharing responsibility, not just tasks. Trust your team, provide guidance.",
                "default": "Management plans, organizes, directs resources. Leadership inspires and guides teams."
            },
            "product": {
                "roadmap": "Roadmap shows features/themes over time. Communicates strategy and priorities to stakeholders.",
                "mvp": "MVP = Minimum Viable Product. Smallest feature set to test hypotheses and learn from users.",
                "default": "Product management defines what to build and why. Combines strategy, user research, execution."
            },
            "communication": {
                "presentation": "Structure: Tell them what you'll say -> Say it -> Tell them what you said. Practice makes perfect.",
                "active listening": "Give full attention, don't interrupt, ask questions, paraphrase to confirm understanding.",
                "feedback": "Give feedback: Specific, Behavior-focused, Actionable, Timely. Use SBI: Situation, Behavior, Impact.",
                "default": "Communication conveys ideas effectively. Includes verbal, written, non-verbal. Critical for success."
            },
            "career": {
                "resume": "Keep 1-2 pages. Quantify achievements. Use action verbs. ATS-friendly format.",
                "interview": "Research company, practice STAR stories, prepare questions, dress professionally.",
                "networking": "Build genuine relationships. Offer value first. Follow up within 48 hours.",
                "default": "Career development involves skill building, networking, job searching, continuous learning."
            }
        }
        
        # Check for specific concepts
        topic_answers = answers.get(category, {})
        for concept, answer in topic_answers.items():
            if concept in doubt_text and concept != "default":
                return answer
        
        return topic_answers.get("default", f"Great question about {category}! Let me explain...")
    
    def _get_explanation(self, category):
        """Get detailed explanation for category"""
        explanations = {
            "python": "Python is a high-level, interpreted language known for simplicity. Used in web dev, data science, AI, automation.",
            "javascript": "JavaScript creates interactive web pages. Runs in browsers and server-side with Node.js.",
            "html": "HTML structures web content. CSS styles it. Together they create modern websites.",
            "sql": "SQL manages relational databases. Query, insert, update, delete data with standard language.",
            "data_science": "Data Science combines statistics, programming, domain knowledge to extract insights from data.",
            "devops": "DevOps improves software delivery through automation, collaboration, continuous improvement.",
            "algorithms": "Algorithms solve problems efficiently. Understanding complexity helps choose the right approach.",
            "business": "Business creates value by solving problems. Understanding customers and markets is key.",
            "marketing": "Marketing connects products with customers. Digital marketing includes SEO, social media, content.",
            "finance": "Finance manages money resources. Key concepts: budgeting, investing, cash flow, ROI.",
            "management": "Management organizes resources to achieve goals. Leadership inspires and guides teams.",
            "product": "Product management defines what to build based on user needs and business goals.",
            "communication": "Communication conveys ideas effectively. Critical skill for professional success.",
            "career": "Career development requires continuous learning, networking, and personal branding."
        }
        return explanations.get(category, "This is an important area to learn.")
    
    def _get_examples(self, category):
        """Get examples for category"""
        examples = {
            "python": "# Variables\nname = 'John'\nage = 25\n\n# Function\ndef greet(person):\n    return f'Hello, {person}!'",
            "javascript": "// Variables\nlet name = 'John';\nconst PI = 3.14;\n\n// Function\nfunction greet(name) {\n    return 'Hello, ' + name;\n}",
            "html": "<!-- HTML Structure -->\n<div class='container'>\n  <h1>Hello World</h1>\n</div>",
            "sql": "-- Select data\nSELECT * FROM users WHERE age > 18;",
            "devops": "# Docker\ndocker build -t myapp .\ndocker run -p 8080:80 myapp",
            "algorithms": "# Binary Search\ndef binary_search(arr, x):\n    lo, hi = 0, len(arr)-1\n    while lo <= hi:\n        mid = (lo+hi)//2\n        if arr[mid] == x: return mid\n        elif arr[mid] < x: lo = mid+1\n        else: hi = mid-1\n    return -1"
        }
        return examples.get(category, "Practice with real-world projects to solidify understanding.")
    
    def _get_resources(self, category):
        """Get recommended resources"""
        resources = {
            "python": [
                {"title": "Python.org", "url": "https://docs.python.org/3/"},
                {"title": "Real Python", "url": "https://realpython.com/"},
                {"title": "W3Schools Python", "url": "https://www.w3schools.com/python/"}
            ],
            "javascript": [
                {"title": "MDN Web Docs", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript"},
                {"title": "JavaScript.info", "url": "https://javascript.info/"},
                {"title": "FreeCodeCamp", "url": "https://www.freecodecamp.org/"}
            ],
            "html": [
                {"title": "MDN HTML", "url": "https://developer.mozilla.org/en-US/docs/Web/HTML"},
                {"title": "W3Schools", "url": "https://www.w3schools.com/"}
            ],
            "sql": [
                {"title": "W3Schools SQL", "url": "https://www.w3schools.com/sql/"},
                {"title": "PostgreSQL Docs", "url": "https://www.postgresql.org/docs/"}
            ],
            "data_science": [
                {"title": "Kaggle", "url": "https://www.kaggle.com/learn"},
                {"title": "Scikit-learn", "url": "https://scikit-learn.org/"}
            ],
            "devops": [
                {"title": "Docker Docs", "url": "https://docs.docker.com/"},
                {"title": "Kubernetes.io", "url": "https://kubernetes.io/docs/"}
            ],
            "algorithms": [
                {"title": "GeeksforGeeks", "url": "https://www.geeksforgeeks.org/"},
                {"title": "LeetCode", "url": "https://leetcode.com/"}
            ]
        }
        return resources.get(category, [{"title": "Google Search", "url": "https://google.com"}])
    
    def _get_follow_up(self, category, difficulty):
        """Get follow-up suggestion"""
        suggestions = {
            "Beginner": f"Would you like more examples of {category}?",
            "Intermediate": f"Would you like to learn advanced {category} concepts?",
            "Advanced": f"Would you like to discuss best practices and common pitfalls?"
        }
        return suggestions.get(difficulty, "Would you like me to elaborate on this?")
    
    def _get_generic_answer(self, doubt_text, topic):
        """Get generic answer"""
        if any(w in doubt_text for w in ["what", "explain", "understand"]):
            return f"That's a great question about {topic}. Let me break it down for you..."
        elif any(w in doubt_text for w in ["how", "implement", "create", "build"]):
            return f"Here's how to approach {topic}: Start with fundamentals, then practice..."
        elif any(w in doubt_text for w in ["why", "reason", "important"]):
            return f"Great question! Understanding {topic} is important because..."
        else:
            return f"I'd be happy to help with {topic}. Could you tell me more specifically what you need?"
    
    def debug_code(self, code, language="python"):
        """Help debug code"""
        issues = []
        
        if language == "python":
            if "==" in code and "= " in code.replace("==", ""):
                if not any(x in code for x in ["!=", "<=", ">="]):
                    pass
            
            if "=" in code and "==" not in code:
                pass
            
            common_issues = [
                ("print ", "print() should have parentheses: print('message')"),
                ("def  ", "Function definition has double space after 'def'"),
                ("for  ", "Loop has double space after 'for'"),
                ("if  ", "Conditional has double space after 'if'"),
                ("range(", "Check range syntax: range(start, stop, step)"),
                ("import ", "Make sure module is installed or spelled correctly")
            ]
            
            for pattern, message in common_issues:
                if pattern in code:
                    issues.append(message)
        
        if not issues:
            return {"issues_found": 0, "suggestions": ["Code looks good!", "Try adding print statements to debug.", "Check the error message for line number."]}
        
        return {"issues_found": len(issues), "issues": issues, "suggestions": ["Fix the issues above", "Run code in smaller chunks", "Check official documentation"]}
    
    def explain_error(self, error_message):
        """Explain programming errors"""
        errors = {
            "SyntaxError": "Syntax errors mean code doesn't follow language rules. Check for missing colons, parentheses, quotes, or indentation.",
            "NameError": "NameError means using a variable that hasn't been defined. Check spelling or ensure it's defined before use.",
            "TypeError": "TypeError means using data incorrectly. For example, adding a string to a number.",
            "IndexError": "IndexError means accessing a position that doesn't exist. Check list length and index.",
            "IndentationError": "IndentationError means inconsistent indentation. Python uses indentation for code blocks.",
            "AttributeError": "AttributeError means calling a method that doesn't exist on that object type.",
            "ValueError": "ValueError means correct type but inappropriate value was passed.",
            "KeyError": "KeyError means dictionary key doesn't exist. Use .get() to safely access.",
            "FileNotFoundError": "FileNotFoundError means the file path doesn't exist or is incorrect.",
            "ZeroDivisionError": "ZeroDivisionError means dividing by zero, which is mathematically undefined."
        }
        
        for error_type, explanation in errors.items():
            if error_type in error_message:
                return {"error_type": error_type, "explanation": explanation, "fix": "1. Find the line in error message\n2. " + explanation + "\n3. Fix and run again"}
        
        return {"error_type": "Unknown", "explanation": "Check the error message for details.", "fix": "Read error carefully, check the line number, look for typos."}
    
    def get_doubt_summary(self):
        """Get summary of all doubts"""
        total = len(self.doubts_database)
        resolved = len([d for d in self.doubts_database if d["status"] == "answered"])
        
        topics = [d["topic"] for d in self.doubts_database]
        topic_counts = {}
        for t in topics:
            topic_counts[t] = topic_counts.get(t, 0) + 1
        
        return {
            "total_doubts": total,
            "resolved_doubts": resolved,
            "pending_doubts": total - resolved,
            "topics_covered": list(set(topics)),
            "recent_conversations": self.conversation_history[-10:] if self.conversation_history else [],
            "common_topics": sorted(topic_counts.items(), key=lambda x: x[1], reverse=True)[:5]
        }
    
    def get_contextual_help(self, current_topic):
        """Get contextual help"""
        category = self._find_category(current_topic)
        if category:
            return {
                "tip": f"Focus on understanding the fundamentals of {category} first.",
                "common_issues": self._get_common_issues(category),
                "next_topics": self._suggest_next_topics(category)
            }
        return {"tip": "Practice regularly and ask questions when stuck!"}
    
    def _get_common_issues(self, category):
        """Get common issues for category"""
        issues = {
            "python": ["Indentation errors", "Forgetting colons", "Mutable default arguments"],
            "javascript": ["Undefined variables", "Async callback hell", "This binding issues"],
            "html": ["Unclosed tags", "Nested div issues", "CSS specificity conflicts"],
            "sql": ["SQL injection", "Missing WHERE clauses", "N+1 query problems"]
        }
        return issues.get(category, ["Syntax errors", "Logic errors", "Debugging issues"])
    
    def _suggest_next_topics(self, category):
        """Suggest next topics to learn"""
        progression = {
            "python": ["Data Structures", "OOP", "Web Development", "Data Science"],
            "javascript": ["React", "Node.js", "APIs", "TypeScript"],
            "html": ["CSS Grid", "JavaScript", "Backend", "Responsive Design"],
            "sql": ["Database Design", "ORM", "NoSQL", "Data Modeling"],
            "data_science": ["Machine Learning", "Deep Learning", "NLP", "Computer Vision"],
            "devops": ["Docker", "Kubernetes", "CI/CD", "Cloud"],
            "business": ["Marketing", "Finance", "Operations", "Strategy"],
            "management": ["Leadership", "Strategy", "Communication", "Team Building"]
        }
        return progression.get(category, ["Advanced topics", "Real-world projects"])


class InteractiveQASession:
    """Interactive Q&A learning session"""
    
    def __init__(self, coach, topic):
        self.coach = coach
        self.topic = topic
        self.session_questions = []
        self.session_score = 0
    
    def generate_quiz_questions(self, difficulty="Beginner"):
        """Generate quiz questions"""
        questions = [
            {"q": f"What is {self.topic}?", "a": "A key concept in this area", "options": ["A programming language", "A key concept", "A type of error", "A function"], "correct": 1},
            {"q": f"Why is {self.topic} important?", "a": "It's fundamental to understanding", "options": ["It's not important", "It's fundamental", "Only for experts", "It speeds up computers"], "correct": 1},
            {"q": f"How do you use {self.topic}?", "a": "Through practice and application", "options": ["Memorization", "Practice and application", "Reading only", "Watching videos"], "correct": 1}
        ]
        
        self.session_questions = [{"id": i+1, **q} for i, q in enumerate(questions)]
        return self.session_questions
    
    def submit_answer(self, question_id, answer):
        """Submit answer"""
        for q in self.session_questions:
            if q["id"] == question_id:
                is_correct = answer == q["correct"]
                if is_correct:
                    self.session_score += 10
                return {"is_correct": is_correct, "explanation": q["a"], "correct_answer": q["correct"], "current_score": self.session_score}
        return None
    
    def get_session_summary(self):
        """Get session summary"""
        return {
            "topic": self.topic,
            "questions_asked": len(self.session_questions),
            "session_score": self.session_score,
            "percentage": (self.session_score / (len(self.session_questions) * 10) * 100) if self.session_questions else 0,
            "next_recommendation": "Move to advanced topics" if self.session_score > 20 else "Practice more basics"
        }
