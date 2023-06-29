menu = """
[d] depoistar
[s] sacar
[e] extrado
[q] sair
"""


saldo = 0
limite = 500
extrato = ""
numero_de_saques = 0
limite_saques = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("imforme o valor do deposito"))

        if valor > 0:
            saldo = saldo + valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
        else:
            print("operação falhou! o valor informado é invalido.")

       
    elif opcao == "s":
        valor = float(input("informe o valor do saque:  "))

        excedeu_saldo = valor > saldo

        exceu_limite = valor > limite

        excedeu_saques = numero_de_saques >= limite_saques


        if excedeu_saldo:
            print("operação falhou! você não tem saldo suficiente.")
        elif exceu_limite:
            print("operação falhou! o valor do saque excede o limite.")
        elif excedeu_saques:
            print("operação falhou! Número máximo de saques excedido.")
        elif valor > 0 :
            saldo -= valor
            extrato += f"saque: R${valor:.2f}\n"
            numero_de_saques +=1
        else:
            print("operação falhou! o valor informado é invalido")
       
    elif opcao == "e":
        print("====================  EXTRATO ========================")
        print("nao foram realizadas movimentações.  " if not extrato else extrato)
        print(f"\n saldo: R${saldo:.2f}")
        print("=======================================================")
    elif opcao == "q":
        print("obrigado por ser cliente do nosso banco")
        break
    else:
        print("operação invalida, por favor selecione novamente a operação desejada")
