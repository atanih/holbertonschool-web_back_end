# NoSQL

## Description
This project covers NoSQL concepts using MongoDB: what NoSQL means, the
difference between SQL and NoSQL, ACID, document storage, NoSQL types,
benefits of a NoSQL database, and how to query, insert, update, and
delete information from a NoSQL database using both the Mongo shell and
PyMongo (Python 3.9 / PyMongo 4.8.0).

## Requirements
- All Mongo shell files interpreted on Ubuntu 20.04 LTS using MongoDB
  (version 4.4)
- All Mongo shell files end with a new line and start with a comment
- All Python files interpreted/compiled on Ubuntu 20.04 LTS using
  python3 (version 3.9) and PyMongo (version 4.8.0)
- All Python files start with `#!/usr/bin/env python3` and end with a
  new line
- Code follows pycodestyle (version 2.5.*)
- All modules and functions have documentation
- Code is not executed when imported

## Files

| File | Description |
| --- | --- |
| `0-list_databases` | Lists all databases in MongoDB |
| `1-use_or_create_database` | Creates or uses the database `my_db` |
| `2-insert` | Inserts a document in the collection `school` |
| `3-all` | Lists all documents in the collection `school` |
| `4-match` | Lists all documents with `name="Holberton school"` |
| `5-count` | Displays the number of documents in the collection `school` |
| `6-update` | Adds an `address` attribute to documents matching `name="Holberton school"` |
| `7-delete` | Deletes all documents with `name="Holberton school"` |
| `8-all.py` | Python function that lists all documents in a collection |
| `9-insert_school.py` | Python function that inserts a new document in a collection |
| `10-update_topics.py` | Python function that changes all topics of a school document |
| `11-schools_by_topic.py` | Python function that returns the list of schools having a specific topic |
| `12-log_stats.py` | Python script that provides stats about Nginx logs stored in MongoDB |

## Author
Antonio Torres Alvarado
