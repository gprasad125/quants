# MVC, Decoupling, & More

> Splitting concerns into bite-sized chunks
> 

---

# The Old Way

In the past, the frontend, backend, and data for common applications were typically all interconnected together into what is usually referred to as a monolith. 

For blog websites, that could simply be a php server that sends HTML files. The frontend (HTML) and the backend (the php server) code tightly depended on each other. 

# The MVC model

Overtime, a common pattern for applications called the Model View Controller model was developed. It split an application into three separated concerns:

| Model | Specifies how the data should look and interact. Usually database models or schemas. |
| --- | --- |
| View | The interface for the user; what the user sees. Usually HTML, JS, CSS, etc. assets |
| Controller | The business logic or brains of the app. |

![Screenshot 2023-02-05 at 2.21.12 PM.png](MVC,%20Decoupling,%20&%20More%209066c9e64d244d40bd5ace0420e71eb0/Screenshot_2023-02-05_at_2.21.12_PM.png)

Examples of server frameworks that use this model are ExpressJS and Django. 

|  | Express | Django |
| --- | --- | --- |
| Model | ORM schema files. E.g. Mongoose | model.py files |
| View | HTML templates in the views directory | templates directory |
| Controller | Route definitions | Route definitions in views.py |

If you have experience using either of the above or any similar framework, you probably have seen how a single framework orchestrates all three layers for the frontend, backend, and data. 

While all the code is nicely wrapped together in one codebase, this also has many consequences as well. Mainly, you cannot change one part of the application without affecting the other parts. If you wanted to make changes to the frontend for example, you would need to redeploy the backend as well regardless of any changes to the backend. If you wanted to change the backend entirely, maybe to a completely new language, then you would likely need to modify the frontend files to match as well. This made it difficult for large teams to work together without stepping on each other’s feet. 

# Decoupling

With the problems mentioned above, applications have begun to divide themselves into isolated parts. The most common of which is a decoupled frontend. Now, instead of having the frontend merged with the backend, the frontend is separately hosted on another server. If it needs to communicate anything, there is usually an API setup on the backend that the frontend can interact with.  

![Screenshot 2023-02-05 at 2.28.16 PM.png](MVC,%20Decoupling,%20&%20More%209066c9e64d244d40bd5ace0420e71eb0/Screenshot_2023-02-05_at_2.28.16_PM.png)

Since the frontend and backend only rely on an API to interact with each other, changing one will not affect anything about the other as long as the API is still the same. You could switch the backend to from Python to Rust and the frontend will need zero changes as long as the backend still implements the API correctly. 

This is the approach that the example project uses for the frontend project walkthrough.

Although decoupling has some drawbacks, such as requiring an additional server, having to communicate via API, working cross-origin, and more, this separation is much more maintainable for complex applications by large teams. 

With the diagram above, you might have realized that you could take this even further, such as splitting the backend into a logic server, to purely handle business logic, and a data server, to purely handle data management. This will likely be unnecessary in most cases, and you will have to personally evaluate the benefits and drawbacks if you ever come up with situations like these.  

At the end of the day, you are trading manageability of the application for code maintainability, since the structure becomes more complex overall but easier to individually maintain.

# One Step Further: Micro-services

> [https://www.youtube.com/watch?v=lL_j7ilk7rc&ab_channel=5MinutesorLess](https://www.youtube.com/watch?v=lL_j7ilk7rc&ab_channel=5MinutesorLess)
> 

For extra-large applications however, it might become reasonable to not only decouple the layers but also the concerns. This further divides the code into isolated chunks that could be maintained by a team without affecting other teams. These micro-services then together makeup the features of the app while remaining individually understandable and maintainable. 

There are drawbacks like before however; if one node fails, all other nodes that depend on it could fail as well. 

![Screenshot 2023-02-05 at 2.41.27 PM.png](MVC,%20Decoupling,%20&%20More%209066c9e64d244d40bd5ace0420e71eb0/Screenshot_2023-02-05_at_2.41.27_PM.png)