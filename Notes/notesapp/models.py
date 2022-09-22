from django.db import models

# Create your models here.

class Note(models.Model):
    title = models.CharField(max_length = 200)
    content = models.CharField(max_length = 2000)
    date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date']
