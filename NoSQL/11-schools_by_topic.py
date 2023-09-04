#!/usr/bin/env python3
"""
comentario
"""


def schools_by_topic(mongo_collection, topic):
    """Function"""

    query: dict = {"topics": topic}
    schools: list = []
    for school in mongo_collection.find(query):
        schools.append(school)
    return schools
