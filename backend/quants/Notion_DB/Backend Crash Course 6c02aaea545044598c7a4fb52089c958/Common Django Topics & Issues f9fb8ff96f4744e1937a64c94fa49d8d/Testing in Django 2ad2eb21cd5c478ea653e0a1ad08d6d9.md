# Testing in Django

Up till now, the Backend Crash Course has followed a strategy of write code —> trial locally —> deploy; however, this crash course is also meant to introduce you to the best practices of development, and so it is important to understand the value of testing your application. 

---

## Looking at a Problem

Let’s consider the following code:

```python
from django.db import models
import timezone
import datetime

class Text(models.Model):
	text = models.CharField(max_length = 500, blank = False)
	time_sent = models.DateTimeField() 

	def is_text_recent(self):
		allowed_minimum = timezone.now() - datetime.timedelta(days=3)
		return allowed_minimum <= self.time_sent
	
```

- What is `is_text_recent()` ?
    
    As we can see, the `Question` model has a method called `is_text_recent()`. This method returns a boolean value indicating whether the `Question` was published recently or not. The method calculates this by checking whether the `pub_date` field of the `Question` is greater than or equal to the current time (as returned by `timezone.now()`) minus three days (as represented by `datetime.timedelta(days=3)`).
    
    In other words, if the `pub_date` of the `Question` is within the past three days, `is_text_recent()` will return `True`; otherwise, it will return `False`. This method can be useful for filtering and displaying recent questions in a web application.
    

While this is a pretty useful feature that could be used in a wide variety of applications, there’s one glaring flaw. Let’s write some tests to see if we can figure out what exactly that issue is! 

## Using the Test File

Let’s navigate over to the boilerplate `tests.py` file and write up some simple tests that probe the logic of our `Text` model and see if it holds up. You can look at the following code as an idea of what tests look like:

```python
import datetime

from django.tests import TestCase
from django.utils import timezone

from .models import Text

class TextTestCases(TestCase):
	
	def text_from_future_test(self):
		
		# Initialize a Text entry that's "sent in" 40 days into the future
		future_timing = timezone.now() + datetime.timedelta(days = 40)
		text_from_future = Text(text = "hello", time_sent = future_timing)

		# This should return False. Future tweets are not "recent" !!
		current_answer = text_from_future.is_text_recent()
		self.assertIs(current_answer, False)
		
```

We can then run the following command in a command line tool in our project directory to run our tests as we’ve written them. 

```bash
python manage.py test my_app
```

You should get a failure message, telling you that `text_from_future_test()` failed since `True` is not `False`, and that a test database was destroyed! What does it all mean? 

1. Yes! We expected this to fail to expose that our model logic has some error in it. Specifically, the fact that, by our current code, any Tweet greater than 3 days ago is “recent” so in our Test, a Text data entry created 40 days into the future is still “recent”! Whoops 😳
2. Test databases? Yup! When Django runs test files, it does not want to sully your development SQLite databases with test data, especially if those are error-prone or have bad data. Therefore, **********************every********************** time Django runs tests, it creates local test-only databases and destroys them after executing them! 

## Fixing The Logic

Now that we have an idea of what went wrong with our code, we can go ahead and fix the logic of our original database. Namely, the definition of “recent” needs to be capped at the current timezone, like so:

```python
class Text(models.Model):
	...
	...
	def is_text_recent(self):
		allowed_minimum = timezone.now() - datetime.timedelta(days=3)
		return allowed_minimum <= self.time_sent <= timezone.now()
```

And voila! Run your tests and see that they’ll pass this time. You’ve now written your first set of 

tests and seen what they’re capable of and useful for. 

---

## Reading On

You’ve just scratched the surface of what testing is all about. You can test your Django models, views, forms, and nearly anything else you can think of. It’s always good practice to find vulnerabilities that you may have missed the first time by using tests. 

[📌 Official Testing Documentation](https://docs.djangoproject.com/en/4.1/intro/tutorial05)