"""
POR JOCEL VIANA
14/04/2024

O OBJETIVO DESSA ATIVIDADE É FAZER UMA LISTA DE COMPRAS UTILIZANDO LISTAS.
O USUÁRIO DEVE TER A POSSIBILIDADE DE INSERIR, APAGAR E LISTAR OS ITENS DA LISTA.
NÃO PERMITIRÁ QUE O PROGRAMA QUEBRE CASO OCORRA ERROS, OU SEJA, TODAS AS EXCEÇÕES SERÃO TRATADAS.
"""
import os
lista_compras = []

while True:
    print('Selecione uma opção:')
    opcao = input('(i) para inserir, (a) para apagar, (e) para exibir: ')


    if opcao == 'i':
        qtd_produto = int(input('Quantos produtos deseja inserir? '))
        cont = 0
        while cont < qtd_produto:
            os.system('cls')
            valor = input(f'{cont + 1}º produto: ')
            lista_compras.append(valor)
            cont += 1

    elif opcao == 'a':
        os.system('cls')
        numero_produto = ''

        if len(lista_compras) == 0:
            print('A lista está vazia!')
            continue

        else:
            numero_produto = input('Escolha o número do produto: ')

        try:
            indice_produto = int(numero_produto)
            del lista_compras[indice_produto]
            print('Produto apagado com sucesso!')
        except IndexError:
           print('Não existe esse número na lista. Por favor, informe um valor válido!')
        except ValueError:
            print('Por favor, informe um número inteiro!')

    elif opcao == 'e':
        os.system('cls')

        if len(lista_compras) == 0:
            print('A lista está vazia!')

        for i, item in enumerate(lista_compras):
            print(i, item)

    else:
        print('Opção inválida!')
