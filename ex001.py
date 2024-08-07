print('Para calcular a soma dos números pares dentro de um intervalo determinado ')
num1 = int(input('Digite o primeiro numero: ')) 
num2  = int(input('Digite o segundo numero: '))
soma = 0
pares = False

for i in range(num1, num2 + 1):
    if i % 2 == 0:
       soma += i 
       pares = True

if pares == True:
    print(f'a soma dos numeros pares dentro do intervalo de {num1} a {num2} é de {soma}')
else:
    print(f'nao foi encontrado numeros pares no intervalo de{num1} a {num2} ')    
        
        
   
