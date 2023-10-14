import utils.mongo
import json


class Office:
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
        return Office.converter(list(utils.mongo.client['vtb']['officces'].find({

        })))

    @staticmethod
    def get_by_id(id):
        return Office.converter(list(utils.mongo.client['vtb']['officces'].find({
            '_id': utils.mongo.ObjectId(id)
        })))

    @staticmethod
    def get_rko():
        return Office.converter(list(utils.mongo.client['vtb']['officces'].find({
            'rko': 'есть РКО'
        })))

    @staticmethod
    def get_kep():
        return Office.converter(list(utils.mongo.client['vtb']['officces'].find({
            'kep': True
        })))
