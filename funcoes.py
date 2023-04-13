# Definindo funções em Python
# Para criar funções em python, utiliza-se do comando def(definition)
# Seguido do nome da fução e o parênteses. Que pode ter ou não Argumentos.
# Em Phyton não é necessário definir o tipo de retorno
def soma(valores):
    x = 0
    for i in valores:
        x = x + i
    return x

def media(valores):
    x = 0
    for i in valores:
        x = x + i
    return x / len(valores)

def maior(valores):
    x = valores[0]
    for i in range(1,len(valores)):
        if(i > x):
            x = i
    return x