def criar_multiplicador(multiplicador):
    if multiplicador not in (2,3,4):
        print('Multiplicadores permitidos: 2, 3, 4.')
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))


def par_impar(numero):
    multiplo_de_dois = numero % 2 == 0

    if multiplo_de_dois:
        return f'{numero} é par'
    else:
        return f'{numero} é ímpar'
    

print( par_impar(2))
print(par_impar(15))
print(par_impar(4))