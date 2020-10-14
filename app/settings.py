MONGO_URI = "mongodb://suez-hw-mongo:27017/biblio?retryWrites=true"

books_schema = {
    'title' : {
        'type': 'string',
        'maxlength': 20,
        'required': True
    },
    'author': {
        'type': 'string',
        'required': True
    },
    'published_at': {
        'type': 'datetime',
        'required': True
    },
    'library': {
        'type': 'objectid'
    }
}

library_schema = {
    'name': {
        'type': 'string',
        'required': True
    },
    'coordinates': {
        'type': 'point',
        'required': True
    }
}

books = {
    'resource_methods': ['POST', 'GET'],
    'item_methods': ['GET', 'PATCH', 'DELETE'],
    'schema': books_schema
}

libraries = {
  'resource_methods': ['POST', 'GET'],
  'item_methods': ['GET', 'PATCH', 'DELETE'],
  'schema': library_schema
}

DOMAIN = {
    'books': books,
    'libraries': libraries
}
