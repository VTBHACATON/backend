from fastapi import APIRouter
from .router_office import office_routers
from .router_maps import map_routers

AzreilRouters = APIRouter(prefix="/api/v1")
AzreilRouters.include_router(office_routers)
AzreilRouters.include_router(map_routers)
