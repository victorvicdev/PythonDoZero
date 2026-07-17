
def minha_funcao(v1, v2):
    return v1 + v2

while True:
    v1 = int(input('Primeiro valor: '))
    v2 = int(input('Segundo valor: '))

    resposta = minha_funcao(v1, v2)


    print('A soma dos valore ', v1,'+',v2 , '=', resposta)
