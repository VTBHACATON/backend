from fastapi import APIRouter
from fastapi.responses import HTMLResponse
import folium
from services.azreil.map import map_routing

map_routers = APIRouter(prefix="/map")


@map_routers.get("/", tags=["maps"])
def get_map(lat: float, lon: float, zoom: int = 12):
    m = folium.Map(location=(float(lat),
                             float(lon)), zoom_start=int(zoom))

    return HTMLResponse(m.get_root().render(), 200)


@map_routers.get("/to", tags=["maps"])
def get_map(lat1: float, lon1: float, lat2: float, lon2: float, zoom: int = 12):
    m = folium.Map(location=(float(lat1),
                             float(lon1)), zoom_start=int(zoom))
    points = map_routing(lon1=lon1, lat1=lat1,
                         lon2=lon2, lat2=lat2)
    folium.PolyLine(points, color="red", weight=100).add_to(m)
    return HTMLResponse(m.get_root().render(), 200)


@map_routers.get("/points", tags=["maps"])
def get_map(lat1: float, lon1: float, zoom: int = 12):
    m = folium.Map(location=(float(lat1),
                             float(lon1)), zoom_start=int(zoom))
    return HTMLResponse(m.get_root().render(), 200)
