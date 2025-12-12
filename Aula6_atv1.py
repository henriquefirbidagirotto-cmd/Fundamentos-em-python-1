lista  =  [1,2,34,5,34,34]

quantidade  =  lista.count(34)

for i in range(quantidade):
    indice =  lista.index(34)
    print(indice)
    lista[indice] = 0
    print(lista)