#!/usr/bin/env python3
"""
comentario
"""


def update_topics(mongo_collection, name, topics):
    """Function"""

    query: dict = {'name': name}
    mongo_collection.update_many(query, {"$set": {"topics": topics}})
