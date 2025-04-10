# 3. tasks/utils.py
from datetime import date

def calculate_priority(task):
    days_left = (task.due_date.date() - date.today()).days  # FIXED HERE
    importance_score = {'Low': 1, 'Medium': 2, 'High': 3}[task.importance]
    time_penalty = task.estimated_minutes / 60
    score = days_left * 1.5 - importance_score * 3 + time_penalty
    return max(0.0, round(score, 2))
