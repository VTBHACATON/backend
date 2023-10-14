
# from backend.services.azreil.office import Office
# from backend.utils import database
# from random import randint
# towns = Office.get_all()
# townss = {'Подольск,', 'Мытищи,', 'Химки,', 'Долгопрудный,', 'Солнечногорск,',
#           'Moскoвский,', 'Пушкино,', 'Дедовск,', 'Лобня,', 'Железнодорожный,',
#           'Красногорск,', 'Люберцы,', 'Москва', 'Дзержинский,', 'Фрязино,',
#           'Раменское,', 'Черноголовка,', 'Москва,', 'Балашиха,', 'Звенигород,',
#           'Реутов,', 'Видное,', 'Жуковский,', 'Одинцово,', 'Истра,', 'Щелково,',
#           'Королев,', 'Ивантеевка,', 'Домодедово,'}

# print(towns[1]["id"])
# for town in towns:
#     adr: list = town["address"].split()
#     try:
#         num = adr.index("г.")
#         gorod = adr[num+1][0:-1]
#         database.register_point_traffic(
#             town["id"], gorod, randint(0, 400), randint(200, 600))
#     except:
#         pass
# print(townss)
