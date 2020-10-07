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
  --data '{"title": "Le capital"}'
```

