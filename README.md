# Repository for QUANTS
🧠 QUANTS is the Q&A (for) Notion (to) Train Students.

Powered by [Langchain](https://github.com/hwchase17/langchain), this project allows you to query the AI Camp Expert Course with natural language prompts.

This project is based off of [notion-qa](https://github.com/hwchase17/notion-qa) by Harrison Chase. 

# Environment Setup

## Backend

Install Python dependencies by running
`pip install -r requirements.txt`

Export your OpenAI API key to the script by running
`export OPENAI_API_KEY=...`
You'll need an OpenAI account to get access to an API Key, which you can make [here](https://platform.openai.com). 

⭐ You may need an API Key without rate limits! ⭐

Ingest your markdown files by going to `backend/quants` and creating a `Notion_DB` directory containing your files. After creating and uploading your files, run `python3 ingest.py` to create the vector embeddings, document indices, and other files important for semantic search. 

# Local Server

Launch the Django server inside `backend`:

`python3 manage.py runserver`

Launch the React server inside `frontend`:

`npm run dev`

Navigate to the frontend link provided in your browser, and paste your question in the text box. Hit ask, and get your answer! 😁


### Written by Alex Zhou, David Kim, and Gokul Prasad
