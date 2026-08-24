# ES6 Classes

Working with ES6 classes: defining a class, instance methods, getters and
setters, static methods, inheritance with `extends`, and metaprogramming
with symbols. Code is transpiled with Babel, tested with Jest, and linted
with ESLint (airbnb-base).

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
| 0-classroom.js | `ClassRoom` class with a constructor attribute |
| 1-make_classrooms.js | Create an array of `ClassRoom` instances |

## Files

| File | Purpose |
|---|---|
| package.json | Dependencies and npm scripts |
| babel.config.js | Babel preset targeting the current Node version |
| .eslintrc.js | ESLint config (airbnb-base + jest plugin) |
