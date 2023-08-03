def criar_multiplicador(multiplicador):
    if multiplicador not in (2,3,4):
        print('Multiplicadores permitidos: 2, 3, 4.')
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criar_multiplicador(5)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))