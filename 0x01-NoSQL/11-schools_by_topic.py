#!/usr/bin/env python3
"""
Returns the list of schools having a specific topic.
"""

import pymongo

def schools_by_topic(mongo_collection, topic):
    """Returns the list of schools in the collection that have the specified
topic."""
    result = mongo_collection.find({'topics': topic})
    return [doc for doc in result]
