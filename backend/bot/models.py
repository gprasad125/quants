from django.db import models

# Create your models here.
class Question(models.Model):
    """
    A model to handle a Question.
    Fields:
    - question_text: The actual String representation of question 
    """

    # define fields
    question_text = models.CharField(max_length = 500)
    
