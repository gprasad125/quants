# HW: Development pt. 1

---

For this step of the Hello World project, we will simply add two basic pages: a hello world page, and an about page. 

---

# 1. Installing wouter

We will be using the wouter library for React routing because it is small and simple.

```bash
# npm
npm install --save wouter

# yarn
yarn add wouter
```

# 2. Remove unneeded boilerplate

Next, remove unnecessary files and code.

- Delete `vite.svg` from `public`
- Delete `react.svg` from `assets`
- Delete everything in `App.css`
- Delete everything in `index.css` except the `@tailwind` directives.
- In `App.tsx` (or `.jsx` if you aren’t using typescript)
    - Delete everything between the parentheses of the `return` on line 8
        - Replace with
            
            ```jsx
            <h1>Hello World</h1>
            ```
            
    - The delete line `6` where the `count` state is declared.
    

After these steps, `App.tsx` should look like this

```jsx
import { useState } from 'react'
import './App.css'

function App () {

  return (
    <h1>Hello World</h1>
  );
}

export default App
```

And running the dev server (`npm run dev` or `yarn dev`) would display

![Screenshot 2023-01-20 at 9.19.09 PM.png](HW%20Development%20pt%201%202afc11f4a984473ab49d030d85656d33/Screenshot_2023-01-20_at_9.19.09_PM.png)

Finally, modify `index.html`:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
		<!-- Remove the link to the Vite icon logo -->
		<!-- <link rel="icon" type="image/svg+xml" href="/vite.svg" /> -->
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
		<!-- Update the App title -->
    <title>Hello World Example</title>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.tsx"></script>
  </body>
</html>
```

If not using typescript (`main.tsx` → `main.jsx`):

```jsx
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
		<!-- Remove the link to the Vite icon logo -->
		<!-- <link rel="icon" type="image/svg+xml" href="/vite.svg" /> -->
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
		<!-- Update the App title -->
    <title>Hello World Example</title>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.jsx"></script>
  </body>
</html>
```

# 3. Creating the pages

We will need two pages with two routes:

1. The hello world home page (`/`)
2. The about page (`/about`)

In the `src` directory, make a new `pages` directory

```bash
mkdir src/pages
```

Then create `home.tsx` and `about.tsx`. If you’re not using Typescript, then it would be `.jsx` instead of `.tsx`.

```bash
touch src/pages/home.tsx

touch src/pages/about.tsx
```

### 1. Home

In `home.tsx` add the following component code if you’re using typescript:

```tsx
import { useEffect, useRef, useState } from "react";

function Home() {
		// create state to track time string
    const [time, setTime] = useState((new Date()).toLocaleTimeString());
		// store interval in a reference to clear it on unmount
    const intervalRef = useRef<number>();
		
		// on component mount
    useEffect(() => {
				// create a recurring interval to update the time
        intervalRef.current = setInterval(() => {
            setTime((new Date()).toLocaleTimeString());
        }, 1000);
				
				// when the component is unmounted, clear the interval
        return () => {
						// need to include "as" here to tell
						// typescript that we know it will always be defined as a number. 
            clearInterval(intervalRef.current as number);
        };
    }, []);

    return (
        <h1 className="text-center text-xl font-bold text-slate-600 mt-20">
						Hello World, it is {time}
				</h1>
    );
}

export default Home;
```

Otherwise if you’re using normal javascript:

```jsx
import { useEffect, useRef, useState } from "react";

function Home() {
		// create state to track time string
    const [time, setTime] = useState((new Date()).toLocaleTimeString());
		// store interval in a reference to clear it on unmount
    const intervalRef = useRef();
		
		// on component mount
    useEffect(() => {
				// create a recurring interval to update the time
        intervalRef.current = setInterval(() => {
            setTime((new Date()).toLocaleTimeString());
        }, 1000);
				
				// when the component is unmounted, clear the interval
        return () => {
            clearInterval(intervalRef.current);
        };
    }, []);

    return (
        <h1 className="text-center text-xl font-bold text-slate-600 mt-20">
						Hello World, it is {time}
				</h1>
    );
}

export default Home;
```

Here we add some display text with a self-incrementing clock.

### 2. About

In `about.tsx` (same for Javascript):

```jsx
function About() {
    return (
        <h1 className="text-center text-xl font-bold text-slate-600 mt-20">
						About Page
				</h1>
    );
}
export default About;
```

# 4. Putting it all together

Now it’s time to connect the routes and pages. 

Replace `App.tsx`with the following:

```tsx
import { Route, Switch } from 'wouter';
import About from './pages/about';
import Home from './pages/home';
import './App.css';

function App () {
    return (
        <Switch>
            <Route path='/' component={Home} />
            <Route path='/about' component={About} />
        </Switch>
    );
}

export default App;
```

Here we declare a `Switch` component so that only one `Route` is matched at a time. Then we specify a `Route` for each component with the corresponding path. Wouter will handle the rest for us. 

If you stop (`ctrl + c` in the terminal) and rerun the dev server now, you should see this when you open the app with the time updating every second. 

![Screenshot 2023-01-20 at 9.41.34 PM.png](HW%20Development%20pt%201%202afc11f4a984473ab49d030d85656d33/Screenshot_2023-01-20_at_9.41.34_PM.png)

If you add `about` to the url (so something like `localhost:5173/about`, where 5173 is whatever port the server is hosted out) and enter it into your browser, you should see the about page. 

![Screenshot 2023-01-20 at 9.43.50 PM.png](HW%20Development%20pt%201%202afc11f4a984473ab49d030d85656d33/Screenshot_2023-01-20_at_9.43.50_PM.png)

# 5. Adding a navbar component

Right now the pages are there, but it would be great if a user could navigate between the pages by clicking on navbar links.

Create a new `components` directory in `src`.

```bash
mkdir src/components
```

Then make a new `navbar.tsx` file inside (`.jsx` for javascript, you know the drill).

```bash
touch src/components/navbar.tsx
```

Inside `navbar.tsx`, add this:

```jsx
import { Link } from "wouter";

function Navbar() {
    return (
        <nav className="container mx-auto max-w-3xl text-blue-600 mt-10 px-5">
            <Link href="/" className="inline-block mr-5 hover:text-blue-400">
                Home
            </Link>
            <Link href="/about" className="inline-block hover:text-blue-400">
                About
            </Link>
        </nav>
    );
}
export default Navbar;
```

Here we specify a `nav` with links to the different pages. Note that we use `Link` here instead of `a` so that `wouter` can handle navigation to the right page for us without causing a page reload. Using `a` tags would tell the browser to navigate to the new page while clearing the current one, causing an unnecessary refresh. 

Finally update `App.tsx` with the new navbar:

```jsx
import { Route, Switch } from 'wouter';
import About from './pages/about';
import Home from './pages/home';
import Navbar from './components/navbar';
import './App.css';

function App () {
    return (
        <>
            <Navbar />
            <Switch>
                <Route path='/' component={Home} />
                <Route path='/about' component={About} />
            </Switch>
        </>
    );
}

export default App;
```

The `Navbar` is put in `App.tsx` outside the `Switch` so that it isn’t unnecessarily re-rendered on every page navigation.

In order to put the `Navbar` side-by-side with the `Switch`, we wrap it in a fragment (the `<></>`) to keep JSX happy. 

Now you should see this with the dev server restarted

![Screenshot 2023-01-20 at 9.54.38 PM.png](HW%20Development%20pt%201%202afc11f4a984473ab49d030d85656d33/Screenshot_2023-01-20_at_9.54.38_PM.png)

Clicking the navigation links instantly switches the page with client-side routing. 

# 6. Conclusion

We have now added two basic pages and simple client-side routing to the `Hello World` app.