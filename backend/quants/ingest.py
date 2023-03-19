from pathlib import Path
from langchain.text_splitter import CharacterTextSplitter
import faiss
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
import pickle
import os

def ingest_md():

    # make sure it isn't empty
    if len(os.listdir('quants/Notion_DB/')) < 1:
        return "No Files Uploaded!"

    # Here we load in the data in the format that Notion exports it in.
    ps = list(Path("quants/Notion_DB/").glob("**/*.md"))


    print('loading data...')
    data = []
    sources = []
    for p in ps:
        with open(p, encoding="utf8") as f:
            data.append(f.read())
        sources.append(p)

    # Here we split the documents, as needed, into smaller chunks.
    # We do this due to the context limits of the LLMs.

    print('loading finished! now splitting data...')
    text_splitter = CharacterTextSplitter(chunk_size=1500, separator="\n")
    docs = []
    metadatas = []
    for i, d in enumerate(data):
        splits = text_splitter.split_text(d)
        docs.extend(splits)
        metadatas.extend([{"source": sources[i]}] * len(splits))

    print('splitting finished! now embedding data...')
    # Here we create a vector store from the documents and save it to disk.
    store = FAISS.from_texts(docs, OpenAIEmbeddings(), metadatas=metadatas)
    faiss.write_index(store.index, "quants/docs.index")
    store.index = None
    with open("quants/faiss_store.pkl", "wb") as f:
        pickle.dump(store, f)

    return True