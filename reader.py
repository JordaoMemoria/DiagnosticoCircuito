import json
from collections import namedtuple
from pandas import read_csv

def readJson(circuitName):
    with open(circuitName, 'r') as f:
        strJson = json.dumps(json.load(f))
    def _json_object_hook(d):
        return namedtuple('object', d.keys())(*d.values())
    def json2obj(data):
        return json.loads(data, object_hook=_json_object_hook)

    return json2obj(strJson)


def getEditableJson(circuitName):
    with open(circuitName, 'r') as f:
        data = json.load(f)
        return data

def readTables(circuitName):
    dfOk = read_csv(circuitName+".csv", sep=' ')
    dfDefeito = read_csv(circuitName+"Defeito.csv", sep=' ')
    return dfOk, dfDefeito