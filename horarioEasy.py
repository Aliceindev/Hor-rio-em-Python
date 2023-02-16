# Modelo Simplificado 

def hora(h, m):  # criando a função hora
    b = h / 24   # formato em 24 horas
    if b <= 1:
        hh = str(h)
        print('\nSua hora: '+ hh + ':', end='')    #\n no inicio serve para pular uma linha antes do texto
    elif b > 1 and b < 2:                          
        hhh = str(h -12)
        print('\nSua hora: '+ hhh + ':', end='')
    else:
        print('\nFormato de hora inválido')
    if b <= 1 and m <= 60:
        print(m, 'a.m')
    elif b > 1 and m <= 60:
        print(m, 'p.m')
    else: 
        print('\nFormato de minutos inválidos')
        
while True:
    print(f'''\n{"-"*25}''')                 # pular uma linha e repetir 25 vezes o sinal de menos "-"
    print('Digite 500 para sair')
    h = int(input('Informe a hora: '))
    if h == 500:                             # caso for digitado 500 vai finalizar o programa
        break
    m = int(input('Informe os minutos: '))
    hora(h, m)                               # atribuir os valores inseridos dentro da função