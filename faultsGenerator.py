from itertools import combinations
from reader import getEditableJson
from tableGenerator import generateTable

class Fault:
    nome = None
    defeito = None

    def __init__(self, nome, defeito):
        self.nome = nome
        self.defeito = defeito


def generateListOfFaults(circuit):
    l = []
    faults = []
    for e in circuit.entradas:
        l.append(e.nome)
    for s in circuit.saídas:
        l.append(s.nome)
    for p in circuit.portas:
        for e in p.entradas:
            l.append(e.nome)
        l.append(p.saída.nome)
    for f in l:
        fault1 = Fault(f, 1)
        fault0 = Fault(f, 0)
        faults.append(fault0)
        faults.append(fault1)
    fault1 = list(combinations(faults, 1))
    fault2 = list(combinations(faults, 2))
    toRemove = []
    for i in range(len(fault2)):
        f0, f1 = fault2[i]
        if f0.nome == f1.nome:
            toRemove.append(fault2[i])
    for f in toRemove:
        fault2.remove(f)
    fault3 = list(combinations(faults, 3))
    toRemove = []
    for i in range(len(fault3)):
        f0, f1, f2 = fault3[i]
        if f0.nome == f1.nome or f0.nome == f2.nome or f1.nome == f2.nome:
            toRemove.append(fault3[i])
    for f in toRemove:
        fault3.remove(f)

    return fault1, fault2, fault3

def updateFault(circuit, fault):
    for entrada in circuit["entradas"]:
        if fault.nome == entrada["nome"]:
            entrada["defeito"] = fault.defeito
            entrada["valor"] = fault.defeito
            return circuit
    for saida in circuit["saídas"]:
        if fault.nome == saida["nome"]:
            saida["defeito"] = fault.defeito
            saida["valor"] = fault.defeito
            return circuit
    for porta in circuit["portas"]:
        for entrada in porta["entradas"]:
            if fault.nome == entrada["nome"]:
                entrada["defeito"] = fault.defeito
                entrada["valor"] = fault.defeito
                return circuit
        if fault.nome == porta["saída"]["nome"]:
            porta["saída"]["valor"] = fault.defeito
            porta["saída"]["defeito"] = fault.defeito
            return circuit

def checkFaults(circuitName, faults, dfDefeito):
    diagList = []
    for faultTuple in faults:
        circuit = getEditableJson(circuitName)
        for f in faultTuple:
            circuit = updateFault(circuit, f)
        df = generateTable(circuit)
        if df.equals(dfDefeito):
            diagList.append(faultTuple)
    return diagList