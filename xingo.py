# Codado por Sierra & Aliyah

# Melhorar o gerador aleatório de Xingamentos
# Adicionar um sistema de buscas
# Adicionar um painel de configuração dos xingamentos

###################################################

# bibliotecas para gerenciar menus
import os
import platform
so = platform.system()
#
# Comando Clear
def clear():
    if so == 'Windows':
        os.system('clr')
    else:
        os.system('clear')
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
            xnum.append(int(ln))
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
# cabeçalho
clear()
print('Bem vindo ao gerador de xingos pseudoaleatórios! By: Mimus \n')
#
# Funcionalidades
while True:
    print('O que deseja fazer? \n\n1 - Xingar alguém \n2 - Pessoas xingadas \n3 - Xingamentos usados \n4 - Como cada pessoa foi xingada \n5 - Sair \n')
    opc = input('Selecione a opção desejada: ') # opc = opção do menu principal
    clear()
# Xingar alguém
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
        clear()
#
# Ver todas as pessoas xingadas
    elif opc == '2':
        print('O que deseja fazer? \n\n1 - Ver últimas 5 pessoas xingadas \n2 - Ver todas as pessoas xingadas \n3 - Retornar \n')
        sel = input('Selecione a opção desejada: ')
        clear()
        if sel == '1':
            verific = len(ppls)
            if verific == 0:
                print('Ninguém foi xingado... \n')
                input('Aperte enter para continuar...')
                clear()
            else:
                print('Foram xingados: \n')
                if verific == 1:
                    print(ppls[verific - 1])
                    input('\nAperte enter para continuar...')
                    clear()
                elif verific == 2:
                    print(ppls[verific - 2] + '\n' + ppls[verific - 1])
                    input('\nAperte enter para continuar...')
                    clear()
                elif verific == 3:
                    print(ppls[verific - 3] + '\n' + ppls[verific - 2] + '\n' + ppls[verific - 1])
                    input('\nAperte enter para continuar...')
                    clear()
                elif verific == 4:
                    print(ppls[verific - 4] + '\n' + ppls[verific - 3] + '\n' + ppls[verific - 2] + '\n' + ppls[verific - 1])
                    input('\nAperte enter para continuar...')
                    clear()
                elif verific >= 5:
                    print(ppls[verific - 5] + '\n' + ppls[verific - 4] + '\n' + ppls[verific - 3] + '\n' + ppls[verific - 2] + '\n' + ppls[verific - 1])
                    input('\nAperte enter para continuar...')
                    clear()
        elif sel =='2':
            verific = len(ppls)
            if verific == 0:
                print('Ninguém foi xingado... \n')
                input('Aperte enter para continuar...')
                clear()
            else:
                print('Foram xingados: \n')
                for pp in ppls: # pp = pessoa na lista de pessoas xingadas & ppls = lista de pessoas
                    print(pp) # pp = pessoa na lista de pessoas xingadas
                input('\nAperte enter para continuar...')
                clear()
        elif sel == '3':
            clear()
        else:
            print('Selecione uma opção válida... \n')
            input('Aperte enter para continuar...')
            clear()
#
# Ver xingamentos usados
    elif opc == '3':
        print('O que deseja fazer? \n\n1 - Ver últimos 5 xingamentos usados \n2 - Ver todos os xingamentos usados \n3 - Retornar \n')
        sel = input('Selecione a opção desejada: ')
        clear()
        if sel == '1':
            verific = len(xnum)
            if verific == 0:
                print('Ninguém foi xingado... \n')
                input('Aperte enter para continuar...')
                clear()
            else:
                print('Foram utilizados: \n')
                if verific == 1:
                    print(x[xnum[verific - 1]])
                    input('\nAperte enter para continuar...')
                    clear()
                elif verific == 2:
                    print(x[xnum[verific - 2]] + '\n' + x[xnum[verific - 1]])
                    input('\nAperte enter para continuar...')
                    clear()
                elif verific == 3:
                    print(x[xnum[verific - 3]] + '\n' + x[xnum[verific - 2]] + '\n' + x[xnum[verific - 1]])
                    input('\nAperte enter para continuar...')
                    clear()
                elif verific == 4:
                    print(x[xnum[verific - 4]] + '\n' + x[xnum[verific - 3]] + '\n' + x[xnum[verific - 2]] + '\n' + x[xnum[verific - 1]])
                    input('\nAperte enter para continuar...')
                    clear()
                elif verific >= 5:
                    print(x[xnum[verific - 4]] + '\n' + x[xnum[verific - 4]] + '\n' + x[xnum[verific - 3]] + '\n' + x[xnum[verific - 2]] + '\n' + x[xnum[verific - 1]])
                    input('\nAperte enter para continuar...')
                    clear()
        elif sel =='2':
            verific = len(xnum)
            if verific == 0:
                print('Ninguém foi xingado... \n')
                input('Aperte enter para continuar...')
                clear()
            else:
                print('Foram utilizados: \n')
                for num in xnum: # num = número na lista de xnum & xnum = número pseudoaleatório que gera um xingamento pseudoaleatório
                    print(x[num]) # x = lista de Xingamentos
                input('\nAperte enter para continuar...')
                clear()
        elif sel == '3':
            clear()
        else:
            print('Selecione uma opção válida... \n')
            input('Aperte enter para continuar...')
            clear()
# Ver como cada pessoa foi xingada
    elif opc == '4':
        print('O que deseja fazer? \n\n1 - Ver últimas 5 pessoas e seus xingamentos \n2 - Ver todas as pessoas e seus xingamentos \n3 - Retornar \n')
        sel = input('Selecione a opção desejada: ')
        clear()
        if sel == '1':
            verific = len(pplsx)
            if verific == 0:
                print('Ninguém foi xingado... \n')
                input('Aperte enter para continuar...')
                clear()
            else:
                print('Cada pessoa foi xingada da seguinte forma: \n')
                if verific == 1:
                    print(pplsx[verific - 1])
                    input('\nAperte enter para continuar...')
                    clear()
                elif verific == 2:
                    print(pplsx[verific - 2] + '\n' + pplsx[verific - 1])
                    input('\nAperte enter para continuar...')
                    clear()
                elif verific == 3:
                    print(pplsx[verific - 3] + '\n' + pplsx[verific - 2] + '\n' + pplsx[verific - 1])
                    input('\nAperte enter para continuar...')
                    clear()
                elif verific == 4:
                    print(pplsx[verific - 4] + '\n' + pplsx[verific - 3] + '\n' + pplsx[verific - 2] + '\n' + pplsx[verific - 1])
                    input('\nAperte enter para continuar...')
                    clear()
                elif verific >= 5:
                    print(pplsx[verific - 5] + '\n' + pplsx[verific - 4] + '\n' + pplsx[verific - 3] + '\n' + pplsx[verific - 2] + '\n' + pplsx[verific - 1])
                    input('\nAperte enter para continuar...')
                    clear()
        elif sel =='2':
            verific = len(pplsx)
            if verific == 0:
                print('Ninguém foi xingado... \n')
                input('Aperte enter para continuar...')
                clear()
            else:
                print('Cada pessoa foi xingada da seguinte forma: \n')
                for px in pplsx: # px = pessoa + xingamento na lista de pplsx & pplsx = lisa de xingamentos usados para as pessoas xingadas
                    print(px) # px = pessoa + xingamento na lista de pplsx
                input('\nAperte enter para continuar...')
                clear()
        elif sel == '3':
            clear()
        else:
            print('Selecione uma opção válida... \n')
            input('Aperte enter para continuar...')
            clear()
#
# Sair
    elif opc == '5':
        with open(txt_nomes, 'w+') as nomestxt:
            for nm in ppls:
                nomestxt.write(nm + '\n')
        nomestxt.close()
        with open(txt_xingos, 'w+') as xingostxt:
            for lt in xnum:
                xingostxt.write(str(lt) + '\n')
        xingostxt.close()
        with open(txt_nomes_xingos, 'w+') as nomes_xingostxt:
            for xn in pplsx:
                nomes_xingostxt.write(xn + '\n')
        nomes_xingostxt.close()
        print('Que a força do ódio esteja com você ;)')
        exit()
    else:
        input('Por favor, selecione uma opção válida. \nAperte enter para continuar...')
        clear()
#
