from random import randint
numero_secreto = randint(1, 10)

tentativa_max = 3
tentativa = 0

while tentativa != numero_secreto and tentativa_max > 0:
    tentativa_max -= 1
    tentativa = int(input('tente adivinhar qual o numero secreto: '))
    if tentativa != numero_secreto:
       print(f'Voce ainda tem {tentativa_max} tentativas')
if tentativa == numero_secreto:
    print('Você acertou o numero secreto!!!')
else:
    print(f'suas tentativas acabaram, o numero secreto era {numero_secreto}')           