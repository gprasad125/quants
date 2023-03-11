# Validation

> “Expect the user to break things” - somebody 2022
> 

---

# Overview

When you’re handling data from unknown sources, you definitely need to verify that the data is in the format you expect it to be. Otherwise it may cause errors and break things you don’t want breaking. 

The most relevant areas of validation that you should know about are client-side validation and backend validation. 

# Client-Side Validation

Client-side validation is the validation that happens on the frontend.

When a user enters in their email, phone number, password, etc., you need to check or validate that it follows the format you expect. This helps with keeping data standardized (e.g. you don’t want phone numbers to vary between using or not using parenthesis) and helps prevent users from entering the wrong data. 

When retrieving data from an API, it would also be good to check that the data is in the format you expect. This may not be as necessary if you know exactly how the API works and are confident that it won’t send an unexpected response. 

# Backend Validation

Frontend or client-side validation is the first line of defense against bad data. However, since all frontend code is accessible and modifiable by the user, malicious users can easily bypass any restrictions put in place on the frontend. As a result, having an identical wall of defense on the backend is necessary to prevent this. 

It would also be good to implement measures to prevent injection attacks, such as [SQL Injection](https://www.w3schools.com/sql/sql_injection.asp), and XSS attacks. This usually takes the form of cleaning input with libraries specifically for this purpose.

# Validation Libraries

While you can certainly develop your own validation with long if-else chains, there are numerous validation libraries that you can use according to your needs. The general usage pattern is that you first define how you want the data to look like (using the library’s methods), then you can give that definition, formally called a schema or model, to the library’s validation checker and it will match data given to it to the schema. If there are any mismatches, it will output the offending violation. 

Below are some quick suggestions. Do recognize however that there are many other great libraries out there not mentioned. 

### Frontend

If you only need to validate simple data, then a library like [SuperStruct](https://docs.superstructjs.org/) is lightweight and straightforward to use. If you need more robust validation with nested objects and more, then [Joi](https://joi.dev/) is the common go-to. 

### Backend

If you are using Django, then Django has [built-in validation systems with their forms](https://docs.djangoproject.com/en/4.1/topics/forms/#working-with-forms). If you are using a backend framework that uses Javascript, then you can’t go wrong with using [Joi](https://joi.dev/).