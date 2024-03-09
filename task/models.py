from django.db import models


class Task(models.Model):
    title = models.TextField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title}'
