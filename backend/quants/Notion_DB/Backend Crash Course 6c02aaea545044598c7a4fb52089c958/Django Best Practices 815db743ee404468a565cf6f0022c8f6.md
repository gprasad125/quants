# Django Best Practices

While you will need to follow the [best practices for Python](Python%20Best%20Practices%20175abddebbbe4dcab9105ed0493f695f.md) in general, there are a few rules and suggestions for keeping your Django project clean and organized as well. 

## 🛋️ Django’s Own Guide

Thankfully, due to the widespread usage of Django, a helpful collection of best practices, use cases, and other advice has been collected for your need **[here](https://django-best-practices.readthedocs.io/en/latest/)**. Refer to this site often as you build your application! Extra advice is below ⬇️

## ✏️ Models and Field Names

Keep your model names singular and capitalized. Avoid using excessively long names, and for fields, use lower_case with underscores, like so:

```python
from django.db import models

class Car(models.Model):
	name = models.CharField(...)
	model_no = models.IntegerField(...)
	...
```

## ⚙️ Settings

When you initialize a Django project, your `settings.py` file will contain a Django secret key, like so:

```python
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ... 
```

Be sure to put this value inside a .env file, and **********NEVER********** push it to GitHub, as you will get an alert that it has been leaked!