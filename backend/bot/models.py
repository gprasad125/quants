from django.db import models
from datetime import datetime

# Create your models here.
class Question(models.Model):
    """
    A model to handle a Question.
    Fields:
    - text: The actual String representation of question 
    """

    # define fields
    text = models.CharField(max_length = 500)
    
class File(models.Model):
    """
    A model to take in a uploaded .md File
    Fields:
        - file: the file
    """

    file = models.FileField(upload_to='quants/Notion_DB/')
    filename = models.CharField(max_length=255, blank=True)
    time_added = models.DateTimeField(auto_now_add = True)

    def save(self, *args, **kwargs):
        if not self.filename:
            cleaned = self.file.name.split('/')[-1]
            self.filename = cleaned
        super().save(*args, **kwargs)