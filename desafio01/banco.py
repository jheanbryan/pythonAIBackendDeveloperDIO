menu = """
##################
Bem Vindo
Escolha uma opcao
1 - Deposito
2 - Saque
3 - Extrato
4 - sair
##################
"""
saldo = 0
qtdSaque = 0
extrato = ''
sair = False

while sair == False:
    op = float(input(menu))
    if op == 1:
        valorDeposito = int(input('Digite o Valor de Deposito: '))
        extrato+= f"\nDeposito no valor de R$ {valorDeposito:.2f}"
    elif op == 2:
        if qtdSaque <= 3:
            valorSaque = int(input('Digite o Valor de Saque: '))
            if valorSaque <= 500:
                if valorSaque <= saldo:
                    saldo -= valorSaque
                    qtdSaque+=1
                    print(f"\Saque no valor de R$ {valorSaque:.2f}")
                    extrato+= f"\Saque no valor de R$ {valorSaque:.2f}"
                else:
                    print(f"Saldo insuficiente: {saldo:.2f}")
            else:
                print('O valor maximo de saque deve ser de R$500.00!')
        else:
            print('A quantidade maxima de saques permitidos é 3!')
    elif op == 3:
        if len(extrato) == '':
            print('Nao foram realizadas movimentacoes')
        else:
            print(extrato)
    elif op == 4:
        sair = True
    else:
        print('Digite uma operacao valida!')
