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
    
