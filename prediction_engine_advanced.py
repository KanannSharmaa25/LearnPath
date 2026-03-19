# prediction_engine_advanced.py
# Predict learning progress, mastery time, and success rates

import math
from datetime import datetime, timedelta

class LearningPredictorAdvanced:
    """Predict learning outcomes based on user behavior"""
    
    def __init__(self, user_profile, learning_path, tracking_logs=None):
        self.user_profile = user_profile
        self.learning_path = learning_path
        self.tracking_logs = tracking_logs or []
    
    def predict_completion_time(self):
        """
        Predict when user will complete the learning path
        
        Returns:
            {
                "estimated_completion_date": "...",
                "completion_weeks": 10,
                "completion_date": "2024-03-15",
                "confidence": 0.75,
                "factors": {...}
            }
        """
        
        # Get parameters
        planned_duration = self.learning_path.get("estimated_duration_weeks", 8)
        daily_hours = self.user_profile.get("daily_hours", 2)
        consistency = self.user_profile.get("consistency", 5)
        procrastination = self.user_profile.get("procrastination_level", 5)
        
        # Adjustment factors
        consistency_factor = consistency / 5  # 0.2 to 2.0
        
        if procrastination >= 8:
            procrastination_penalty = 1.3
        elif procrastination >= 6:
            procrastination_penalty = 1.15
        elif procrastination <= 2:
            procrastination_penalty = 0.9
        else:
            procrastination_penalty = 1.0
        
        # Adjust based on actual logs if available
        if len(self.tracking_logs) >= 3:
            actual_performance = self._analyze_actual_performance()
            performance_multiplier = actual_performance.get("adjustment_multiplier", 1.0)
        else:
            performance_multiplier = 1.0
        
        # Calculate adjusted duration
        adjusted_duration = planned_duration * (procrastination_penalty / consistency_factor) * performance_multiplier
        
        # Calculate confidence
        if len(self.tracking_logs) >= 5:
            confidence = 0.85
        elif len(self.tracking_logs) >= 3:
            confidence = 0.70
        else:
            confidence = 0.55
        
        completion_date = datetime.now() + timedelta(weeks=adjusted_duration)
        
        return {
            "estimated_completion_weeks": round(adjusted_duration, 1),
            "estimated_completion_date": completion_date.strftime("%Y-%m-%d"),
            "confidence_percentage": round(confidence * 100, 1),
            "confidence_level": self._get_confidence_label(confidence),
            "factors": {
                "planned_duration_weeks": planned_duration,
                "consistency_adjustment": round(consistency_factor, 2),
                "procrastination_adjustment": round(procrastination_penalty, 2),
                "actual_performance_adjustment": round(performance_multiplier, 2),
                "daily_hours_commitment": daily_hours
            },
            "estimated_total_hours": round(adjusted_duration * daily_hours * 7, 0)
        }
    
    def predict_mastery_timeline(self):
        """
        Predict timeline to mastery (not just completion)
        
        Mastery levels:
        - Beginner: Can do basic tasks
        - Intermediate: Can solve problems independently
        - Advanced: Can teach others
        - Expert: Deep mastery
        """
        
        completion = self.predict_completion_time()
        base_weeks = completion["estimated_completion_weeks"]
        
        timeline = {
            "beginner_achievement": {
                "weeks_from_now": round(base_weeks * 0.25, 1),
                "date": (datetime.now() + timedelta(weeks=base_weeks * 0.25)).strftime("%Y-%m-%d"),
                "description": "Can understand basic concepts and complete simple tasks",
                "criteria": ["Completed fundamentals stage", "Score 70%+ on assessments"]
            },
            "intermediate_achievement": {
                "weeks_from_now": round(base_weeks * 0.65, 1),
                "date": (datetime.now() + timedelta(weeks=base_weeks * 0.65)).strftime("%Y-%m-%d"),
                "description": "Can solve problems independently and build small projects",
                "criteria": ["Completed core concepts", "Built 2-3 projects", "Score 85%+ on assessments"]
            },
            "advanced_achievement": {
                "weeks_from_now": round(base_weeks * 1.2, 1),
                "date": (datetime.now() + timedelta(weeks=base_weeks * 1.2)).strftime("%Y-%m-%d"),
                "description": "Can teach others and contribute meaningfully",
                "criteria": ["Built portfolio projects", "Help others learn", "Score 90%+ on assessments"]
            },
            "expert_achievement": {
                "weeks_from_now": round(base_weeks * 2, 1),
                "date": (datetime.now() + timedelta(weeks=base_weeks * 2)).strftime("%Y-%m-%d"),
                "description": "Deep mastery, can solve complex problems and innovate",
                "criteria": ["Years of practice", "Original projects", "Industry recognition"]
            }
        }
        
        return timeline
    
    def predict_success_rate(self):
        """
        Predict probability of successfully completing the learning path
        
        Returns: percentage 0-100
        """
        
        consistency = self.user_profile.get("consistency", 5)
        motivation = self.user_profile.get("motivation", 5)
        daily_hours = self.user_profile.get("daily_hours", 2)
        burnout_freq = self.user_profile.get("burnout_frequency", "Sometimes")
        procrastination = self.user_profile.get("procrastination_level", 5)
        
        # Base score
        score = 70
        
        # Adjust for consistency
        score += (consistency - 5) * 3
        
        # Adjust for motivation
        score += (motivation - 5) * 2
        
        # Adjust for time commitment
        if daily_hours >= 3:
            score += 5
        elif daily_hours < 1:
            score -= 10
        
        # Adjust for burnout
        if burnout_freq == "Often":
            score -= 15
        elif burnout_freq == "Very often":
            score -= 25
        elif burnout_freq == "Rarely":
            score += 10
        
        # Adjust for procrastination
        score -= (procrastination - 5) * 2
        
        # Look at actual performance
        if len(self.tracking_logs) >= 3:
            actual = self._analyze_actual_performance()
            score += actual.get("success_adjustment", 0)
        
        # Cap between 20-95%
        score = max(20, min(95, score))
        
        return {
            "success_probability_percentage": round(score, 1),
            "success_rating": self._get_success_rating(score),
            "key_factors": self._identify_success_factors()
        }
    
    def _get_confidence_label(self, confidence):
        """Get confidence label"""
        if confidence >= 0.8:
            return "Very High"
        elif confidence >= 0.65:
            return "High"
        elif confidence >= 0.5:
            return "Medium"
        else:
            return "Low"
    
    def _get_success_rating(self, score):
        """Get success rating label"""
        if score >= 85:
            return "Very High"
        elif score >= 70:
            return "High"
        elif score >= 55:
            return "Medium"
        elif score >= 40:
            return "Low"
        else:
            return "Very Low"
    
    def _identify_success_factors(self):
        """Identify key factors affecting success"""
        factors = {
            "positive": [],
            "negative": [],
            "neutral": []
        }
        
        consistency = self.user_profile.get("consistency", 5)
        if consistency >= 7:
            factors["positive"].append("High consistency - you stick to goals")
        elif consistency <= 3:
            factors["negative"].append("Low consistency - may struggle with sustained effort")
        else:
            factors["neutral"].append("Moderate consistency - could improve")
        
        daily_hours = self.user_profile.get("daily_hours", 2)
        if daily_hours >= 3:
            factors["positive"].append("Good daily time commitment")
        elif daily_hours < 1:
            factors["negative"].append("Limited daily time - learning will be slow")
        
        motivation = self.user_profile.get("motivation", 5)
        if motivation >= 7:
            factors["positive"].append("Strong intrinsic motivation")
        
        if len(self.tracking_logs) >= 3:
            actual = self._analyze_actual_performance()
            if actual.get("trend") == "improving":
                factors["positive"].append("Showing improvement over time")
            elif actual.get("trend") == "declining":
                factors["negative"].append("Performance trend is declining")
        
        return factors
    
    def _analyze_actual_performance(self):
        """Analyze actual performance from logs"""
        if len(self.tracking_logs) < 2:
            return {"adjustment_multiplier": 1.0}
        
        # Get recent logs
        recent_logs = self.tracking_logs[-5:]
        
        # Average metrics
        avg_hours = sum(log.get("hours_spent", 0) for log in recent_logs) / len(recent_logs)
        avg_understanding = sum(log.get("understanding_level", 5) for log in recent_logs) / len(recent_logs)
        avg_productivity = sum(log.get("productivity_rating", 5) for log in recent_logs) / len(recent_logs)
        
        # Detect trend
        if len(recent_logs) >= 3:
            early_understanding = sum(log.get("understanding_level", 5) for log in recent_logs[:2]) / 2
            late_understanding = sum(log.get("understanding_level", 5) for log in recent_logs[-2:]) / 2
            trend = "improving" if late_understanding > early_understanding else "declining"
        else:
            trend = "stable"
        
        # Calculate adjustment
        if avg_productivity >= 7 and avg_understanding >= 6:
            adjustment_multiplier = 0.85  # You're ahead of schedule
            success_adjustment = 5
        elif avg_productivity <= 3 or avg_understanding <= 3:
            adjustment_multiplier = 1.3  # You're behind schedule
            success_adjustment = -10
        else:
            adjustment_multiplier = 1.0  # On track
            success_adjustment = 0
        
        return {
            "average_hours_spent": round(avg_hours, 2),
            "average_understanding": round(avg_understanding, 1),
            "average_productivity": round(avg_productivity, 1),
            "trend": trend,
            "adjustment_multiplier": adjustment_multiplier,
            "success_adjustment": success_adjustment
        }
    
    def predict_optimal_learning_schedule(self):
        """Predict optimal schedule based on user patterns"""
        
        if not self.tracking_logs or len(self.tracking_logs) < 3:
            return {
                "recommendation": "Need more data to predict optimal schedule",
                "message": "Log 3+ days of learning to get personalized recommendations"
            }
        
        # Analyze logs by day of week and time patterns
        days_of_week = {}
        for log in self.tracking_logs:
            date_obj = datetime.fromisoformat(log["date"])
            day_name = date_obj.strftime("%A")
            
            if day_name not in days_of_week:
                days_of_week[day_name] = []
            
            days_of_week[day_name].append({
                "productivity": log.get("productivity_rating", 5),
                "understanding": log.get("understanding_level", 5),
                "hours": log.get("hours_spent", 0)
            })
        
        # Find best days
        day_scores = {}
        for day, logs in days_of_week.items():
            avg_productivity = sum(l["productivity"] for l in logs) / len(logs)
            avg_understanding = sum(l["understanding"] for l in logs) / len(logs)
            score = (avg_productivity + avg_understanding) / 2
            day_scores[day] = score
        
        best_days = sorted(day_scores.items(), key=lambda x: x[1], reverse=True)[:3]
        
        return {
            "optimal_schedule": {
                "best_days": [day for day, _ in best_days],
                "intensity": "High" if best_days[0][1] >= 7 else "Medium"
            },
            "recommendations": [
                f"Focus most learning effort on {best_days[0][0]}" if best_days else "No recommendation yet",
                "Maintain consistency with your daily routine",
                "Adjust based on how you feel each week"
            ]
        }
    
    def generate_prediction_report(self):
        """Generate complete prediction report"""
        
        report = {
            "generated_at": datetime.now().isoformat(),
            "user_profile_summary": {
                "consistency": self.user_profile.get("consistency", 5),
                "daily_hours": self.user_profile.get("daily_hours", 2),
                "motivation": self.user_profile.get("motivation", 5),
                "burnout_frequency": self.user_profile.get("burnout_frequency", "Unknown")
            },
            "completion_prediction": self.predict_completion_time(),
            "mastery_timeline": self.predict_mastery_timeline(),
            "success_prediction": self.predict_success_rate(),
            "optimal_schedule": self.predict_optimal_learning_schedule(),
            "personalized_recommendations": self._generate_personalized_predictions()
        }
        
        return report
    
    def _generate_personalized_predictions(self):
        """Generate personalized prediction insights"""
        recommendations = []
        
        completion = self.predict_completion_time()
        success = self.predict_success_rate()
        
        # Based on completion timeline
        if completion["estimated_completion_weeks"] > 20:
            recommendations.append({
                "prediction": "Extended Timeline",
                "insight": f"Based on your current pace, expect to complete in ~{completion['estimated_completion_weeks']} weeks",
                "action": "Consider increasing daily hours or seeking accountability"
            })
        
        # Based on success rate
        if success["success_probability_percentage"] < 50:
            recommendations.append({
                "prediction": "Success Risk",
                "insight": "Success probability is below 50% based on current factors",
                "action": [
                    "Improve consistency with daily practice",
                    "Increase daily time commitment",
                    "Reduce procrastination triggers",
                    "Find an accountability partner"
                ]
            })
        elif success["success_probability_percentage"] > 80:
            recommendations.append({
                "prediction": "High Success Probability",
                "insight": f"You have a {success['success_probability_percentage']}% chance of successful completion",
                "action": "Maintain your current momentum and consistency!"
            })
        
        # Based on burnout risk
        if self.user_profile.get("burnout_frequency") == "Often":
            recommendations.append({
                "prediction": "Burnout Risk",
                "insight": "You're prone to burnout - adjust learning pace accordingly",
                "action": [
                    "Take strategic breaks",
                    "Don't overload yourself",
                    "Mix difficult and easy topics",
                    "Celebrate small wins"
                ]
            })
        
        # Based on actual performance
        if len(self.tracking_logs) >= 5:
            actual = self._analyze_actual_performance()
            if actual.get("trend") == "improving":
                recommendations.append({
                    "prediction": "Positive Momentum",
                    "insight": "Your performance is improving over time!",
                    "action": "Keep up the excellent work"
                })
            elif actual.get("trend") == "declining":
                recommendations.append({
                    "prediction": "Declining Performance",
                    "insight": "Recent performance is declining - address this quickly",
                    "action": [
                        "Review concepts you're struggling with",
                        "Take a break and rest",
                        "Change learning method",
                        "Seek help"
                    ]
                })
        
        return recommendations
