import json

from rest_framework.decorators import api_view
from rest_framework.response import Response

from bot.models import Question
from quants.qa import askQuestion

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
        formatted = "Validated: {0}, Answer: {1}, Sources: {2}".format(validated, possible, sources)

        # return value
        return Response(formatted)