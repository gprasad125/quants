# Picking The Right Starting Tool

---

With meta frameworks, bundlers, and more, there are many tools/tool-chains that you can start with, each deciding how you will develop the app and how the app will behave in production. Below is a quick overview of the main tools you might want to look at.

---

# Next - the dynamic all-rounder

> [https://nextjs.org/](https://nextjs.org/)
> 

### Key Features

- Easy deployment to Vercel
- Designed specifically to work with React
- Powerful server with many nice features (can literally serve as a backend)
- Supports SSG, SSR, and more

### Description

Chances are this is the one for you. Very flexible build options with numerous features such as image optimization, streaming, and more. You can’t go wrong choosing this one. Uses Webpack for bundling.

# Vite - performant alternative for static apps

> [https://vitejs.dev/guide/](https://vitejs.dev/guide/)
> 

### Key Features

- Simple and fast
- Only supports static builds, mainly SPA

### Description

An alternative if you only need to make an SPA. There are plugins for potential pre-rendering and SSG and maybe even SSR, but you might as well just use Next at that point. Uses ESBuild, which is written in Go, for the dev server and RollupJS for the final build output, making it very fast. If you require browser support, note that Vite only supports modern browsers by default, and you need to enable the legacy plugin to generate alternative versions for older browsers.

# Astro - extreme minimalism

> [https://astro.build/](https://astro.build/)
> 

### Key Features

- Make zero-javascript static-sites with your favorite frameworks
- Introduces, island architecture, most notably lazy-loading components when they are scrolled into view
- Mainly supports SSG

### Description

Offers some neat features if your site is strictly static or only a tiny bit dynamic. Supports SPA, SSG, and other static options, mainly the ability to compile everything into only HTML and CSS (zero JS) if your site is purely static and the ability to control component rendering on a fine-grained level, such as only loading a component when it is scrolled into view by the user. You can also use multiple frameworks together like Svelte with React, though reasons to do so is 🤷.

# Create React App - avoid this

### Short Answer

It is old, and using Vite is just better in almost all ways.

### Long Answer

The first major React toolchain. Being the first, it had to be designed to solve problems of today with the knowledge and experience of yesterday. Has grown to be bulky and cumbersome, though it has been improving recently. Vite is just a more modern alternative, using much faster build tools than what Create React App uses (Webpack).