soma = 0 
quant = 0
chave = 0 

while True:
    nun = int(input('digite um numero inteiro '))
    soma += nun
    quant += 1
    if nun != chave:
        print('continue...')
    if nun == chave:
      quant -= 1 # ola Professor, entedi que o "zero" seria pra interromper o loop, entao o tirei da contagem da media aritimentica"
      break
print(f'foram iseridos {quant} numeros, a soma de todos os numeros corresponde a {soma}, e a media é de {soma / quant} ')