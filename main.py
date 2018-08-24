from reader import readJson
from reader import getEditableJson
from reader import readTables
from logicFunctionGenerator import generateLogicFunctions
from tableGenerator import generateTable
from tableGenerator import applyFaults
from writter import write
from faultsGenerator import generateListOfFaults
from faultsGenerator import checkFaults

def createTables():
    circuitName = "circuito1"
    circuit = readJson(circuitName)
    expression = generateLogicFunctions(circuit)
    circuit = getEditableJson(circuitName)
    circuit = applyFaults(circuit)
    df = generateTable(circuit)
    write(circuitName, expression, df)

#createTables()

def diagnostic():
    circuitName = "circuito1"
    circuit = readJson(circuitName)
    dfOk, dfDefeito = readTables(circuitName)
    circuit = readJson(circuitName)
    faults1, faults2, faults3 = generateListOfFaults(circuit)
    diagList = checkFaults(circuitName, faults3, dfDefeito)
    for fTuple in diagList:
        f0, f1, f2 = fTuple
        print(f0.nome, f0.defeito, f1.nome, f1.defeito, f2.nome, f2.defeito)
    print(len(diagList))

diagnostic()
