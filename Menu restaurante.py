from time import sleep


def menu_principal(): #concluido momentaniamente

    print()
    print('Olá, Seja Bem Vindo(a)')
    print()
    print('Menu Principal')
    print('-' * 20)
    print('[1] - Comidas Regionais')
    print('[2] - Churrasco')
    print('[3] - Encerrar!')
    print('-' * 20)

    opcao = int(input('Digite sua Escolha: '))
    sleep(3)

    if opcao == 1:
        print()
        print('Comidas Regionais')
        print()
        print('Escolha seu pedido:')
        regionais()

    elif opcao == 2:
        print()
        print('Churrasco')
        print()
        print('Escolha seu pedido:')
        churrasco()
    elif opcao == 3:
        print('Muito Obrigado!')
        exit()
    else:
        print()
        print('Opção Inválida!')
        print()
        menu_principal()

def regionais(): #concluido momentaniamente
    print()
    print('[1] - Carne de Sol  - Acompanha Baião e Salada Verde, serve até 2 pessoas.')
    print('[2] - Galinha Caipira - Acompanha Arroz e Pirão, serve até 3 pessoas.')
    print('[3] - Feijoada - Acompanha Baião e Salada Verde, serve até 2 pessoas.')
    print('[4] - Voltar ao Menu Principal')
    print()

    reg1 = int(input('Escolha uma opção: '))
    if reg1 == 1:
        print()
        print('Carne de Sol')
        print()
    
    elif reg1 == 2:
        print()
        print('Galinha Caipira ')
        print()
        
    elif reg1 == 3:
        print()
        print('Feijoada ')
        print()
        
    elif reg1 == 4:
        print()
        print('Voltando ao menu principal...')
        print()
        menu_principal()

    else:
        print('Opção inválida!')
        regionais()
    
    def algo_mais1 ():
        algo_mais = int(input('Deseja algo mais? [1] SIM [2] NÃO: '))
        while (algo_mais):
            if algo_mais == 1:
                menu_principal()
            elif algo_mais == 2:
                print()
                print('Seu pedido foi encaminhado para nossa cozinha e logo estará pronto!')
                exit()
            else:
                print('Opção Inválida!\nTente Novamente!')
                algo_mais1()
    algo_mais1()

def churrasco():
    print()
    print('[1] - Maminha (A partir de 100g)')
    print('[2] - Alcatra (A partir de 100g)')
    print('[3] - Picanha (A partir de 100g)')
    print('[4] - Voltar ao Menu Principal')

    chur1 = int(input('Escolha sua Opção: '))
    
    if chur1 == 1:
        print()
        print('Maminha')
        print()
        peso = float(input('Digita a quantidade de gramas: '))
        print()
        
    elif chur1 == 2:
        print()
        print('Alcatra')
        print()
        peso = float(input('Digita a quantidade de gramas: '))
        print()
        
    elif chur1 == 3:
        print()
        print('Picanha')
        print()
        peso = float(input('Digita a quantidade de gramas: '))
        print()
        
    elif chur1 == 4:
        print()
        print('Voltando ao menu principal...')
        print()
        menu_principal()
    else:
        print()
        print('Opção inválida!')
        print()
        churrasco()
    def possivel_erro():
        if chur1 != float:
            print('Opção inválida!')
            churrasco()
        churrasco()
    def algo_mais1():
        algo_mais = int(input('Deseja algo mais? [1] SIM [2] NÃO: '))
        while (algo_mais):
            if algo_mais == 1:
                menu_principal()
            elif algo_mais == 2:
                print()
                print('Seu pedido foi encaminhado para nossa cozinha e logo estará pronto!')
                exit()
            else:
                print('Opção Inválida!\nTente Novamente!')
                algo_mais1()

def churrasco():
    print()
    print('[1] - Maminha (A partir de 100g)')
    print('[2] - Alcatra (A partir de 100g)')
    print('[3] - Picanha (A partir de 100g)')
    print('[4] - Voltar ao Menu Principal')

    chur1 = int(input('Escolha sua Opção: '))
    
    if chur1 == 1:
        print()
        print('Maminha')
        print()
        peso = float(input('Digita a quantidade de gramas: '))
        print()
        
    elif chur1 == 2:
        print()
        print('Alcatra')
        print()
        peso = float(input('Digita a quantidade de gramas: '))
        print()
        
    elif chur1 == 3:
        print()
        print('Picanha')
        print()
        peso = float(input('Digita a quantidade de gramas: '))
        print()
        
    elif chur1 == 4:
        print()
        print('Voltando ao menu principal...')
        print()
        menu_principal()
    else:
        print()
        print('Opção inválida!')
        print()
        churrasco()
    def possivel_erro():
        if chur1 != float:
            print('Opção inválida!')
            churrasco()
        churrasco()
    def algo_mais1():
        algo_mais = int(input('Deseja algo mais? [1] SIM [2] NÃO: '))
        while (algo_mais):
            if algo_mais == 1:
                menu_principal()
            elif algo_mais == 2:
                print()
                print('Seu pedido foi encaminhado para nossa cozinha e logo estará pronto!')
                exit()
            else:
                print('Opção Inválida!\nTente Novamente!')
                algo_mais1()
                
    algo_mais1()
menu_principal()