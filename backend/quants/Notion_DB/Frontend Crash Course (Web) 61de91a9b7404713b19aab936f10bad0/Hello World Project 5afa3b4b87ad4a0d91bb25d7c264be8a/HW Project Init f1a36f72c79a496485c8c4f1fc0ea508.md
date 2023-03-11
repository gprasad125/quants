# HW: Project Init

---

Quick walkthrough on setting up a new Vite project with React.

All of which is documented in [Vite’s documentation](https://vitejs.dev/guide/).

---

# 1. Run setup command

In the parent directory of where you want the frontend directory to be, run the following command in the terminal with the name of the final app directory:

### With NPM

```bash
# npm 6.x
npm create vite@latest <your-app-directory-name-here> --template react

# npm 7+, extra double-dash is needed:
npm create vite@latest <your-app-directory-name-here> -- --template react
```

### With Yarn

```bash
yarn create vite <app-directory-name> --template react
```

### With Typescript

Replace `react` with `react-ts` in the above commands.

# 2. Check Output Result

Assuming you named the directory `myapp`, you should see something like this. 

![Screenshot 2023-01-16 at 2.22.22 PM.png](HW%20Project%20Init%20f1a36f72c79a496485c8c4f1fc0ea508/Screenshot_2023-01-16_at_2.22.22_PM.png)

If you opted for Typescript, it will look like this.

![Screenshot 2023-01-16 at 2.23.38 PM.png](HW%20Project%20Init%20f1a36f72c79a496485c8c4f1fc0ea508/Screenshot_2023-01-16_at_2.23.38_PM.png)

# 3. Install Dependencies

Next, install all the necessary dependencies for the project.

```bash
# first enter the app directory
cd myapp # replace "myapp" with what you named the app directory

# then install dependencies

# with npm
npm install

# or with yarn
yarn install
```

# 4. Run Development Server

Test that everything was installed correctly by starting the development server.

```bash
# with npm
npm run dev

# with yarn
yarn dev

# Expected Output
VITE v4.0.4  ready in xxx ms

  ➜  Local:   http://localhost:5173/
  ➜  Network: use --host to expose
  ➜  press h to show help
```

Then navigate to the url displayed in your browser and you should see something like this:

![Screenshot 2023-01-16 at 2.31.28 PM.png](HW%20Project%20Init%20f1a36f72c79a496485c8c4f1fc0ea508/Screenshot_2023-01-16_at_2.31.28_PM.png)

Feel free to go into `src/App.js` and change some text in the `<p>` tags. As soon as you save your changes, you should see your browser update automatically to reflect the changes.

Once you have confirmed that everything is working, you can stop the development server with `ctrl + c` in the terminal where you ran the `dev` command.

# 5. Configuration

Refer to [official documentation](https://vitejs.dev/config/) for configuration options. 

One configuration you might want to do is to change the port that the development server is hosted at. To do this, simply modify `vite.config.ts` (or `.js` if you aren’t using Typescript). 

Here we change the port to `3000` ([documentation reference](https://vitejs.dev/config/server-options.html#server-port)) so that we can connect it to the example backend later. 

```jsx
// vite.config.ts

import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    port: 3000
  }
})
```