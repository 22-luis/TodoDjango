from django.db import models
from todoApp.models.user import User

class Task(models.Model):
    status_choices = models.TextChoices('pending', 'done')
    title = models.CharField(max_length=150)
    description = models.TextField()
    status = models.CharField(choices=status_choices, default='pending')
    user = models.ForeignKey(User, on_delete=models.CASCADE)