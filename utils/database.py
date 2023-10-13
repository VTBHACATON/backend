import os
from pony.orm import *
from pony import orm

from dotenv import load_dotenv

load_dotenv()

db = Database()


class Traffics(db.Entity):
    id = PrimaryKey(int, size=64)
    town = Required(str)
    traffic = Required(int)
    max = Required(int)


db.bind(provider='postgres',
        user=os.environ['DATABASE_USER'],
        password=os.environ['DATABASE_PASS'],
        host=os.environ['DATABASE_HOST'],
        database=os.environ['DATABASE_NAME'],
        port=os.environ['DATABASE_PORT'])
db.generate_mapping(create_tables=True)

# region CRUD Traffics

@db_session
def register_point_traffic(id: int, town: str,
                           traffic: int, max: int):

    if not Traffics.exists(id=id):
        user = Traffics(id=id, town=town,
                        traffic=traffic, max=max)
        flush()
        return user
    else:
        print(f'Point traffic {id} exists')


@db_session
def get_point_traffic(id: int):
    return Traffics.get(id=id)


@db_session
def get_points_traffic(attribute=None):
    if attribute:
        return select(getattr(p, attribute) for p in Traffics)[:]
    else:
        return select(p for p in Traffics)[:]


@db_session
def update_point_traffic(id: int, town: str = None,
                         traffic: int = None, max: int = None):

    user_to_update = Traffics.get(id=id)
    if town:
        user_to_update.town = town
    if traffic:
        user_to_update.traffic = traffic
    if max:
        user_to_update.max = max

# endregion


register_point_traffic(1, "Moscow", 203, 250)
register_point_traffic(2, "Saint-Peterburg", 124, 200)
register_point_traffic(3, "Moscow", 194, 400)
register_point_traffic(4, "Surgut", 32, 110)