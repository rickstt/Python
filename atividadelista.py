# Exercício: Crie uma lista com os seguintes números [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# Mostre os intervalos de 1 a 9
# Mostre o intervalo de 8 a 13
# Mostre os números pares
# Mostre os números impares
# Todos os múltiplos de 2, 3 e 4
# Exibir a lista em ordem decrescente

lista = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

print("-----------") 

for l in range(1, 10):
    print("Números em um intervalo de 1 a 9: " + str(lista[l]))

print("-----------") 

for l in range(8, 14):
    print("Números em um intervalo de 8 a 13: " + str(lista[l]))

print("-----------") 

for x in lista:
    if(x % 2 == 0):
        print("Números pares da lista: " + str(x))

print("-----------") 

for x in lista:
    if(x % 2 != 0):
        print("Números impares da lista: " + str(x))

print("-----------") 

for x in lista:
    if(x % 2 == 0):
        print("Números múltiplos de 2: " + str(x))

print("-----------") 

for x in lista:
    if(x % 3 == 0):
        print("Números múltiplos de 3: " + str(x))

print("-----------") 

for x in lista:
    if(x % 4 == 0):
        print("Números múltiplos de 4: " + str(x))

print("-----------") 

for x in range(15, -1, -1):
    print("Números da lista em ordem invertida: " + str(lista[x]))