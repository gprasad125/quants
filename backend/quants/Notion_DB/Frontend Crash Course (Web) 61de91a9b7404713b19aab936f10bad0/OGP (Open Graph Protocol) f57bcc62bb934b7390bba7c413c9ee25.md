# OGP (Open Graph Protocol)

> Sharing is caring
> 

---

# Overview

OGP is a standard for specifying metadata that helps 3rd party sites, namely social media sites like Twitter, Facebook, Discord, etc., understand the content of your website.

Practically, this enables neat little cards and embeds to appear whenever someone mentions your website’s url. This becomes nice if your website is targeted towards a broad audience and would benefit from social media sharing. 

# Implementing

For normal websites, OGP is really just adding the appropriate `meta` HTML tags to the appropriate pages. [Refer to the official website for specific instructions](https://ogp.me/). 

A typical OGP setup for a page could be:

```html
<head>
<title>Joe's Bakery</title>
<meta property="og:title" content="Joe's Bakery" />
<meta property="og:type" content="website" />
<meta property="og:url" content="https://bakery.com/" />
<meta property="og:image" content="https://images.unsplash.com/photo-1568254183919-78a4f43a2877?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1469&q=80" />
<meta property="og:description" content="The world's finest bakery" />
<meta property="description" content="The world's finest bakery" />
</head>
```

Some websites like Twitter and Facebook have additional special tags that you can add to further enhance the embed card on those platforms. There should be numerous guides online for each platform.  

# Testing

You can test to see if your OGP is working by simply pasting the url to your site into a message. Otherwise, Facebook and Twitter both have online tools that you can search for and use to preview how the site embed would look on their platform.