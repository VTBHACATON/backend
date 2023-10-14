from fastapi import APIRouter

from backend.services.azreil.office import Office


office_routers = APIRouter(prefix="/office")


@office_routers.get("/", tags=["office"])
def get_all_office(id: str = None, kep: bool = False, rko: bool = False):
    result = None
    if id:
        result = Office.get_by_id(id)
    elif kep:
        result = Office.get_kep()
    elif rko:
        result = Office.get_rko()
    else:
        result = Office.get_all()
    return result
