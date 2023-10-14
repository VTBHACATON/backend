
from services.azreil.office import Office

towns = Office.get_all()

for town in towns:
    print(town)