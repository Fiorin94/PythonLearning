import random


nove_digitos = ''
for i in range(9):
    nove_digitos += str(random.randint(0, 9))

contador = 10
resultado_1 = 0

for digito in nove_digitos:
    resultado_1 += int(digito) * contador
    contador -= 1

primeiro_digito = (resultado_1 * 10) % 11
primeiro_digito = primeiro_digito if primeiro_digito <= 9 else 0

cpf_range_2 = nove_digitos + str(primeiro_digito)
contador_2 = 11
resultado_2 = 0

for digito in cpf_range_2:
    resultado_2 += int(digito) * contador_2
    contador_2 -= 1

segundo_digito = (resultado_2 * 10) % 11
segundo_digito = segundo_digito if segundo_digito <= 9 else 0

cpf_gerado = f'{nove_digitos}{primeiro_digito}{segundo_digito}'

print(cpf_gerado)