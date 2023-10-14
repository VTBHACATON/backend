from fastapi import APIRouter, HTTPException
from backend.utils import database

testRouter = APIRouter(prefix="/test/ismail")


@testRouter.get("/traffic", tags=["traffic"])
async def traffic_routing(id: str | None = None, town: str | None = None):
    traffics = database.get_points_traffic()

    if id:
        for date in traffics:
            if date.id == id:
                print(date)
                return date.to_dict()

        raise HTTPException(status_code=404, detail="Id not found")
    elif town:
        towns = []
        for date in traffics:
            if date.town == town:
                towns.append(date.to_dict())
        return towns

    return [traffic.to_dict() for traffic in traffics]


async def calculate_percent(traffic) -> float:
    traffic_data = traffic.to_dict()
    now = traffic_data["traffic"]
    max = traffic_data["max"]
    return round(now * 100 / max, 2)


@testRouter.get("/traffic/rating", tags=["rating"])
async def traffic_rating(id: str | None = None, town: str | None = None):
    traffics = database.get_points_traffic()
    answer = {}

    for traffic in traffics:
        percent = await calculate_percent(traffic)
        answer[traffic.id] = percent

    sorted_answer = dict(sorted(answer.items(), key=lambda item: item[1]))

    if id:
        return {id: sorted_answer.get(id)}

    if town:
        points = [
            {"id": traffic.id, "town": traffic.town, "percent": percent}
            for traffic, percent in zip(traffics, answer.values())
            if traffic.town == town
        ]

        if points:
            return sorted(points, key=lambda item: item["percent"])

        raise HTTPException(status_code=404, detail="Town not found")

    return sorted_answer
