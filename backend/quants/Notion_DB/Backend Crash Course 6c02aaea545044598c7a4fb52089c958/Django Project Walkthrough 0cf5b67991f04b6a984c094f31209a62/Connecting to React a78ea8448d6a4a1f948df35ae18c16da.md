# Connecting to React

By now, your team has written up a snazzy React frontend, a slick Django backend, and yet we can’t connect the two! This guide will walk you through the necessary setup so that your React app can communicate properly with your Django web app. 

---

## 👹 Step 1: Installation

We’ll need to install the Django Cross Origin Resource Sharing (CORS) package, which allows apps like frontends to communicate with our Django API. 

```bash
pip install django-cors-headers
```

### Additional Resources

[**💭 Cross Origin Resource Sharing**](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)

## 🔧 Step 2: Settings Modification

Navigate over to `settings.py` , include the CORS info as an installed app, and add the middleware along with our boilerplate Django middleware, like so:

```python
INSTALLED APPS = [
	...,
	...,
	"corsheaders"
]

MIDDLEWARE = [
  "corsheaders.middleware.CorsMiddleware",
	...,
	...,
]
```

Next, include the allowed origins for other applications by including the following two lines in your `settings.py` file:

```python
CORS_ORIGIN_ALLOW_ALL = False

CORS_ORIGIN_WHITELIST = [
    "http://localhost:3000"
]
```

This tells Django all allowed sources of web requests, which currently, will be the server that runs our React frontend. When you deploy onto a production endpoint, remember to add that URL here as well! 

### Additional Resources

[The Backend Dictionary](../The%20Backend%20Dictionary%20c1a2ec05ac36439ea64f2905987c9b46.md)

[**📓 What is Middleware?**](https://docs.djangoproject.com/en/4.1/topics/http/middleware/) 

## 🐈‍⬛ Step 3: Get the Frontend

You’ve set up your backend to handle connecting, but what about the frontend? We’ll need to make some changes there to fit our situation. Firstly, clone the frontend repository by running the following command **************outside************** our Django project directory:

```bash
git clone https://github.com/organization-x/frontend-crashcourse.git
```

This frontend is written in React, the most popular JavaScript library for building user interfaces. It was developed and is maintained by Facebook, and is used for creating reusable UI components for web applications.

In order to use React code, we’ll need to first install Node.js and npm (Node Package Manager) — two tools that form the base of React code and libraries. We can install Node [here](https://nodejs.org/en/), and npm comes installed with it. 

Then, navigate into the newly made `frontend-crashcourse/app` that was cloned, and run 

```bash
npm run dev
```

This will launch the local server on [localhost:3000](http://localhost:3000), and you should see something like below:

**********Home Page**********

![Screenshot 2023-02-01 at 8.06.05 PM.png](Connecting%20to%20React%20a78ea8448d6a4a1f948df35ae18c16da/Screenshot_2023-02-01_at_8.06.05_PM.png)

************************Summary Page************************

![Screenshot 2023-02-01 at 8.06.48 PM.png](Connecting%20to%20React%20a78ea8448d6a4a1f948df35ae18c16da/Screenshot_2023-02-01_at_8.06.48_PM.png)

### Additional Resources

[Untitled](https://www.notion.so/4190b289614648df9c32ba4a1d91fbc0)  

## 🚌 Step 5: Testing the Full Production

Launch your Django server.

- Not using port 8000?
    
    The frontend code is currently specified as sending data to port 8000, so we’ll need to edit it if you are launching your Django server on a different port.
    
    Inside `frontend-crashcourse/app`, navigate to `summarize.tsx` and modify the following lines:
    
    ```bash
    import { useState } from "react";
    
    const getSummary = (prompt) => {
        const url = 'https://localhost:PORT NUMBER HERE' + '/summary/';
        const options = {
            method: 'POST',
    				...
    				...,
    ```
    
    Replace `PORT NUMBER HERE` with your chosen port and save. Then, proceed onwards! 
    

Switch over to your React server, and paste some text into the blank bar on top. Then, click Summarize! and give the page a few seconds to load the data. Then, you’ll see the outputted text displayed in the result bar 🔥

![Screenshot 2023-02-01 at 8.21.57 PM.png](Connecting%20to%20React%20a78ea8448d6a4a1f948df35ae18c16da/Screenshot_2023-02-01_at_8.21.57_PM.png)

## 🤠 Closing Thoughts

Woohoo !! 🥳 You’ve now connected your backend and frontend. However, there’s a lot of code on the frontend that supports this connection that you may not about. You can read more about here: 

[HW: Development pt. 2](https://www.notion.so/HW-Development-pt-2-ce94cc0df03a4f4f91a1f9033434c9e4)