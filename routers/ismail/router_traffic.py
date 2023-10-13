from fastapi import APIRouter, HTTPException

testRouter = APIRouter(prefix="/test/ismail")


database = [
    {
        "id": 12345678,
        "town": "Moscow",
        "traffic": 321
    },
    {
        "id": 87654321,
        "town": "Surgut",
        "traffic": 123
    }
]

@testRouter.get("/traffic", tags=["traffic"])
async def testRout(id: int | None = None, town: str | None = None):

    if id:
        for date in database:
            if date["id"] == id:
                return date

        raise HTTPException(status_code=404, detail="Item not found")
    elif town:
        towns = []
        for date in database:
            if date["town"] == town:
                towns.append(date)
        return towns

    return database


# /api/v1 - документация

# /api/v1/traffic - json файл со всеми отделениями {
#     "id": 12345678,
#     "town": "Moscow",
#     "traffic": 205
# }

# /api/v1/traffic?id=12345678
# /api/v1/traffic?town=Moscow
