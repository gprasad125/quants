# Project Start To Finish (wip)

---

## Philosophy

This guide is a walkthrough on the steps towards developing your own application using a basic React SPA as an example.

It seeks to provide a specific example that can be used to base your project on while also providing resources for you to explore alternatives.

Do recognize that nothing mentioned is absolute and that there are numerous paths towards approaching an app, none exactly better than the other.

If you at any point feel confused, know that professional web developers feel the same as well, and definitely do not feel afraid or ashamed to ask others for help or clarification. 

Otherwise I hope this guide provides all the necessary knowledge you need to kickstart your journey and wish you all the best in your endeavors. 

---

# 1. Preparation 🛠️

You’re probably prepared already for the journey ahead, but just in case, refreshing on the basics might be helpful.

### New Quest

<aside>
⚡ Check out the `Relevant Resources`.

</aside>

### Relevant Resources

[What is “F*********rontend”?*********](What%20is%20%E2%80%9CFrontend%E2%80%9D%203cbb9d72b2664787892cb5f53f39d8d0.md)

[Building Blocks of a Webpage](Building%20Blocks%20of%20a%20Webpage%20b2fca7bc3f874cdeb889f45c1f4bad03.md)

[Frontend Lingo](Frontend%20Lingo%200a3ed29c3ab04445b694a6a1c0e7e6bf.md)

# 2. Choosing the UI and Style tools 🤔

Using a UI (User Interface) Framework is not always necessary, but it will very likely be helpful for creating a robust project. The same can be said for style libraries and tools.

There are many different frameworks and libraries that you can use for your project. For the purposes of providing a step-by-step guide, we will be using the `React` and `Tailwind` frameworks to build an example project called `Hello World`.

While following the example is recommended, definitely feel free to use a different UI Framework, rendering strategy, meta framework, style library, etc. if you want to challenge yourself, though you will have to figure things out on your own using its documentation and other online resources.

### New Quest

<aside>
⚡ Research what UI and Styling tools to use for your project.

</aside>

### Share

<aside>
💬 Which tools did you end up picking? Why? Share your findings with your team members!

</aside>

### Relevant Resources

[UI Frameworks (& Libraries)](UI%20Frameworks%20(&%20Libraries)%203aaf9b90aa4c4502976d7301e62aa00c.md)

[Styling Libraries, Enhancements, and Frameworks](Styling%20Libraries,%20Enhancements,%20and%20Frameworks%2074f2891ae0374e8484bf2b44897b9a60.md)

# 3. Picking a Tool Chain 🔗

By now you should have picked a UI Framework to use (`React`, `Svelte`, etc.). However, you will also need to decide on the tool chain that can compile your app into a production-ready build. 

On top of deciding the tool chain, you should also consider the `rendering strategy` for your app, since each tool chain supports different rendering strategies.

The `Hello World` example will use `Vite` as its tool chain and `SPA` as its rendering strategy. 

As mentioned above, you can choose to use different tool chains and rendering strategies if you are feeling up for the challenge.

### New Quest

<aside>
⚡ Research what Tool Chain to use for your project. Discuss your findings with your team for additional input.

</aside>

### Relevant Resources

General

[Bundlers](Bundlers%20047be33254414f979c2a69644f31cd3f.md)

[Package Managers](Package%20Managers%20b0916dd86bd94e059d2bc9a85762debc.md)

[Tool Chains](Tool%20Chains%202f46434c9de34ab0a0f4f77e49722562.md)

[Rendering Strategies in Production](Rendering%20Strategies%20in%20Production%203b572635aef440bdad55cc0e5fe807ba.md)

React-Specific

[Picking The Right Starting Tool](React%20fc189d56df0542f9a379e5aec2decf50/Picking%20The%20Right%20Starting%20Tool%20022e728ecf84472e8f35c9b1edb76497.md)

# 4. Initializing the Project ⛳

Now that you have done the research and picked the tools for your project, you can now proceed towards setting up the boilerplate code for the frontend.

Most tool chains should have `npm` commands that automatically setup a fresh new project for you. 

Below is `Hello World`'s setup example.

[HW: Project Init](Hello%20World%20Project%205afa3b4b87ad4a0d91bb25d7c264be8a/HW%20Project%20Init%20f1a36f72c79a496485c8c4f1fc0ea508.md)

### New Quest

<aside>
⚡ Reference your tool chain’s documentation to initialize the frontend code.

</aside>

### Share

<aside>
💬 Showcase the initial project to your team! Take a screenshot or recording of the default app working in your browser and demo it to your team!

</aside>

### Relevant Resources

[Typescript](Typescript%2010a0ab594b08456c922e77ba6017a00c.md)

# 5. Adding in your Style Tool and Linter ⚙️

With the boilerplate setup, you now have a basic app that you could deploy right now if you wanted to. Of course it probably wouldn’t do much, but it’s a start 🙃.

Before you go and develop however, you’ll likely also want to add on your styling tools and a **linter** to keep your code nice and tidy as well. 

Below is `Hello World`'s setup for Tailwind and ESLint.

[HW: Adding Tailwind](Hello%20World%20Project%205afa3b4b87ad4a0d91bb25d7c264be8a/HW%20Adding%20Tailwind%20e9620f1d7c0e42ec8e17756a4f1f6d5c.md)

[HW: Adding ESLint](Hello%20World%20Project%205afa3b4b87ad4a0d91bb25d7c264be8a/HW%20Adding%20ESLint%20f43800236d794c108cbe8507b3b482bd.md)

### New Quest

<aside>
⚡ Setup the additional tools you will need for the frontend.

</aside>

### Share

<aside>
💬 Now that you’ve added in a style framework or library, spend a minute or two personalizing the default app! Try making a dark-mode or light-mode version, or maybe something as simple as changing all text to forest green. Don’t forget to share the final art piece with your team 😊

</aside>

### Relevant Resources

[Linters](Linters%2062ce6b956bba411ca7a74b27a218dedf.md)

Previously mentioned:

# 5.5.  Design Addendum 🎨

Frontend encompasses a broad focus on connecting a user to a service or application. One major part of that is designing the interactions, appearance, or in other words, the overall experience of the product you are providing. Thinking in Design is more than just finding pretty colors but also optimizing how your app will be used, communicating with users, and much more that could make or break the user experience. A functional app is un-functional if no one wants to use it. 

While it is certainly passable to have a bare-bone interface for this project, perhaps some default Bootstrap styling, making a decent effort towards the presentation and user experience of your application can go a long way towards attracting new users and wow-ing others. 

The relevant resources lists some basic design guides and overviews. If you plan to go into design or have some interest, you should definitely go through the Design Crash Course as well, which has many more in-depth guides and walkthroughs. 

[Design Crash Course](https://www.notion.so/Design-Crash-Course-db079f982fdc49fd8c1426eb2e94b889)

### New Quest

<aside>
⚡ Think about how you want the final App to look like. Maybe draft some rough sketches using tools like [Figma](https://www.figma.com/) 🖌️ to share with your team.

</aside>

### Relevant Resources

[What is “*********Design”?*********](https://www.notion.so/What-is-Design-b69e88c903a141c0941e2ca3122884f6)

[Figma](https://www.notion.so/Figma-cd852eef84004350a54f01e9b19927bc)

[Organization - Design Crash Course](https://www.notion.so/Organization-Design-Crash-Course-88b4bcae7ab34ee1b3478283e3491936)

# 6. Developing your App 💻

Now that you have everything setup, it’s time to develop your app 🎉. This will likely the most time-consuming and difficult stage of the journey. You will likely face many challenges, but you will surely learn just as much as you will suffer. It is by *****doing***** that most people learn their development skills, and it is likely the same for you as well. 

Always remember to communicate in your respective Discord channel for updates, blockers, difficulties, and more. If you’re faced with a difficult challenge, try breaking it into smaller chunks and searching online for solutions. If you tried your best but still couldn’t make progress, definitely don’t be afraid to reach out to other people and seek assistance. 

Below is a basic example of adding pages and a router to the `Hello World` app (part 1) and communicating with a backend API server (part 2). `Relevant Resources` also lists various guides and docs for you to reference in a rough order of most important to least important. 

[HW: Development pt. 1](Hello%20World%20Project%205afa3b4b87ad4a0d91bb25d7c264be8a/HW%20Development%20pt%201%202afc11f4a984473ab49d030d85656d33.md)

[HW: Development pt. 2](Hello%20World%20Project%205afa3b4b87ad4a0d91bb25d7c264be8a/HW%20Development%20pt%202%20ce94cc0df03a4f4f91a1f9033434c9e4.md)

While you’re at it, create a local Git repository from your Hello World project, and push it to your remote repository on GitHub. Be sure to add .gitignore file to your project following the Git Crash Course. Once you’ve added, committed, and pushed your changes, take a screenshot of your GitHub repo and send it in your team discord channel!

[Git & Github Crash Course](https://www.notion.so/Git-Github-Crash-Course-95777f5bc4ee487a9f60efb3f49681a5)

### New Quest

<aside>
⚡ Time to develop your app!

</aside>

### Share

<aside>
💬 Showcase the app you made from the Hello World tutorial with your team! Maybe try a funny prompt for the summarizer 👀

</aside>

### Relevant Resources

[Javascript](Javascript%206e61d398f17b43e584f695deba264d67.md)

[CSS](CSS%2051aa170070ff46ab83c9a541f8c31667.md)

[HTML](HTML%203b2c4b0784d04fa8ad2c33f31166d819.md)

[APIs](APIs%20158298affaed40d384a0ccaceb4015dd.md)

[React](React%20fc189d56df0542f9a379e5aec2decf50.md)

[MVC, Decoupling, & More](MVC,%20Decoupling,%20&%20More%209066c9e64d244d40bd5ace0420e71eb0.md)

[Security & Secrets](Security%20&%20Secrets%2066ff6a6b783543a69343ea3d9d5f1fdf.md)

[Validation](Validation%20cc69f343a71446bdb4da3aa03dde0b07.md)

[Browser DevTools](Browser%20DevTools%203767fa2fc82e42f8b76eae40ea40f9ef.md)

[Postman](Postman%20e92d1cab5b4941e1bf3ceee124b2eb3a.md)

[Browser Support](Browser%20Support%2011794a107f19469ea2aac46c95264e94.md)

[Basic SEO and Accessibility](Basic%20SEO%20and%20Accessibility%20386a7dd1548f45c99c3b41acb6e86138.md)

[Page Load & Compression](Page%20Load%20&%20Compression%20202f52883a2847ce973fa021a35db216.md)

[OGP (Open Graph Protocol)](OGP%20(Open%20Graph%20Protocol)%20f57bcc62bb934b7390bba7c413c9ee25.md)

# 7. Building your code 🏗️

It’s amazing to see that you’ve finished developing your app and are prepared to deploy it 🙂! Before you do so however, you’ll likely want to compile all of your code into a production-ready bundle to make sure everything works properly. Definitely refer to your toolchain’s documentation for instructions. Usually there should already be a `build` npm command in package.json that you can just call. 

As always the walkthrough is linked below for the `Hello World` example:

[HW: Code Building](Hello%20World%20Project%205afa3b4b87ad4a0d91bb25d7c264be8a/HW%20Code%20Building%2059e2d40f915445d28a2a424a0715615d.md)

### New Quest

<aside>
⚡ Build your app!

</aside>

### Relevant Resources

Previously mentioned:

# 8. Deploying your App 🚀

You’re at the final step of your journey. After hours and hours of development, you’re now prepared to share your app to the world. 

For the `Hello World` app, we’ll be deploying it in a `decoupled` setup to `Railway` using a `Node` `Docker` image with `Fastify` as the frontend server. 

Otherwise for `SPA`s, you simply want to have a server that serves the build directory files as static assets and a catch-all GET endpoint that sends `index.html` . 

Deployment becomes more tricky if you use a different rendering strategy like `SSG` or `SSR` where there are more requirements.  

[HW: Deploying to Railway](Hello%20World%20Project%205afa3b4b87ad4a0d91bb25d7c264be8a/HW%20Deploying%20to%20Railway%20c1465c9d0b0540fd8a65df1b5951a7b3.md)

### New Quest

<aside>
⚡ Deploy your app!

</aside>

### Share

<aside>
💬 You’ve done it! You’ve just started, developed, and deployed an app from A to Z😎 Share the link with your teammates and have them try it out on the web!

</aside>

### Relevant Resources

[Deploying to Production (wip)](Deploying%20to%20Production%20(wip)%20f232352aad154860a89083fb5f6799a6.md)