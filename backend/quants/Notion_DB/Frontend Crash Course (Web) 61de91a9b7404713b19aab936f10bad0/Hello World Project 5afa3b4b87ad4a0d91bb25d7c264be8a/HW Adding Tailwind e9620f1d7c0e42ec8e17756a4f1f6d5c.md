# HW: Adding Tailwind

> Referencing [https://tailwindcss.com/docs/guides/vite](https://tailwindcss.com/docs/guides/vite)
> 

---

<aside>
📌 Note: 
Don’t forget to add Tailwind’s developer tools to your IDE if available! For VSCode, that would be the Tailwind intellisense extension. It gives auto-complete suggestions and saves a lot of headache!

</aside>

# 1. Install dependencies

Install the necessary packages for Tailwind to work.

```bash
# -D flag tells package manager to install as development dependency

# using npm
npm install -D tailwindcss postcss autoprefixer

# OR using yarn
yarn add -D tailwindcss postcss autoprefixer
```

2. Initialize Tailwind configuration

Initialize the default configuration files for Tailwind and PostCSS.

```bash
npx tailwindcss init -p
```

# 3. Specify files for Tailwind to watch

Modify `tailwind.config.cjs` and add in the file-paths in the `content` option to tell Tailwind which files to track so that it can know which CSS classes you use and which you don’t. Just if you’re wondering, the extension `.cjs` just stands for common js and just indicates that the file uses Node’s import and export syntax (`.mjs` would be module js and indicate ES6 module import/export syntax). 

```jsx
// tailwind.config.cjs

/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [ // tell Tailwind which files to track
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}", // all js and ts files in src/
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

# 4. Add Tailwind directives

Add the Tailwind directives to the top of `src/index.css`. This is where Tailwind will be putting all the compiled CSS classes at the end when you build your app into a production bundle. It’s best that they are universal and go before all other CSS. Thus, the best place to put it would be `src/index.css` since it is the root CSS file for the entire project. You can use `index.css` for any global settings. For specific styling, it would be preferable to use `src/App.css` instead. 

```css
/* Add this */
/* ================== */
@tailwind base;
@tailwind components;
@tailwind utilities;
/* ================== */

:root {
  font-family: Inter, Avenir, Helvetica, Arial, sans-serif;
  font-size: 16px;
  line-height: 24px;
  font-weight: 400;

  color-scheme: light dark;
  color: rgba(255, 255, 255, 0.87);
  background-color: #242424;

  font-synthesis: none;
  text-rendering: optimizeLegibility;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  -webkit-text-size-adjust: 100%;
}
```

You might see your IDE highlight the directives with squiggly lines—those are completely safe to ignore. 

![Screenshot 2023-01-20 at 9.48.34 PM.png](HW%20Adding%20Tailwind%20e9620f1d7c0e42ec8e17756a4f1f6d5c/Screenshot_2023-01-20_at_9.48.34_PM.png)

# 5. Finish

You should be all set to use Tailwind classes in your project. As a test, you can add the following class to `line 19` of `src/App.tsx` (`.jsx` if you aren’t using Typescript) to test giving the text a different color. 

```html
<!-- Change this -->
<div className="card">

<!-- To this -->
<div className="card text-blue-500">
```

You should now see this when you start the dev server.

![Screenshot 2023-01-20 at 3.07.46 PM.png](HW%20Adding%20Tailwind%20e9620f1d7c0e42ec8e17756a4f1f6d5c/Screenshot_2023-01-20_at_3.07.46_PM.png)

The text is blue, showing that Tailwind was correctly added. 

You might also notice that the icons are positioned differently now. Tailwind adds some default styling to certain elements to help standardize styling across browsers. For example, `h1` and `p` become the same font size. This gives you a blank canvas to add on your preferred styles.