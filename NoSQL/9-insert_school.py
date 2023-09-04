#!/usr/bin/env python3
"""
comentario
"""


def insert_school(mongo_collection, **kwargs):
    """Function"""
    output = mongo_collection.insert_one(kwargs)
    return output.inserted_id
