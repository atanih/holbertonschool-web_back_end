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
| 2-hbtn_course.js | Getters, setters, and type validation |
| 3-currency.js | `Currency` class with an instance method |
| 4-pricing.js | Composition with `Currency` and a static method |
| 5-building.js | Abstract class that forces subclasses to override a method |
| 6-sky_high.js | Inheritance with `extends` and `super` |
| 7-airport.js | `Symbol.toStringTag` for the default string description |
| 8-hbtn_class.js | Type casting with `valueOf` and `toString` |
| 9-hoisting.js | Fix hoisting and `this` bugs in a broken file |
| 10-car.js | `Symbol.species` to clone into the right subclass |

## Files

| File | Purpose |
|---|---|
| package.json | Dependencies and npm scripts |
| babel.config.js | Babel preset targeting the current Node version |
| .eslintrc.js | ESLint config (airbnb-base + jest plugin) |
