# Matthew Guarino
# Southern New Hampshire Univeristy 
# CS-499 Computer Science Capstone

"""
helpers.py

This module was created to improve modularity, reusability, and performance in the MongoDB dashboard project.
It offloads utility functions that support filtering, sorting, and data structure enhancements from the main dashboard logic.

The following enhancements are for category Two - Data Structures and Algorithms
- Enhancement 1: Query abstraction using the `build_query()` function for clear rescue-type logic.
- Enhancement 2: Added breed indexing with `build_breed_index()` to allow fast in-memory filtering.
- Enhancement 3: Centralized and optimized data filtering and sorting in `filter_and_sort_data()`.
- Enhancement 4: Implemented a Binary Search Tree (BST) to support efficient range queries on age.

"""

import pandas as pd
# Enhancement 1: Modular query builder to support filter types from the dashboard
# Build a MongoDB query based on the rescue type selected in the dashboard
def build_query(filter_type):
    if filter_type == 'Water':
        # Return query for Water Rescue dogs (intact females, specific breeds, age 6mo to 3yrs)
        return {
            "breed": {"$in": ["Labrador Retriever Mix", "Chesa Bay Retr Mix", "Newfoundland"]},
            "sex_upon_outcome": "Intact Female",
            "age_upon_outcome_in_weeks": {"$gte": 26, "$lte": 156}
        }

    elif filter_type == 'Mountain':
        # Return query for Mountain/Wilderness Rescue dogs (intact males, specific breeds)
        return {
            "breed": {"$in": ["German Shepherd", "Alaskan Malamute", "Old English Sheepdog", "Siberian Husky", "Rottweiler"]},
            "sex_upon_outcome": "Intact Male",
            "age_upon_outcome_in_weeks": {"$gte": 26, "$lte": 156}
        }

    elif filter_type == 'Disaster':
        # Return query for Disaster/Tracking dogs (intact males, wider age range)
        return {
            "breed": {"$in": ["Doberman Pinsch", "German Shepherd", "Golden Retriever", "Bloodhound", "Rottweiler"]},
            "sex_upon_outcome": "Intact Male",
            "age_upon_outcome_in_weeks": {"$gte": 20, "$lte": 300}
        }

    elif filter_type in ['All', 'Reset']:
        # General query to retrieve all relevant breeds regardless of sex or age
        return {
            "breed": {"$in": [
                "Labrador Retriever Mix", "Chesapeake Bay Retriever", "Newfoundland Mix", "German Shepherd",
                "Alaskan Malamute", "Old English Sheepdog", "Siberian Husky", "Rottweiler", "Doberman Pinsch",
                "Golden Retriever", "Bloodhound", "Newfoundland/Labrador Retriever", "Labrador Retriever/Newfoundland"
            ]}
        }
    else:
        return {}

# Enhancement 2: Create a breed index to allow in-memory lookup instead of repeated DB queries
# Build an in-memory index (dictionary) for fast filtering by breed
def build_breed_index(df):
    index = {}
    for idx, row in df.iterrows():
        breed = row['breed']
        if breed not in index:
            index[breed] = []
        index[breed].append(idx)  # Store row index for the breed
    return index

# Enhancement 3: Filter and sort data based on UI selections (with support for breed index and sorting)
# Main data processing function that handles filtering and sorting
def filter_and_sort_data(db, query, sort_by=None, breed_index=None, filter_breed=None):
    if filter_breed and breed_index:
        # If using breed index for fast lookup
        df = pd.DataFrame.from_records(db.read({})) # Load full data
        df.drop(columns=['_id'], inplace=True)
        if filter_breed in breed_index:
            df = df.loc[breed_index[filter_breed]]
    else:
        # Standard DB query filtering
        df = pd.DataFrame.from_records(db.read(query))
        if '_id' in df:
            df.drop(columns=['_id'], inplace=True)

    # Convert age to numeric format for proper sorting
    if 'age_upon_outcome_in_weeks' in df:
        df['age_upon_outcome_in_weeks'] = pd.to_numeric(df['age_upon_outcome_in_weeks'], errors='coerce')

    # Apply sort if requested
    if sort_by and sort_by in df.columns:
        df = df[df[sort_by].notnull()]  # Remove NaN values for that column
        if sort_by in ['name', 'breed']:
            df[sort_by] = df[sort_by].astype(str) # Ensure strings for consistent sorting
        df.sort_values(by=sort_by, ascending=True, inplace=True)

    return df

# Node definition for Binary Search Tree (BST)
class BSTNode:
    def __init__(self, key, record):
        self.key = key
        self.records = [record]
        self.left = None
        self.right = None

# Enhancement 4: Binary Search Tree (BST) to support fast range queries by age
# Binary Search Tree class for fast age range queries
class BST:
    def __init__(self):
        self.root = None

    def insert(self, key, record):
        def _insert(node, key, record):
            if node is None:
                return BSTNode(key, record)
            if key < node.key:
                node.left = _insert(node.left, key, record)
            elif key > node.key:
                node.right = _insert(node.right, key, record)
            else:
                node.records.append(record)
            return node
        self.root = _insert(self.root, key, record)

    def range_query(self, low, high):
        result = []
        def _in_order(node):
            if node is None:
                return
            if node.key > low:
                _in_order(node.left)
            if low <= node.key <= high:
                result.extend(node.records)
            if node.key < high:
                _in_order(node.right)
        _in_order(self.root)
        return result

# Build BST using age for efficient range filtering
def build_age_bst(df):
    bst = BST()
    for _, row in df.iterrows():
        age = row.get("age_upon_outcome_in_weeks")
        if pd.notnull(age):
            bst.insert(age, row.to_dict())
    return bst

print("helpers.py loaded successfully")