# Codado por Sierra & Aliyah

# Melhorar o gerador aleatório de Xingamentos
# Adicionar um sistema de buscas
# Adicionar um painel de configuração dos xingamentos

###################################################

# bibliotecas para gerenciar menus
import os
#
# Comando Clear
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
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
# cabeçalho
clear()
print('Bem vindo ao gerador de xingos pseudoaleatórios! By: Mimus \n')
#
# Funcionalidades:
#
# Mensagem de erro
def erro():
    print('Selecione uma opção válida... \n')
    input('Aperte enter para continuar...')
    clear()
#
#
while True:
    print('O que deseja fazer? \n\n1 - Xingar alguém \n2 - Pessoas xingadas \n3 - Xingamentos usados \n4 - Como cada pessoa foi xingada \n5 - Sair \n')
    opc = input('Selecione a opção desejada: ') # opc = opção do menu principal
    clear()
# Xingar alguém
    if opc == '1':
        ppl = input('Quem deseja xingar? ') # ppl = nome da pessoa a ser xingada
        print()
        ppls.append(ppl) # ppls = lista de pessas xingadas
        xing = random.choice(x) # gerador pseudoaleatório de xingos
        x_util.append(xing) # lista de xingamentos utilizados
        pplx = (xing + ' ' + ppl + '!') # pplx = xingamento + pessoa xingadas
        pplsx.append(pplx) # pplsx = lisa de xingamento + pessoa xingadas
        print(pplx, '\n')
        input('Aperte enter para continuar...')
        clear()
#
# Ver todas as pessoas xingadas
    elif opc == '2':
        print('O que deseja fazer? \n\n1 - Ver últimas 5 pessoas xingadas \n2 - Ver todas as pessoas xingadas \n3 - Retornar \n')
        sel = input('Selecione a opção desejada: ')
        clear()
        verific = len(ppls)
        def verific_ppls():
            print('Ninguém foi xingado... \n')
            input('Aperte enter para continuar...')
            clear()
        if sel == '1':
            if verific == 0:
                verific_ppls()
            else:
                print('Foram xingados: \n')
                for i in ppls[-5:]:
                    print(i)
                input('\nAperte enter para continuar...')
                clear()
        elif sel =='2':
            if verific == 0:
                verific_ppls()
            else:
                print('Foram xingados: \n')
                for pp in ppls: # pp = pessoa na lista de pessoas xingadas & ppls = lista de pessoas
                    print(pp) # pp = pessoa na lista de pessoas xingadas
                input('\nAperte enter para continuar...')
                clear()
        elif sel == '3':
            clear()
        else:
            erro()
#
# Ver xingamentos usados
    elif opc == '3':
        print('O que deseja fazer? \n\n1 - Ver últimos 5 xingamentos usados \n2 - Ver todos os xingamentos usados \n3 - Retornar \n')
        sel = input('Selecione a opção desejada: ')
        clear()
        verific = len(x_util)
        def verific_x_util():
            print('Ninguém foi xingado... \n')
            input('Aperte enter para continuar...')
            clear()
        if sel == '1':
            if verific == 0:
                verific_x_util()
            else:
                print('Foram utilizados: \n')
                for i in x_util[-5:]:
                    print(i)
                input('\nAperte enter para continuar...')
                clear()
        elif sel =='2':
            if verific == 0:
                verific_x_util()
            else:
                print('Foram utilizados: \n')
                for num in x_util: # num = xingo na lista x_util
                    print(num) # x = lista de Xingamentos
                input('\nAperte enter para continuar...')
                clear()
        elif sel == '3':
            clear()
        else:
            erro()
# Ver como cada pessoa foi xingada
    elif opc == '4':
        print('O que deseja fazer? \n\n1 - Ver últimas 5 pessoas e seus xingamentos \n2 - Ver todas as pessoas e seus xingamentos \n3 - Retornar \n')
        sel = input('Selecione a opção desejada: ')
        clear()
        verific = len(pplsx)
        def verific_pplsx():
            print('Ninguém foi xingado... \n')
            input('Aperte enter para continuar...')
            clear()
        if sel == '1':
            if verific == 0:
                verific_pplsx()
            else:
                print('Cada pessoa foi xingada da seguinte forma: \n')
                for i in pplsx[-5:]:
                    print(i)
                input('\nAperte enter para continuar...')
                clear()
        elif sel =='2':
            if verific == 0:
                verific_pplsx()
            else:
                print('Cada pessoa foi xingada da seguinte forma: \n')
                for px in pplsx: # px = pessoa + xingamento na lista de pplsx & pplsx = lisa de xingamentos usados para as pessoas xingadas
                    print(px) # px = pessoa + xingamento na lista de pplsx
                input('\nAperte enter para continuar...')
                clear()
        elif sel == '3':
            clear()
        else:
            erro()
#
# Sair
    elif opc == '5':
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
        erro()
#
