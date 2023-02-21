# Deployment (Railway)

You’ve written a great Django app, it runs smoothly and serves as a solid backend to your overall program. But, now what? How do we get this application deployed? Look no further than the ease provided by [Railway](https://railway.app)! 

---

**************************************************************************************************************************************Note: As you deploy and edit settings on Railway, your deployment may fail before you complete the tutorial! Do not worry — your deployment will restart once you make changes each time, so finish this tutorial before checking the availability of your deployment!************************************************************************************************************************************** 

---

## 🐳 Step 1: Dockerizing the Backend

**Docker** is a tool that makes it easier to share code and run programs across different computers. 

- What is Docker?
    
    By using Docker, you can package up your code, its environment, and all the dependencies needed to run the code in one package. This package can then be shared with others, who can easily run the code without having to worry about setting up their own environment or having the same versions of the dependencies that you have. 
    

We will first need to create a **Dockerfile** in the root directory of our backend. Open a new file called `Dockerfile` with no extension in the same level as `my_project` and include the following lines:

```docker
FROM python:3.8.13-bullseye

ARG secret_key
ARG api_key

WORKDIR /my_project

COPY . .

RUN pip install --upgrade pip 
RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

- **********************************Reading the Dockerfile**********************************
    
    The `Dockerfile` is a collection of step-by-step instructions for Railway to read in order to run our particular project. Let’s understand that piece-by-piece:
    
    ```docker
    FROM python:3.8.13-bullseye
    ```
    
    This is where we tell Docker which base image  of Python we are using. In this particular case, Python 3.9, although you can change this based on your project requirements. 
    
    ```docker
    ARG secret_key
    ARG api_key
    ```
    
    This is where we tell Docker what variables to use during the “build” phase. Essentially, we are telling it to expect two variables, `secret_key` and `api_key`, that will get their values from an `.env` file.  
    
    ```docker
    WORKDIR /my_project
    COPY . .
    ```
    
    We then tell Docker that all further commands will run relative to our first my_project directory, so we can get access to `manage.py`, `requirements.txt`, and other necessary files. We then copy all the contents of the subdirectory. 
    
    - Why do we use the `COPY` command?
        
        This is necessary because containers run isolated from the host file system, so any files or dependencies needed by the application must be included within the container. The **`COPY`**
         command allows you to include your application code, configuration files, scripts, and other required files into the container, so that the application can run in an isolated environment with everything it needs.
        
    
    ```docker
    RUN pip install --upgrade pip 
    RUN pip install -r requirements.txt
    ```
    
    Once we have access to all the files, we can run two commands:
    
    - Upgrade the base `pip` package that we have if possible
    - Install all Python dependencies from our `requirements` file
    
    ```docker
    EXPOSE 8000
    CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
    ```
    
    We then expose the 8000 port, and then run our Django server. 
    

### Additional Resources:

**[🐋 Why Docker?](https://www.docker.com/101-tutorial/)** 

## 🌲 Step 2: Project Requirements

We’ll also need to install some libraries / edit some files to prep for deployment on Railway. 

Firstly, we need the packages to help us with connecting to PostgreSQL, a cloud database option to replace SQLite, the database we’ve been using for local development in Django. 

```bash
pip install psycopg2 
```

- Failed to install?
    
    First, remove any other dependencies by running
    
    ```
    pip uninstall psycopg2 psycopg2-binary
    ```
    
    Then run
    
    ```
    pip install psycopg2-binary
    ```
    

The `pyscopg2` package is Python adapter for using PostgreSQL databases. 

******************************************************************************REMEMBER TO ADD IT TO YOUR `requirements.txt` FILE !!** 

Next, navigate to the `.env` file and include the following line. This is a variable that will only be included in our local `.env` file, and not in the Railway-specific variables (i.e., if we see `DEBUG = "True"` in the file, that means we are running on localhost, not deployed). 

```
DEBUG="True"
```

We also need to tell Django two things:

1. the `DEBUG` variable should be equivalent to `True` if it is present in the environment variables, otherwise False. 
2. This app can run on other hosts beyond local deployment 

To accomplish this, navigate over to `settings.py` and add the following information:

```python
DEBUG = True if os.environ.get("DEBUG") else False
ALLOWED_HOSTS = ["*"]
```

- Why do we need `DEBUG = “True”`
    
    When we are deployed, we’ll be using a PostgreSQL database to store our data. However, we don’t want to clutter that database with test data we might use when we are developing locally. Therefore, we need a way to tell Django whether or not we are running locally, and the presence of a DEBUG variable serves to do just that. By ******NOT****** including this later on in Step 3, DEBUG will be False, and therefore NOT running locally! 
    

### Additional Resources

[**⚡Why PostgreSQL?**](https://www.databasestar.com/why-use-postgresql/)

- Keep in Mind
    
    This is a SQL-based look into why PostgreSQL is a great database management, so if you do not have prior SQL experience, you may not understand all of the article. However, it is a good overall discussion as to why Railway would offer PostgreSQL databases.
    

## 👨‍💻 Step 3: Set Up Railway

Create an account @ [Railway](https://railway.app), and navigate to the [Dashboard](http://railway.app/dashboard). You should see something like below, although you won’t have any Projects yet up. 

![Screenshot 2023-01-22 at 12.21.05 PM.png](Deployment%20(Railway)%20a0b00f8cc92a4ff489fcc744bd5c9667/Screenshot_2023-01-22_at_12.21.05_PM.png)

Click the “New Project” button, and select the option to deploy from a GitHub repository. Add your repository that contains the backend code like so: 

![Screenshot 2023-01-29 at 1.00.20 PM.png](Deployment%20(Railway)%20a0b00f8cc92a4ff489fcc744bd5c9667/Screenshot_2023-01-29_at_1.00.20_PM.png)

Then, select “Add Variables” to add the necessary tokens / keys for your app, and you should come across the following screen. 

- Following the Django Project Walkthrough?
    
    If you were following the Django project walkthrough crash course, this would be:
    
    - Django Secret Key
    - OpenAI GPT-3 API Key
    

![Screenshot 2023-01-29 at 1.03.38 PM.png](Deployment%20(Railway)%20a0b00f8cc92a4ff489fcc744bd5c9667/Screenshot_2023-01-29_at_1.03.38_PM.png)

Click **Raw Editor**, and paste in the same information from the `.env` file in your local repository (Remember, our `.gitignore` ignores our `.env` file so we need to manually add them to Railway!). 

********************************************DO NOT INCLUDE `DEBUG=”True”` !! We want Django to know when it’s being deployed.**

![Screenshot 2023-01-29 at 1.13.56 PM.png](Deployment%20(Railway)%20a0b00f8cc92a4ff489fcc744bd5c9667/Screenshot_2023-01-29_at_1.13.56_PM.png)

Select Update Variables. Your build will start deploying, but do not pay this much attention — there are still other things we need to adjust for before the deployment will successfully work. 

## 🎾 Step 4: Advanced Railway Settings

Click Settings, and edit the Root Directory to be the folder containing your application, `Dockerfile`, `requirements.txt` file, etc. 

![Screenshot 2023-02-01 at 10.31.10 AM.png](Deployment%20(Railway)%20a0b00f8cc92a4ff489fcc744bd5c9667/Screenshot_2023-02-01_at_10.31.10_AM.png)

Next, we have to expose our application to the internet, so scroll up and select “Generate a Domain” to create a custom Railway-based URL to your Django application! (Remember, we set `ALLOWED_HOSTS` to be any value in Step 1!) 

![Screenshot 2023-02-01 at 10.50.44 AM.png](Deployment%20(Railway)%20a0b00f8cc92a4ff489fcc744bd5c9667/Screenshot_2023-02-01_at_10.50.44_AM.png)

Now step out of the Settings page, and select “New” —> “Add Database” and select PostgreSQL from the following options: 

![Screenshot 2023-02-01 at 2.10.58 PM.png](Deployment%20(Railway)%20a0b00f8cc92a4ff489fcc744bd5c9667/Screenshot_2023-02-01_at_2.10.58_PM.png)

Click on the spun-up database, click “Connect”, copy the PSQL URL in the first bar, which will automatically connect the PostgreSQL database to our Django app! 

![Screenshot 2023-02-02 at 1.45.25 PM.png](Deployment%20(Railway)%20a0b00f8cc92a4ff489fcc744bd5c9667/Screenshot_2023-02-02_at_1.45.25_PM.png)

However, now we’ll have to reflect these changes for our Django app as well. Click on the “Variables” tab in the PostgreSQL database and copy each variable over to the local `.env` file in your project directory. 

```
secret_key=...
openai_api=...
PGHOST=...
PGPASSWORD=...
PGPORT=...
PGUSER=...
```

Then, navigate to `settings.py` and modify the DATABASES information to look like the following code. We use local SQLite3 if developing locally (`DEBUG = True`) and PostgreSQL in production (`DEBUG = False`)

```python
if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ.get('PGDATABASE'),
            'USER': os.environ.get('PGUSER'),
            'PASSWORD': os.environ.get('PGPASSWORD'),
            'HOST': os.environ.get('PGHOST'),
            'PORT': os.environ.get('PGPORT'),
        }
    }
```

**************************************************************************MAKE SURE TO MIGRATE YOUR CHANGES!!************************************************************************** Run the following line to migrate your database modifications to PostgreSQL:

```json
python manage.py migrate
```

Verify that these changes are reflected by clicking on your new database and seeing your information automatically added like so: 

![Screenshot 2023-02-04 at 1.08.39 PM.png](Deployment%20(Railway)%20a0b00f8cc92a4ff489fcc744bd5c9667/Screenshot_2023-02-04_at_1.08.39_PM.png)

Commit and push all changes to your GitHub repository, and jump back to Railway, and let’s test our app!

## 👊 Step 5: Using the App

When you click on your deployment link after the GitHub push redeploys, you’ll likely come across the following screen. Why do you think this is? How does URL pathing work in Django? 

![Screenshot 2023-02-04 at 12.38.46 PM.png](Deployment%20(Railway)%20a0b00f8cc92a4ff489fcc744bd5c9667/Screenshot_2023-02-04_at_12.38.46_PM.png)

Next, navigate to the link + “/summary” and you should see the same Summary API page like so: 

![Screenshot 2023-02-04 at 12.41.10 PM.png](Deployment%20(Railway)%20a0b00f8cc92a4ff489fcc744bd5c9667/Screenshot_2023-02-04_at_12.41.10_PM.png)

Paste in some JSON Formatted text like we had done locally, and click POST. Wait for a brief time, and your data should return summarized! 

```json
{
"text": "to be summarized" 
}
```

Finally, navigate to your PostgreSQL database, select the table you’re manipulating, and you should see everything that you’ve added! 🥳

![Screenshot 2023-02-04 at 1.16.01 PM.png](Deployment%20(Railway)%20a0b00f8cc92a4ff489fcc744bd5c9667/Screenshot_2023-02-04_at_1.16.01_PM.png)

Woohoo! You’ve now deployed your application with a PostgreSQL database to a publicly-accessible URL that anybody can use 🔥 Continue exploring with Railway’s various options and see how far you can take your app! Happy coding 😁