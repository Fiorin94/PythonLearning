nome = input('Qual o seu primeiro nome? ')

tamanho = len(nome)

if tamanho >= 1:
    if tamanho < 4:
        print('Seu nome é curto')
    elif tamanho >= 5 and tamanho <= 6:
        print('Seu nome é normal')
    elif tamanho >= 7:
        print('Seu nome é grande')
    else:
        print('Digite um nome válido')
else:
    print('Digite pelo menos uma letra')
