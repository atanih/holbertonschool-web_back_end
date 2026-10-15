# ES6 Promises

Proyecto de Holberton School — promesas en JavaScript: `then`, `resolve`, `catch`, `finally`, los métodos estáticos del objeto `Promise`, `throw`/`try` y `async`/`await`.

## Objetivos

- Promesas: qué son, cómo y por qué
- Usar los métodos `then`, `resolve`, `catch`
- Usar todos los métodos del objeto `Promise`
- `throw` / `try`
- El operador `await` y las funciones `async`

## Requisitos

- Ubuntu 20.04 LTS, Node.js 20.x, npm 9.x
- Todos los archivos terminan con una línea nueva
- Extensión `.js`
- Tests con Jest (`npm run test`), lint con ESLint
- Todas las funciones deben exportarse

## Instalación

```bash
npm install
```

## Archivos

| Archivo | Función | Concepto |
|---|---|---|
| `utils.js` | `uploadPhoto`, `createUser` | Helpers provistos por el proyecto |
| `0-promise.js` | `getResponseFromAPI` | Crear una Promise |
| `1-promise.js` | `getFullResponseFromAPI` | `resolve` / `reject` |
| `2-then.js` | `handleResponseFromAPI` | `then` / `catch` / `finally` |
| `3-all.js` | `handleProfileSignup` | `Promise.all` |
| `4-user-promise.js` | `signUpUser` | `Promise.resolve` |
| `5-photo-reject.js` | `uploadPhoto` | `Promise.reject` |
| `6-final-user.js` | `handleProfileSignup` | `Promise.allSettled` |
| `7-load_balancer.js` | `loadBalancer` | `Promise.race` |
| `8-try.js` | `divideFunction` | `throw` |
| `9-try.js` | `guardrail` | `try` / `catch` / `finally` |
| `100-await.js` | `asyncUploadUser` | `async` / `await` |

## Uso

```bash
npm run dev 0-main.js
npm run test
npm run full-test
```

## Autor

Antonio Torres
