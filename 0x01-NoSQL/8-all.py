#!/usr/bin/env python3
"""
Lists all documents in a collection using pymongo.
"""

import pymongo


def list_all(mongo_collection):
    """
    Returns a list of all documents in the given pymongo collection.

    Args:
        mongo_collection (pymongo.collection.Collection): A pymongo collection
object.

    Returns:
        list: A list of dictionaries, where each dictionary represents a
document in the collection.
              Returns an empty list if no documents are found.
    """
    if not mongo_collection:
        return []

    docs = mongo_collection.find()
    return [doc for doc in docs]
