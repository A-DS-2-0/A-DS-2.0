lista =[]
lista2 =[]
def funcao (a):
    if int(a) not in lista:
        lista.append(int(a))
    lista2.append(int(a))
    return lista,lista2
with open(r'txt.txt', 'r') as lista3:
    for a in lista3:
        funcao(a)
    print(funcao(a))
 