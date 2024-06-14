vel = int(input('informe a velocidade do veiculo em km/h '))
mt = (vel - 80)*20.00
if vel > 80:
    print(f'voce foi multado por exceder a velocidade, transitando a {vel}km/h sendo a velocidade maxima permitida nesta via de 80km/h, a mulda sera no valor de R${mt:.2f} considerando a velocidade exedente\n Dirija com cuidado!')
else:
    print('velocidade permitida.\n respeite o transito, respeite a vida!')