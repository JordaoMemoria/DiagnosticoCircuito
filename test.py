import json
import os

with open('circuito1', 'r') as f:
    with open("circuito1Teste.json","w") as f2:
        data = json.load(f)
        data["portas"][1]["nome"] = "AAAAAAAAAAAAA"
        print(data["portas"][1]["nome"])

#os.remove("cacatuaTest.json")
