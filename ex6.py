
N = int(input("Digite um número inteiro não-negativo: "))


resultado = 1

contador = N


while contador > 1:
    resultado *= contador
    contador -= 1


print(f"{N}! = {resultado}")