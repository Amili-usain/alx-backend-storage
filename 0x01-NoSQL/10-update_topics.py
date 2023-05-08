#!/usr/bin/env python3
"""
Changes all topics of a school document based on the name.
"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """Updates the topics of a school document with the specified name. """
    result = mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
    return result.modified_count
