import pymongo

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
    'schema': library_schema,
    'mongo_indexes': {
        'coordinates_2dsphere': ([('coordinates', pymongo.GEOSPHERE)], {"sparse": True}),
    }
}

booksaround = {
    'resource_methods': ['GET'],
    'datasource': {
        'source': 'libraries',
        'aggregation': {
            'pipeline': [
                {"$geoNear": {
                    "near": {
                        "type": "Point",
                        "coordinates": "$center"
                    },
                    "key": "coordinates",
                    "spherical": True,
                    "distanceField": "distance",
                    "maxDistance": "$distance",
                }},
                {"$lookup": {
                    "from": "books",
                    "localField": "_id",
                    "foreignField": "library",
                    "as": "books"
                }}
            ]
        }
    }
}

MONGO_URI = "mongodb://suez-hw-mongo:27017/biblio?retryWrites=true"
DOMAIN = {
    'books': books,
    'libraries': libraries,
    'books-around': booksaround
}
