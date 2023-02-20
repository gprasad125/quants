"""Ask a question to the notion database."""
import faiss
from langchain import OpenAI
from langchain.chains import VectorDBQAWithSourcesChain
import pickle
import argparse

# Load the LangChain.
index = faiss.read_index('quants/docs.index')

with open('quants/faiss_store.pkl', 'rb') as f:
    store = pickle.load(f)

store.index = index
chain = VectorDBQAWithSourcesChain.from_llm(llm=OpenAI(temperature=0), vectorstore=store)

def askQuestion(question):
    return chain({'question': question})

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ask a question to the notion DB.')
    parser.add_argument('question', type=str, help='The question to ask the notion DB')
    args = parser.parse_args()

    result = askQuestion(args.question)
    print(f"Answer: {result['answer']}")
    print(f"Sources: {result['sources']}")