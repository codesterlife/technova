from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Score(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='score')
    score = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.user.username
    
class VisitedTasks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='visited_tasks')
    visited_level1_task1 = models.BooleanField(default=False)
    visited_level1_task2 = models.BooleanField(default=False)
    visited_level1_task3 = models.BooleanField(default=False)
    visited_level1_task4 = models.BooleanField(default=False)
    visited_level1_task5 = models.BooleanField(default=False)
    visited_level2_task1 = models.BooleanField(default=False)
    visited_level2_task2 = models.BooleanField(default=False)
    visited_level2_task3 = models.BooleanField(default=False)
    visited_level2_task4 = models.BooleanField(default=False)
    visited_level3_task = models.BooleanField(default=False)
    visited_level4_task1 = models.BooleanField(default=False)
    visited_level4_task2 = models.BooleanField(default=False)
    visited_level5_task = models.BooleanField(default=False)
    visited_level5_task_clue1 = models.BooleanField(default=False)
    visited_level5_task_clue2 = models.BooleanField(default=False)
    visited_level5_task_clue3 = models.BooleanField(default=False)
    visited_level5_task_clue4 = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.user.username