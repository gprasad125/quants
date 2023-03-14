"""Ask a question to the notion database."""
import faiss
import pickle
import openai
import os

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

def final_validation(question, answer):

    rules = '''
    Determine if the given answer is appropriate for the given question. If not, then return "I do not know". Otherwise, simply return the given answer. For example:

    EXAMPLE PROMPT:
    Given Question: "Who is the president of the United States?"
    Given Answer: "The president of the U.S. is Joe Biden.


    EXAMPLE CORRECT RESPONSE: The president of the U.S. is Joe Biden. 

    EXAMPLE PROMPT:
    Given Question: "Why do we like to use linters?"
    Given Answer: "HTML is a markup language for building websites."

    EXAMPLE CORRECT RESPONSE: I do not know. 

    '''

    prompt = 'Given question: ' + question + ", Given Answer: " + answer

    openai.api_key = os.environ['OPENAI_API_KEY']
    model = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo', 
        messages = [
            {'role': 'system', 'content': rules},
            {'role': 'user', 'content': prompt}
        ]
    )

    validated = model['choices'][0]['message']['content'].strip()

    return validated