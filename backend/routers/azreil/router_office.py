from fastapi import APIRouter

from backend.services.azreil.officeController import OfficeController


office_routers = APIRouter(prefix="/office")


@office_routers.get("/", tags=["office"])
def get_all_office(id: str = None, kep: bool = False, rko: bool = False, dn: str = None):
    result = None
    if id:
        result = OfficeController.get_by_id(id)
    elif kep:
        result = OfficeController.get_kep()
    elif rko:
        result = OfficeController.get_rko()
    else:
        result = OfficeController.get_all()

    if dn:
        old_result = result
        result = []
        for i in old_result:
            for j in i["openHoursIndividual"]:
                if (j["days"] == dn):
                    if j["hours"] != "выходной":
                        result.append(i)
    return result
