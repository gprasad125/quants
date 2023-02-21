# Django Project Walkthrough

Below is a set up walkthrough for a Django application that summarizes input text. 

All code for this project can be found in [this repository](https://github.com/gprasad125/test_cc). 

---

## 💻 Introduction to Django

Django is a Python-based framework to write web applications. It is one of the most popular options for developers, given its immense flexibility, strong security protocols, and easy integration of AI models. 

In this crash course, you’ll learn to **set up and modify your own Django application** to serve as a backend API to your program. Don’t know what an API is? See a definition [here](https://www.notion.so/Frontend-Lingo-0a3ed29c3ab04445b694a6a1c0e7e6bf). 

### Additional Resources

[How does Django work? ](Django%20Project%20Walkthrough%200cf5b67991f04b6a984c094f31209a62/How%20does%20Django%20work%2003a2907183ac446b937cc25c1646e432.md)

[The Backend Dictionary](The%20Backend%20Dictionary%20c1a2ec05ac36439ea64f2905987c9b46.md)

---

## ✅ To-Do List

Throughout, you will see ****************************[Action Items]**************************** for you to do as you go through this project. 

### Set Up

- [ ]  Ensure you are working in a virtual environment
- [ ]  Install the necessary Python libraries
- [ ]  Launch a Django project and internal application
- [ ]  Run the Django server
- [ ]  Create an Admin account (Super User)

### Building the Summarizer

- [ ]  Build a Django model with a text and date-time field
- [ ]  Register your model on the admin page
- [ ]  Create a summarizer using the OpenAI GPT-3 language model
- [ ]  Write a view to interact between Models and the data

### Using the App

- [ ]  Write a URL to path back to your view
- [ ]  Launch the Django admin site
- [ ]  Post some text to the webpage and summarize

⭐ You will also sometimes see **[Discussion]** tags. These will be times for you to share your progress and work with your teammates! ⭐

---

## 🤖 Step 1: Installing Dependencies

Make sure you are working in a virtual environment, which you can read about [here](Python%20Best%20Practices%20175abddebbbe4dcab9105ed0493f695f.md). Once that is set up, run the following command to install a few necessary packages for Django:

```bash
pip install django djangorestframework
```

This will install:

- The base Django package for your application
- Django REST framework for making your application act like a REST API

### Additional Resources

[Python Best Practices](Python%20Best%20Practices%20175abddebbbe4dcab9105ed0493f695f.md)

[Django Libraries](Django%20Libraries%209011e5767235480bb2d74c6e1b8cc38e.md)

### Action Item

<aside>
💫 **[Action Item] Install the necessary Django dependencies for your application.**

</aside>

## 🔀 Step 2: Launching the Django App

Now that we have the necessary installations, we’ll run a few commands to create the Django boilerplate code. By the end of this step, we’ll have a base Django project with your app activated. 

Firstly, run the following command inside your project directory to launch a Django project:

```python
django-admin startproject project-name 
```

This will create the [following file structure](https://docs.djangoproject.com/en/4.1/intro/tutorial01/#creating-a-project) inside your folder:

- 📁 project-name
    - 📁 project-name
        
        📄 settings.py
        
        configuration settings for your django app
        
        📄 urls.py
        
        URL declaration for your application
        
        📄 wsgi.py and 📄 asgi.py
        
        entry points for WSGI / ASGI web servers
        
    
    📄 manage.py 
    
    launch script - do not edit!
    

Now, navigate to the same level as `manage.py` and run the following command to launch your Django app:

```python
python manage.py startapp app_name
```

This will create the following file structure:

- 📁 app-name
    
    📄 admin.py
    
    📄 apps.py
    
    📄 models.py
    
    📄 tests.py
    
    📄 views.py 
    
    - 📁 migrations

If you would like to know more about the difference between projects vs applications in Django, you can read more about it [here](https://docs.djangoproject.com/en/4.1/intro/tutorial01/#creating-the-polls-app). Briefly, applications are web-based and actively **do** something, while projects are a collection of configurations & settings for several applications. 

Open your project directory in an IDE of your choice (we recommend [VSCode](https://code.visualstudio.com)), and you should see something like the following:

![Here, my virtual environment is called “env”, my Django project is called “my_project” and my application is called “my app”. ](Django%20Project%20Walkthrough%200cf5b67991f04b6a984c094f31209a62/Screenshot_2023-01-18_at_6.06.01_PM.png)

Here, my virtual environment is called “env”, my Django project is called “my_project” and my application is called “my app”. 

Now, we have to register the app inside our project, which we can do by adding our app name, as well as the REST Framework base app, to the list of INSTALLED_APPS inside `settings.py` like so:

```python
INSTALLED_APPS = [
	...,
	...,
	my_app,
	rest_framework
]
```

Next, let’s create a Django administrative account. This will let you register further components of your application onto your Django project. Run the following line in the same level as `manage.py`:

```bash
python manage.py migrate
python manage.py createsuperuser
```

You’ll be prompted to create a username, enter an email, and password. Fill in all of these, and your account will be registered! 

Now, let’s verify it all worked out well! Open your command line tool, navigate to the same level as `manage.py` and run the following command:

```bash
python manage.py runserver
```

You should then be able to open up [localhost:8000](http://localhost:8000) (or whatever port you’ve chosen) and you should see the following image:

![django.png](Django%20Project%20Walkthrough%200cf5b67991f04b6a984c094f31209a62/django.png)

Awesome! You’ve launched your first Django app 👏 

Next, we’ll look into modifying it to have it complete some cool tasks. 

### Additional Resources

[The Django Dictionary](The%20Django%20Dictionary%200e1176b3d08a4c24be8ed973d737702f.md)

### Action Item

<aside>
💫 **[Action Item] Start your project, application, and then verify that it launches on your localhost server. 

[Discussion] Take a screenshot of your file structure with the project + app, and send it into the specified Discord thread!**

</aside>

## 👺 Step 3: Models

Let’s navigate to `models.py` and add a model that your app will use. We are expecting the following parts of data:

1. text: The actual text value that a user sends to our application to be summarized
    - Additional Info
        
        We’ll mark that the max length (in characters) should be 500. You can edit this for your specific scenario. We’ll also say that this field CANNOT be blank, since the summarizer cannot run on nothing. I**n other scenarios, you may want to mark this to be True!** 
        
2. time_sent: The collected date and time of submission.
    - Additional Info
        
        We’ll set auto_now_add as True, which means that every time the text field is entered and sent, the Django application will also automatically collect the date/time information for us. Be careful, you ************CANNOT************ override this in submission, so read up and decide if this what you want should you choose to use this field. 
        

```python
from django.db import models

class Text(models.Model):
	text = models.CharField(max_length = 500, blank = False)
	time_sent = models.DateTimeField(auto_now_add = True) 
```

Now, as admin, we can now register this model on an admin level, meaning we can manage all functions of the model. Navigate to `admin.py` and add the following lines:

```python
from django.contrib import admin
from .models import Text

admin.site.register(Text) 
```

Now that we have a registered model, let’s migrate our changes to our database! Run the following commands inside your command line tool inside your project directory at the same level as `manage.py`: 

```bash
python manage.py makemigrations
python manage.py migrate 
```

Your terminal should spit out some information about changes being added, and now we’re all good to go! 

### Additional Resources

[Migrations](Django%20Project%20Walkthrough%200cf5b67991f04b6a984c094f31209a62/Migrations%20278b6827417249f9870b8185e5186dfb.md)

### Action Item

<aside>
💫 ****[Action Item] Add the Text model to `models.py`, and then migrate those changes over to the database.**

</aside>

Every time you make a change to a model (add, edit, delete, etc.), you will need to make those migrations reflect by running the two commands above! Keep that in mind as you develop your own Django app. 

## 👷‍♂️ Step 4: Building your App!

Now, let’s step away from Django for a second, and build out the actual summarizer, where we’ll use OpenAI’s GPT-3 language model to handle text. 

Let’s create a folder at the same level as `manage.py` called “summarizer” and place the following code block inside a “`summarizer.py`” file within that new folder. 

```python
# import library
import openai

# configure openai to your account 
openai.api_key = ########

def summarize(text):
	
	# create prompt
	prompt = "Write a concise summary of the following content: \n"
	prompt += text
	
	# ping model and generate a response
	response = openai.Completion.create(
			engine = "text-davinci-003",
			prompt = prompt,
			...,
			...,
			...
	)
	
	# clean up response to just the actual String value and return 
	answer = response["choices"][0]["text"].strip()
	return answer 

########################################################
# you can tinker even further with model settings.     #
# read about your options [here](https://beta.openai.com/docs/api-reference/completions/create)                         #
########################################################
```

Afterwards, you should have a file structure like so: 

![Screenshot 2023-01-19 at 5.06.01 PM.png](Django%20Project%20Walkthrough%200cf5b67991f04b6a984c094f31209a62/Screenshot_2023-01-19_at_5.06.01_PM.png)

### Additional Resources

[Environment Variables in Python](Django%20Project%20Walkthrough%200cf5b67991f04b6a984c094f31209a62/Environment%20Variables%20in%20Python%208f607e0c82514fbaa2f9e5237b2508bc.md)

### Action Item

<aside>
💫 **********[Action Item] Create an extra directory to hold your summarizer, and add in the relevant code to a new .py file inside that. 

[Discussion] Change up the prompt! Create a different prompt, and share it with your group!**********

</aside>

## 🥸 Step 5: Views

Up till this point, we’ve built:

- Model, which tells us what the inputted data should look like
- Summarizer, which is how we handle the data

But now, the question becomes how do we get the data from the Text model into the summarizer and back? We’ll now use Django’s **********views********** to accomplish this. 

Navigate to `views.py` and include the following lines:

```python
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Text

from summarizer.summary import * 

# says that this function can do handle POST requests
@api_view(["POST"])
def summarize_view(request):
	
	# handle data inputs
	if request.method == "POST":
		
		# get the data and provide No value if not given
		text = request.data.get("text", None)
		
		# add it to the database and save
		new_addition = Text(text=text)
		new_addition.save()

		# pull the text and summarize it
		summary = summarize(new_addition.text)
		
		# return answer & status 200 (meaning everything worked!) 
		return Response(summary, status=200)
		
```

### Additional Resources

### Action Item

<aside>
💫 **[Action Item] Add a view to** `views.py` **that can handle both POST and GET requests. 

[Discussion] Create an additional view to handle your text data in a different manner. Send your new view into the specific Discord chat.**

</aside>

## 🌐 Step 6: URLs

Up till this point, we have gotten a working backend that can, in theory, take some text, store it inside a database, and if desired, run a summarization function on it. But how do we actually put this into action? We’ll need to use Django URLs to create a pathway for a user to input data and see a response. URLs are like a “table of contents” for your application, telling us where we can go in our web app to get specific tasks completed. 

Navigate to `urls.py`  and include the following:

```python
from my_app.views import *

urlpatterns = [
	...,
	path("/summary", summarize_view),
	...,
]
```

This tells the Django application that when the server swaps to localhost:8000/summary, it should run the view we wrote earlier to handle web requests. In other words, when a user sends some text data to our application, we can go to that URL to see its summary. 

### Additional Resources

[URL Pathways](Django%20Project%20Walkthrough%200cf5b67991f04b6a984c094f31209a62/URL%20Pathways%20fd2fb76e8f5d4a879889c232d9b81600.md)

### Action Item

<aside>
💫 **[Action Item] Add a URL pathway to** `urls.py` **that links back to the view(s) you wrote in Step 5.**

</aside>

## 🔬 Step 7: Trialing Your Application!

Up till this point, we’ve just been writing some code to handle our desired behavior, but now, let’s actually try to use what we’ve built to verify it works as intended. 

Rerun the server, using the command from [above](Django%20Project%20Walkthrough%200cf5b67991f04b6a984c094f31209a62.md), and navigate to [localhost:8000/summary](http://localhost:8000/summary) and you should have an output page like so:

![Note that it says `“Method \GET\ not allowed.”` - Why do you think that is? What are POST vs GET requests doing here? ](Django%20Project%20Walkthrough%200cf5b67991f04b6a984c094f31209a62/Screenshot_2023-01-28_at_5.03.10_PM.png)

Note that it says `“Method \GET\ not allowed.”` - Why do you think that is? What are POST vs GET requests doing here? 

Now, let’s send some data to be summarized. In the “Content” box, enter some text in the following format:

```json
{
	"text": "Some text to be summarized!" 
}
```

After choosing your input text, hit the big POST button to send the data to our backend. After a few seconds, the page should reload and you can see your summarized output like below:

![Screenshot 2023-01-28 at 5.09.49 PM.png](Django%20Project%20Walkthrough%200cf5b67991f04b6a984c094f31209a62/Screenshot_2023-01-28_at_5.09.49_PM.png)

Ta-da! 🥳 We’ve sent some text data to our Django app, and it summarized it and sent it back to us! Note that the output is not perfect, and the summarizer will definitely need to be tweaked with, but you have written your first Django application with POST/GET requests, databases, and URL pathing 🔥 Congratulations! Try out some more text inputs and see what kind of outputs you can get. Can you tweak `summarizer.py` to be better? 

### Additional Resources

[Admin](Django%20Project%20Walkthrough%200cf5b67991f04b6a984c094f31209a62/Admin%20b2979e0b22d94a3eab24199cc4a1d1aa.md)

### Action Item

<aside>
💫 **[Action Item] Launch your server, send some text data through, and verify that an output summary comes back at the correct path. 

[Discussion] For your prompt, what input gave you the best output? Find that text and share it with your team.**

</aside>

## 🏹 Step 8: Creating a GitHub Repository

Now it’s time to upload our code to GitHub, where we can collaborate with others as well as keep track of our changes. Follow this guide to create a local repository from your code and push to a remote repository in GitHub! 

[Git & Github Crash Course](https://www.notion.so/Git-Github-Crash-Course-95777f5bc4ee487a9f60efb3f49681a5)

### Action Item

<aside>
💫 **[Action Item] Create a Git repository from your Django project, and push it to your remote repository on GitHub.

[Discussion] Add a .gitignore file to your Django project following the Git Crash Course. Once you’ve added, commited, and pushed your changes, take a screenshot of your GitHub repo and send it in your team discord channel!**

</aside>

## 👻 Step 9: Connect to Frontend

Try and connect your Django application to a React frontend by following this given guide! 🤩

### Action Item

<aside>
💫 ****[Action Item] Complete the following guide****

[Connecting to React](Django%20Project%20Walkthrough%200cf5b67991f04b6a984c094f31209a62/Connecting%20to%20React%20a78ea8448d6a4a1f948df35ae18c16da.md)

****************************[Discussion] Record a Loom video of your locally-run connected app and send the video to your team over Discord!**************************** 

</aside>

## 💥 Extra Challenge 1! Deploy the App!

Open your app to public online access by deploying it via an easy deployment tool in Railway! 🤩

[Deployment (Railway)](Django%20Project%20Walkthrough%200cf5b67991f04b6a984c094f31209a62/Deployment%20(Railway)%20a0b00f8cc92a4ff489fcc744bd5c9667.md)

## 🤔 Closing Thoughts

You’ve now completed the Django crash course, but you likely will have tons of unanswered questions! That’s great! Now that you have a little more understanding into how Django works, continue exploring and building and using more pieces, especially areas we did not cover here:

- Testing your application’s behavior with `test.py`
- Exploring class-based options in `views.py`
- Using different Django libraries!

As you build your apps, keep looking up what resources are available online, and never hesitate to ask questions when you need to!

Additional resources, tips, and guides can be found [here](Common%20Django%20Topics%20&%20Issues%20f9fb8ff96f4744e1937a64c94fa49d8d.md) as well. 

Happy building! 🔨 🔨