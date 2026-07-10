notas_alunos = []

cont = 1

while cont <= 5 :
    regis_a = input('RG: ')
    nota = float(input('Nota: '))
    info_a = (regis_a, nota)
    notas_alunos.append(info_a)
    cont += 1

print('Quantidade de notas: ', len(notas_alunos))
print(notas_alunos)
print(notas_alunos[0])
print(notas_alunos[1])