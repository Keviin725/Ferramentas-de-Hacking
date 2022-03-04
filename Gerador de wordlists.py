import itertools

string = input("Strings a serem permutadas")

resultado = itertools.permutations(string, len(string))# 3- nr de permutacoes ou tamanho da string

for i in resultado:
    print(''.join(i))
