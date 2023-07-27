"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""
import re
import sys

entrada = input('CPF [398.236.618-63]: ')
cpf = re.sub(
    r'[^0-9]',
    '',
    entrada
)

entrada_e_sequencial = entrada == entrada[0] * len(entrada)

if entrada_e_sequencial:
    print('Você enviou dados sequenciais.')
    sys.exit()

cpf_range = cpf[0:9]
contador = 10
resultado_1 = 0

for digito in cpf_range:
    resultado_1 += int(digito) * contador
    contador -= 1

primeiro_digito = (resultado_1 * 10) % 11
primeiro_digito = primeiro_digito if primeiro_digito <= 9 else 0

cpf_range_2 = cpf_range + str(primeiro_digito)
contador_2 = 11
resultado_2 = 0

for digito in cpf_range_2:
    resultado_2 += int(digito) * contador_2
    contador_2 -= 1

segundo_digito = (resultado_2 * 10) % 11
segundo_digito = segundo_digito if segundo_digito <= 9 else 0

cpf_gerado = f'{cpf_range}{primeiro_digito}{segundo_digito}'

if cpf == cpf_gerado:
    print(f'O CPF {cpf} é válido.')
else:
    print(f'O CPF {cpf} é inválido.')