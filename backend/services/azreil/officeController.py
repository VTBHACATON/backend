import backend.utils.mongo
import json


class OfficeController:
    @staticmethod
    def converter(data):
        collection = []
        for i in data:
            collection.append(i)
            collection[-1]["id"] = str(collection[-1]["_id"])
            collection[-1].pop("_id")
        return collection

    @staticmethod
    def get_all():
        return OfficeController.converter(list(backend.utils.mongo.client['vtb']['officces'].find({

        })))

    @staticmethod
    def get_by_id(id):
        return OfficeController.converter(list(backend.utils.mongo.client['vtb']['officces'].find({
            '_id': backend.utils.mongo.ObjectId(id)
        })))

    @staticmethod
    def get_rko():
        return OfficeController.converter(list(backend.utils.mongo.client['vtb']['officces'].find({
            'rko': 'есть РКО'
        })))

    @staticmethod
    def get_kep():
        return OfficeController.converter(list(backend.utils.mongo.client['vtb']['officces'].find({
            'kep': True
        })))

    @staticmethod
    def get_rko_kep():
        return OfficeController.converter(list(backend.utils.mongo.client['vtb']['officces'].find({
            'rko': 'есть РКО',
            'kep': True
        })))
