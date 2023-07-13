""" Calculadora com while """

while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')

    if numero_1.isdigit() and numero_2.isdigit():
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
    else:
        print('Um ou mais números digitados são inválidos.')
        continue
    
    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador')
        continue
    
    if operador == '+':
        soma = num_1_float + num_2_float
        print(soma)
    elif operador == '-':
        subtrai = num_1_float - num_2_float
        print(subtrai)
    elif operador == '/':
        divide = num_1_float / num_2_float
        print(divide)
    elif operador == '*':
        multiplica = num_1_float * num_2_float
        print(multiplica)
    else:
        print('Não deveria chegar aqui')
    
    sair = input('Quer sair [s]im: ').lower().startswith('s')

    if sair is True:
        break