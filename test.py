
from services.azreil.office import Office

towns = Office.get_all()

print(towns[1]["id"])
for town in towns:
    print(town["address"])