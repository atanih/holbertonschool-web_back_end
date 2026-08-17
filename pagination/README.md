# Pagination

Proyecto sobre paginación de datasets en Python 3: paginación simple con
parámetros `page`/`page_size`, paginación con metadatos hipermedia (HATEOAS)
y paginación resiliente a borrados.

## Tareas

| Archivo | Descripción |
|---|---|
| 0-simple_helper_function.py | `index_range`: rango de índices para una página |
| 1-simple_pagination.py | `Server.get_page`: paginación simple del dataset |
| 2-hypermedia_pagination.py | `Server.get_hyper`: paginación con metadatos hipermedia |
| 3-hypermedia_del_pagination.py | `Server.get_hyper_index`: paginación resiliente a borrados |

## Dataset

`Popular_Baby_Names.csv`: nombres de bebés populares en Nueva York
(usado como fuente de datos para los ejercicios).