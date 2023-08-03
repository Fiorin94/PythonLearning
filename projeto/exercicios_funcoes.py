#Função que multiplica os argumentos

def multiplica(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

multiplicacao = multiplica(1,2,3,4,5,6)

print(multiplicacao)

#Função que diz se o número inserido é par ou ímpar

def par_impar(x):
    numero = int(x)
    resultado = ''

    if numero % 2 == 0:
        resultado = 'O número é par'
    else:
        resultado = 'O número é impar'
    return resultado

impar = par_impar(1)
print(impar)

par = par_impar(2)
print(par)