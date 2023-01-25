# Codado por Sierra & Aliyah

###################################################

# Gerenciar menus
import os
menu = ['1', '2', '3', '4', '5', '6']
sub_menu = ['1', '2', '3']
#
# xingamentos pseudoaleatórios
import random
x = ['Vai tomar no cu,', 'Vai se foder,', 'Você é um lixo,', 'Você é um desperdício de oxigênio,', 'Você é um bosta,', 'Você é a vergonha da família,', 'Nem sua mãe gosta de você,', 'Some daqui,']
x_util = []
#
# lista de pessoas
ppls = [] # ppls = lista de pessoas
pplsx = [] # pplsx = lisa de xingamento + pessoa xingadas
#
# Swap
txt_nomes = 'nomes.txt'
txt_xingos = 'xingos.txt'
txt_nomes_xingos = 'nomes_xingos.txt'

if os.path.exists('nomes.txt'):
    with open(txt_nomes) as nomestxt:
        nome = nomestxt.read().splitlines()
        for ln in nome:
            ppls.append(ln)
    nomestxt.close()
else:
    pass

if os.path.exists('xingos.txt'):
    with open(txt_xingos) as xingostxt:
        xi = xingostxt.read().splitlines()
        for ln in xi:
            x_util.append(ln)
    xingostxt.close()
else:
    pass

if os.path.exists('nomes_xingos.txt'):
    with open(txt_nomes_xingos) as nomes_xingostxt:
        nx = nomes_xingostxt.read().splitlines()
        for ln in nx:
            pplsx.append(ln)
    nomes_xingostxt.close()
else:
    pass
#
# Funcionalidades:
#
# Comando Clear
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
#
# Aperte enter para continuar
def enter():
    ctrl = True
    input('\nAperte enter para continuar...')
    clear()
#
# Mensagem de erro
def erro():
    print('Selecione uma opção válida...')
    enter()
#
# Menu clear
def opc_clear():
    if opc in menu:
        clear()
    else:
        pass
#
# Verificação
def veri():
    print('Não há dados registrados...')
    enter()
#
# Submenu clear
def subclear():
    if sel in sub_menu:
        clear()
    else:
        pass

#
# cabeçalho
clear()
print('Bem vindo ao gerador de xingos pseudoaleatórios! By: Mimus \n')
#
while True:
    ctrl = True
    print('O que deseja fazer? \n\n1 - Xingar alguém \n2 - Pessoas xingadas \n3 - Xingamentos usados \n4 - Como cada pessoa foi xingada \n5 - Reset \n6 - Sair \n')
    opc = input('Selecione a opção desejada: ') # opc = opção do menu principal
    opc_clear()
#
# Xingar alguém
    if opc == '1':
        ppl = input('Quem deseja xingar? ') # ppl = nome da pessoa a ser xingada
        print()
        ppls.append(ppl) # ppls = lista de pessas xingadas
        xing = random.choice(x) # gerador pseudoaleatório de xingos
        x_util.append(xing) # lista de xingamentos utilizados
        pplx = (xing + ' ' + ppl + '!') # pplx = xingamento + pessoa xingadas
        pplsx.append(pplx) # pplsx = lisa de xingamento + pessoa xingadas
        print(pplx)
        enter()
#
# Ver todas as pessoas xingadas
    elif opc == '2':
        while ctrl == True:
            ctrl = False
            print('O que deseja fazer? \n\n1 - Ver últimas 5 pessoas xingadas \n2 - Ver todas as pessoas xingadas \n3 - Retornar \n')
            sel = input('Selecione a opção desejada: ')
            verific = len(ppls)
            subclear()
            if sel == '1':
                if verific == 0:
                    veri()
                else:
                    print('Foram xingados: \n')
                    for i in ppls[-5:]:
                        print(i)
                    enter()
            elif sel =='2':
                if verific == 0:
                    veri()
                else:
                    print('Foram xingados: \n')
                    for pp in ppls: # pp = pessoa na lista de pessoas xingadas & ppls = lista de pessoas
                        print(pp) # pp = pessoa na lista de pessoas xingadas
                    enter()
            elif sel == '3':
                pass
            else:
                print()
                ctrl = True
                erro()
#
# Ver xingamentos usados
    elif opc == '3':
        while ctrl == True:
            ctrl = False
            print('O que deseja fazer? \n\n1 - Ver últimos 5 xingamentos usados \n2 - Ver todos os xingamentos usados \n3 - Retornar \n')
            sel = input('Selecione a opção desejada: ')
            verific = len(x_util)
            subclear()
            if sel == '1':
                if verific == 0:
                    veri()
                else:
                    print('Foram utilizados: \n')
                    for i in x_util[-5:]:
                        print(i)
                    enter()
            elif sel =='2':
                if verific == 0:
                    veri()
                else:
                    print('Foram utilizados: \n')
                    for num in x_util: # num = xingo na lista x_util
                        print(num) # x = lista de Xingamentos
                    enter()
            elif sel == '3':
                pass
            else:
                print()
                ctrl = True
                erro()
# Ver como cada pessoa foi xingada
    elif opc == '4':
        while ctrl == True:
            ctrl = False
            print('O que deseja fazer? \n\n1 - Ver últimas 5 pessoas e seus xingamentos \n2 - Ver todas as pessoas e seus xingamentos \n3 - Retornar \n')
            sel = input('Selecione a opção desejada: ')
            verific = len(pplsx)
            subclear()
            if sel == '1':
                if verific == 0:
                    veri()
                else:
                    print('Cada pessoa foi xingada da seguinte forma: \n')
                    for i in pplsx[-5:]:
                        print(i)
                    enter()
            elif sel =='2':
                if verific == 0:
                    veri()
                else:
                    print('Cada pessoa foi xingada da seguinte forma: \n')
                    for px in pplsx: # px = pessoa + xingamento na lista de pplsx & pplsx = lisa de xingamentos usados para as pessoas xingadas
                        print(px) # px = pessoa + xingamento na lista de pplsx
                    enter()
            elif sel == '3':
                pass
            else:
                print()
                ctrl = True
                erro()
#
# Reset
    elif opc == '5':
        while ctrl == True:
            ctrl = False
            print('Tem certeza que deseja excluir os dados armazenados? \n\n1 - Sim \n2 - Não \n')
            ex_d = input('Selecione a opção desejada: ')
            if ex_d == '1':
                del ppls[0:], x_util[0:], pplsx[0:]
                with open(txt_nomes, 'w+') as nomestxt:
                    pass
                nomestxt.close()
                with open(txt_xingos, 'w+') as xingostxt:
                    pass
                xingostxt.close()
                with open(txt_nomes_xingos, 'w+') as nomes_xingostxt:
                    pass
                nomes_xingostxt.close()
                print('\nLista resetada com sucesso!')
                enter()
            elif ex_d == '2':
                print('\nReset abortado!')
                enter()
            else:
                print()
                ctrl = True
                erro()
#
# Sair
    elif opc == '6':
        with open(txt_nomes, 'w+') as nomestxt:
            for nm in ppls:
                nomestxt.write(nm + '\n')
        nomestxt.close()
        with open(txt_xingos, 'w+') as xingostxt:
            for lt in x_util:
                xingostxt.write(lt + '\n')
        xingostxt.close()
        with open(txt_nomes_xingos, 'w+') as nomes_xingostxt:
            for xn in pplsx:
                nomes_xingostxt.write(xn + '\n')
        nomes_xingostxt.close()
        print('Que a força do ódio esteja com você ;)')
        exit()
    else:
        print()
        erro()
#
