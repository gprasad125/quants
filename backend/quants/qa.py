"""Ask a question to the notion database."""
import faiss
import pickle

from quants.custom.chain import CustomChain
from quants.custom.prompts import CUSTOM_COMBINE_PROMPT
from quants.custom.validation import validate_answers
from quants.custom.llm import CustomOpenAI

# find_dotenv(load_dotenv())

# # set openai key
# os.environ['OPENAI_API_KEY'] = os.environ.get('openai_api_key')

# Load the LangChain.
index = faiss.read_index('quants/docs.index')

with open('quants/faiss_store.pkl', 'rb') as f:
    store = pickle.load(f)

store.index = index
chain = CustomChain.from_llm(
    llm=CustomOpenAI(temperature=0, model_name="gpt-3.5-turbo"), 
    combine_prompt=CUSTOM_COMBINE_PROMPT,
    vectorstore=store
)

def askQuestion(question):
    results = chain({'question': question})
    validated = validate_answers(results)
    answer = results['answer'].split(':::')
    sources = results['sources']

    return validated, answer, sources

# if __name__ == '__main__':
#     parser = argparse.ArgumentParser(description='Ask a question to the notion DB.')
#     parser.add_argument('question', type=str, help='The question to ask the notion DB')
#     args = parser.parse_args()

#     result = askQuestion(args.question)
#     print(f"Answer: {result['answer']}")
#     print(f"Sources: {result['sources']}")