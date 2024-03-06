menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Ver saldo
[5] Sair

"""



saldo = 0
limite = 500
extrato = ""
numero_de_saques = 0
LIMITE_SAQUES = 3


while True:

    print(menu)
    opcao = int(input('Escolha uma opcao: '))


#DEPOSITAR
    if opcao == 1:
        print('Você escolheu depositar')


        valor_deposito = float(input('Valor que deseja depositar: '))
        print(f'Valor depositado: R${valor_deposito},00')


        saldo += valor_deposito
        print(f'Seu saldo atual é R${saldo},00')

        extrato += f'Depositado: R${valor_deposito},00\n'
#DEPOSITAR



#SACAR
    elif opcao == 2:
        valor = float(input('Quanto deseja sacar? '))

        #VALIDAÇÕES
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saque =  numero_de_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print(f'Você está tentando sacar um valor maior do que possui, seu saldo é R${saldo},00')
        
        elif excedeu_limite:
            print(f'Limite de R${limite},00 excedido')

        elif excedeu_saque:
            print(f'Você excedeu seus saques de hoje, tente novamente amanha, limite de saque: {LIMITE_SAQUES}')
        
        elif valor > 0:
            print(f'Saque realizado com sucesso no valor de R${valor},00')
            saldo -= valor
            extrato += f'Saque de: R${valor},00\n'
            numero_de_saques += 1
#SACAR


#EXTRATO
    elif opcao == 3:
        print('Você escolheu extrato')
        if extrato != "":
            print(extrato)
        else:
            print('Nenhuma movimentação foi encontrada')
        print(f'Seu saldo atual é R${saldo},00')
#EXTRATO



#VER SALDO
    elif opcao == 4:
        print('Você escolheu ver saldo')
        print(f'Seu saldo atual é R${saldo},00')
#VER SALDO
        

#SAIR
    elif opcao == 5:
        print('Você escolheu sair')
        break
#SAIR


    else:
        print('Opção inválida')

