# Postman

> Makes APIs easy
> 

---

# Overview

[Postman API Platform | Sign Up for Free](https://www.postman.com/)

Postman is a free application that lets you test and debug API endpoints. It makes debugging your APIs a lot easier for cases where you need fine control of what gets sent. You can also use it to play around with a 3rd party API without having to write your own test code.

Note that Postman does a lot for you when sending a Request. You come into cases where Requests that work in Postman don’t seem to work in your app when you actually implement it. For cases like these, make sure that your implementation has all the request parameters properly setup. For example, you can directly send JSON data in Postman, whereas using `fetch` in JavaScript you need to set the `Content-Type` header to `application/json` and `JSON.stringify` the Request body data. 

Otherwise, it is definitely a tool to pickup if you see yourself working with a lot of APIs in the future.