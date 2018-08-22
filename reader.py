import json
from collections import namedtuple


def readJson(circuitName):
    with open(circuitName, 'r') as f:
        strJson = json.dumps(json.load(f))
    def _json_object_hook(d):
        return namedtuple('object', d.keys())(*d.values())
    def json2obj(data):
        return json.loads(data, object_hook=_json_object_hook)

    return json2obj(strJson)


def getEditableJson(circuitName):
    with open('circuito1', 'r') as f:
        with open("circuito1Teste.json", "w") as f2:
            data = json.load(f)
            return data