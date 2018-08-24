def write(circuitName, expression, df):
    f = open(circuitName+"Resultado", "w")
    for s in expression:
        f.write(s+"\n")
    f.close()
    with open(circuitName+"Resultado", 'a') as f:
        df.to_string(f, header=True, index=False)
    df.to_csv(circuitName+".csv", index=False, sep=' ')

