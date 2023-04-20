from typing import Collection
import json
import pymongo


with open('json/data.json', encoding='utf8') as f:
    dataset = json.load(f)

class Database:
    def __init__(self, database, collection):
        self.connect(database, collection)

    def connect(self, database, collection):
        try:
            connection = "localhost:27017"
            self.clusterConnection = pymongo.MongoClient(
                connection,
                tlsAllowInvalidCertificates=True
            )
            self.db = self.clusterConnection[database]
            self.collection = self.db[collection]
            print("Successfully connected!")
        except Exception as e:
            print(e)

    def dbreset(self):
        try:
            self.db.drop_collection(self.collection)
            self.collection.insert_many(dataset)
            print("Successfully reseted!")
        except Exception as e:
            print(e)