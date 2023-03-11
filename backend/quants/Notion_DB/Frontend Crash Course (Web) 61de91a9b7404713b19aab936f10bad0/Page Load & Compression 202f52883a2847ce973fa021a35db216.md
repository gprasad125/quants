# Page Load & Compression

> 100kb of overhead! 😎
> 

---

# Overview

Page load refers to the amount of assets that is required to be loaded before your website can be used. This usually focuses on the Javascript file sizes but can also include images, CSS, and other assets. 

Why should I care about this? Well, having smaller files means that users can load your website faster. This isn’t very impactful for users on wifi, but if your users are loading your site with cellular data, it could mean the difference of seconds in loading speed. Seconds may or may not sound much to you, but websites that take longer to load tend to turn away more users. This is why web developers often compete on the scale of milliseconds. Speed is very much key for high traffic apps.  

# Decreasing Page Load

The most straightforward way to decrease the load is to write less Javascript, use less assets, etc. The smaller the file sizes, the less data that needs to be loaded by the user. 

One of the key areas to pay attention to is the libraries you use. One library might only be 12 kb in size, while another might be 140 kb. Make sure to consider what features you really need and choose a library without too many excess features. One helpful tool to check the size of a library is [Bundle Phobia************.************](https://bundlephobia.com/) Some libraries are tree-shakable, meaning that a build tool can break apart the library code and only include the code that you used instead of integrating the entire library. In this case, the total size of the library does not matter much. 

Otherwise, developers also rely on code minimization, where unnecessary spaces and long variable names are cut down to make the code as compact and dense as possible. This significantly reduces the file sizes for JS and CSS. 

The next trick that developers use is compression. You can further compress the minimized files and have the browser decompress the files to achieve even smaller file sizes. Common compression algorithms used are Brotli and Gzip. You can implement compression on the server serving the assets, a reverse proxy like Nginx, or more. 

# In relation to UI frameworks

Since the size of the end app matters a lot, page load becomes a major point of debate for UI frameworks. You might have heard criticism for React on how it uses a virtual DOM that adds extra overhead to your app, causing significant increases to your JS file sizes. You might have heard praise for frameworks like Svelte that use zero overhead, making your JS files as slim as possible. 

In all honesty, it only matters in the extreme-end when you’re dealing with high demands for performance. Many companies use React just fine for performance. For the purposes of your project, larger file sizes also likely won’t matter as much unless your app requires as fast loading times as possible, which is unlikely.