# Node JS basic

Proyecto de Holberton School — fundamentos de Node.js, Express, Babel y Nodemon.

## Objetivos

- Ejecutar JavaScript con Node.js
- Usar módulos de Node.js y leer archivos con `fs`
- Usar `process` para argumentos de línea de comandos y variables de entorno
- Crear servidores HTTP con Node.js puro y con Express
- Crear rutas avanzadas con Express
- Usar ES6 con Node.js gracias a Babel-node
- Usar Nodemon para desarrollar más rápido

## Requisitos

- Ubuntu 20.04 LTS, Node.js 20.x
- Todos los archivos terminan con una línea nueva
- Extensión `.js`
- Los tests corren con Jest (`npm run test`) y el lint con ESLint (`npm run check-lint`)
- Todo junto: `npm run full-test`

## Instalación

```bash
npm install
```

## Archivos

| Archivo | Descripción |
|---|---|
| `0-console.js` | `displayMessage` imprime un string en STDOUT |
| `1-stdin.js` | Lee el nombre del usuario desde STDIN |
| `2-read_file.js` | `countStudents` lee la base de datos de forma síncrona |
| `3-read_file_async.js` | `countStudents` asíncrono, devuelve una Promise |
| `4-http.js` | Servidor HTTP con Node.js puro |
| `5-http.js` | Servidor HTTP con ruta `/students` |
| `6-http.js` | Servidor HTTP con Express |
| `7-http.js` | Servidor Express con ruta `/students` |
| `full_server/` | Servidor Express organizado en controllers y routes (ES6) |

## Uso

```bash
node 4-http.js
node 5-http.js database.csv
node 7-http.js database.csv
npm run dev full_server/server.js database.csv
```

## Autor

Antonio Torres
