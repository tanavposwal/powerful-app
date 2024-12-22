from django.db import models

# Create your models here.
class TodoItem(models.Model):
  title = models.CharField(max_length=100)
  is_done = models.BooleanField(default=False)
