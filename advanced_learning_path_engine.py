# advanced_learning_path_engine.py
# AI-powered learning path generation with customization and path analysis

import json
from datetime import datetime, timedelta

class LearningPathGenerator:
    """Generate personalized learning paths with analysis and recommendations"""
    
    def __init__(self, profile, skill_selection):
        self.profile = profile
        self.skill = skill_selection
        self.path = None
        
    def generate_base_path(self):
        """Generate base learning path"""
        # Validate that skill is selected
        if self.skill is None:
            return None
            
        daily_hours = self.profile.get("daily_hours", 2)
        consistency = self.profile.get("consistency", 5)
        learning_depth = self.profile.get("learning_depth", "Balanced")
        
        # Determine pace based on consistency
        if consistency >= 8:
            pace = "Accelerated"
            pace_multiplier = 0.7
        elif consistency >= 6:
            pace = "Fast"
            pace_multiplier = 0.85
        elif consistency >= 4:
            pace = "Balanced"
            pace_multiplier = 1.0
        else:
            pace = "Slow"
            pace_multiplier = 1.3
        
        # Calculate estimated duration weeks
        estimated_duration_weeks = int(self.skill.get("duration_weeks", 8) * pace_multiplier)
        
        # Create stages first
        stages = self._create_stages()
        
        # Initialize path with basic info first
        self.path = {
            "skill": self.skill.get("skill", "Unknown Skill"),
            "created_at": datetime.now().isoformat(),
            "pace": pace,
            "pace_multiplier": pace_multiplier,
            "estimated_duration_weeks": estimated_duration_weeks,
            "daily_hours_required": daily_hours,
            "learning_depth": learning_depth,
            "stages": stages,
            "timeline": [],  # Will be populated next
            "milestones": [],  # Will be populated next
            "customizations_applied": [],
            "path_analysis": None
        }
        
        # Now we can safely call timeline and milestones creation since self.path is set
        self.path["timeline"] = self._create_timeline()
        self.path["milestones"] = self._create_milestones()
        
        return self.path
    
    def _create_stages(self):
        """Create learning stages based on skill"""
        stages = []
        
        # Safely get skill name
        skill_name = self.skill.get("skill", "") if self.skill else ""
        
        if skill_name in ["Python Programming", "JavaScript & Web Development"]:
            stages = [
                {
                    "title": "Foundations",
                    "number": 1,
                    "duration_weeks": 2,
                    "description": "Learn syntax, variables, and basic concepts",
                    "topics": ["Syntax", "Variables", "Data types", "Basic operations"],
                    "learning_methods": ["Videos", "Reading", "Small exercises"],
                    "practice": ["Daily coding drills", "Simple scripts"],
                    "milestone": "Write first working program"
                },
                {
                    "title": "Problem Solving & Logic",
                    "number": 2,
                    "duration_weeks": 3,
                    "description": "Develop computational thinking",
                    "topics": ["Control flow", "Loops", "Conditionals", "Functions"],
                    "learning_methods": ["Problem sets", "Interactive coding", "Debugging"],
                    "practice": ["Algorithm problems", "Logic puzzles"],
                    "milestone": "Solve 20 coding problems"
                },
                {
                    "title": "Core Concepts",
                    "number": 3,
                    "duration_weeks": 3,
                    "description": "Master libraries and tools",
                    "topics": ["Libraries", "Data structures", "File handling", "Error handling"],
                    "learning_methods": ["Documentation", "Tutorials", "Projects"],
                    "practice": ["Build mini-projects", "Code real examples"],
                    "milestone": "Complete 3 mini-projects"
                },
                {
                    "title": "Projects & Application",
                    "number": 4,
                    "duration_weeks": 4,
                    "description": "Build real-world applications",
                    "topics": ["Project planning", "Code organization", "Testing", "Deployment"],
                    "learning_methods": ["Project-based", "Code review", "Mentorship"],
                    "practice": ["Build portfolio projects", "Open source contribution"],
                    "milestone": "Complete 1 significant project"
                }
            ]
        else:
            # Generic stages for other skills
            stages = [
                {
                    "title": "Foundations",
                    "number": 1,
                    "duration_weeks": 2,
                    "description": "Understand core concepts",
                    "topics": ["Key terminology", "Basic principles"],
                    "learning_methods": ["Lectures", "Reading"],
                    "practice": ["Exercises", "Quizzes"],
                    "milestone": "Pass foundational quiz"
                },
                {
                    "title": "Core Knowledge",
                    "number": 2,
                    "duration_weeks": 3,
                    "description": "Deep dive into main topics",
                    "topics": ["Main concepts", "Theory", "Applications"],
                    "learning_methods": ["Tutorials", "Case studies", "Experiments"],
                    "practice": ["Problem sets", "Real examples"],
                    "milestone": "Complete practical assignments"
                },
                {
                    "title": "Advanced Topics",
                    "number": 3,
                    "duration_weeks": 2,
                    "description": "Explore advanced applications",
                    "topics": ["Advanced patterns", "Optimization", "Best practices"],
                    "learning_methods": ["Deep dives", "Research papers", "Mentorship"],
                    "practice": ["Complex problems", "Optimization tasks"],
                    "milestone": "Master advanced concepts"
                },
                {
                    "title": "Practical Application",
                    "number": 4,
                    "duration_weeks": 2,
                    "description": "Apply knowledge to real projects",
                    "topics": ["Project execution", "Problem solving", "Continuous learning"],
                    "learning_methods": ["Project-based", "Feedback loops"],
                    "practice": ["Real-world projects", "Portfolio building"],
                    "milestone": "Complete capstone project"
                }
            ]
        
        return stages
    
    def _create_timeline(self):
        """Create week-by-week timeline"""
        timeline = []
        start_date = datetime.now()
        
        total_weeks = self.path["estimated_duration_weeks"]
        
        for week in range(1, total_weeks + 1):
            week_date = start_date + timedelta(weeks=week)
            
            timeline.append({
                "week": week,
                "start_date": week_date.strftime("%Y-%m-%d"),
                "focus": f"Week {week} progress",
                "expected_hours": self.profile.get("daily_hours", 2) * 7,
                "goals": [],
                "checkpoints": []
            })
        
        return timeline
    
    def _create_milestones(self):
        """Create major milestones"""
        milestones = []
        
        for stage in self.path["stages"]:
            milestones.append({
                "stage": stage["title"],
                "milestone": stage.get("milestone", "Complete stage"),
                "expected_week": sum(s["duration_weeks"] for s in self.path["stages"][:stage["number"]]),
                "success_criteria": ["Complete all exercises", "Score 80%+ on assessments"],
                "reward": f"Badge: {stage['title']} Achieved"
            })
        
        return milestones
    
    def customize_path(self, customization):
        """
        Apply customization to path
        
        Args:
            customization: {
                "type": "add_stage", "increase_pace", "focus_area", etc.
                "details": {...}
            }
        """
        if not self.path:
            return None
        
        if customization["type"] == "increase_pace":
            old_weeks = self.path["estimated_duration_weeks"]
            self.path["pace_multiplier"] *= 0.9
            self.path["estimated_duration_weeks"] = int(old_weeks * 0.9)
            self.path["customizations_applied"].append({
                "type": "pace_adjustment",
                "from": old_weeks,
                "to": self.path["estimated_duration_weeks"],
                "note": "Increased pace"
            })
        
        elif customization["type"] == "decrease_pace":
            old_weeks = self.path["estimated_duration_weeks"]
            self.path["pace_multiplier"] *= 1.1
            self.path["estimated_duration_weeks"] = int(old_weeks * 1.1)
            self.path["customizations_applied"].append({
                "type": "pace_adjustment",
                "from": old_weeks,
                "to": self.path["estimated_duration_weeks"],
                "note": "Decreased pace"
            })
        
        elif customization["type"] == "focus_area":
            # Focus on specific topic
            focus = customization.get("focus", "")
            self.path["customizations_applied"].append({
                "type": "focus_adjustment",
                "focus_area": focus,
                "note": f"Added deeper focus on {focus}"
            })
        
        elif customization["type"] == "skip_stage":
            stage_num = customization.get("stage_number", 0)
            if stage_num < len(self.path["stages"]):
                stage = self.path["stages"][stage_num]
                self.path["estimated_duration_weeks"] -= stage["duration_weeks"]
                self.path["customizations_applied"].append({
                    "type": "skip_stage",
                    "stage": stage["title"],
                    "note": "Skipped this stage based on prior knowledge"
                })
        
        return self.path
    
    def analyze_path_flaws(self):
        """Analyze potential flaws in the learning path"""
        if not self.path:
            return None
        
        flaws = []
        warnings = []
        recommendations = []
        
        daily_hours = self.profile.get("daily_hours", 2)
        consistency = self.profile.get("consistency", 5)
        burnout_freq = self.profile.get("burnout_frequency", "Sometimes")
        procrastination = self.profile.get("procrastination_level", 5)
        
        # ============================================================================
        # FLAW ANALYSIS
        # ============================================================================
        
        # Flaw 1: Time mismatch
        if daily_hours < 2 and self.path["estimated_duration_weeks"] < 6:
            flaws.append({
                "flaw": "Aggressive Timeline",
                "severity": "High",
                "description": f"With only {daily_hours} hours/day, completing in {self.path['estimated_duration_weeks']} weeks may be unrealistic",
                "impact": "High risk of burnout and incomplete learning",
                "difficulty": "Very Hard"
            })
        
        # Flaw 2: Inconsistency risk
        if consistency <= 3:
            flaws.append({
                "flaw": "Low Consistency Risk",
                "severity": "High",
                "description": "Your reported consistency is low, but this path requires sustained effort",
                "impact": "High likelihood of abandoning the path",
                "difficulty": "Medium"
            })
        
        # Flaw 3: Burnout potential
        if burnout_freq in ["Often", "Very often"] and daily_hours >= 4:
            flaws.append({
                "flaw": "Burnout Risk",
                "severity": "High",
                "description": "You're prone to burnout but planning intensive learning",
                "impact": "May experience motivation loss mid-way",
                "difficulty": "Medium-Hard"
            })
        
        # Flaw 4: Prerequisite gaps
        if self.skill.get("prerequisites", []):
            learned = self.profile.get("skills_learned", [])
            missing_prereqs = [p for p in self.skill.get("prerequisites", []) if p not in learned]
            if missing_prereqs:
                flaws.append({
                    "flaw": "Missing Prerequisites",
                    "severity": "Medium",
                    "description": f"This skill requires: {', '.join(missing_prereqs)}",
                    "impact": "May struggle with concepts; foundation is weak",
                    "difficulty": "Hard",
                    "missing_prerequisites": missing_prereqs
                })
        
        # Flaw 5: Procrastination mismatch
        if procrastination >= 7 and self.path["pace"] == "Accelerated":
            flaws.append({
                "flaw": "Procrastination vs Pace Mismatch",
                "severity": "Medium",
                "description": "You tend to procrastinate, but this accelerated path leaves no buffer",
                "impact": "Falls behind schedule quickly",
                "difficulty": "Medium"
            })
        
        # ============================================================================
        # WARNINGS
        # ============================================================================
        
        if self.skill.get("difficulty", "Easy") in ["Hard", "Very Hard"]:
            warnings.append({
                "warning": "High Difficulty Skill",
                "description": f"This is a {self.skill['difficulty']} skill - expect steep learning curve",
                "suggestion": "Consider breaking it into smaller milestones"
            })
        
        if daily_hours < 1.5:
            warnings.append({
                "warning": "Limited Daily Time",
                "description": "With less than 1.5 hours/day, learning new skills takes much longer",
                "suggestion": "Consider combining with smaller time investments"
            })
        
        # ============================================================================
        # RECOMMENDATIONS
        # ============================================================================
        
        # Recommendation 1: Buffer time
        recommendations.append({
            "recommendation": "Add Buffer Weeks",
            "description": "Add 20% buffer time for unexpected obstacles",
            "action": f"Extend timeline from {self.path['estimated_duration_weeks']} to {int(self.path['estimated_duration_weeks'] * 1.2)} weeks",
            "benefit": "Reduces stress and increases completion likelihood"
        })
        
        # Recommendation 2: Accountability
        if consistency <= 4:
            recommendations.append({
                "recommendation": "Increase Accountability",
                "description": "Your consistency is low - use accountability mechanisms",
                "actions": [
                    "Join a study group or find an accountability partner",
                    "Set daily reminders",
                    "Track progress publicly",
                    "Use streak-based motivation"
                ],
                "benefit": "Significantly increases completion rates"
            })
        
        # Recommendation 3: Flexible schedule
        if burnout_freq in ["Often", "Very often"]:
            recommendations.append({
                "recommendation": "Build in Rest Days",
                "description": "Burnout-prone learners need strategic breaks",
                "actions": [
                    "Take 1-2 days off per week for complete rest",
                    "Alternate intense days with light review days",
                    "Use exercise and sleep for recovery"
                ],
                "benefit": "Sustainable long-term learning"
            })
        
        # Recommendation 4: Progressive difficulty
        recommendations.append({
            "recommendation": "Gradual Difficulty Increase",
            "description": "Start easy, gradually increase difficulty",
            "actions": [
                "Week 1-2: Focus on basics and understanding",
                "Week 3-4: Intermediate problems",
                "Week 5+: Advanced challenges"
            ],
            "benefit": "Builds confidence and prevents frustration"
        })
        
        # Recommendation 5: Use multiple resources
        recommendations.append({
            "recommendation": "Diverse Learning Resources",
            "description": "Single resource may not cover your learning style",
            "actions": [
                "Combine videos, text, and hands-on practice",
                "Use official docs + tutorials + YouTube",
                "Find examples and real-world applications"
            ],
            "benefit": "Faster comprehension and better retention"
        })
        
        # Recommendation 6: Track progress
        recommendations.append({
            "recommendation": "Implement Progress Tracking",
            "description": "Visible progress motivates and helps identify struggles early",
            "actions": [
                "Track daily hours spent",
                "Note concepts understood vs struggling",
                "Weekly self-assessment",
                "Portfolio building"
            ],
            "benefit": "Early detection of issues; maintains motivation"
        })
        
        self.path["path_analysis"] = {
            "flaws": flaws,
            "warnings": warnings,
            "recommendations": recommendations,
            "overall_risk_level": self._calculate_risk_level(flaws, warnings),
            "success_probability": self._calculate_success_probability(),
            "analysis_date": datetime.now().isoformat()
        }
        
        return self.path["path_analysis"]
    
    def _calculate_risk_level(self, flaws, warnings):
        """Calculate overall risk level"""
        high_severity_flaws = len([f for f in flaws if f["severity"] == "High"])
        
        if high_severity_flaws >= 3:
            return "Very High"
        elif high_severity_flaws >= 2:
            return "High"
        elif high_severity_flaws >= 1:
            return "Medium-High"
        elif len(warnings) >= 2:
            return "Medium"
        else:
            return "Low"
    
    def _calculate_success_probability(self):
        """Estimate success probability"""
        consistency = self.profile.get("consistency", 5)
        daily_hours = self.profile.get("daily_hours", 2)
        motivation = self.profile.get("motivation", 5)
        
        base_probability = 70  # Base 70%
        
        # Adjust for consistency
        base_probability += (consistency - 5) * 3
        
        # Adjust for time
        if daily_hours >= 3:
            base_probability += 5
        elif daily_hours < 1.5:
            base_probability -= 10
        
        # Adjust for motivation
        base_probability += (motivation - 5) * 2
        
        # Cap between 20-95%
        return max(20, min(95, base_probability))
    
    def get_recommendations_vs_custom(self, user_custom_path):
        """Compare AI recommendations with user's custom path choices"""
        comparison = {
            "ai_recommendation": self.path,
            "user_custom_path": user_custom_path,
            "comparison": {
                "pace_difference": {
                    "ai": self.path.get("pace", "Balanced"),
                    "user": user_custom_path.get("pace", "Unknown"),
                    "recommendation": "User's pace is realistic given your profile"
                },
                "duration_difference": {
                    "ai_weeks": self.path.get("estimated_duration_weeks", 8),
                    "user_weeks": user_custom_path.get("estimated_duration_weeks", 8),
                    "delta": user_custom_path.get("estimated_duration_weeks", 8) - self.path.get("estimated_duration_weeks", 8),
                    "note": "Positive delta means user is taking longer (safer)"
                },
                "stage_differences": [],
                "potential_issues": []
            },
            "best_path_recommendation": self._recommend_best_path(user_custom_path)
        }
        
        return comparison
    
    def _recommend_best_path(self, user_custom_path):
        """Recommend the best path between AI and user's custom"""
        ai_risk = self.path.get("path_analysis", {}).get("overall_risk_level", "Unknown")
        
        return {
            "recommendation": "AI-Recommended Path",
            "reasoning": [
                f"Risk level is {ai_risk}",
                "Pace matches your consistency level",
                "Includes proper milestones and feedback loops"
            ],
            "why_better_than_custom": [],
            "caveats": [],
            "personalization_note": "These recommendations are tailored to your specific profile"
        }

# Helper function to generate complete path
def generate_complete_learning_path(profile, skill):
    """Generate a complete learning path"""
    generator = LearningPathGenerator(profile, skill)
    generator.generate_base_path()
    generator.analyze_path_flaws()
    return generator.path

# Example usage
if __name__ == "__main__":
    sample_profile = {
        "daily_hours": 2,
        "consistency": 5,
        "learning_depth": "Balanced",
        "burnout_frequency": "Sometimes",
        "procrastination_level": 5,
        "skills_learned": []
    }
    
    sample_skill = {
        "skill": "Python Programming",
        "duration_weeks": 8,
        "prerequisites": [],
        "difficulty": "Medium"
    }
    
    path = generate_complete_learning_path(sample_profile, sample_skill)
    print(json.dumps(path, indent=2, default=str))
