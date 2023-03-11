# HW: Deploying to Railway

---

This doc covers the steps to deploy the `Hello World` example to Railway. 

---

# 1. Setup the frontend server

Since we’re using a decoupled setup, we will need to setup a basic server to serve the frontend assets. We’ll use the FastifyJS server framework with NodeJS for this. 

### 1.1. Splitting the repo

We will be setting up the Fastify server code in the same directory as the frontend app. 

If all of your frontend assets are in the root of the Github Repository, you will want to move it into a directory to keep it separate from the server. So the repository should look something like this:

---

- 📁 Repository Root Directory
    - 📁 app
        - 📁 node_modules
        - 📁 public
        - 📁 src
            - 📁 components
            - 📁 pages
            - 📎 App.css
            - 📎 App.tsx
            - 📎 index.css
            - 📎 main.tsx
        - 📎 package.json
        - 📎 .gitignore
        - 📎 vite.config.cjs
        - and more …

---

### 1.2. Move `.gitignore` to root

Once everything has been organized as above, you’ll want to keep the `.gitignore` in the root directory so that git can find it.

---

- 📁 Repository Root Directory
    - 📁 app
        - 📁 node_modules
        - 📁 public
        - 📁 src
            - 📁 components
            - 📁 pages
            - 📎 App.css
            - 📎 App.tsx
            - 📎 index.css
            - 📎 main.tsx
        - 📎 package.json
        - 📎 vite.config.cjs
        - and more …
    - 📎 .gitignore

---

### 1.3. Create `server` directory

Next, create the `server` directory in the project root where we’ll be keeping the server code.

---

- 📁 Repository Root Directory
    - 📁 app
        - 📁 node_modules
        - 📁 public
        - 📁 src
            - 📁 components
            - 📁 pages
            - 📎 App.css
            - 📎 App.tsx
            - 📎 index.css
            - 📎 main.tsx
        - 📎 package.json
        - 📎 vite.config.cjs
        - and more …
    - 📁 server
    - 📎 .gitignore

---

### 1.4. Initialize `npm`

Initialize `npm` in the `server` directory.

```bash
cd server

npm init -y
```

### 1.5. Install dependencies

We will be using the following libraries.

```bash
# npm
npm install --save fastify @fastify/compress @fastify/static

# yarn
yarn add fastify @fastify/compress @fastify/static
```

### 1.6. Create `server.js`

Create the file where we will setup the frontend server and paste the following code into it.

---

- 📁 Repository Root Directory
    - 📁 app
        - 📁 node_modules
        - 📁 public
        - 📁 src
            - 📁 components
            - 📁 pages
            - 📎 App.css
            - 📎 App.tsx
            - 📎 index.css
            - 📎 main.tsx
        - 📎 package.json
        - 📎 vite.config.cjs
        - and more …
    - 📁 server
        - 📁 node_modules
        - 📎 server.js
        - 📎 package.json
        - 📎 package-lock.json `or` yarn.lock
    - 📎 .gitignore

---

```jsx
// server.js

// require libraries
const fastify = require('fastify')();
const fastifyStatic = require('@fastify/static');
const fastifyCompress = require('@fastify/compress');
const path = require('path');
// store PORT env variable with default to 3000
const PORT = process.env.PORT || 3000;

// add compression plugin
fastify.register(fastifyCompress);
// add static file serving plugin
fastify.register(fastifyStatic, {
    root: path.join(__dirname, 'dist'),
    prefix: '/public/'
});

// create catch-all route that serves index.html of app
fastify.get('*', (req, reply) => {
    return reply.sendFile('index.html');
});

// start server
fastify.listen({ port: PORT, host: '0.0.0.0' }, (err) => {
    if (err) throw err;
    console.log('Server listening at port ' + PORT);
});
```

# 2. Configure `Vite` base

The `Fastify` server above is configured to serve static assets at the `/public/` url. This will require us to update `Vite`'s configuration to map the asset urls correctly. Modify `app/vite.config.cjs` as follows:

```jsx
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  // ...
  base: '/public' // set host-base to "/public"
})
```

# 3. Setup Docker

We will be using Docker to containerize the frontend and make deploying the Railway easy.

### 3.1. Create `Dockerfile`

In the repository root, create a new file named as `Dockerfile`.

---

- 📁 Repository Root Directory
    - 📁 app
        - 📁 node_modules
        - 📁 public
        - 📁 src
            - 📁 components
            - 📁 pages
            - 📎 App.css
            - 📎 App.tsx
            - 📎 index.css
            - 📎 main.tsx
        - 📎 package.json
        - 📎 vite.config.cjs
        - and more …
    - 📁 server
        - 📁 node_modules
        - 📎 server.js
        - 📎 package.json
        - 📎 package-lock.json `or` yarn.lock
    - 📎 .gitignore
    - 📎 Dockerfile

---

```docker
ARG PORT

# work on top of node image
FROM node:18 
# specifiy working directory
WORKDIR /frontend
# make port argument available as environment variable
ENV PORT=$PORT

# init directories
RUN mkdir server && mkdir app

# install pm2
RUN npm install -g pm2

# ========================
# Server Setup
# ========================
# copy dependency files to docker image
COPY server/package.json server/
COPY server/yarn.lock server/
# install dependencies
RUN cd server && yarn install
# copy remaining assests to docker image
COPY server/ server/

# ========================
# Frontend Setup
# ========================
# copy dependency files to docker image
COPY app/package.json app/
COPY app/yarn.lock app/
# install dependencies
RUN cd app && yarn install
# copy remaining assests to docker image
COPY app/ app/
# build frontend code
RUN cd app && yarn build

# move static files to server
RUN mv app/dist server/

# Expose container port
EXPOSE $PORT
# set working directory to server
WORKDIR /frontend/server
# start server daemon
CMD [ "pm2-runtime", "start", "server.js" ]
```

### 3.2. Create `.dockerignore`

In the repository root, create a new file named as `.dockerignore` and copy-paste everything from your `.gitignore`. Just like with `.gitignore`, `.dockerignore` tells Docker what files and folders to ignore when containerizing the app. 

---

- 📁 Repository Root Directory
    - 📁 app
        - 📁 node_modules
        - 📁 public
        - 📁 src
            - 📁 components
            - 📁 pages
            - 📎 App.css
            - 📎 App.tsx
            - 📎 index.css
            - 📎 main.tsx
        - 📎 package.json
        - 📎 vite.config.cjs
        - and more …
    - 📁 server
        - 📁 node_modules
        - 📎 server.js
        - 📎 package.json
        - 📎 package-lock.json `or` yarn.lock
    - 📎 .dockerignore
    - 📎 .gitignore
    - 📎 Dockerfile

---

```bash
# .dockerignore

# Logs
logs
*.log
npm-debug.log*
yarn-debug.log*
yarn-error.log*
pnpm-debug.log*
lerna-debug.log*

node_modules
dist
dist-ssr
*.local

# Editor directories and files
.vscode/*
!.vscode/extensions.json
.idea
.DS_Store
*.suo
*.ntvs*
*.njsproj
*.sln
*.sw?
```

# 4. Setup Railway

Now, it’s time to link your repository to a Railway project. 

### 4.1. Signup or Login to Railway

Go to [Railway](https://railway.app/) and create an account. If you already have an account, then simply login.

**Make sure to signup with your Github account** if you don’t want to enter credit card information.

### 4.2. Create a new Railway project

In the [Railway dashboard](https://railway.app/dashboard), create a new project by selecting `Empty project` at the bottom. 

![Screenshot 2023-01-21 at 5.25.53 PM.png](HW%20Deploying%20to%20Railway%20c1465c9d0b0540fd8a65df1b5951a7b3/Screenshot_2023-01-21_at_5.25.53_PM.png)

### 4.3. Install the Railway CLI

Next, we’ll want to connect the project we just created to our local code using the CLI.

Refer to the [Getting Started Guide](https://docs.railway.app/getting-started#install-and-link-the-cli) under `Install and Link the CLI`. 

Should be as simple as

```bash
npm install -g @railway/cli
```

### 4.4. Login to the CLI

After installing the CLI, run the following command to login.

```bash
railway login
```

# 5. Deploy to Railway

Now that everything has been setup, we can proceed with deploying the app. 

### 5.1. Link the Railway project

In the repository root where the `Dockerfile`, `app` directory, and `server` directory are located, run the command

```bash
railway link
```

It will open up an interactive prompt where you should select the project that you created in step `4.2.`.

### 5.2. Deploy

You can now press the big red button.

```bash
railway up
```

It will give you a link where you can see the deployment logs as Railway builds the Docker image and starts a new Docker container. This process might take a while. 

It might also error, saying that you are not verified. Simply go to the link the error message provides and verify your account. If you signed up with Github, that would just be agreeing to not use their servers for crypto mining and other dumb things. Otherwise you might also have to add a credit card. Once you’ve finished verification, just rerun the command, and it’s off to the races.

### 5.3. Add a domain

Now return to your Railway project dashboard in your browser and navigate to your project.

Railway does not automatically assign a domain to your project, so you will have to do an additional step to access your app on the web. 

When your project has finished deploying (status has changed from `building` → `active`), click on it to access the project settings. Then navigate to `Settings` and find the `Domain` section. You might need to wait a few minutes after deployment for Railway to verify that your project can be assigned a domain. Once you find it, you should also see a button to `autogenerate domain`. You should see a url generated for your project once you click on it.

Below is an image of an already deployed and later deleted project, but most things should look the same.

![Screenshot 2023-01-21 at 5.39.15 PM.png](HW%20Deploying%20to%20Railway%20c1465c9d0b0540fd8a65df1b5951a7b3/Screenshot_2023-01-21_at_5.39.15_PM.png)

It might take Railway a few minutes to setup the domain. Once it’s ready however, you’ll be able to click on the url and view your app, hopefully fully functional, on the web 🎉.

### 5.4. Final Notes

Congrats, you just deployed a decoupled React app to Railway using Docker and Fastify! Unless you upgraded your plan, your account should currently be on the free plan, giving you 500 hours of uptime every month. Your app will likely go to sleep if there is inactivity for some time, and will occasionally have to wake up again once you try to re-access it. 

If you want 100% uptime, you will either have to upgrade your plan with money or use another provider that also requires money but may also provide cheaper rates.