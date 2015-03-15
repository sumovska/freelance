import json


class JsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj, 'isoformat'):
            return obj.isoformat()
        if hasattr(obj, 'as_dict'):
            return obj.as_dict()
        return super(JsonEncoder, self).default(obj)
