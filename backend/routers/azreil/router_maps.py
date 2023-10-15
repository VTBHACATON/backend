from fastapi import APIRouter
from fastapi.responses import HTMLResponse
import folium
from backend.services.azreil.map import map_routing
from backend.services.azreil.officeController import OfficeController
map_routers = APIRouter(prefix="/map")


@map_routers.get("/", tags=["maps"])
def get_map(lat: float, lon: float, zoom: int = 12):
    """ Получиение карты

    Args:

        - lat (float): долгота

        - lon (float): широта

        - zoom (int, optional): увелечение. Defaults to 12.

    Returns:

        _type_: карта в формате HTML
    """
    m = folium.Map(location=(float(lat),
                             float(lon)), zoom_start=int(zoom))

    return HTMLResponse(m.get_root().render().replace(
        "</script>", 'document.querySelector("div.leaflet-control-container > div.leaflet-bottom.leaflet-right").remove()</script>'), 200)


@map_routers.get("/points", tags=["maps"])
def get_map_points(lat: float, lon: float, zoom: int = 12, kep: bool = False, rko: bool = False):
    m = folium.Map(location=(float(lat),
                             float(lon)), zoom_start=int(zoom))
    if kep or rko:
        pointers = OfficeController.get_rko_kep()
    elif kep:
        pointers = OfficeController.get_kep()
    elif rko:
        pointers = OfficeController.get_rko()
    else:
        pointers = OfficeController.get_all()

    for i in pointers:
        text = "Время работы:\n"
        for j in i["openHours"]:
            text += f"{j['days']}:\n{j['hours']}\n"
        folium.Marker(location=[float(i["latitude"]), float(
            i["longitude"])], fill_color='#43d9de', radius=8, tooltip=i["salePointName"], popup=text,
            icon=folium.CustomIcon(
                "backend/src/image/png/2023-10-14 15.51.07.jpg")
        ).add_to(m)

    return HTMLResponse(m.get_root().render().replace(
        "</script>", 'document.querySelector("div.leaflet-control-container > div.leaflet-bottom.leaflet-right").remove()</script>'), 200)
