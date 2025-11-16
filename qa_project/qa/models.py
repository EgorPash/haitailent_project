from typing import Any

from django.db import models
import uuid

class Question(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(args, kwargs)
        self.id = None

    def __str__(self):
        return self.text

class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    user_id = models.UUIDField(default=uuid.uuid4, editable=False)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
