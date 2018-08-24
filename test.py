from itertools import combinations
from pandas import read_csv

a = list(combinations(['a','b','c'], 2))
print(a)

df1 = read_csv("circuito1.csv",sep=' ')
df2 = read_csv("circuito1Defeito.csv",sep=' ')

if df2.equals(df1):
    print("Foi")
else:
    print("Cague")