def findLogicFunction(resp,circuit, porta):
    list = resp + porta.tipo+"("
    for entradaPorta in porta.entradas:
        for entradaCircuito in circuit.entradas:
            if entradaPorta.valor == entradaCircuito.nome:
                list += entradaCircuito.nome + ","
    for entradaPorta in porta.entradas:
        list2 = []
        for portaCircuito in circuit.portas:
            if entradaPorta.valor == portaCircuito.saída.nome:
                list2.append(findLogicFunction("", circuit, portaCircuito)+",")
        for r in list2:
            list += r
    list += ")"
    list = list.replace(",)", ")")
    return list


# This function generate the string expression of the circuit
def generateLogicFunctions(circuit):
    resps = []
    for saída in circuit.saídas:
        for entrada in circuit.entradas:
            if saída.valor == entrada.nome:
                return saída.nome + " = " + entrada.nome
        for porta in circuit.portas:
            if saída.valor == porta.saída.nome:
                resps.append(saída.nome+" = "+findLogicFunction("", circuit, porta))
    return resps