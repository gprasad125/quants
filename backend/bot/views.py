import json

from rest_framework.decorators import api_view
from rest_framework.response import Response

from bot.models import Question, File
from quants.qa import askQuestion, final_validation
from quants.ingest import ingest_md

# Create your views here.

@api_view(["POST"])
def handle_file(request):

    if request.method == "POST":

        file = request.data.get('file', None)
        if file == None:
            return Response('Files failed to be uploaded.')

        add = File(file=file)
        add.save()

        return Response('files uploaded!')

@api_view(["POST"])
def ingest(request):

    if request.method == "POST":

        trial = ingest_md()
        if trial:
            return Response('files ingested! ready to be queried')
        elif trial == "No Files Uploaded!":
            return Response(trial)
        else:
            return Response('files failed to be ingested.')


@api_view(["POST"])
def handle_text(request):

    if request.method == "POST":

        # add new Question to database
        text = request.data.get("text", "What is Django?")
        add = Question(text=text)
        add.save()

        # run qa langchain
        validated, possible, sources = askQuestion(text)
        # final_test = final_validation(text, validated)

        # if final_test == "I do not know.":
            
        #     sources = []
        
        formatted = json.dumps({
            'question': text,
            'answer': validated,
            'sources': sources
        })

        # return value
        return Response(formatted)