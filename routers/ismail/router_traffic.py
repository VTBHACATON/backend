from fastapi import APIRouter, HTTPException
from utils import database

testRouter = APIRouter(prefix="/test/ismail")


@testRouter.get("/traffic", tags=["traffic"])
async def traffic_routing(id: int | None = None, town: str | None = None):
    traffics = database.get_points_traffic()

    if id:
        for date in traffics:
            if date.id == id:
                print(date)
                return date.to_dict()

        raise HTTPException(status_code=404, detail="Item not found")
    elif town:
        towns = []
        for date in traffics:
            if date.town == town:
                towns.append(date.to_dict())
        return towns

    return [traffic.to_dict() for traffic in traffics]
