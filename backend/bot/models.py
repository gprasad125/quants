from django.db import models

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

    file = models.FileField(upload_to='quants/Notion_DB')