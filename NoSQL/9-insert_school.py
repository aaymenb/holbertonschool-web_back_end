#!/usr/bin/env python3
import pymongo


def insert_school(mongo_collection, **kwargs):
    """insert the new document"""
    return mongo_collection.insert_one(kwargs).inserted_id
