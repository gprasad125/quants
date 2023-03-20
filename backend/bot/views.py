import os

from rest_framework.decorators import api_view
from rest_framework.response import Response

from bot.models import Question, File, SourceDocument
from quants.qa import askQuestion, final_validation, process_query
from quants.ingest import ingest_md
from quants.custom.postgres_faiss import PostgresFAISS
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
import numpy as np

# Create your views here.

embedding = OpenAIEmbeddings()

@api_view(["GET", "POST"])
def upload_file(request):
    '''
    Maps to /documents. API for uploading user documents
    '''

    if request.method == "POST":

        files = request.data.getlist('files')
        if not files or len(files) < 1:
            return Response('No files received', status=400)

        data = []
        sources = []
        for file in files:
            ext = os.path.splitext(file.name)[1]
            if ext.lower() in ['.md', '.txt']:
                data.append(str(file.read(), encoding="utf-8", errors="ignore"))
                sources.append(file.name)
        text_splitter = CharacterTextSplitter(chunk_size=1500, separator="\n")
        docs = []
        metadatas = []
        for i, d in enumerate(data):
            splits = text_splitter.split_text(d)
            docs.extend(splits)
            metadatas.extend([{"source": sources[i]}] * len(splits))

        embeddings = embedding.embed_documents(docs)

        # delete prev documents
        SourceDocument.objects.all().delete()

        for i in range(len(embeddings)):
            SourceDocument.objects.create(
                name=metadatas[i]['source'],
                content=docs[i],
                embedding=embeddings[i]
            )
        return Response('files ingested! ready to be queried', status=200)
    else:
        docs = SourceDocument.objects.all()
        res = []
        for doc in docs:
            res.append(doc.name)
        return Response(res, status=200)


@api_view(['GET'])
def get_file(request, file_id):
    '''
    Maps to /documents/file_id/. API for getting user documents
    '''
    try:
        doc = SourceDocument.objects.get(id=file_id)
    except SourceDocument.DoesNotExist:
        return Response('file not found!', status=404)
    
    res = {
        'name': doc.name,
        'content': doc.content
    }
    return Response(res, status=200)


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

        query = SourceDocument.objects.all()

        # run qa langchain
        validated, possible, sources = process_query(query, text)
        # validated, possible, sources = askQuestion(text)
        
        parsed_sources = map(lambda x: x.strip(), sources.split(','))
        formatted_sources = []
        for source in parsed_sources:
            doc = SourceDocument.objects.filter(id=source).first()
            if doc is not None:
                formatted_sources.append({
                    'name': doc.name,
                    'id': doc.id,
                    'extract': '' # set extract here
                })

        formatted = {
            'question': text,
            'answer': validated,
            'sources': formatted_sources
        }

        # return value
        return Response(formatted)
