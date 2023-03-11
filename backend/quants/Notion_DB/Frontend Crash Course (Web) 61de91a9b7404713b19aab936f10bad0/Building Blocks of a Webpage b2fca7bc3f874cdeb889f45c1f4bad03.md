# Building Blocks of a Webpage

> Look mom, I made a website!
> 

---

In essence, a webpage is made up of HTML, CSS, Javascript, and any other supporting files (videos, images, metadata, etc.). These files include all the instructions and information needed for your browser to build and put together the website for the user. They’re like recipes for a webpage that the browser follows.

---

## HTML - The Skeleton 💀

HTML (Hyper Text Markup Language) tells the browser *what* is there. For example, that there should be a paragraph with “Hello world”, a button that says “Click me”, etc. Over time there have been extra features added so that you can do more than just specify scaffolds, but you will mostly use HTML to dictate what should or should not be on the webpage. 

All webpages start off with a basic structure: the `head` and the `body` tags. The `head` indicates meta data about the webpage, like the page title (the text on the tab in the browser), what other files the page depends on (JS files, CSS files, etc.), and more metadata. The `body` is where the actual contents are described. 

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Some Web Page</title>
</head>
<body>
    <h1>Content goes here!</h1>
</body>
</html>
```

## CSS - The Flesh 🙂

CSS (Cascading Style Sheets) tells the browser *how* everything is there. It involves its own language on specifying how HTML elements should look, where they should be placed, etc.

For example, if you wanted to make all text on a page red, you could do this:

```css
body {
	color: red;
}
```

## JS - The Muscle 💪

JS (JavaScript) tells the browser how everything *********interacts.* This could mean tracking the number of times a user presses a button, scrolling the user to a specific section on the page, sending a request to an API and handling the data returned, etc. It also has the ability to modify the page itself through the DOM API (document object model). For example, you can hide a menu once a user clicks a button, change the color of the page background every second, and much more.

Here is a simple example of changing a button’s color to red when it is clicked:

```html
<!-- in the HTML file -->

<button id="change-on-click">Click me to change my color!</button>
```

```jsx
// in the JavaScript file

const button = document.getElementById('change-on-click');

button.addEventListener('click', function() {
		button.style.color = 'red';
});
```