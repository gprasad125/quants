# Rendering Strategies in Production

> Hyper-optimizing user experience
> 

---

`Rendering` isn’t only decided by the framework but in how you deploy your frontend as well. Different rendering strategies come with their own pros and cons. Below are some of the rendering methods that’ll be most relevant to you.

---

## SPA - if you don’t care about SEO

The most basic deployment method for frameworks is an SPA (single page application). As its name suggests, an SPA app has a single HTML file (usually called index.html) for the entire app that serves as the entrypoint, and JS is relied upon to render all the different pages/screens into HTML for the browser when the code is run. 

| Pros | Cons |
| --- | --- |
| Simple to deploy. As simple as an AWS S3 bucket with cloudfront or static hosting with a server. | HTML file is blank, which confuses search engine indexers and has poor SEO (search engine optimization) |
|  | Dynamic content will require on-the-spot data fetching when the code is run. |

## SSR - if things change constantly and you want best SEO

Server Side Rendering is where the web server renders all the HTML and resources on-request before sending the files to the user. This means that the content will always be up-to-date and that the HTML will be fully fleshed out once it reaches the user.

| Pros | Cons |
| --- | --- |
| Best SEO (search engine optimization) support. HTML is rendered before the user sees them. | Requires a dedicated server to constantly pre-render the pages on request, which complicates deployment and may slightly increase the time before the user sees anything |
| Data can be fetched and rendered before the user sees anything |  |

## SSG - if things aren’t as dynamic and you just need decent SEO

Static Site Generation is an in-between of SPA and SSR, where the app is pre-rendered before being deployed. Has some pros and cons of both worlds.

| Pros | Cons |
| --- | --- |
| Some SEO (search engine optimization) support. HTML is flushed out, but is static. | Dynamic content will require constant redeployment or on-the-spot data fetching when the code is run. |
| Does not require dedicated server for rendering |  |