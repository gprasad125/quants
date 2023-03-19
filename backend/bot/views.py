import json
import os

from rest_framework.decorators import api_view
from rest_framework.response import Response

from bot.models import Question, File
from quants.qa import askQuestion, final_validation
from quants.ingest import ingest_md

# Create your views here.

@api_view(["POST"])
def upload_file(request):
    '''
    Maps to /documents. API for uploading user documents
    '''

    if request.method == "POST":

        files = request.data.getlist('files')
        if not files or len(files) < 1:
            return Response('No files received', status=400)

        current = os.listdir('quants/Notion_DB')
        if len(current) > 1:
            for existing_file in current: 

                # if markdown
                if existing_file[-2:] == "md":
                    if os.path.exists(existing_file):
                        os.remove(existing_file)

        for file in files:
            add = File(file=file)
            add.save()

        trial = ingest_md()
        if trial:
            return Response('files ingested! ready to be queried', status=200)
        elif trial == "No Files Uploaded!":
            return Response(trial, status=400)
        else:
            return Response('files failed to be ingested.', status=500)
        

@api_view(['GET'])
def get_file(request, filename):
    '''
    Maps to /documents/filename. API for getting user documents
    '''

    try:

        file = File.objects.get(filename = filename)
        
        filepath = file.file.path
        with open(filepath, 'r') as f:
            content = f.read()

        answer = {
            "name": filename,
            "content": content
        }

        return Response(answer)

    except File.DoesNotExist:
        current_files = '['
        for f in File.objects.all():
            current_files += f.filename + ', '

        return Response('File does not exist! Current files include: ' + current_files + ']')

    except File.MultipleObjectsReturned:

        file = File.objects.filter(filename = filename).latest('time_added')
        filepath = file.file.path
        with open(filepath, 'r') as f:
            content = f.read()

        answer = {
            "name": filename,
            "content": content
        }

        return Response(answer)

@api_view(["POST"])
def query(request):
    '''
    Maps to query/. API for querying document database. 
    '''

    if request.method == "POST":

        # add new Question to database
        text = request.data.get("question", "What is Django?")
        add = Question(text=text)
        add.save()

        # run qa langchain
        validated, possible, sources = askQuestion(text)
        
        formatted = {
            'question': text,
            'answer': validated,
            'sources': sources
        }

        # return value
        return Response(formatted)