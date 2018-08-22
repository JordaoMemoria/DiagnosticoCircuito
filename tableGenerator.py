import itertools

def generateTable(circuit):
    sequence = ["".join(seq) for seq in itertools.product("01", repeat=len(circuit["entradas"]))]
    for s in sequence:
        print(s)
        i = 0
        while i < len(circuit["entradas"]):
            circuit["entradas"][i]["valor"] = int(s[i])
            i += 1
        print(circuit["entradas"])