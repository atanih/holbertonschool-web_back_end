# ES6 Basic

Introduction to ES6 features: `const` and `let` scoping, arrow functions,
default and rest parameters, spread syntax, template literals, object
shorthand, and iterators. Code is transpiled with Babel and linted with
ESLint (airbnb-base).

## Setup

```
npm install
```

## Usage

```
npm run dev 0-main.js     # run a main file through babel-node
npm run test              # run the jest test suite
npm run check-lint        # lint all task files
npm run full-test         # lint + test
```

## Tasks

| File | Description |
|---|---|
| 0-constants.js | `const` and `let` instead of `var` |

## Files

| File | Purpose |
|---|---|
| package.json | Dependencies and npm scripts |
| babel.config.js | Babel preset targeting the current Node version |
| .eslintrc.js | ESLint config (airbnb-base + jest plugin) |
