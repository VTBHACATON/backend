import os
from pony.orm import *
from pony import orm

from dotenv import load_dotenv
load_dotenv()

db = Database()
db.bind(provider='postgres', user=os.environ['DATABASE_USER'], password=os.environ['DATABASE_PASS'],
        host=os.environ['DATABASE_HOST'], database=os.environ['DATABASE_DB'], port=os.environ['DATABASE_PORT'])


class Person(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    age = Required(int)


db.generate_mapping(create_tables=True)
