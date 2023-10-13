from fastapi import APIRouter

testRouter = APIRouter(prefix="/test/azreil")


@testRouter.get("/", tags=["test", "azreil"])
async def testRout():
    return {
        "test": 1
    }
