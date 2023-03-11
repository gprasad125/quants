# HW: Development pt. 2

---

In this second section, we’ll go through the specific steps of connecting our current frontend to the example backend via an API. 

---

# 1. Setting up the example backend

### 1.1. Python requirements

The backend uses `Python 3`. Make sure you have version 3.6 or higher on your machine. `Pip` is also necessary to install all the package requirements. 

You can run

```bash
python3 --version
pip3 --version
```

To see the version installed currently on your machine. 

### 1.2. Clone the repository

In the location where you would like to store the backend code, clone the repository using git.

```bash
git clone https://github.com/gprasad125/django_walkthrough.git
```

You should now see a directory called `django_walkthrough`.

`cd` into it for the next steps

```bash
cd django_walkthrough
```

### 1.3. Create virtual environment

Next you will want to create a python virtual environment so that the dependencies are not installed globally. Refer to [documentation](https://packaging.python.org/en/latest/tutorials/installing-packages/#creating-virtual-environments) for more details.

```bash
# for Unix/macOS
python3 -m venv <DIR>
source <DIR>/bin/activate

# for Windows
py -m venv <DIR>
<DIR>\Scripts\activate
```

replace `<DIR>` with the name of what you want to name the environment. Something like `python_env` will do. 

### 1.4. Installing dependencies

Once your environment has been created and activated (refer to previous step), you can now install all the dependencies. 

```bash
pip3 install -r requirements.txt
```

### 1.5. Migrating Django

With all dependencies installed, you can now run the Django migrations to sync the database. For this example backend project, it uses a simple sqlite file as the database.

From `django_walkthrough`, first `cd` into the Django project directory

```bash
cd my_project
```

Once you’re in the same directory as the `manage.py` file, you can now run Django’s management tools.

```bash
python3 manage.py migrate
```

It should output something like this.

![Screenshot 2023-01-28 at 3.54.31 PM.png](HW%20Development%20pt%202%20ce94cc0df03a4f4f91a1f9033434c9e4/Screenshot_2023-01-28_at_3.54.31_PM.png)

### 1.6. Environment variables

Environment variables are just key-value variables that you set on your machine. This enables you to use secret values in your project without including them in your public git repository for everybody else to see.  

The example backend depends two environment variables:`secret_key` & `api_key`. The first is a secret that Django uses for encrypting things on the backend. The second is an api key to an OpenAI account to grant access to the summarizer. 

First, create a `.env` file. The project uses the `dotenv` library to automatically load environment variables from this file.

```bash
touch .env
```

Next, add the following to `.env`

```
secret_key="django-insecure-0^ecd1c0z617wah(1((kp*6otvj$kd!4-@kn58705$4xm$b6r8"
api_key=
```

You’ll recognize that the `api_key` variable is blank. For that, you’ll need to create an OpenAI account. 

First, signup at [https://beta.openai.com/signup](https://beta.openai.com/signup). If you already have account, login. 

Next, at the dashboard when you login, click your profile icon at the top right

![Screenshot 2023-01-28 at 4.19.36 PM.png](HW%20Development%20pt%202%20ce94cc0df03a4f4f91a1f9033434c9e4/Screenshot_2023-01-28_at_4.19.36_PM.png)

Select `view api keys` in the dropdown. Then click `create new secret key`

![Screenshot 2023-01-28 at 4.21.15 PM.png](HW%20Development%20pt%202%20ce94cc0df03a4f4f91a1f9033434c9e4/Screenshot_2023-01-28_at_4.21.15_PM.png)

It will show a popup with a string of text like `sk-8pDhvKS3dsdcMk8RUH3dT3blbkfJiMca3sVrZaIrHSacUUF2`. Copy that and save it somewhere since you will never be able to see it again after closing the popup. 

Finally, add that to `.env` for `api_key`.

```
secret_key="django-insecure-0^ecd1c0z617wah(1((kp*6otvj$kd!4-@kn58705$4xm$b6r8"
api_key="<your key here>"
```

### 1.7. Start the Django server

Now that you’ve installed dependencies, migrated the database, and setup the environment, you can now start the server

```bash
python3 manage.py runserver
```

If successful, you should see something like this.

![Screenshot 2023-01-28 at 3.56.12 PM.png](HW%20Development%20pt%202%20ce94cc0df03a4f4f91a1f9033434c9e4/Screenshot_2023-01-28_at_3.56.12_PM.png)

Now, if you go to [http://localhost:8000/summary/](http://localhost:8000/summary/), you should see this

![Screenshot 2023-01-28 at 4.35.53 PM.png](HW%20Development%20pt%202%20ce94cc0df03a4f4f91a1f9033434c9e4/Screenshot_2023-01-28_at_4.35.53_PM.png)

This means that everything has been setup correctly. 

To shut down the server, simply enter `ctrl + c` in the terminal where you ran `python3 manage.py runserver`. However, you’ll need the server up for the next steps. 

# 2. Adding the API to the frontend

Now that the backend server is up and running, we can now setup a page on the frontend to interact with it. 

### 2.1. Setup the `summarize` page

```bash
touch src/pages/summarize.tsx
```

Paste the following inside

```jsx
// summarize.tsx

function Summarize() {
    return (
        <h1 className="text-center text-xl font-bold text-slate-600 mt-20">
            Summarize
        </h1>
    );
}
export default Summarize;
```

Then update `navbar.tsx` and `App.tsx` with the new page

```jsx
// navbar.tsx

import { Link } from "wouter";

function Navbar() {
    return (
        <nav className="container mx-auto max-w-3xl text-blue-600 mt-10 px-5">
            <Link href="/" className="inline-block mr-5 hover:text-blue-400">
                Home
            </Link>
						{/* add "mr-5" class to /about link for spacing */}
            <Link href="/about" className="inline-block mr-5 hover:text-blue-400">
                About
            </Link>
						{/* add summarize page link */}
            <Link href="/summarize" className="inline-block hover:text-blue-400">
                Summarize
            </Link>
        </nav>
    );
}
export default Navbar;
```

```jsx
// App.tsx

import { Route, Switch } from 'wouter';
import About from './pages/about';
import Home from './pages/home';
import Navbar from './components/navbar';
import Summarize from './pages/summarize'; // import page
import './App.css';

function App () {
    return (
        <>
            <Navbar />
            <Switch>
                <Route path='/' component={Home} />
                <Route path='/about' component={About} />
								{/* Set page to route */}
                <Route path='/summarize' component={Summarize} />
            </Switch>
        </>
    );
}

export default App;
```

If you restart the vite dev server, you should see this now when you navigate to `Summarize`.

![Screenshot 2023-01-28 at 5.04.01 PM.png](HW%20Development%20pt%202%20ce94cc0df03a4f4f91a1f9033434c9e4/Screenshot_2023-01-28_at_5.04.01_PM.png)

### 2.2. Scaffold the component logic

First, we’ll setup some of the initial ingredients we’ll need to interact with the backend’s API. Currently, there is a `/summary/` endpoint that takes a request body attribute of `text` and runs it through one of OpenAI’s text processing models. 

So essentially, we `POST` text to the endpoint, and the endpoint will respond with text. For the purposes of this walkthrough, we can just have a text `input` where users can submit text and see results. 

Let’s start then:

```jsx
// summarize.tsx

import { useState } from "react";

function Summarize() {
    const [prompt, setPrompt] = useState('');
    const [result, setResult] = useState('...');

    const onSubmit = () => {
        setResult('You entered: ' + prompt);
    };

    return (
        <div className="container mx-auto max-w-3xl mt-20 px-5">
            <form onSubmit={e => e.preventDefault()} className="mb-10">
                <label htmlFor="prompt" className="block text-2xl font-bold mb-3">
                    Enter text to summarize
                </label>
                <input 
                    type="text" 
                    name="prompt" 
                    id="prompt" 
                    placeholder="..."
                    value={prompt}
                    className="w-full mb-5 rounded bg-slate-200 p-2"
                    onChange={e => setPrompt(e.target.value)}
                />
                <button 
                    className="px-5 py-3 rounded bg-slate-600 text-white block ml-auto"
                    onClick={onSubmit}
                >
                    Summarize!
                </button>
            </form>
            <h1 className="text-2xl mb-3 font-bold">
                Result
            </h1>
            <p className="p-2 bg-slate-200 rounded">
                {result}
            </p>
        </div>
    );
}
export default Summarize;
```

Here, we start by setting two states, `prompt` and `result`, with default empty values to track the user input and store what we expect to receive from the backend API. 

In the `return` template, we have a `form` with an `onSubmit` function that prevents the default form behavior, since we will be handling everything in the Javascript and do not want the browser to redirect or reload the page when the user submits. 

Inside the `form`, we have a controlled `input` that is set to `prompt` as its value and updates `prompt` whenever there is a change. 

Below the `input` is a `button` that calls the `onSubmit` function when clicked, which for now just simply echoes the `prompt` in the `result`. 

Finally, at the bottom is a results section that simply displays `result`. 

![Screenshot 2023-01-28 at 5.31.00 PM.png](HW%20Development%20pt%202%20ce94cc0df03a4f4f91a1f9033434c9e4/Screenshot_2023-01-28_at_5.31.00_PM.png)

### 2.3. Add in the API call

Now that all the logic is mostly there, we just need to insert the API calls to complete the connection. 

Above and outside the `Summarize` component, we’ll create a new function that uses Javascript’s `fetch` method to send a http request to the backend:

```jsx
import { useState } from "react";

const getSummary = (prompt) => {
    const url = 'https://localhost:8000' + '/summary/';
    const options = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json' // this part is important!
        },
        body: JSON.stringify( // must JSON encode request body
            {
                text: prompt
            }
        )
    };
    return fetch(url, options).then(res => res.json()); // returns a Promise
}

function Summarize() {
	// ...
```

Here, we basically define the parameters for the request. At the end, we return the fetch request, which is a Promise. We chain on `.then` to parse the response into JSON so that we can utilize the response data.

Then we can add it in to `onSubmit` with some promise handling

```jsx
// ...
const onSubmit = () => {
    getSummary(prompt).then(result => {
        setResult(result);
    }).catch(error => {
        setResult(error.message);
    });
};
// ...
```

Here, `getSummary` returns a Promise for the request as mentioned previously. We wait for it to complete and for the response JSON to be parsed with `.then`, before we grab the final result and set the local `result` state to it. We add a `.catch` to catch any errors that may occur and set `result` to the error message instead. 

### 2.4. Test

That’s it! Now we can test to see if it’s working. Enter in some text, press the button, and wait for a response. It may take a couple of seconds before you see the result, since the backend needs to wait for OpenAI to process the text. Hopefully everything goes as expected. 

![Screenshot 2023-01-28 at 6.06.40 PM.png](HW%20Development%20pt%202%20ce94cc0df03a4f4f91a1f9033434c9e4/Screenshot_2023-01-28_at_6.06.40_PM.png)

It’s not exactly a summarizer, but linking the frontend to the backend via API is the important part here!

Now you know how to communicate information between the two. 

# 3. Frontend environment variables

In the previous steps, you might have noticed already that the url used by `getSummary` is a static string to `localhost:8000`. This works when you’re developing locally on your machine, but when you deploy your frontend, you likely won’t be having the backend running on the same exact server. In fact, the backend will likely be hosted on its own domain/url, separate from the frontend. So, how would you change the url to properly match the context? On your machine, it needs to be `localhost:8000`. In production, it needs to be whatever url the backend is hosted at. 

To do this, we can use environment variables, and `Vite` has out-of-the-box support for environment variable files.

### 3.1. Create development environment file

In the root directory of the frontend, create  `.env.development`

```bash
touch .env.development
```

Note that the name is important here, so be sure not to misspell or change it!

Next, create `.env.production` 

```bash
touch .env.production
```

To add environment variables, simply do

```bash
# in .env.development
VITE_API_URL=http://localhost:8000

# in .env.production
VITE_API_URL=<some-url-where-backend-is-hosted>
```

where it’s `VITE_` followed by a name for the variable. 

### 3.2. Create settings file

In the `src` directory, now create `settings.ts` (or `.js` if you’re not using Typescript)

```bash
touch src/settings.ts
```

Inside, paste the following

```jsx
export const API_URL = import.meta.env.VITE_API_URL;
```

`Vite` will automatically use the correct `.env` file depending on the mode (development/production) and insert the environment variable value. 

Now go back to `summarize.tsx` and update `getSummary`

```jsx
import { useState } from "react";
import { API_URL } from "../settings"; // new import

const getSummary = (prompt) => {
    const url = API_URL + '/summary/'; // uses dynamic API_URL
    const options = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(
            {
                text: prompt
            }
        )
    };
    return fetch(url, options).then(res => res.json());
}
```

With this, `.env.development` will be used when you run the dev server while developing, and `.env.production` will be used when you build the app. 

Now you just need to remember to update `.env.production` with the correct url once the backend is deployed.