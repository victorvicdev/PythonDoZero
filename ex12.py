# Exercício de Função

flow_caixa = []

def linha():
    print('-' * 30)

linha()
print('@ Fluxo de Caixa')
linha()
print('Digite 1 - Adicionar Receita')
print('Digite 2 - Adicionar Despesa')
print('\n# Digite qualquer outro número para encerrar #\n')
linha()

def add_transacao():
    nome = input('Nome: ')
    valor = float(input('Valor: '))
    flow_caixa.append({
        'nome': nome,
        'valor': valor
    })

while True:

    opcao = int(input('Digite uma opção: '))

    if opcao == 1:
        add_transacao()

    elif opcao == 2:
        add_transacao()

    else:
        break

# Nota Fiscal
total = 0
cont_fc = 1
for fc in flow_caixa:
    print(cont_fc,'Nome: ', fc['nome'], ', valor: R$', fc['valor'])
    total += fc['valor']
    cont_fc += 1

print('Saldo Atual: R$ ', total)