lista1 = [2,11,3,6,4,17,10]
lista2 = [1,3,6,12,20,8]
soma = 0

# Exibir os números pares da lista 1 ,2 e somar os números pares
for x in lista1:
    if(x % 2 == 0):
        print("Primeira lista: " + str(x))
        soma = soma + x

for y in lista2:
    if(y % 2 == 0):
        print("Segunda lista: " + str(y))
        soma = soma + y

print("Soma dos números paes de cada lista: " + str(soma))
