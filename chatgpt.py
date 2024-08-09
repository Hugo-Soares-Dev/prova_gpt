num_alunos = int(input('Informe a quantidade de alunos nesta turma? '))

apv = []
rpv = []

soma_media = 0

for i in range(num_alunos):
    nome = input(f'informe nome do aluno {i+1}: ').lower()

    nota1 = float(input('digite a primeira nota: '))
    nota2 = float(input('digite a segunda nota: '))
    nota3 = float(input('digite a terceira nota: '))

    media = (nota1 + nota2 + nota3) / 3

    if media >= 7.0:
        status = 'Aprovado'
        apv.append(nome)

    else:
        status = 'Reprovado'
        rpv.append(nome)  

    print(f'O Aluno {nome}, com as notas: \n prova 1:{nota1} Pts\n prova 2:{nota2} Pts\n prova 3: {nota3} Pts\n obteve a media de {media} pontos, estando {status} nesta materia')  

    soma_media += media  

media_geral = soma_media / num_alunos
print(f'A media geral da turma é de {media_geral:.2}')
print(f'lista de aprovados:\n {', '.join(apv)}')
print(f'lista de reprovados:\n{', '.join(rpv)}')      
    