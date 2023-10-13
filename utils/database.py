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


class OpenHours(db.Entity):
    days = Required(str)
    hours = Required(str)


class OpenHoursIndividual(db.Entity):
    days = Required(str)
    hours = Required(str)


class Office(db.Entity):
    salePointName = Required(str)
    address = Required(str)
    status = Required(str)
    openHours = Required(OpenHours)
    rko = Required(str)
    openHoursIndividual = Required(OpenHoursIndividual)
    officeType = Required(str)
    salePointFormat = Required(str)
    suoAvailability = Required(str)
    hasRamp = Required(str)
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

# region CRUD office
# Создание


@db_session
def create_office(sale_point_name, address, status, open_hours, rko,
                  open_hours_individual, office_type, sale_point_format,
                  suo_availability, has_ramp, latitude, longitude, metro_station,
                  distance, kep, my_branch):
    office = Office(salePointName=sale_point_name, address=address, status=status,
                    openHours=open_hours, rko=rko,
                    openHoursIndividual=open_hours_individual, officeType=office_type,
                    salePointFormat=sale_point_format, suoAvailability=suo_availability,
                    hasRamp=has_ramp, latitude=latitude, longitude=longitude,
                    metroStation=metro_station, distance=distance, kep=kep,
                    myBranch=my_branch)

# Чтение


@db_session
def get_office(id):
    return Office[id]

# Обновление


@db_session
def update_office(id, sale_point_name=None, address=None, status=None,
                  open_hours=None, rko=None, open_hours_individual=None,
                  office_type=None, sale_point_format=None, suo_availability=None,
                  has_ramp=None, latitude=None, longitude=None, metro_station=None,
                  distance=None, kep=None, my_branch=None):
    office = Office[id]
    if sale_point_name is not None:
        office.salePointName = sale_point_name
    if address is not None:
        office.address = address
    # и т.д. для остальных полей

# Удаление


@db_session
def delete_office(id):
    Office[id].delete()

# endregion
