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
| 1-block-scoped.js | Block scoping so the conditional doesn't overwrite outer variables |
| 2-arrow.js | Arrow function syntax and lexical `this` |
| 3-default-parameter.js | Default parameter values |
| 4-rest-parameter.js | Rest parameter syntax |
| 5-spread-operator.js | Spread syntax on arrays and strings |
| 6-string-interpolation.js | Template literals instead of string concatenation |
| 7-getBudgetObject.js | Object property value shorthand |
| 8-getBudgetCurrentYear.js | Computed property names |
| 9-getFullBudget.js | ES6 method properties in an object literal |
| 10-loops.js | `for...of` instead of `for...in` |
| 11-createEmployeesObject.js | Build an object keyed by department name |

## Files

| File | Purpose |
|---|---|
| package.json | Dependencies and npm scripts |
| babel.config.js | Babel preset targeting the current Node version |
| .eslintrc.js | ESLint config (airbnb-base + jest plugin) |
