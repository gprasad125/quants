# Environment Variables in Python

In your time as a developer, you’ll come across tons of information that should remain private to ensure the security of your application. One of the most common types of info is authentication tokens, such as API keys that provide you access to services like Twitter or OpenAI GPT-3. We don’t want to push this to public sites like GitHub repositories, yet we obviously need them in our applications, so how do we handle this? We use ********************************************environment variables********************************************!

---

********************************************Step 1: Install packages********************************************

We’ll be using the `dotenv` Python library, which we install in a command line tool like so: 

```bash
pip install python-dotenv
```

********************************************************Step 2: Create the .env file********************************************************

Next, create a `.env` file in your project directory. This is a file with no name, and just a `.env` extension, which you can do like so:

```bash
touch .env
```

Go ahead and add whatever secret values are needed for your project here in a key=value style. For this course, we’ll need to include the Django secret key (found in `settings.py` — read more [here](../Django%20Best%20Practices%20815db743ee404468a565cf6f0022c8f6.md).) and our OpenAI account’s API key. Paste in the values like so: 

```
django_secret_key = ...
openai_api_key = ...
```

****************************************Step 3: Load and pull variables****************************************

Next, whenever you need these values, you can load them like so: 

```python
import os
from dotenv import load_dotenv, find_dotenv

# finds and loads the .env file
load_dotenv(find_dotenv())

# call the variable from the loaded file
openai.api_key = os.environ.get("openai_api_key")
```

****************Step 4: Ignore the Variables!**************** 

Ensure that your .env file is ignored in your Git repository by checking your .gitignore file to see if `.env` is listed. Read about that [here](https://www.notion.so/Git-Github-Crash-Course-95777f5bc4ee487a9f60efb3f49681a5).