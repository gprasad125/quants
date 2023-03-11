# Frontend Lingo

> Jargon, yay!
> 

---

Some buzzwords and jargon thrown around on the web and this guide that you should probably know. These are not dictionary-worthy definitions so don’t rely on them to pass any interviews (though you can maybe try, who knows). Feel free to keep this tab open on the side as you go through the crash course!

---

## JSON

Javascript Object Notation. A format for storing and communicating information. Uses similar syntax to Javascript objects. Think of it like two countries that speak different languages using English to communicate with one another (otherwise known as a Lingua Franca). 

Also refers to information that is stored in JSON format. So you can say that JSON is in JSON format and be perfectly correct (and redundant). 

## HTTP

Hyper Text Transfer Protocol. The protocol (in other words a universally-agreed-upon system of communication and data sending) that the internet uses to send most of its information and webpages. 

## Endpoint

A specific url for a specific purpose. For instance, `https://bread.com/list` might give you a list of available bread. `https://bread.com/buy` might be where you can purchase bread. (These endpoints are made-up, don’t try going to them).

## Request

You can think of it like a request or question asking for something from a server. Usually an HTTP message to an endpoint that can range from requesting the homepage for a website to telling the backend server to create a new user account in the database.

## Response

The answer to a request that the server sends back in response to the request. Can be as simple as a 200 OK status code indicating that everything went as expected or JSON containing any requested data.

## Status Code

Every HTTP Response has an arbitrary number named the `status code` that conveys how successful the response and request were. Status codes that start with 2, such as 200, 201, etc., usually mean that everything worked just as expected. Status codes that start with 4, such as 400, 401, etc., usually mean that something about the Request was unacceptable or invalid. Status code 500 (internal server error) means that the server errored while processing the Request.

## API

Application Program Interface (It’s “program,” not “programming.” Fight me). Any specified system to interact with another program. Your keyboard and mouse are the API for your computer system. Old English is the API that medieval lords would use to give commands to their servants. 

In the context of web development, it is usually the specified HTTP endpoints of a server to interact with a specific service. For example, Discord has an API that allows you to do many things, like send messages with your account using an HTTP request (don’t do this it’s against Discord ToS). There are other types of APIs that work differently (e.g. websockets), but the one described here (REST API) is the most prevalent. 

## DOM

The Document Object Model. Refers to the way the browser models the page. Has an API that enables Javascript methods to modify the DOM and page. Without this, JS would be mostly useless.