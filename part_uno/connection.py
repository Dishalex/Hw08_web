#python -m pip install pymongo

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://dishalex:JiAQGB42M7iwRE2J@cluster0.dxmzxl1.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server

client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client.Hw_08_authors

