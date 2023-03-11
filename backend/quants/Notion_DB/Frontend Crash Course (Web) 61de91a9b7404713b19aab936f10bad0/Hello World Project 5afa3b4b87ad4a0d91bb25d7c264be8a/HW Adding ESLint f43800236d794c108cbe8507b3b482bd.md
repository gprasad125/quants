# HW: Adding ESLint

> Referencing [https://eslint.org/docs/latest/use/getting-started](https://eslint.org/docs/latest/use/getting-started)
> 

---

# Interactive setup tool

ESLint has a package that specifically helps you setup ESLint for your project.

```bash
npm init @eslint/config
```

Once you run it, it should prompt you to install a package, before showing an interactive menu to decide how you would like to use ESLint. 

Answer accordingly. Ideally commit your current changes to `git` before adding in ESLint in case you need to revert changes and choose another option.  

Below are some of the recommended answers for specific questions. Questions may change based on the options you pick. If you ever become unsatisfied with your choices, feel free to delete `.eslintrc.cjs` that is created at the end and repeat this process again to start fresh. 

### 1. How would you like to use ESLint?

Any option is fine here. 

If you’re fine with following an opinionated, standardized guideline, pick “check syntax, find problems, and enforce”. **We recommend this option when starting out.**

Otherwise select “check syntax and find problems” if you want more freedom in formatting your code and prefer to spend less time debugging arbitrary syntax. 

<aside>
📌 If you choose to have ESLint enforce code style (third option), it will also prompt:
`How would you like to define a style for your project?`
Pick `Use a popular style guide`. 

Then it will ask you to pick a style guide to follow. There is no correct answer here, you are merely deciding which arbitrary rulesets to follow. Picking `Airbnb` or `Standard` are likely safe bets for now.

</aside>

### 2. What type of modules does your project use?

Select `Javascript Modules`

### 3. Which framework does your project use?

Select `React`

### 4. Where does your code run?

Select `browser`

### 5. What format do you want your config file to be in?

Select `JavaScript`

# Final Setup

Once you’ve finished answering the setup tool questions, it should install the necessary dependencies, create a `.eslintrc.cjs` file, and install all the necessary dependencies. However, there are a few steps you still need to do. 

First, create a npm command to run the linter by modifying `package.json`:

```json
// package.json

{
	// ...
	"scripts": {
    "dev": "vite",
    "build": "tsc && vite build",
    "preview": "vite preview",
    "lint": "eslint ./src --ext .js,.jsx,.ts,.tsx" // add this
  },
	// ...
}
```

Now, you can run the linter using npm or yarn in the root directory:

```bash
# npm
npm run lint

# yarn
yarn lint
```

You might come across some errors (of the linter running, not errors that the linter detects) that require some additional steps. Right below are some specific ones you might see. Otherwise, if you see a screen that looks like this

![Screenshot 2023-01-28 at 2.34.40 PM.png](HW%20Adding%20ESLint%20f43800236d794c108cbe8507b3b482bd/Screenshot_2023-01-28_at_2.34.40_PM.png)

then you are good to proceed to the next section. 

### 1. Unexpected token <

This lint error is likely due to the linter not being properly configured to parse JSX syntax. Add the following in `.eslintrc.cjs` to fix it.

```jsx
module.exports = {
	// ...
	parserOptions: {
    // ...
    ecmaFeatures: { // add this config option
      jsx: true // set parse jsx to true
    },
		// ...
  },
	// ...
}
```

### 2. Error while loading rule '@typescript-eslint/dot-notation’

This error might come up if your project uses Typescript. To fix it, you’ll have to point ESLint to your typescript config file in `.eslintrc.cjs`:

```jsx
module.exports = {
	// ...
	parserOptions: {
    // ...
    project: ['tsconfig.json'] // add this config option
		// ...
  },
	// ...
}
```

# Configuration

Under `rules` is where you will be adding in extra rules or overriding existing ones. 

Refer to [documentation](https://eslint.org/docs/latest/use/configure/rules) on how to configure rules.

Refer to the [rules list](https://eslint.org/docs/latest/rules/) on all possible lint rules.

Below is an example configuration to make all indents 4 spaces and semi-colons required:

```jsx
module.exports = {
	// ...
	rules: {
    'indent': ['warn', 4],
    'semi': ['warn', 'always']
  },
	// ...
}
```

# Automatic Fixing

Most basic lint rules also allow you to automatically fix the syntax issues. To do this, you run ESLint with the `--fix` flag. 

Using the npm command you made previously, it would just be running the command like so:

```bash
# npm
npm run lint -- --fix

# yarn
yarn lint --fix
```

You can also make it into a new npm command:

```json
// package.json

{
	// ...
	"scripts": {
    // ...
    "lint": "eslint ./src --ext .js,.jsx,.ts,.tsx",
		"lint:fix": "eslint ./src --ext .js,.jsx,.ts,.tsx --fix"
  },
	// ...
}
```

```bash
# npm
npm run lint:fix

# yarn
yarn lint:fix
```

After running the linter in fix mode, you might still have this error remaining:

![Screenshot 2023-01-28 at 2.41.48 PM.png](HW%20Adding%20ESLint%20f43800236d794c108cbe8507b3b482bd/Screenshot_2023-01-28_at_2.41.48_PM.png)

If you see different errors, then you’ll likely need to look into those by yourself and decide whether to fix it or to ignore it. Usually just looking up the specific rule (search `react/react-in-jsx-scope` in Google in this case) should lead you to the right docs. 

For `react/react-in-jsx-scope`, the docs are [located here](https://github.com/jsx-eslint/eslint-plugin-react/blob/master/docs/rules/react-in-jsx-scope.md). In short, it requires us to add `import React` to the top of every file that uses JSX. However, we don’t actually need to do that with Vite, since importing it once in `main.jsx` (or `.tsx` with Typescript) is enough. 

As a result, we want to tell ESLint to ignore this rule. To do so, simply add the following to `.eslintrc.cjs`:

```jsx
module.exports = {
    // ...
    rules: {
				// ...
				"react/react-in-jsx-scope": 'off' // add this
    }
}
```

Now, when we run the linter again, we should no longer see it anymore. 

![Screenshot 2023-01-28 at 2.51.05 PM.png](HW%20Adding%20ESLint%20f43800236d794c108cbe8507b3b482bd/Screenshot_2023-01-28_at_2.51.05_PM.png)

It is perfectly fine to just ignore all rules that raise an issue currently since all the project code at this point is boilerplate and hasn’t been modified much.  

However, it is highly encouraged for you to look into them and decide for yourself whether you would like to see the rule being enforced throughout your project. 

# Conclusion

Now you’ve setup ESLint and can use it to lint your code and enforce correct and consistent syntax. 

Make it a good habit to lint your code before you commit your code to `git`. Professional teams usually have linters automatically run at certain stages in development, such as setting up a Github action on the repository to automatically lint code and run checks on pull requests.