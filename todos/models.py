from datetime import datetime
from django.db import models


class Todo(models.Model):
    text = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    is_complete = models.BooleanField(default=False)
    def __str__(self):
        return self.text
