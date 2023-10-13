from fastapi import APIRouter

testRouter = APIRouter(prefix="/test/ismail")


@testRouter.get("/", tags=["test", "ismail"])
async def testRout():
    return {
        "test": 2
    }
