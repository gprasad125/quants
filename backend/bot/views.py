import json

from rest_framework.decorators import api_view
from rest_framework.response import Response

from bot.models import Question
from quants.qa import askQuestion, final_validation

# Create your views here.

@api_view(["POST"])
def handle_text(request):

    if request.method == "POST":

        # add new Question to database
        text = request.data.get("text", "What is Django?")
        add = Question(text=text)
        add.save()

        # run qa langchain
        validated, possible, sources = askQuestion(text)
        final_test = final_validation(text, validated)

        if final_test == "I do not know.":
            formatted = "I do not know. That information does not exist in the data."
        else:
            formatted = 'Answer: ' + final_test + ', Sources: ' + sources

        # return value
        return Response(formatted)