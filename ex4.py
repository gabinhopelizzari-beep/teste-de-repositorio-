numero_secreto = 20
tentativas = 1 
chute = int(input("chute um numero de 1 a 100"))
while chute!= numero_secreto:
    if chute  <numero_secreto:
        print('muito baixo')
    elif chute >numero_secreto:
        print('muito alto')

tentativas+= 2
chute = int(input("Tente novamente: "))
