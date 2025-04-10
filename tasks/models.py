from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class Registrationmodel(models.Model):
#     Frist_name=models.CharField(max_length=100)
#     last_name=models.CharField(max_length=100)
#     email=models.CharField(max_length=100)
#     phone=models.IntegerField()
#     password1=models.CharField(max_length=100)
#     password2=models.CharField(max_length=100)
class Task(models.Model):
    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    due_date = models.DateField()
    importance = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    estimated_minutes = models.PositiveIntegerField()
    is_completed = models.BooleanField(default=False)
    ai_priority_score = models.FloatField(default=0.0)

    def __str__(self):
        return self.title
    

class Task_high(models.Model):
    STATUS_CHOICES = [
        ('To Do', 'To Do'),
        ('In Progress', 'In Progress'),
        ('Done', 'Done'),
    ]

    REPEAT_CHOICES = [
        ('None', 'None'),
        ('Daily', 'Daily'),
        ('Weekly', 'Weekly'),
        ('Monthly', 'Monthly'),
    ]
    IMPORTANCE_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    due_date = models.DateTimeField()
    estimated_minutes = models.PositiveIntegerField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='To Do')
    repeat_interval = models.CharField(max_length=50, choices=REPEAT_CHOICES, default='None')
    importance = models.CharField(max_length=10,null=True,blank=True, choices=IMPORTANCE_CHOICES, default='High') 

    def __str__(self):
        return self.title

class Task_medium(models.Model):
    STATUS_CHOICES = [
        ('To Do', 'To Do'),
        ('In Progress', 'In Progress'),
        ('Done', 'Done'),
    ]

    CATEGORY_CHOICES = [
        ('Work', 'Work'),
        ('Personal', 'Personal'),
        ('Study', 'Study'),
        ('Other', 'Other'),
    ]
    IMPORTANCE_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    due_date = models.DateTimeField()
    estimated_minutes = models.PositiveIntegerField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Other')
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='To Do')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    importance = models.CharField(max_length=10, blank=True,null=True,choices=IMPORTANCE_CHOICES, default='Medium')

    def __str__(self):
        return self.title
    


class Task_low(models.Model):
    IMPORTANCE_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]
    importance = models.CharField(max_length=10, blank=True,null=True,choices=IMPORTANCE_CHOICES, default='Medium')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    estimated_minutes = models.IntegerField(default=30)     
    due_date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
