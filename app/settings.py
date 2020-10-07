MONGO_URI = "mongodb+srv://user:password@server/collection?retryWrites=true"

books_schema = {
        'title' : {
            'type': 'string',
            'maxlength': 20,
            'required': True
        }
}

books = {
    'resource_methods': ['POST', 'GET'],
    'item_methods': ['GET', 'PATCH', 'DELETE'],
    'schema': books_schema
}

DOMAIN = {
    'books': books
}
