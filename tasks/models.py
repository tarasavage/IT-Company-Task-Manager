from django.contrib.auth.models import AbstractUser
from django.db import models


class Position(models.Model):
    name = models.CharField(max_length=55, unique=True)

    def __str__(self) -> str:
        return f"{self.name}"


class TaskType(models.Model):
    name = models.CharField(max_length=55, unique=True)

    def __str__(self) -> str:
        return f"{self.name}"


class Worker(AbstractUser):
    position = models.ForeignKey(to=Position, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.position} {self.first_name} {self.last_name}"


class Task(models.Model):
    PRIORITY_CHOICES = (
        ("1", "Urgent"),
        ("2", "High"),
        ("3", "Medium"),
        ("4", "Low"),
    )

    name = models.CharField(max_length=55)
    description = models.TextField(blank=True, null=True)
    deadline = models.DateTimeField(blank=True, null=True)
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(
        max_length=1,
        choices=PRIORITY_CHOICES,
        default="3",
    )
    task_type = models.ForeignKey(to=TaskType, on_delete=models.CASCADE)
    assignees = models.ManyToManyField(to=Worker, related_name="tasks", blank=True)

    def __str__(self) -> str:
        return f"{self.name} {self.priority} {self.deadline} {self.is_completed}"
