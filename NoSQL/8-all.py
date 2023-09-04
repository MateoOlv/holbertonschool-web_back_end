#!/usr/bin/env python3
"""
comentario
"""
import pymongo


def list_all(mongo_collection):
    """Function"""
    output = mongo_collection.find()
    return output
