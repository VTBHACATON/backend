from fastapi import APIRouter, HTTPException
from utils import database

testRouter = APIRouter(prefix="/test/ismail")


@testRouter.get("/traffic", tags=["traffic"])
async def testRout(id: int | None = None, town: str | None = None):
    traffics = database.get_points_traffic()

    if id:
        for date in traffics:
            if date["id"] == id:
                return date

        raise HTTPException(status_code=404, detail="Item not found")
    elif town:
        towns = []
        for date in traffics:
            if date["town"] == town:
                towns.append(date)
        return towns

    return traffics


# /api/v1 - документация

# /api/v1/traffic - json файл со всеми отделениями {
#     "id": 12345678,
#     "town": "Moscow",
#     "traffic": 205
# }

# /api/v1/traffic?id=12345678
# /api/v1/traffic?town=Moscow
