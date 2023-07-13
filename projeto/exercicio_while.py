"""
iterando strings com while
"""

#....Índices..012345678910
nome = 'Izabella Moreno' #iteráveis
tamanho_nome = len(nome)
indice = 0
novo_nome = '*'

while indice < tamanho_nome:
    letra = nome[indice]
    novo_nome += letra
    novo_nome += '*'
    indice += 1

print(novo_nome)
