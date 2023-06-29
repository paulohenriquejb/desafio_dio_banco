import textwrap
def menu():
    menu = """
    ================= MENU ============================
    [d]\t Depositar
    [s]\t sacar
    [e]\t Extrato
    [nc]\t Nova conta
    [lc]\t Listar contas
    [nu]\t Novo usuário
    [q]\t Sair
    
    =>"""
    return input(textwrap.dedent(menu))



def depositar(saldo, valor, extrato, /):

    if valor > 0:
        saldo = saldo + valor
        extrato += f"Deposito: R$ {valor:.2f}\n"
        print("\n ==== Depósito realizado com sucesso =====")
    else:
        print("\n @@@ Operação falhou! o valor informado é invalido. @@@")

    return saldo,extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo

    exceu_limite = valor > limite

    excedeu_saques = numero_de_saques >= limite_saques

    if excedeu_saldo:
            print("\n@@@operação falhou! você não tem saldo suficiente.@@@")
    elif exceu_limite:
            print("\n@@@operação falhou! o valor do saque excede o limite.@@@")
    elif excedeu_saques:
            print("\n@@@operação falhou! Número máximo de saques excedido.@@@")
    elif valor > 0 :
            saldo -= valor
            extrato += f"saque: R${valor:.2f}\n"
            numero_de_saques +=1
            print("\n==== Saque realizado com sucesso! =====")
    else:
            print("operação falhou! o valor informado é invalido")

    return saldo, extrato
        



def main():
    limite_saques = 3
    agencia = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("informe o valor do deposito: "))

            saldo, extrato = depositar(saldo, valor, extrato)
        elif opcao == "s":
            valor = float(input("informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques = numero_saques,
                limite_saques = limite_saques
                                        )
        elif opcao == "e":
            exibir_extrato(saldo, extrato = extrato)
        elif opcao == "nu":
            criar_usuario(usuarios)
        elif opcao == "nc":
            numero_conta = len(constas) + 1
            conta = criar_conta(agencia, numero_conta, usuarios)

            if conta:
                contas.append(conta)



main()



