hora = input('Que horas são? ')
hora_verificador = hora[0:2]
hora_int = int(hora_verificador) #Converte os dois primeiros valores das horas de str para int
hora_dia = hora_int >= 0 and hora_int < 12 #Verifica se o período do dia é de manhã.
hora_tarde = hora_int >= 12 and hora_int < 18 #Verifica se o período do dia é de tarde.
hora_noite = hora_int >= 18 and hora_int < 24 #Verifica se o período é o noturno.

try: 
    if hora_dia:
        print(f'Bom dia')
    elif hora_tarde:
        print(f'Boa tarde')
    elif hora_noite:
        print(f'Boa noite')
    else:
        print('Não conheço essa hora')
except:
    print('Formato de hora inválido.')
