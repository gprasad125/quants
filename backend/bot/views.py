import json

from django.http import JsonResponse
from django.shortcuts import render
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
        answer = askQuestion(text)
        answer = json.dumps(answer)

        # return value
        return Response(answer)