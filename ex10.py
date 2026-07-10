import os
from os import system
from os import system

mensagens = []

nome = input('Nome: ')

while True:

    #Limpando Terminal
    system('cls')

    if len(mensagens) > 0:
        for m in mensagens:
            print(m['nome'], '-', m['texto'])


    print('______________________')

    #Obtendo texto
    texto = input('Mensagem: ')
    if texto == 'fim':
        break

    #Adicionando mensagem na lista
    mensagens.append({
        'nome': nome,
        'texto': texto
    })





