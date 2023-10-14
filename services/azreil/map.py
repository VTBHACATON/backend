import requests


def map_routing(lat1: float, lon1: float, lat2: float, lon2: float):
    url = f"https://api.openrouteservice.org/v2/directions/driving-car?api_key=5b3ce3597851110001cf6248136ac4fa068443dbb2db0b962104d594&start={lon1},{lat1}&end={lon2},{lat2}"
    res = requests.get(url)
    data = res.json()
    geometry = data["features"][0]["geometry"]["coordinates"]

    return geometry
