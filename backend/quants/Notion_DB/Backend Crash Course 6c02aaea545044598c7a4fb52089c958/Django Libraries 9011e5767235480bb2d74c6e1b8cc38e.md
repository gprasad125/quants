# Django Libraries

Over the time that Django has risen in popularity, the community around the tool has developed some incredible libraries to extend functionality in some awesome ways. 

---

You’ve worked with `djangorestframework` and `django-cors-headers` but there’s many more that could prove useful to you as you develop your applications. Here’s a few to think about: 

- `django-extensions`
    
    This library adds a lot more functionality to your Django development environment. Whether you need to add a log-in system with auto generated passwords, or automatically collect all user emails, the `django-extensions` library gives you a ton of cool new tools to use. 
    
    ```bash
    pip install django-extensions
    ```
    
    ********************Resources:********************
    
    [📌 PyPI link](https://pypi.org/project/django-extensions/)
    
    [📎 Documentation](https://django-extensions.readthedocs.io/en/stable/index.html)
    
- `django-simple-history`
    
    You’ll make a ton of changes to your databases as you develop your apps, and the django-simple-history library helps keep track of those edits. 
    
    ```bash
    pip install django-simple-history
    ```
    
    **Resources:**
    
    [📌 PyPI link](https://pypi.org/project/django-simple-history/)
    
    [📎 Documentation](https://django-simple-history.readthedocs.io/)
    
- `celery`
    
    Oftentimes, you develop a web app with the purview of just a few infrequent uploads, but it is good practice to plan for the case of high-usage and demand for your application. Deployment onto cloud platforms can be made tricky when your tool faces a ton of requests all at once, and one way to handle that can be passing processes onto a separate system. That’s where `celery` comes in.  
    
    Unlike the other two linked above, `celery` is ******not****** a Django-centric package, but can be combined smoothly into your Django app as a task-handler for heavy requests. 
    
    ************Note:************ You can also look into using the more Django-centric `django-carrot` library if `celery` proves to be more than what you need. Read the docs [here](https://django-carrot.readthedocs.io/en/1.2.1/)!
    
    ********************Resources:********************
    
    [🤝 Django + Celery Tutorial](https://realpython.com/asynchronous-tasks-with-django-and-celery/)
    
    [📌 PyPI Link](https://pypi.org/project/celery/)
    
    [📎 Documentation](https://docs.celeryq.dev/en/stable/)
    

These are far from the only ones you will encounter that you can use. Make sure to look around in the following links to see if you would like using any other Django-helpful library 🔥

1. ****[10 Django Packages Every Developer Must Know](https://codete.com/blog/10-django-packages-every-developer-must-know)****
2. ****[The 10 Most-Used Django Packages](https://learndjango.com/tutorials/10-most-used-django-packages)****
3. ****[8 Python packages that will simplify your life with Django](https://opensource.com/article/18/9/django-packages)****