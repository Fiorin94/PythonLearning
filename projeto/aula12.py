nome = 'Felipe Fiorin'
altura = 1.76
peso = 95

imc = peso // (altura * altura)

#f-strings - f significa 'format'
linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)
