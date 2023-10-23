from pymongo import MongoClient
from bson.objectid import ObjectId


class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, user, password, host, port, db, collection):
        # Initialize the MongoDB client with the given parameters
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (user, password, host, port))
        self.database = self.client[db]
        self.collection = self.database[collection]

    def create(self, data):
        if data:
            try:
                self.database.animals.insert_one(data)
                return True
            except Exception as e:
                print(f"An error occurred while inserting data: {e}")        
        return False

    def read(self, search={}):
        try:
            searchResult = self.database.animals.find(search)
            if searchResult.count() > 0:
                return searchResult
            else:
                print("No records found")
                return []
        except Exception as e:
            print(f"An error occurred while searching data: {e}")
            return []

    
    def update(self, search, update_data):
        if search and update_data:
            try:
                update_operation = {"$set": update_data}
                result = self.database.animals.update_many(search, update_operation)
                return result.modified_count
            except Exception as e:
                print(f"An error occurred while updating data: {e}") 
        return 0
    
    def delete(self,search):
        if search:
            try:
                result = self.database.animals.delete_many(search)
                return result.deleted_count
            except Exception as e:
                print(f"An error occurred while deleting data: {e}") 
            return 0
