from pymongo import MongoClient
from bson import ObjectId
import os
from dotenv import get_key

client = MongoClient(get_key(".env", "MONGO_CONN"))
