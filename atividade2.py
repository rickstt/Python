n1 = None
n2 = None
n3 = None

n1 = input("Digite o primeiro número: ")
n2 = input("Digite o segundo número: ")
n3 = input("Digite um número real: ")


produto = int(n1) * 2
rs = int(n2) / 2 + produto
print("O dobro do produto do primeiro número com a metado do segundo valor é: " + str(rs))

somaTriplo = int(n1) * 3 + float(n3)
print("A soma triplo do primeiro número com o terceiro é de: " + str(somaTriplo))

terceiroCubo = pow(float(n3),3)
print("O terceiro número elevado ao cubo é: " + str(terceiroCubo))
