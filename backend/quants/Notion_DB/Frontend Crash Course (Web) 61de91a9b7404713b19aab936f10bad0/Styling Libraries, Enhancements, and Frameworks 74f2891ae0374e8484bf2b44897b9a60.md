# Styling Libraries, Enhancements, and Frameworks

> Making CSS not suck so bad
> 

---

# Introduction

You may have noticed a recurring theme that when something is repetitive and annoying to work with, developers will endeavor to find new ways to make it less repetitive and less annoying to work with. 

The CSS styling system isn’t the best developer experience, thus there have been multiple attempts towards making it better. 

---

# Types of Styling Libs & Frameworks

> All ideas below have been taken from [Theo](https://www.youtube.com/@t3dotgg)
> 

You can generally characterize CSS tools by three types: CSS extensions, style systems, and behavior libraries. 

CSS extensions build on top of CSS. You are still writing your own CSS, just that the tools provide more efficient or easier ways to write it. A good example is [Tailwind](https://tailwindcss.com/).

Style systems dictate the CSS that you use. You are using styles that other people have already written for you. A good example is [Bootstrap](https://getbootstrap.com/). 

Behavior libraries dictate the behavior of the component, going one level beyond. You are using pre-built, default-styled components with all the logic and behavior built-in. A good example is [HeadlessUI](https://headlessui.com/). 

Of course, many hover between the lines.

You will find below a quick overview of some relevant CSS tools.

# 1. Tailwind

> [https://tailwindcss.com/](https://tailwindcss.com/)
> 

### Key Features

- Provides utility CSS classes - simple, straightforward, flexible
- Main drawback is “class clutter” due to using numerous CSS classes in HTML
- Compiler only includes the classes you use in your app, minimizing the size
- A little more complex to setup because of the previous note.

### Description

Tailwind is a CSS extension. It basically creates a bunch of utility CSS classes for all basic CSS properties (font-size, color, padding, etc.). Instead of `color: red;` in the CSS for example, you would just add the `text-red-500` class to the HTML element directly. This makes it so that you can quickly scaffold designs directly in your HTML, sometimes not needing a `.css` file entirely. 

Additionally, there are preset ranges for most indeterminate CSS attributes (margin, padding, etc.) specifically coordinated into a design system that will aid you in making consistent styling across your entire app. 

Tailwind also compiles your styles and includes only the classes you need, reducing the “zombie” or unused code in your final app bundle. 

Of course, you should recognize that inserting all the style definitions into HTML could cause a lot of clutter, which is one of the few, main criticisms for Tailwind. And at the end of the day, you are still writing your own CSS. However, most developers find that the significantly increased speed in development more than makes up for the clutter caused by abusing HTML class. 

# 2. Bootstrap

> [https://getbootstrap.com/](https://getbootstrap.com/)
> 

### Key Features

- Pre-styled CSS classes
- Straightforward, but annoying to customize
- Easy to setup
- Component libraries for many UI Frameworks

### Description

Probably the most well known CSS tool out there, Bootstrap is a framework and style system, meaning that it provides CSS classes that have styles written and decided by other developers. One main issue with Bootstrap is that Bootstrap websites tend to look similar without extensive customization and styling overrides. If you only need a basic interface without too much flashy personality, then Bootstrap works great. 

Including it into your project is as simple as adding a `src` link of a Bootstrap CDN to the `head` of your HTML. Alternatively, there are libraries for various UI Frameworks like React that provide components directly pre-styled with Bootstrap. 

Overall, there’s a good reason why it’s frequently used in beginner tutorials, though definitely make sure to not become dependent on it. Making good unique websites will ultimately require some custom CSS. 

# 3. Material UI (MUI)

> [https://mui.com/](https://mui.com/)
> 

### Key Features

- Pre-built, pre-styled components
- Lets you make *****sharp***** interfaces
- React-specific

### Description

Somewhat similar to Bootstrap as a style-system, but also a behavior library that provides pre-made UI components with all the bells and whistles. Should have better customization options than Bootstrap, though it likely also suffers a similar issue of being cookie-cutter without thoughtful customization. But the UIs you make do look really sharp and snazzy. 

Definitely something work looking at if you’re using React.