# Browser DevTools

> Life savers
> 

---

# Intro

All major browsers come with a set of features meant for developers that help them dissect websites. This comes in VERY handy for debugging. Usually these tools are opened in a panel with tabs at the top to navigate between the different screens. Below is an example of Chrome’s.

![Screenshot 2023-02-12 at 3.07.21 PM.png](Browser%20DevTools%203767fa2fc82e42f8b76eae40ea40f9ef/Screenshot_2023-02-12_at_3.07.21_PM.png)

On Chrome, you can simply right-click on the page and select `inspect` in the popup menu to open up the dev tool panel. If you are using another browser, you should be able to just look it up. 

The following sections will cover some of the most useful tabs for Chrome. Other browsers should have similarly named tabs that cover the same purpose. 

# Elements

This screen lets you look at the current HTML and CSS of the page. This is where you’ll likely be debugging your styles and making sure that the correct HTML elements were created. 

![Screenshot 2023-02-12 at 3.10.58 PM.png](Browser%20DevTools%203767fa2fc82e42f8b76eae40ea40f9ef/Screenshot_2023-02-12_at_3.10.58_PM.png)

# Console

This displays any logs from any `console.log`s that run in the Javascript code or any other messages that appear from the website. Often, you might add a `console.log` into your code and check the browser console after running the page to see what went wrong. In the example image below, it displays the HTTP errors from the various API calls made by the page. 

![Screenshot 2023-02-12 at 3.13.16 PM.png](Browser%20DevTools%203767fa2fc82e42f8b76eae40ea40f9ef/Screenshot_2023-02-12_at_3.13.16_PM.png)

# Sources

This shows you all the assets that the browser has retrieved for the website. You can check here to see if all your assets were linked properly.

![Screenshot 2023-02-12 at 3.15.38 PM.png](Browser%20DevTools%203767fa2fc82e42f8b76eae40ea40f9ef/Screenshot_2023-02-12_at_3.15.38_PM.png)

# Network

This shows you all the HTTP requests that the browser made when getting, loading, and running the page. All API requests you make will also show up here, making it perfect for debugging API calls in your app. You can check the request headers, payload, the response body, the compression type, the status code, and much more.

![Screenshot 2023-02-12 at 3.17.44 PM.png](Browser%20DevTools%203767fa2fc82e42f8b76eae40ea40f9ef/Screenshot_2023-02-12_at_3.17.44_PM.png)

![Screenshot 2023-02-12 at 3.18.25 PM.png](Browser%20DevTools%203767fa2fc82e42f8b76eae40ea40f9ef/Screenshot_2023-02-12_at_3.18.25_PM.png)

# Application

This shows all the data related to the page, including cookies, data stored in the browser (local and session storage), and more. You will likely use this screen to debug issues involving authentication cookies and saving data locally to the user’s browser.

![Screenshot 2023-02-12 at 3.21.06 PM.png](Browser%20DevTools%203767fa2fc82e42f8b76eae40ea40f9ef/Screenshot_2023-02-12_at_3.21.06_PM.png)