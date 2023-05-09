#!/usr/bin/env python3
"""
A function that returns all students sorted by their average score.
"""


def top_students(mongo_collection):
    """
    Returns all students sorted by their average score.

    Args:
        mongo_collection (pymongo.collection.Collection): A pymongo collection
object representing a MongoDB collection containing student data.

    Returns:
        pymongo.command_cursor.CommandCursor: A cursor object containing the
student documents, sorted by average score in descending order.
    """
    return mongo_collection.aggregate([
        {
            "$project":
                {
                    "name": "$name",
                    "averageScore": {"$avg": "$topics.score"}
                }
        },
        {
            "$sort":
                {
                    "averageScore": -1
                }
        }
    ])
