#!/usr/bin/env python3
"""
comentario
"""


def schools_by_topic(mongo_collection, topic):
    """Function"""

    query: dict = {'topic': topic}
    schools: list = []
    for school in mongo_collection.find(query):
        school.append(school)
    return school
