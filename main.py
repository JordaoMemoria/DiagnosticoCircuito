from reader import readJson
from reader import getEditableJson
from logicFunctionGenerator import generateLogicFunctions
from tableGenerator import generateTable

# circuit = readJson("circuito1")
# resp = generateLogicFunctions(circuit)
# print(resp)
circuit = getEditableJson("circuit1")
generateTable(circuit)