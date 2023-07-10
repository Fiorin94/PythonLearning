primeiro_numero = input('Digite um valor: ')
segundo_numero = input('Digite outro valor: ')

if primeiro_numero > segundo_numero:
    print(f'O primeiro número {primeiro_numero}, é maior que o segundo número, {segundo_numero}')
elif segundo_numero > primeiro_numero:
    print(f'O segundo número {segundo_numero}, é maior que o primeiro número, {primeiro_numero}')
elif primeiro_numero == segundo_numero:
    print('Os números são iguais')
else:
    print('Não foi possível realizar a comparação')