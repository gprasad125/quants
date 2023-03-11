# Basic SEO and Accessibility

> To the moon 🚀
> 

---

There are many hyper-optimizations that you can do to improve search rankings and how assistive devices can access your site, some of which may or may not be relevant to you. Below are just some minimal and basic tips on SEO (Search Engine Optimization) and accessibility. If your project desires the best discoverability possible, definitely search online for more specific  practices for improving SEO. Same if it targets users that rely on screen-readers for example.  

---

# 1. Use Semantic HTML tags

> [https://www.w3schools.com/html/html5_semantic_elements.asp](https://www.w3schools.com/html/html5_semantic_elements.asp)
> 

When building the page’s HTML, you have unlimited options. For a sentence of text for example, you can use `p`, `h1`, `span`, `div`, `a`, and more. However, each tag comes with its own semantic meaning. `h1` indicates that it’s a header, `a` that it is a link, etc. With CSS, you could style all of them to look and behave exactly the same. For the search indexer and screen-reader however, the only information it sees is usually just the HTML. What tag you use can convey completely different messages to the search indexer. Using the right tag for the right situation helps the indexer a lot in understanding what content your website has. 

You can also take advantage of tags such as `article`, `main`, `nav`, and more instead of just using bland `div`s.

# 2. Use Meta HTML tags

> [https://www.w3schools.com/tags/tag_meta.asp](https://www.w3schools.com/tags/tag_meta.asp)
> 

Including a `title`, description, and other `meta` tags in the `head` of the HTML directly ties to what Google displays in search results, how the site is interpreted and displayed, and more.

```html
<head>
	<title>Website title here</title>
  <meta charset="UTF-8">
  <meta name="description" content="Free Web tutorials">
  <meta name="keywords" content="HTML, CSS, JavaScript">
  <meta name="author" content="John Doe">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
```

# 3. Add textual information to Images

For visual media files like images, there is usually an attribute or additional tag that can be added to provide additional textual information about the file you’re linking. Otherwise naming the media file something descriptive instead of just `image_101.jpg` would aid as well.

```html
<img 
	src="https://www.thesprucepets.com/thmb/7dqFqgodJPWbkgKGGXKDllS2qsQ=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/dog-breed-profile-golden-retriever-1117969-hero-da398f6462704058ace0ef5ae007866d.jpeg" 
	alt="A very good boy"
>
```