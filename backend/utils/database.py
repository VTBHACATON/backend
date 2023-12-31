import json
from pony.orm import select
import os
from pony.orm import *
from pony import orm

from dotenv import load_dotenv

load_dotenv()

db = Database()


class Traffics(db.Entity):
    id = PrimaryKey(str)
    town = Required(str)
    traffic = Required(int)
    max = Required(int)


class SalePoint(db.Entity):
    salePointName = Required(str)
    address = Required(str)
    status = Required(str)
    openHours = Required(Json)
    rko = Required(str)
    openHoursIndividual = Required(Json)
    officeType = Optional(str)
    salePointFormat = Optional(str)
    suoAvailability = Optional(str)
    hasRamp = Optional(str)
    latitude = Required(float)
    longitude = Required(float)
    metroStation = Optional(str)
    distance = Required(int)
    kep = Required(bool)
    myBranch = Required(bool)


db.bind(provider='postgres',
        user=os.environ['DATABASE_USER'],
        password=os.environ['DATABASE_PASS'],
        host=os.environ['DATABASE_HOST'],
        database=os.environ['DATABASE_NAME'],
        port=os.environ['DATABASE_PORT'])

db.generate_mapping(create_tables=True)

# region CRUD Traffics

@db_session
def register_point_traffic(id: str, town: str,
                           traffic: int, max: int):

    if not Traffics.exists(id=id):
        user = Traffics(id=id, town=town,
                        traffic=traffic, max=max)
        flush()
        return user
    else:
        print(f'Point traffic {id} exists')


@db_session
def get_point_traffic(id: str):
    return Traffics.get(id=id)


@db_session
def get_points_traffic(attribute=None):
    if attribute:
        return select(getattr(p, attribute) for p in Traffics)[:]
    else:
        return select(p for p in Traffics)[:]


@db_session
def update_point_traffic(id: str, town: str = None,
                         traffic: int = None, max: int = None):

    user_to_update = Traffics.get(id=id)
    if town:
        user_to_update.town = town
    if traffic:
        user_to_update.traffic = traffic
    if max:
        user_to_update.max = max

# endregion
