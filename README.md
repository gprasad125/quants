# Repository for QUANTS
🧠 QUANTS is the Q&A (for) Notion (to) Train Students.

Powered by [Langchain](https://github.com/hwchase17/langchain), this project allows you to query the AI Camp Notion with natural language prompts.

This project is based off of [notion-qa](https://github.com/hwchase17/notion-qa) by Harrison Chase. 

# Environment Setup

## Backend

Install Python dependencies by running
`pip install -r requirements.txt`

Export your OpenAI API Key by running
`export OPENAI_API_KEY=...`

⭐ You may need an API Key without rate limits! ⭐

Launch the Django server
`python manage.py runserver`

Then, navigate to localhost:8000/ask, and paste in your query like so:
```
{
"text": "...your question goes here..."
}
```

Hit POST, and get your answer! 😁


### Written by Alex Zhou, David Kim, and Gokul Prasad
