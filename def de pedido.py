def refrigerantes(): #concluido momentaniamente
    print()
    print('[1] - Coca Lata')
    print('[2] - Coca Zero Lata')
    print('[3] - Guaraná Lata')
    print('[4] - Voltar ao Menu Principal')
    print()

    opcao1 = int(input('Escolha uma opção: '))
    if opcao1 == 1:
        print()
        print('Coca Lata')
        print()
        quantidade = float(input('Digite a quantidade: '))
        print()
    
    elif opcao1 == 2:
        print()
        print('Coca Zero Lata')
        print()
        quantidade = float(input('Digite a quantidade: '))
        print()

    elif opcao1 == 3:
        print()
        print('Guaraná Lata')
        print()
        quantidade = float(input('Digite a quantidade: '))
        print()

    elif opcao1 == 4:
        print()
        print('Voltando ao menu principal...')
        print()
        menu_principal()

    else:
        print('Opção inválida!')
        espetos()
    
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




    #def churrasco():
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