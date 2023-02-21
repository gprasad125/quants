# Login Systems

Many Django applications, including the one you may build, may benefit from having a robust login authentication system that allows users to create accounts and receive a personalized experience with the program. 

Thankfully, Django makes building this system very easy, with many of the required pieces needed already built into the existing Django architecture. In this guide, we’ll cover the most helpful pieces of the Django `auth` module and show how you can include it for your code. ]

---

## Django Authentication

The Django `auth` module handles much of the framework for login systems. You can import various submodules from it like so:

```python
from django.contrib.auth import ...
```

## Add Users

Users are the the base unit in the `auth` module. Each user has the following attributes:

- First & Last Name
- Email
- Username
- Password

You can create a user through the `create_user()` function, like so:

```python
from django.contrib.auth.models import User

# This creates AND adds user to database
new_user = User.objects.create_user("Bill", "bills_email@example.com", "password")

# Edit user information as desired
new_user.last_name = "last_name"

# Save changes
new_user.save()
```

## Authenticate Users

Once users are created, you can authenticate their information like so:

```python
from django.contrib.auth import authenticate

# returns a value if user exists, None otherwise 
authenticated = authenticate(username = "Username", password = "Password")

if authenticated is not None:
	#
	# code to run if user exists
	#
else:
	#
	# code to run if user is not authenticated
	# 
```

## Web Request Login

Once a login system is set up, it’s important to open it to your frontend at the necessary points on your webpage. You can do that like so in `views.py`:

```python
from django.contrib.auth import authenticate, login

def login_view(request):

	username = request.POST["Username"]
	password = request.POST["Password"]

	authenticated = authenticate(request, username = username, password = password)
	if authenticated is not None:
		login(username, password)
		# code to run for a logged-in user
	else:
		#
		# code to run for a not logged-in user
```

---

You’ve got a brief glimpse at the Django `auth` module, but there’s plenty more it can do:

- Change passwords for a given user
- Logout system and handling
- Superuser admin management

You can read about all that is possible with the `auth` module [here](https://docs.djangoproject.com/en/4.1/topics/auth/default/).