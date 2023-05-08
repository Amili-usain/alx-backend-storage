#!/usr/bin/env python3
"""
Inserts a new document into a collection based on kwargs.

Args:
    mongo_collection: A pymongo collection object representing the collection
to insert into.
    **kwargs: Keyword arguments representing the fields and values of the
document to be inserted.

Returns:
    The _id of the inserted document.
"""

import pymongo


def insert_school(mongo_collection, **kwargs):
    """Inserts a new document into the specified MongoDB collection using the
provided keyword arguments."""
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
