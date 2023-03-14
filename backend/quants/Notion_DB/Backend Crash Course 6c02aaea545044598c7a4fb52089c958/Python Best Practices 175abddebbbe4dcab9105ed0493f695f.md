# Python Best Practices

Python is one of the most-used programming languages in the world, and with that, comes a variety of use-cases. Ranging from building machine learning models to launching web applications, developers use Python to solve all kinds of problems. Nonetheless, there are a few industry-standard practices that keeps Python code **readable and clean**. Here’s a few helpful tips and tricks.

---

## ✋ Read!

While there are a wide-variety of beliefs and practices on writing good Python code, it’s important that no matter what you decide, ******************************be consistent!****************************** Don’t suddenly swap variable naming styles or quotation uses, because that’ll make your code harder to read for someone else. Stick with your choices !! 

---

## 💫 Virtual Environments

A virtual environment is an **isolated** Python environment on your local machine that keeps a separate installation of Python and libraries from other environments. This keeps project dependencies away from each other to avoid version issues. 

For example, imagine you have a project that requires NumPy version 1.24.0, while another project needs 1.21.0. You can use a virtual environment in each project that has its own specific NumPy installation. 

You can set up a virtual environment by running the following command inside your project directory via a Terminal window. 

```python
python3 -m venv env_name
```

Once the environment is created, launch it by running the following command:

**************[MacOS / Linux]**************

```python
source env_name/bin/activate
```

**[Windows]**

```python
env_name/Scripts/activate.bat
```

You should see some marker that the environment is running. Typically, the next line in your command line tool should start with the environment name in parentheses like so:

```python
(env_name) gokul ~ %: .... 
```

You can simply enter `deactivate` in your command line tool to exit the virtual environment! 

- **************Virtual Environments & GitHub**************
    
    Do **NOT** push your virtual environment to GitHub! Make sure to add the folder name to your `.gitignore` file like so: 
    
    ```python
    # ignore the entire virtual env directory
    env_name/
    ```
    
    Most premade `.gitignore` files will include common environment names like `env`, `venv`, etc. so consider using these!
    

## 📝 Dependency Requirements

If you would like to send information about your dependencies used (including name & version), run the following command to create a requirements file:

```python
pip freeze > requirements.txt
```

This is push-able to Git, so the next person to use your code can simply run the following command to install all the packages needed for your project! 

```python
pip install -r requirements.txt 
```

Now we can see the value of virtual environments, since someone else can just install the absolutely necessary packages, and not every Python library you may have installed on your local machine! 

# ⌨️ Coding Practices

## PEP8

`pep8` is the ultimate style guide for Python. It is a collection of tips, suggestions, and rules for writing reusable and shareable code, and has been universally adopted by Python developers worldwide. We’ll cover some of the most important `pep8` standards here, but you can read about all that it discusses [here](https://pep8.org/#introduction). 

## Naming

### Variables

Avoid using long variable names, and make sure each variable name is specific to the value that it contains, and use _ to break up longer names. 

Use entirely-capitalized variable names for constants. 

```python
# good example
actor_names = [ ... ]

# bad example: too long 
list_of_names_of_actors = [ ... ]

# good example
student_count = 54

# bad example: too vague to know what it means
x = 54

# good example
GROUPS = 10
```

### Classes

Classes should follow camelCase in naming, like so:

```python
class exampleClass():

	...
	...
```

## Functions

Documentation is an absolute necessity for good code. If you create a User Defined Function, you should include a brief explanation of what that function does, what to expect from it, and any other critical information that the next user might need. Documentation is written between triple double-quotes right after the function is defined, like so:

```python
def example_function(variable_1, variable_2):
	"""
	Here is where I can write some documentation. 
	This function takes two variables and returns the sum. 
	"""
	return variable_1 + variable_2 
```

Functions are also critical to one of the biggest ideas in good programming: 

***Don’t Repeat Yourself !!*** 

Use classes, functions, and other modular code to **avoid** repetitive programming. 

## File Handling

Many of your projects will require manipulation of data from files. Avoid complications with opening / closing these files by always using Python’s `with` function, like so:

```python
with open('file.txt', 'r') as file:
	...
	...
```

Because we are using `with`, if there are any issues in the code, the file will still close, preventing data damage and/or loss. 

## Handling Errors

Python allows for a variety of error-handling, and it’s good practice to use these:

### **Try / Except Block**

Try / Except is the most common way to handle specific error types, because they allow the user to run certain code in the case of success AND in the case of failure.

```python
try:
	...
	# code to run in case of success 
	...
except Exception as e:
	...
	# code to run in case of failure
	...
```

Try / Except gives you the chance to catch error types you know can happen (entering a float instead of an String, etc.) and handle them without completely killing the program. Use Try / Except blocks for really critical portions of your code. 

You can even include Else / Finally blocks for further scenarios like so:

```python
try:
	...
	# code to run in case of success 
	...
except Exception as e:
	...
	# code to run in case of failure
	...
else:
	...
	# further code to run w/o error
	...
finally:
	...
	# code to run at the very end regardless of errors
	...
```

### **************Asserts**************

Python’s `assert` functionality allows you to test for scenarios where you know something must be true. For example, let’s say you had a function that could only accept positive values, you can write it with asserts like so:

```python
def function_with_positive_arguments(arg_1, arg_2):
	"""
	This is a function that only takes in two positive values and returns the sum
	"""

	assert arg_1 > 0
	assert arg_2 > 0 

	return arg_1 + arg_2 
```

The two `assert` statements will verify that the two statements are true, and if not, will throw an AssertionError back for you to handle. 

# 📖 The Zen of Python

Open your command line tool, enter “python”, and then run the following command:

```python
import this
```

This generates the following snippet: 

![Screenshot 2023-01-30 at 9.34.43 PM.png](Python%20Best%20Practices%20175abddebbbe4dcab9105ed0493f695f/Screenshot_2023-01-30_at_9.34.43_PM.png)

These are a few guiding principles of writing good Python code. While they are all high-level, try and follow these to make readable and reusable code! 🔥