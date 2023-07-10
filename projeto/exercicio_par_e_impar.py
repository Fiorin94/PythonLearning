numero = input('Digite um número inteiro: ')

if numero.isdigit():
    numero_int = int(numero)
    par_impar = numero_int % 2 == 0
    par_impar_texto = 'Ímpar'

    if par_impar:
        par_impar_texto = 'Par'

    print(f'O número {numero_int} é {par_impar_texto}')
else:
    print('Você não digitou um número inteiro')