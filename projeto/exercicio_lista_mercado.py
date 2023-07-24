import os



lista = []

while True:
    print('Selecione uma opção')
    opcoes = input('[i]nserir [a]pagar [l]istar: ')

    if opcoes == 'i':
        os.system('cls')
        valor = input('Insira um item: ')
        lista.append(valor)

    elif opcoes == 'a':
        os.system('cls')
        indice = input('Insira um índice para apagar: ')

        try:
            indice_int = int(indice)
            del lista[indice_int]
            #lista.pop(indice_int)
        except ValueError:
            print('Digite apenas números.')
        except IndexError:
            print(f'Item {indice_int} não encontrado.')
        except Exception:
            print('Erro desconhecido')

    elif opcoes == 'l':
        os.system('cls')

        if lista == 0:
            print('Não tem nada para listar.')

        for indice, item in enumerate(lista):
            print(indice, item)

    elif opcoes not in 'i,a,l':
        os.system('cls')
        print('Opção inválida')
