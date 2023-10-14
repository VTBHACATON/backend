from pymongo import MongoClient

from dotenv import load_dotenv

load_dotenv()

client = MongoClient('mongodb+srv://root:FNaF1122@npk.waicn9k.mongodb.net/')
filter = {}
result = client['vtb']['officces'].find(
    filter=filter
)
