# APIs

> The possibilities are endless
> 

---

# Intro

Hopefully you already have an idea of what an API is at this point. If not, feel free to checkout a brief description in 

[Frontend Lingo](Frontend%20Lingo%200a3ed29c3ab04445b694a6a1c0e7e6bf.md)

Essentially, its purpose is to provide a consistent system to interact with a service or program. With Twitter as a service for example, you might use the Twitter API to get a list of the latest tweets. APIs sort of form a language that different services and programs can use to communicate with each other, enabling some amazing possibilities. 

For example, [you can use Reddit’s API to get the latest posts from `r/wallstreetbets`, train a sentiment analysis model to evaluate stock picks, use a stock trading platform’s API to automatically buy and sell shares, and pit it against a similar trading bot based on the spatial location of a goldfish](https://www.youtube.com/watch?v=USKD3vPD6ZA&ab_channel=MichaelReeves). 

Or maybe something as simple as [updating a youtube video’s title to reflect the up-to-date view count, making it seem like you’re a seer](https://www.youtube.com/watch?v=BxV14h0kFs0&ab_channel=TomScott). 

The rest of this doc will mainly focus on REST APIs, one of the many types of APIs, because they are the most used and typically the only one you really need. However, the concepts discussed should be applicable for other types of APIs as well to a certain extent. 

# The Basics

At the bare minimum, an API has an `endpoint` that accepts `requests`, does some magic, and returns a `response`. 

### Endpoints

`Endpoints` or `routes` are selected `urls` intended for a certain purpose. For example, if I have a domain of `bread.com` for my bakery business, I might select `bread.com/buy` to be the `endpoint` for customers to purchase bread. This is completely arbitrary, and I could even select `bread.com/come/by/this/very-absolutely-delicious/bread-ready-hotfromtheoven` if I really wanted to. 

However, it’s good practice to make them consistent and reasonable, and REST APIs have a general standard to picking your `routes` that we’ll be looking at later. 

`Endpoints` also have special verbs, the most relevant of which are `POST`, `GET`, `PATCH`, `PUT`, `DELETE`. Each verb carries a certain semantic meaning or intent, and each `endpoint` accepts and handles a certain selection of these verbs (usually it’s just `GET` and `POST`).

| Verb | Use | Example |
| --- | --- | --- |
| GET | retrieving information. | Whenever you search something on Google, you are making a GET to one of Google’s endpoints for making searches. |
| POST | creating information or sending information to the API | Whenever you login or signup to Google, you are making a POST with your username and password.  |
| PATCH / PUT | updating existing information | Whenever you change your Google username, you are making a PATCH with the new username you want to change to.
The difference between PUT and PATCH, is that PUT is when you are replacing all of the information with a new record, and PATCH is when you are only modifying a piece of it. Either works honestly for updating information, and you shouldn’t sweat too much about this detail.  |
| DELETE | deleting information | When you delete your Google account, you are making a DELETE.  |

Using the bakery business as an example, for the `bread.com/buy` endpoint I might accept `GET` and `POST`. `GET` returns a list of available bread in the store, and `POST` creates a new order for a certain type of bread. 

Note that these verbs are mostly arbitrary in use, and some verbs may be used for things not exactly aligned with their semantic meaning. For example, `POST` is often used for updating information as well, and `GET` can also pass information to the API as well through certain means (e.g. filtering a list with custom filters). You can have a `DELETE` endpoint to create a new user.

Of course, it is best to not make things confusing. 

### Requests

`Requests` are a structured message sent to an API `endpoint`. It has three main parts: the `header`, the `body`, and the `method`. 

The `header` is similar to the `head` of an HTML document. It contains meta-data about the `request`, such as the browser used to send the `request`, which `url` the user came from, and more (this is one of the sources for sneaky data collection). They are like a Javascript Object or Python dictionary, where each `header` has a corresponding `key` and `value`. For example, setting `Content-Type: application/json` specifies that the information in the `body` is in JSON encoding. A lot of people also use “auth headers” to pass authentication data to the backend with headers. 

The `method` is the verb (`GET`, `POST`, etc.) that you want to use for the `endpoint`. 

The `body` is where you can include any data for the API `endpoint` to receive. An `endpoint` that signs up a new user for example might require you to have the username and password stored inside the `body`. For most APIs, it is usually stored as a JSON string. 

### Responses

`Responses` are a structured message sent back by the API in response to a `request`. It also has three main parts: the `header`, the `body`, and the `status code`. 

The response `header` is similar to the request `header`. However it does have some additional functionality. When a website gives your browser a cookie for example, it’s through the `set-cookie` response `header`. 

The `body` contains any information or content returned by the `endpoint`. When you navigate to a website in your browser for example, it is sending a `GET` request to the website’s url address, and the website’s backend returns a HTML document in the `response` that your browser subsequently renders and turns into the webpage you view. Usually with APIs however, it’s JSON encoded data. 

The `status code` is a 3-digit number that communicates the status of the `request`. Numbers that start with 2 mean that things were successful and went as expected. Numbers that start with 4 means that something about the `request` was unsatisfactory (i.e. bad data, not logged in, etc.). Numbers that start with 5 usually mean that something went wrong on the backend handling the `request`. The basic ones you should know are listed below.

| Status Code | Meaning |
| --- | --- |
| 200 | OK, success. |
| 400 | Bad request. Usually invalid data was provided (e.g. a nonexistent email, etc.) |
| 401 | Unauthorized. Need to be logged in or have permissions to access. |
| 404 | Not found. Resource requested does not exist or could not be found. |
| 500 | Internal server error. Server errored while handling the request. |

As with other things discussed before, there is no law requiring you to use one over the other, but it’s best to follow general convention. 

# Dynamic Endpoints

So far the routes and endpoints given as examples are static, meaning that they are always the exact same. However, this may not be what we want. 

Take the scenario of updating a user’s username. The client, or the frontend, needs to tell the backend through an API that a specific user wants to change their name from A to B. But let’s say that there are hundreds of users in the database, each with their own unique ID. How would the backend know which user needs to have their name changed? 

One possible solution is to include the user’s ID in the request `body`. That way the backend knows which user to find and can change the name accordingly. 

What if you could convey that information in the endpoint instead? So instead of some endpoint like `/user/update`, you could have `/user/<some_id>/update`. With this, assuming the user has an ID of 1, the client would be able to `POST` to `/user/1/update`, and the backend will be able to parse the ID from the url, obviating the need to include it in the request body. 

This is in fact what most APIs do, and most if not all backend server frameworks support dynamic routes. Usually, a parameter in a route is represented by `:` followed by the parameter name. So the previous example could be formally written as `/user/:userId/update`. 

Again, there is nothing stopping you from using the first solution of putting the ID in the body, and it is perfectly fine to do so. However, putting it in the route url is just the agreed-upon organization of information by the community. 

# RESTful Routing

As foreshadowed previously, there is a general standard to specifying your endpoints. Below is an example with blogs, but you can definitely substitute it with whatever objects your API uses. 

![Untitled](APIs%20158298affaed40d384a0ccaceb4015dd/Untitled.png)

Here, you can see the verbs and dynamic route parameters being used to distinguish between different intentions and keep the url straightforward and simple. 

This convention should cover most of the functionality needed by your API. If not, you can build on top of it for any need you see fit. If I wanted to have an endpoint to download a blog for example, I could add a new `/blogs/:id/download` `POST` endpoint. 

As long as no endpoints share the same url and verb, and they make reasonable sense, you are fine. 

Your app might not even deal with any RESTful routing. A machine learning project may only need a `/` `GET` endpoint for the home page (commonly called the root endpoint) and a `/inference` `POST` endpoint for running a machine learning model on data sent via the request body. 

# Query Parameters

In addition to dynamic route parameters, you can also pass information via the url with query parameters (also called query strings). This is particularly useful for filtering lists, where you cannot pass information via a `body` for `GET`, but still want to give the user the ability to set custom filters. You probably won’t be needing to use it often, but it’s good to know just in case.

The general structure is something like this

```
https://some-domain.com/route?query1=some-query&query2=another-query
```

The `?` of the url denotes the point at which the query string starts, and the `&` separates query parameters from each other. Here we have a parameter `query1` with a value of `some-query` and a `query2` with a value of `another-query`. 

Like dynamic route parameters, the backend server will need to parse the url to extract the parameters and their values. With `Django` for example, they are typically made available in the `request.GET` object.

You’ll also notice that query parameters are only strings. You will need to store numbers and other datatypes in the query as strings, and you can even store complex Javascript objects after turning them into JSON strings. 

Do note that since it is part of the url, you will need to encode special characters (like `/` and non-english characters) to prevent them from messing up the url. With Javascript, this can easily be done with the `encodeURIComponent` method. Usually, backend frameworks like `Django` automatically decode encoded query parameters, but it’s good to double check just in case. 

# Request Body Encoding Types

This is just a small side note for those that might need it.

When you’re sending data with request bodies, you have several options for what format to send the data as. 

`JSON` is the most straightforward. All data is sent as a string in Javascript Object syntax. It’s very flexible for most needs and is the most used. 

`multipart/form-data` is when you need to send files such as images. Since JSON sends string data, it’s better to use a different encoding for files instead of hacking together a JSON file encoding system. 

You can refer to online guides on how to use this encoding with Javascript fetch, such as [this stackoverflow post.](https://stackoverflow.com/questions/35192841/how-do-i-post-with-multipart-form-data-using-fetch) The backend framework should also have its own syntax for handling it.