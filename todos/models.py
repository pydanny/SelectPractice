from django.db import models


class Todo(models.Model):
    is_selected = models.BooleanField()
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField()


    def __str__(self):
      return self.title
