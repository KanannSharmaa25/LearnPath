# daily_tracking_and_progress.py
# Track daily learning, progress, and provide insights

import json
from datetime import datetime, timedelta
from collections import defaultdict

class DailyLearningTracker:
    """Track daily learning activities and progress"""
    
    def __init__(self, user_id, learning_path_id):
        self.user_id = user_id
        self.learning_path_id = learning_path_id
        self.logs = []  # Daily log entries
        self.insights = {}
    
    def log_daily_activity(self, activity_data):
        """
        Log daily learning activity
        
        Args:
            activity_data: {
                "date": "2024-01-29",
                "hours_spent": 2.5,
                "sleep_hours": 7,
                "topics_covered": ["Python basics", "Variables"],
                "understanding_level": 7,  # 1-10
                "difficulty_faced": "Loops were confusing",
                "completed_tasks": ["5 coding exercises"],
                "mood": "Motivated",  # Motivated, Neutral, Frustrated, Tired
                "productivity_rating": 7,  # 1-10
                "environment": "Home",
                "notes": "Took more breaks than usual"
            }
        """
        
        log_entry = {
            "id": len(self.logs) + 1,
            "date": activity_data.get("date", datetime.now().strftime("%Y-%m-%d")),
            "hours_spent": activity_data.get("hours_spent", 0),
            "sleep_hours": activity_data.get("sleep_hours", 8),
            "topics_covered": activity_data.get("topics_covered", []),
            "understanding_level": activity_data.get("understanding_level", 5),
            "difficulty_faced": activity_data.get("difficulty_faced", None),
            "completed_tasks": activity_data.get("completed_tasks", []),
            "mood": activity_data.get("mood", "Neutral"),
            "productivity_rating": activity_data.get("productivity_rating", 5),
            "environment": activity_data.get("environment", "Not specified"),
            "notes": activity_data.get("notes", ""),
            "logged_at": datetime.now().isoformat()
        }
        
        self.logs.append(log_entry)
        return log_entry
    
    def get_progress_summary(self):
        """Get overall progress summary"""
        if not self.logs:
            return None
        
        total_hours = sum(log["hours_spent"] for log in self.logs)
        total_days = len(self.logs)
        avg_hours_per_day = total_hours / total_days if total_days > 0 else 0
        avg_sleep = sum(log["sleep_hours"] for log in self.logs) / total_days if total_days > 0 else 0
        avg_understanding = sum(log["understanding_level"] for log in self.logs) / total_days if total_days > 0 else 0
        avg_productivity = sum(log["productivity_rating"] for log in self.logs) / total_days if total_days > 0 else 0
        
        mood_counts = defaultdict(int)
        for log in self.logs:
            mood_counts[log["mood"]] += 1
        
        all_difficulties = [log["difficulty_faced"] for log in self.logs if log["difficulty_faced"]]
        all_topics = []
        for log in self.logs:
            all_topics.extend(log["topics_covered"])
        
        summary = {
            "total_days_active": total_days,
            "total_hours_invested": round(total_hours, 2),
            "average_hours_per_day": round(avg_hours_per_day, 2),
            "average_sleep_hours": round(avg_sleep, 2),
            "average_understanding_level": round(avg_understanding, 1),
            "average_productivity_rating": round(avg_productivity, 1),
            "mood_distribution": dict(mood_counts),
            "most_common_mood": max(mood_counts, key=mood_counts.get) if mood_counts else "Unknown",
            "topics_covered": list(set(all_topics)),
            "common_difficulties": self._get_top_difficulties(all_difficulties),
            "completion_rate": f"{(total_hours / (total_days * 2) * 100):.1f}%"  # Assuming 2 hrs/day target
        }
        
        return summary
    
    def _get_top_difficulties(self, difficulties):
        """Get most common difficulties"""
        counts = defaultdict(int)
        for diff in difficulties:
            counts[diff] += 1
        
        sorted_diffs = sorted(counts.items(), key=lambda x: x[1], reverse=True)
        return [diff[0] for diff in sorted_diffs[:5]]
    
    def identify_problem_areas(self):
        """Identify areas where user is struggling"""
        if len(self.logs) < 3:
            return None
        
        problem_areas = []
        
        # Low understanding areas
        low_understanding_logs = [log for log in self.logs if log["understanding_level"] <= 4]
        if len(low_understanding_logs) >= 2:
            topics = []
            for log in low_understanding_logs:
                topics.extend(log["topics_covered"])
            
            if topics:
                problem_areas.append({
                    "type": "Low Understanding",
                    "severity": "High" if len(low_understanding_logs) >= 3 else "Medium",
                    "topics": list(set(topics)),
                    "occurrences": len(low_understanding_logs),
                    "recommendation": "Review these topics with a different resource or ask for help"
                })
        
        # Consistent difficulties
        recurring_difficulties = self._get_top_difficulties([
            log["difficulty_faced"] for log in self.logs if log["difficulty_faced"]
        ])
        
        if recurring_difficulties:
            problem_areas.append({
                "type": "Recurring Difficulties",
                "severity": "Medium",
                "issues": recurring_difficulties[:3],
                "recommendation": "Try breaking these down into smaller concepts"
            })
        
        # Low productivity patterns
        low_productivity_logs = [log for log in self.logs if log["productivity_rating"] <= 3]
        if len(low_productivity_logs) >= 2:
            moods = [log["mood"] for log in low_productivity_logs]
            problem_areas.append({
                "type": "Low Productivity",
                "severity": "Medium",
                "associated_moods": moods,
                "count": len(low_productivity_logs),
                "recommendation": "Consider changing study environment or taking longer breaks"
            })
        
        # Sleep correlation
        avg_sleep = sum(log["sleep_hours"] for log in self.logs) / len(self.logs)
        low_sleep_logs = [log for log in self.logs if log["sleep_hours"] < avg_sleep - 1]
        if len(low_sleep_logs) >= 2:
            low_sleep_productivity = sum(log["productivity_rating"] for log in low_sleep_logs) / len(low_sleep_logs)
            if low_sleep_productivity < 5:
                problem_areas.append({
                    "type": "Sleep Impact",
                    "severity": "High",
                    "message": f"Less sleep correlates with lower productivity",
                    "recommendation": "Prioritize 7-8 hours of sleep for better learning"
                })
        
        return problem_areas
    
    def get_insights_and_patterns(self):
        """Generate insights from learning data"""
        if len(self.logs) < 3:
            return {"message": "Need at least 3 days of data for insights"}
        
        insights = {
            "summary": self.get_progress_summary(),
            "problem_areas": self.identify_problem_areas(),
            "positive_trends": self._identify_positive_trends(),
            "recommendations": self._generate_recommendations()
        }
        
        return insights
    
    def _identify_positive_trends(self):
        """Identify positive learning trends"""
        positive_trends = []
        
        # Improving understanding
        if len(self.logs) >= 5:
            recent_understanding = sum(log["understanding_level"] for log in self.logs[-3:]) / 3
            earlier_understanding = sum(log["understanding_level"] for log in self.logs[:3]) / 3
            
            if recent_understanding > earlier_understanding:
                improvement = round(recent_understanding - earlier_understanding, 1)
                positive_trends.append({
                    "trend": "Improving Understanding",
                    "details": f"+{improvement} points improvement",
                    "insight": "You're getting better at understanding concepts!"
                })
        
        # Consistent high productivity days
        high_productivity_logs = [log for log in self.logs if log["productivity_rating"] >= 7]
        if len(high_productivity_logs) >= 2:
            positive_trends.append({
                "trend": "High Productivity Days",
                "count": len(high_productivity_logs),
                "insight": f"You have {len(high_productivity_logs)} highly productive days"
            })
        
        # Good sleep habits
        good_sleep_logs = [log for log in self.logs if 7 <= log["sleep_hours"] <= 9]
        if len(good_sleep_logs) >= len(self.logs) * 0.6:
            positive_trends.append({
                "trend": "Healthy Sleep Schedule",
                "percentage": round(len(good_sleep_logs) / len(self.logs) * 100),
                "insight": "You're maintaining good sleep hygiene!"
            })
        
        # Consistent learning
        if len(self.logs) >= 5:
            avg_hours = sum(log["hours_spent"] for log in self.logs) / len(self.logs)
            if avg_hours >= 2:
                positive_trends.append({
                    "trend": "Consistent Learning",
                    "hours_per_day": round(avg_hours, 1),
                    "insight": f"You're averaging {avg_hours:.1f} hours per day - great consistency!"
                })
        
        return positive_trends
    
    def _generate_recommendations(self):
        """Generate personalized recommendations"""
        recommendations = []
        
        if len(self.logs) < 3:
            return []
        
        # Based on understanding level
        avg_understanding = sum(log["understanding_level"] for log in self.logs) / len(self.logs)
        if avg_understanding < 5:
            recommendations.append({
                "title": "Revisit Fundamentals",
                "description": "Your understanding level is lower than expected",
                "action": "Slow down, re-watch videos, or try a different resource",
                "priority": "High"
            })
        
        # Based on productivity
        avg_productivity = sum(log["productivity_rating"] for log in self.logs) / len(self.logs)
        if avg_productivity < 5:
            recommendations.append({
                "title": "Optimize Study Environment",
                "description": "Your productivity is lower than ideal",
                "actions": [
                    "Try a different location",
                    "Reduce distractions",
                    "Adjust study timing",
                    "Take more breaks"
                ],
                "priority": "High"
            })
        
        # Based on sleep
        avg_sleep = sum(log["sleep_hours"] for log in self.logs) / len(self.logs)
        if avg_sleep < 7:
            recommendations.append({
                "title": "Prioritize Sleep",
                "description": f"You're averaging {avg_sleep:.1f} hours - below recommended",
                "action": "Aim for 7-9 hours. It significantly impacts learning",
                "priority": "High"
            })
        
        # Based on mood
        mood_counts = defaultdict(int)
        for log in self.logs:
            mood_counts[log["mood"]] += 1
        
        if mood_counts.get("Frustrated", 0) >= len(self.logs) * 0.3:
            recommendations.append({
                "title": "Take Strategic Breaks",
                "description": "You're feeling frustrated frequently",
                "actions": [
                    "Take a day off from learning",
                    "Switch to easier topics",
                    "Do a different activity",
                    "Practice self-compassion"
                ],
                "priority": "High"
            })
        
        # Based on difficulty
        difficulties = [log["difficulty_faced"] for log in self.logs if log["difficulty_faced"]]
        if difficulties and len(difficulties) >= len(self.logs) * 0.5:
            recommendations.append({
                "title": "Seek Additional Help",
                "description": "You're facing consistent difficulties",
                "actions": [
                    "Ask in study groups or forums",
                    "Use multiple resources",
                    "Pair program with someone",
                    "Consult our AI coach"
                ],
                "priority": "Medium"
            })
        
        return recommendations

class ProgressVisualizer:
    """Generate progress metrics for visualization"""
    
    def __init__(self, tracker):
        self.tracker = tracker
    
    def get_chart_data_hours(self):
        """Get daily hours for line chart"""
        return {
            "labels": [log["date"] for log in self.tracker.logs],
            "data": [log["hours_spent"] for log in self.tracker.logs],
            "title": "Daily Learning Hours"
        }
    
    def get_chart_data_understanding(self):
        """Get understanding level progression"""
        return {
            "labels": [log["date"] for log in self.tracker.logs],
            "data": [log["understanding_level"] for log in self.tracker.logs],
            "title": "Understanding Level Progress"
        }
    
    def get_chart_data_mood(self):
        """Get mood distribution"""
        mood_counts = defaultdict(int)
        for log in self.tracker.logs:
            mood_counts[log["mood"]] += 1
        
        return {
            "labels": list(mood_counts.keys()),
            "data": list(mood_counts.values()),
            "title": "Mood Distribution",
            "type": "pie"
        }
    
    def get_chart_data_sleep_vs_productivity(self):
        """Correlation between sleep and productivity"""
        return {
            "sleep_hours": [log["sleep_hours"] for log in self.tracker.logs],
            "productivity": [log["productivity_rating"] for log in self.tracker.logs],
            "title": "Sleep vs Productivity",
            "type": "scatter"
        }
    
    def get_all_charts(self):
        """Get all chart data"""
        return {
            "hours": self.get_chart_data_hours(),
            "understanding": self.get_chart_data_understanding(),
            "mood": self.get_chart_data_mood(),
            "sleep_productivity": self.get_chart_data_sleep_vs_productivity()
        }

# Example usage
def create_sample_tracking():
    """Create sample tracking data for demo"""
    tracker = DailyLearningTracker("user_123", "path_456")
    
    # Sample data
    for i in range(5):
        date = (datetime.now() - timedelta(days=5-i)).strftime("%Y-%m-%d")
        tracker.log_daily_activity({
            "date": date,
            "hours_spent": 2 + (i * 0.3),
            "sleep_hours": 7 + (i % 2),
            "topics_covered": ["Python basics", "Variables", "Functions"][:i+1],
            "understanding_level": 5 + (i * 0.5),
            "difficulty_faced": "Loops" if i % 2 == 0 else None,
            "completed_tasks": [f"{5 * (i+1)} exercises completed"],
            "mood": ["Motivated", "Neutral", "Frustrated", "Neutral", "Motivated"][i],
            "productivity_rating": 6 + (i * 0.3),
            "notes": f"Day {i+1} of learning"
        })
    
    return tracker
