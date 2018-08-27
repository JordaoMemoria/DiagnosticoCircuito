def write(circuitName, expression, df):
    f = open(circuitName+"Resultado", "w")
    for s in expression:
        f.write(s+"\n")
    f.close()
    with open(circuitName+"Resultado", 'a') as f:
        df.to_string(f, header=True, index=False)


def writeFault(circuitName, i, faultTuple, df):
    with open(circuitName + "Resultado", 'a') as f:
        f.write("\nIteração "+str(i+1)+" \n")
        for fa in faultTuple:
            f.write(fa.nome+" preso em "+str(fa.defeito)+"\n")
        df.to_string(f, header=True, index=False)
        f.write("\n")

def writeDiag(circuitName, d1, d2, d3):
    with open(circuitName + "Resultado", 'a') as f:
        f.write("Número de defeitos únicos: "+str(d1)+"\n")
        f.write("Número de dupla de defeitos: "+str(d2)+"\n")
        f.write("Número de trio de defeitos: "+str(d3)+"\n")
        f.write("Diagnóstico encontrado")

