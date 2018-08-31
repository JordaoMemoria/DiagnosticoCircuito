from reader import readJson
from reader import getEditableJson
from reader import readTables
from logicFunctionGenerator import generateLogicFunctions
from tableGenerator import generateTable
from tableGenerator import applyFaults
from writter import write
from writter import writeFault
from writter import writeDiag
from faultsGenerator import generateListOfFaults
from faultsGenerator import checkFaults
from faultsGenerator import updateFault
from random import randint

def createTables():
    circuitName = "circuito1Defeito"
    circuit = readJson(circuitName)
    expression = generateLogicFunctions(circuit)
    circuit = getEditableJson(circuitName)
    circuit = applyFaults(circuit)
    df = generateTable(circuit)
    write(circuitName, expression, df)

#createTables()

def diagnostic():
    circuitName = "circuito1"
    dfOk, dfDefeito = readTables(circuitName)
    circuit = readJson(circuitName)
    faults1, faults2, faults3 = generateListOfFaults(circuit)
    diagList = checkFaults(circuitName, faults1, dfDefeito)
    for fTuple in diagList:
        f0, = fTuple
        print(f0.nome, f0.defeito)
    print(len(diagList))

#diagnostic()

def main():
    #circuitList = ["circuito2", "circuito3", "circuito4"]
    circuitList = ["circuito5"]
    for circuitName in circuitList:
        print(circuitName)
        circuit = getEditableJson(circuitName)
        df = generateTable(circuit)
        circuit = readJson(circuitName)
        expression = generateLogicFunctions(circuit)
        write(circuitName, expression, df)
        faults1, faults2, faults3 = generateListOfFaults(circuit)
        faultsList = [faults1, faults2, faults3]
        for faults in faultsList:
            for i in range(10):
                print(i)
                errorNumber = randint(0, len(faults)-1)
                faultTuple = faults[errorNumber]
                circuit = getEditableJson(circuitName)
                for f in faultTuple:
                    print(f.nome, f.defeito)
                    circuit = updateFault(circuit,f)
                dfDefeito = generateTable(circuit)
                writeFault(circuitName, i, faultTuple, dfDefeito)
                diagList1 = checkFaults(circuitName, faults1, dfDefeito)
                diagList2 = checkFaults(circuitName, faults2, dfDefeito)
                diagList3 = checkFaults(circuitName, faults3, dfDefeito)
                writeDiag(circuitName, len(diagList1), len(diagList2), len(diagList3))

main()
