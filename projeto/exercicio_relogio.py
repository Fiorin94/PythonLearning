hora = input('Que horas são? ')

if hora.isdigit():

    horas = int(hora)
    DIA = horas >= 0 and horas <= 11
    TARDE = horas >= 12 and horas <= 17
    NOITE = horas >= 18 and horas <= 23

    if DIA:
        print('Bom dia')
    if TARDE:
        print('Boa tarde')
    if NOITE:
        print('Boa noite')
    if horas not in (1, 2, 3, 4, 5, 6, 7, 8 ,9 ,10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24):
        print('Horário inválido')
else:
    print('Somente números são aceitos')