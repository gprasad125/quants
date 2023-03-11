# UI Frameworks (& Libraries)

> The thing web developers love yet hate. Yeesh.
> 

---

## Intro

When you think frontend, you’ve probably heard of JS frameworks like React, Svelte, Angular, etc. Well what exactly are those? If you wanted to build an interactive site like Discord, Twitter, Twitch, etc., using normal JavaScript from scratch would not be the most productive way to go about it. 

Instead, developers have designed frameworks built on JavaScript that aid you in developing a dynamic app. These frameworks come with tools and design patterns that help you build on top of existing methods so you don’t have to wrangle with basic syntax, file structure, DOM APIs, etc. 

## The Component-Based Model

Most if not all of the frameworks that you will be working with use a **component philosophy**, meaning that they organize a web page into reusable building blocks called `components`. You can think of them as individual lego pieces for the page each with their own logic. This helps keep code **DRY** (don’t repeat yourself) and allows you to create many elements each with their own logic and states with just a few lines of code, letting you easily reuse code and logic in multiple areas of a website/app while keep everything simple and organized.

## State

Each framework has its own way of managing data, which is referred to as the `state`. This could be any information the app needs to store, like user information, authentication tokens, API results, etc. You can think of it like variables for the framework just like programming languages have variables. Some frameworks allow you to use normal JavaScript variables for `state`. Other frameworks provide their own abstractified methods to handle data in the app. 

## Rendering

Since frameworks give you an abstractified way to build a page/app, it needs to have some way of translating the abstract components you wrote in framework-lingo into concrete HTML, CSS, and JS that the browser can understand. That process is commonly referred to as `rendering`. `Rendering` is strongly tied to `state` as the structure and appearance of the page is often dependent on the data or `state` of the app. Unsurprisingly, every framework has its own approach to `rendering`. Some frameworks add an extra layer that translates the framework code into browser-understandable code on-the-spot when the code is run in the user’s browser. Others compile the framework code into browser code beforehand so that there is no in-between step. Some frameworks reflect page changes to `state` immediately on change. Other frameworks have an extra layer that can group changes together for efficiency while not being as immediate. This gets into the discussion of `reactivity`,  or in other words how frameworks approach updating the page with changes to `state`.

---

# Framework Overview

Below are some quick overviews and comparisons of some current JS frameworks.

[This video](https://www.youtube.com/watch?v=cuHDQhDhvPE&ab_channel=Fireship) is also a good introduction to the below and more if you are interested.

 

![Untitled](UI%20Frameworks%20(&%20Libraries)%203aaf9b90aa4c4502976d7301e62aa00c/Untitled.png)

# React

### Description

React is currently the dominating JS library/framework. Despite not being the most performant, it is relatively older, more mature, has a large and robust community, and is the most used. 

Being older, React was based on the SPA (single page application) model where, instead of just starting with HTML, the webpage would start with a blank html template and rely entirely on javascript to manage the application’s state and create+manage all the necessarily HTML elements. As a result, React uses JSX, a sort-of javascript version of HTML, inside of javascript files to dictate the webpage’s structure. When “rendering” the app, React has a “virtual DOM” in the background that keeps track of how the page should look like, changing the actual page to apply changes when necessary. 

Components are made using normal javascript functions that return JSX, and state is managed using React-provided “hooks”.

### Key Features

- Uses a virtual DOM to manage rendering and reactivity, which includes a ~60kb overhead
- Uses JSX to scaffold the page
- Simple structure with few opinions (it’s a library 🙃)
- Large selection of useful packages made by the community for virtually anything
- Most used. Largest community
- NextJS meta framework enables alternative rendering (e.g. SSR) and deployment (e.g. Vercel) options
- [Amazing documentation](https://beta.reactjs.org/)

![Untitled](UI%20Frameworks%20(&%20Libraries)%203aaf9b90aa4c4502976d7301e62aa00c/Untitled%201.png)

# Svelte

### Description

One of the newer frameworks, Svelte realizes that the virtual DOM is not necessarily a good idea and opts for a zero-overhead approach, instead compiling all the code into vanilla HTML and JS at the build step. 

State is abstractified into a simple syntax so you can use normal JS variables. Uses HTML instead of JSX as well. These and all other features combine to a simple and excellent developer experience. Community is smaller but passionate. 

### Key Features

- Code is compiled into native JS + HTML at build step, meaning zero overhead
- Uses HTML and JS (no JSX)
- Simple structure
- Relatively newer framework with excellent developer satisfaction
- Sveltekit meta framework for alternative rendering and more

![Untitled](UI%20Frameworks%20(&%20Libraries)%203aaf9b90aa4c4502976d7301e62aa00c/Untitled%202.png)

# Angular

### Description

One of the older frameworks. Higher initial learning curve and less customizability. Likely not the best choice for you.

### Key Features

- The most structured (and perhaps clunky)
- No virtual DOM
- Uses HTML and keeps it separate from JS
- Comes with opinionated tools out of the box
- Large package sizes
- Designed for enterprise-level applications
- Memed on a lot (negatively)

![Untitled](UI%20Frameworks%20(&%20Libraries)%203aaf9b90aa4c4502976d7301e62aa00c/Untitled%203.png)

# Vue

### Description

Like Angular, but more approachable, more developer satisfaction, and more modern.

### Key Features

- Very similar to Angular except less structured & simpler, more customizable, and with virtual DOM
- Documentation is great in many languages
- NuxtJS meta framework for alternative rendering and more