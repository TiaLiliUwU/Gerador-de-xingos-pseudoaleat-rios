# Codado por Sierra & Aliyah

# P/ debugar, comece a ler de baixo p/ cima p/ entender o workflow.

###################################################

# biblioteca para gerenciar menus
import os
#

# xingamentos pseudoaleatórios
import random
x = ['Vai tomar no cu,', 'Vai se foder,', 'Você é um lixo,', 'Você é um desperdício de oxigênio,', 'Você é um bosta,', 'Você é a vergonha da família,', 'Nem sua mãe gosta de você,', 'Some daqui,']
xnum = [] # xnum = número pseudoaleatório que gera um xingamento pseudoaleatório
#

# lista de pessoas
ppls = [] # ppls = lista de pessoas
pplsx = [] # pplsx = lisa de xingamentos usados para as pessoas xingadas
#

# menu continuação
def cont():
    while True:
        print('Deseja continuar? \n\n1 - Sim \n2 - Não \n')
        opc2 = input('Selecione a opção desejada: ') # opc2 = opção do menu de continuação
        os.system('clear')
        if opc2 == '1':
            menu()
        elif opc2 == '2':
            print('Que a força do ódio esteja com você ;)')
            exit()
        else:
            print('Por favor, selecione uma opção válida.')
            os.system('clear')
#
# Funcionalidades principais
def menu():
    while True:
        print('O que deseja fazer? \n\n1 - Xingar alguém \n2 - Ver todas as pessoas xingadas \n3 - Ver xingamentos usados \n4 - Ver como cada pessoa foi xingada \n5 - Sair \n')
        opc = input('Selecione a opção desejada: ') # opc = opção do menu principal
        os.system('clear')
        if opc == '1':
            ppl = input('Quem deseja xingar? ') # ppl = nome da pessoa a ser xingada
            ppls.append(ppl) # ppls = lista de pessas xingadas
            print()
            # Gerador pseudoaleatório de xingos
            alt_num = random.randint(0,7) # alt_num = número pseudoaleatório gerado pelo "import random"
            xnum.append(alt_num) # xnum = número pseudoaleatório que gera um xingamento pseudoaleatório
            pplx = (x[alt_num] + ' ' + ppl + '!') # pplx = xingamento + pessoa xingadas
            pplsx.append(pplx) # pplsx = lisa de xingamentos usados para as pessoas xingadas
            print(pplx, '\n')
            input('Aperte enter para continuar...')
            os.system('clear')
            cont()
        elif opc == '2':
            print('Foram xingados: \n')
            for pp in ppls: # pp = pessoa na lista de pessoas xingadas & ppls = lista de pessoas
                print(pp) # pp = pessoa na lista de pessoas xingadas
            input('\nAperte enter para continuar...')
            os.system('clear')
            cont()
        elif opc == '3':
            print('Xingamentos usados: \n')
            for num in xnum: # num = número na lista de xnum & xnum = número pseudoaleatório que gera um xingamento pseudoaleatório
                print(x[num]) # x = lista de Xingamentos
            input('\nAperte enter para continuar...')
            os.system('clear')
            cont()
        elif opc == '4':
            print('Cada pessoa foi xingada da seguinte forma: \n')
            for px in pplsx: # px = pessoa + xingamento na lista de pplsx & pplsx = lisa de xingamentos usados para as pessoas xingadas
                print(px) # px = pessoa + xingamento na lista de pplsx
            input('\nAperte enter para continuar...')
            os.system('clear')
            cont()
        elif opc == '5':
            print('Que a força do ódio esteja com você ;)')
            exit()

        else:
            input('Por favor, selecione uma opção válida. Aperte enter para continuar...')
            os.system('clear')
#

# cabeçalho
os.system('clear')
print('Bem vindo ao gerador de xingos pseudoaleatórios! By: Mimus \n')
menu()
#
