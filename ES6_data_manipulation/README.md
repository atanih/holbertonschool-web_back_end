# ES6 data manipulation

Proyecto de Holberton School — manipulación de datos con ES6: `map`, `filter`, `reduce`, typed arrays y las estructuras `Set`, `Map` y `WeakMap`.

## Objetivos

- Usar `map`, `filter` y `reduce` sobre arrays
- Entender los typed arrays (`ArrayBuffer`, `DataView`)
- Usar las estructuras `Set`, `Map` y `WeakMap`

## Requisitos

- Ubuntu 20.04 LTS, Node.js 20.x, npm 9.x
- Todos los archivos terminan con una línea nueva
- Extensión `.js`
- Tests con Jest (`npm run test`), lint con ESLint (`npm run check-lint`)
- Todo junto: `npm run full-test`
- Todas las funciones deben exportarse

## Instalación

```bash
npm install
```

## Archivos

| Archivo | Función | Concepto |
|---|---|---|
| `0-get_list_students.js` | `getListStudents` | Array de objetos |
| `1-get_list_student_ids.js` | `getListStudentIds` | `map` |
| `2-get_students_by_loc.js` | `getStudentsByLocation` | `filter` |
| `3-get_ids_sum.js` | `getStudentIdsSum` | `reduce` |
| `4-update_grade_by_city.js` | `updateStudentGradeByCity` | `filter` + `map` |
| `5-typed_arrays.js` | `createInt8TypedArray` | `ArrayBuffer` / `DataView` |
| `6-set.js` | `setFromArray` | `Set` |
| `7-has_array_values.js` | `hasValuesFromArray` | `Set.has` |
| `8-clean_set.js` | `cleanSet` | Recorrido de `Set` |
| `9-groceries_list.js` | `groceriesList` | `Map` |
| `10-update_uniq_items.js` | `updateUniqueItems` | Mutación de `Map` |
| `100-weak.js` | `weakMap`, `queryAPI` | `WeakMap` |

## Uso

```bash
npm run dev 0-main.js
npm run test
npm run full-test
```

## Autor

Antonio Torres
