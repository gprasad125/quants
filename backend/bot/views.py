from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from bot.models import Question

# Create your views here.

@api_view(["POST"])
def handle_text(request):

    if request.method == "POST":

        # add new Question to database
        text = request.data.get("text", '')
        add = Question(question_text=text)
        add.save()

        return Response("Your data has been saved!", status=200)
