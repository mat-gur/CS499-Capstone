#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Matthew Guarino
# Southern New Hampshire Univeristy 
# CS-499 Computer Science Capstone

"""
crud.py

This module provides basic CRUD operations for managing records in the 'animals' collection of the AAC MongoDB database.

"""

from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter:

    """
    Handles all Create, Read, Update, and Delete operations
    for the animal shelter MongoDB collection.
    """
    
    def __init__(self, user='aacuser', password='guest123', host='localhost', port=27017, db='AAC', collection='animals'):
        self.client = MongoClient(f'mongodb://{user}:{password}@{host}:{port}/?authSource={db}')
        self.database = self.client["AAC"]
        self.collection = self.database["animals"]
           
    def create(self, data):
        """
        CREATE: Insert a new document or batch of documents into the collection.
        Automatically assigns a 'rec_num' for indexing purposes.
        """
        if data is not None:
            # Makes sure data is a list to allow batch inserations 
            if not isinstance(data, list):
                data = [data]
                
                for item in data:
                    index_num = self.getNextRecordNum()
                    item.update({"rec_num": index_num})
                    item.pop("_id", None)
                    
                    result = self.collection.insert_one(item)
                    
                    if not ObjectId.is_valid(result.inserted_id):
                        return False
                    return True
                else:
                    raise Exception("Nothing to save, data parameter is empty.")
                    
    def read(self, query=None):

        """
        READ: Return documents that match a query. 
        If no query is given, return the first document in the collection.
        """
        if query is not None:
            cursor = self.collection.find(query)
            return list(cursor) 
        else:
            return [self.collection.find_one()]
        
    def update(self, query, new_values, update_many=False):
        """
        UPDATE: Modify one or more documents based on the query.
        """
        if query is not None and new_values is not None:
            if not isinstance(query, dict) or not isinstance(new_values, dict):
                raise TypeError("Query and new_values must be dictionaries.")

        if "_id" in query and isinstance(query["_id"], str):
            query["_id"] = ObjectId(query["_id"])  # Convert string ID to ObjectId

        try:
            if update_many:
                result = self.collection.update_many(query, {"$set": new_values})
            else:
                result = self.collection.update_one(query, {"$set": new_values})

            return result.modified_count  # This returns the number of updated documents
        except Exception as e:
            print(f"Error updating document(s): {e}")
            return 0
        else:
            raise ValueError("Query and new_values parameters cannot be None")
            
    def delete(self, query, delete_many=False):
        """
        DELETE: Remove one or more documents from the collection based on the query.
        """
        if query is not None:
            if not isinstance(query, dict):
                raise TypeError("Query must be a dictionary.")

        if "_id" in query and isinstance(query["_id"], str):
            query["_id"] = ObjectId(query["_id"])  # Convert string ID to ObjectId

        try:
            print("Executing Delete:")
            print("Query:", query)

            if delete_many:
                result = self.collection.delete_many(query)
            else:
                    result = self.collection.delete_one(query)

            print("Deleted Count:", result.deleted_count)  # Debugging output
            return result.deleted_count  # Returns the number of deleted documents

        except Exception as e:
            print(f"Error deleting document(s): {e}")
            return 0

        else:
            raise ValueError("Query parameter cannot be None")
            
    def getNextRecordNum(self):
        """
        Helper: Returns the next available record number by finding the current max.
        """
        last_record = self.collection.find_one(sort=[("rec_num", -1)])
        return last_record["rec_num"] + 1 if last_record else 1
