i_a = []

for n in range(3):
    n_a = input('Nome do aluno: ')
    nota = float(input('Nota do aluno: '))
    notaalunos = [ n_a, nota ]
    i_a.append(notaalunos)

print( i_a )
print( 'Ao todo foram registrados ', len(i_a) )
for x in i_a:
    info1 = x[0]
    info2 = x[1]
    print(' O aluno ', info1, 'tirou nota ', info2 )
