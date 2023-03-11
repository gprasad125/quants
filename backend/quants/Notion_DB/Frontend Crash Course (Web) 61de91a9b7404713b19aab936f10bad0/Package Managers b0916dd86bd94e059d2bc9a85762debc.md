# Package Managers

> Downloading other people’s code has never been easier
> 

---

Package managers help you find, download, and manage the different dependencies and libraries you need for your project. There are multiple, and this doc will mainly go through the two main ones you will want to look at. 

## Npm

> [https://docs.npmjs.com/downloading-and-installing-node-js-and-npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)
> 

The Node Package Manager is the main package manager used for Javascript purposes. Originally made for the NodeJS server runtime, its applications have long spread to frontend and other purposes. Dependency and other project information is stored in a file named `package.json` in the project root. When installing libraries, npm creates another file called `package-lock.json` which should not be manually edited. Libraries are saved into a folder called `node_modules` in the project root, which should not be committed to git. 

## Yarn

> [https://yarnpkg.com/](https://yarnpkg.com/)
> 

Yarn was made to fix many of Npm’s deficiencies. It is much faster and easier to work with and the is recommended package manager for you to use. If you already have `npm` installed, simply run

```bash
npm install -g yarn
```

to install yarn globally on your device. 

Yarn uses `npm`'s `package.json` as well to manage dependencies. Instead of `package-lock.json`, it creates a `yarn.lock` file. Libraries are still saved into a folder called `node_modules` in the project root, which, again, should not be committed to git. 

# Basic Usage

Below are just some basic usage examples for both `npm` and `yarn`.

### Installing a new package

```bash
# yarn
yarn add <package-name>

# npm
npm install --save <package-name>
# Note: if your npm is up-to-date enough, --save is unnecessary I believe
```

### Uninstalling a package

```bash
# yarn
yarn remove <package-name>

# npm
npm uninstall <package-name>
```

### Installing dependencies from existing `package.json`

```bash
# yarn
yarn install

# npm
npm install
```