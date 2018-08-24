import itertools
from pandas import DataFrame

def simulateLogic(resps, typePort):
    if typePort == "AND":
        for r in resps:
            if r == 0:
                return 0
        return 1
    elif typePort == "OR":
        for r in resps:
            if r == 1:
                return 1
        return 0
    elif typePort == "NAND":
        for r in resps:
            if r == 0:
                return 1
        return 0
    elif typePort == "NOR":
        for r in resps:
            if r == 1:
                return 0
        return 1
    elif typePort == "NOT":
        if len(resps) != 1:
            raise Exception
        if resps[0] == 0:
            return 1
        else:
            return 0
    elif typePort == "XOR":
        count = 0
        for r in resps:
            if r == 1:
                count +=1
        if count == 1:
            return 1
        else:
            return 0

def getResult(circuit, porta):
    if porta["saída"]["valor"] != None:
        return porta["saída"]["valor"]
    resps = []
    for entradaPorta in porta["entradas"]:
        if entradaPorta["valor"] == 1 or entradaPorta["valor"] == 0:
            resps.append(entradaPorta["valor"])
        else:
            for entradaCircuito in circuit["entradas"]:
                if entradaCircuito["nome"] == entradaPorta["valor"]:
                    resps.append(entradaCircuito["valor"])
                    continue
            for portaCircuit in circuit["portas"]:
                if portaCircuit["saída"]["nome"] == entradaPorta["valor"]:
                    resps.append(getResult(circuit, portaCircuit))
    return simulateLogic(resps,porta["tipo"])


def getResults(circuit):
    lenSaidas = len(circuit["saídas"])
    i = 0
    results = []
    while i < lenSaidas:
        if circuit["saídas"][i]["valor"] == 0 or circuit["saídas"][i]["valor"] == 1:
            results.append(circuit["saídas"][i]["valor"])
        else:
            for porta in circuit["portas"]:
                if circuit["saídas"][i]["valor"] == porta["saída"]["nome"]:
                    results.append(getResult(circuit, porta))
        i += 1
    return results


def generateTable(circuit):
    lenEntradas = len(circuit["entradas"])
    sequence = ["".join(seq) for seq in itertools.product("01", repeat=lenEntradas)]
    table = []
    cols = []
    i = 0
    while i < lenEntradas:
        cols.append(circuit["entradas"][i]["nome"])
        i += 1
    for s in circuit["saídas"]:
        cols.append(s["nome"])
    for s in sequence:
        line = []
        i = 0
        while i < lenEntradas:
            if circuit["entradas"][i]["defeito"] == None:
                circuit["entradas"][i]["valor"] = int(s[i])
            line.append(int(s[i]))
            i += 1
        results = getResults(circuit)
        for r in results:
            line.append(r)
        table.append(line)
    df = DataFrame(table,columns=cols)
    return df

def applyFaults(circuit):
    for entrada in circuit["entradas"]:
        if entrada["defeito"] != None:
            entrada["valor"] = entrada["defeito"]
    for saida in circuit["saídas"]:
        if saida["defeito"] != None:
            saida["valor"] = saida["defeito"]
    for porta in circuit["portas"]:
        entradas = porta["entradas"]
        for entrada in entradas:
            if entrada["defeito"] != None:
                entrada["valor"] = entrada["defeito"]
        if porta["saída"]["defeito"] != None:
            porta["saída"]["valor"] = porta["saída"]["defeito"]
    return circuit