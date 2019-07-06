import json


def deserialize_json(object_type, data):
    if object_type:
        return object_type(data)
    return data
