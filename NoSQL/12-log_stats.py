#!/usr/bin/env python3
"""
comentario
"""


def schools_by_topic(mongo_collection, topic):
    """Function"""

    mongo_collection.find({"topics": topic})
