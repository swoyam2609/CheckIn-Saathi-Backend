import dependencies.config as config
from pymongo import MongoClient

client = MongoClient(config.mongourl)
db = client.get_database('test-frontend')
