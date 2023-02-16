import sys, time
import os
os.system("cls")

# Colorir o código em Python
roxo        = "\033[34m"
verde		= "\033[32m"
azul		= "\033[36m"
amarelo		= "\033[33m" 
vermelho	= "\033[31m"
cinza       = "\033[30m"
fim         = "\033[m"

# Funções
def animacao(texto):
    for msg in texto:
        sys.stdout.write(msg)
        sys.stdout.flush()
        time.sleep(0.10)
        
def animacaoInfo(texto):
    for msg in texto:
        sys.stdout.write(msg)
        sys.stdout.flush()
        time.sleep(0.05)
   
def hora12(h, m):  #12/12=1 e 24/12=2
    b = h / 12
    if b <= 1:
        hh = str(h)
        print(roxo + ' Sua hora: '+ hh + ':', end='' + fim)
    elif b > 1 and b < 2:
        hhh = str(h -12)
        print(roxo + ' Sua hora: '+ hhh + ':', end='' + fim)
    else:
        print(f'{vermelho} Formato de hora inválido{fim}')
    if b <= 1 and m <= 60:
        print(f'{roxo}{m} a.m {fim}')
    elif b > 1 and m <= 60:
        print(f'{roxo}{m} p.m {fim}')
    else: 
        print(f'{vermelho} Formato de minutos inválidos{fim}')
       
def hora24(h, m):  #12/24=0.5 e 24/24=1
    b = h / 24
    if b <= 0.5:
        hh = str(h)
        print(roxo + ' Sua hora: '+ hh + ':', end='' + fim)
    elif b > 0.5 and b < 1:
        hhh = str(h)
        print(roxo + ' Sua hora: '+ hhh + ':', end='' + fim)
    else:
        print(f'{vermelho} Formato de hora inválido{fim}')
    if b <= 0.5 and m <= 60:
        print(f'{roxo}{m} a.m {fim}')
    elif b > 0.5 and m <= 60:
        print(f'{roxo}{m} p.m {fim}')
    else: 
        print(f'{vermelho} Formato de minutos inválidos{fim}')
        
# Fim das Funções  
   

# Início do Código na tela
animacao(f'''
{verde}coded by: Aliceindev
{vermelho}Github: {azul}github.com/Aliceindev{azul}
{amarelo}Aguarde carregando...{fim}
''')
time.sleep(3)  #tempo 


# Escolha
animacaoInfo(f'''
Escolha o formato do horário:
{cinza} [1] Formato de 12 horas
{cinza} [2] Formato de 24 horas
{vermelho} [3] Sair {fim}
\n''')
opcao = int(input())
time.sleep(1.2) #tempo 
os.system("cls") #apagar


# Loop infinito só irá parar se for digitado [3] na Escolha... 
while opcao != 3 :
    if opcao == 1:  #12 horas
        os.system("cls" if os.name == "nt" else "clear")
        h = int(input('\n Informe a hora: '))
        m = int(input(' Informe os minutos: '))
        hora12(h, m)
    
    elif opcao == 2:  #24 horas
        os.system("cls" if os.name == "nt" else "clear")
        h = int(input('\n Informe a hora: '))
        m = int(input(' Informe os minutos: '))
        hora24(h, m)
    
    # Escolha
    animacaoInfo(f'''
    Escolha o formato do horário:
    {cinza} [1] Formato de 12 horas
    {cinza} [2] Formato de 24 horas
    {vermelho} [3] Sair {fim}
    \n''')
    opcao = int(input())
    time.sleep(1.2)   #tempo 
    os.system("cls")  #apagar