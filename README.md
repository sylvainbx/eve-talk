## setup
```bash
pip install --no-cache-dir -r requirements.txt
cd app
python run.py
```
## CURL commands
- get all books
```bash
curl -XGET http://localhost:5000/books
```

- create new book
```bash
curl -XPOST http://localhost:5000/books \
  --header 'content-type: application/json' \
  --data '{"title": "Le capital", "author": "Karl Marx", "published_at": "Mon, 14 Oct 1867 00:00:00 GMT"}'
```
```bash
# some books exemples:
## {"title": "Guerre et Paix", "author": "Léon Tolstoï", "published_at": "Sun, 01 Jan 1865 00:00:00 GMT"}
## {"title": "Les Misérables", "author": "Victor Hugo", "published_at": "Wed, 01 Jan 1862 00:00:00 GMT"}
## {"title": "Les Misérables", "author": "Victor Hugo", "published_at": "Wed, 01 Jan 1862 00:00:00 GMT"}
## {"title": "Le Petit Prince", "author": "Antoine de Saint-Exupéry", "published_at": "Fri, 01 Jan 1943 00:00:00 GMT"}
```

- create new library
```bash
curl  -XPOST http://localhost:5000/libraries \
  --header 'content-type: application/json' \
  --data '{"name": "Bibliothèque d'\''Étude et du Patrimoine", "coordinates": { "type": "Point", "coordinates": [45.185468, 5.730911] }}'
```

```bash
# some libraries exemples:
## {"name": "Bibliothèque Universitaire de Médecine et Pharmacie", "coordinates": { "type": "Point", "coordinates": [45.202010, 5.744917] }}
```

- get all libraries
```bash
curl -XGET http://localhost:5000/libraries
```

