from fastapi import APIRouter

from .router_traffic import testRouter
IsmailRouters = APIRouter(prefix="/api/v1")
IsmailRouters.include_router(testRouter)
