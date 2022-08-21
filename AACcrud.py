from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        self.client = MongoClient('mongodb://%s:%s@127.0.0.1:47424/AAC' % (username, password))
        self.database = self.client['AAC']

# Create method, the C in CRUD.
    def create(self, data):
        if data is not None:
            create = self.database.animals.insert(data)  # data should be dictionary
            if create == 0:
                return False
            else:
                return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")

# Read method, the R in CRUD. 
    def read(self, query):
        queryResult = self.database.animals.find(query,{"_id":False})
        return queryResult
        
                
# Update method, the U in CRUD. 
    def update(self, query, newData):
        if (query is not None) and (newData is not None):
            if query:
                updateResult = self.database.animals.find_and_modify(query, newData)
                if updateResult == 0:
                    raise Excepction("Update failed, because updat parameters are empty")
                else:
                    return updateResult
        else:
            raise Exception("Nothing to search, because query parameter is empty")
               
# Delete method, the D in CRUD
    def delete(self, query):
        if (query is not None):
            if query:
                deleteResult = self.database.animals.find_one_and_delete(query)
                return deleteResult
        else:
            raise Exception("Nothing to delete, because query parameter is empty")


                