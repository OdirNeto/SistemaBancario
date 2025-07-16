import textwrap


def menu():
    menu = '''
    ======menu=====

    [1] Extrato
    [2] Depositar
    [3] Sacar
    [4] Criar Conta
    [5] Listar Contas
    [6] Cadastrar Novo Usuário
    [0] Sair

    ===============

    Por favor digite o numero da opção desejada: 
    '''
    return input(textwrap.dedent(menu))



def extrato_da_conta(saldo, /, *, extrato):
        print("\n------------------------EXTRATO------------------------")
        print("Você não realizou nenhuma transação até o momento" if not extrato else extrato)
        print(f"\nSeu saldo atual é de R${saldo:.2f}")
        print("---------------------------------------------------------")


def depositar(saldo, valor, extrato, /):
    if valor >= 1:
        saldo += valor
        extrato += f"Deposito: R$ {valor:.2f}\n"     
   
        print(f"\nA quantia de R${valor:.2f} foi depositada com sucesso. Seu saldo atual é de R${saldo:.2f}.")      
    
    else:
        print("O deposito não pode ser concluído pois o valor informado é inválido")
    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite_de_valor, saques_realizados, limite_de_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite_de_valor = valor > limite_de_valor
    excedeu_saques = saques_realizados >= limite_de_saques

    
    if excedeu_saldo:
        print("""
        Infelizmente não há saldo suficiente na sua conta.
        Fale com o seu gerente e ative o cheque especial para te ajudar em momentos como este.
        """)

    elif excedeu_limite_de_valor:
        print("""
        Para a sua segurança o valor limite por saque é de $R500.00. Tente um valor menor.
        """)

    elif excedeu_saques:
        print("""
                 Por motivo de segurança você atingiu o numero máximo de saques por dia.
                                     Selecione outra opção do menu:
                  """)

    elif valor >= 1:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        saques_realizados += 1
        print(f"""
        Saque realizado com sucesso. Seu saldo atual é de R${saldo:.2f}
        """)

    else:
        print("\nInfelizmente não conseguimos realizar a transação, o valor informado é inválido")

    return saldo, extrato


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Sua conta foi criada com sucesso ===\n=== Você já pode aproveitar as vantagens que só o nosso banco oferece para você ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    else:
        print("\nO cpf não está vinculado a nenhum usuário, para criar uma conta você deve primeiro cadastrar um novo usuário \nPara isso, favor digitar a opção [6] no menu principal e seguir todos os passos")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def criar_usuario(usuarios):
    cpf = input("Informe o numero do seu CPF (sem pontos ou caracteres especiais): ")
    cliente = filtrar_usuario(cpf, usuarios)

    if cliente:
        print("\nEsse CPF já está cadastrado em nosso sistema, favor procurar o gerente mais próximo.")
        return

    nome = input("Informe o seu nome completo: ")
    data_nascimento = input("Informe sua data de nascimento no seguinte formato: (dd-mm-aaaa): ")
    endereco = input("Informe seu endereço (logradouro, numero - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print(" ")
    print(f"\nUsuário cadastrado com sucesso! \nSeja bem vindo, {nome}")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [cliente for cliente in usuarios if cliente["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None







def main():
    LIMITE_DE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    saques_realizados = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()


        if opcao == "1":
            extrato_da_conta(saldo, extrato=extrato)


        elif opcao == "2":
            valor = float(input("\nInforme o valor do deposito: R$"))

            saldo, extrato = depositar(saldo, valor, extrato)


        elif opcao == "3":
            valor = float(input("Informe o valor do saque: R$"))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite_de_valor=limite,
                saques_realizados=saques_realizados,
                limite_de_saques=LIMITE_DE_SAQUES,
            )


        elif opcao == "4":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)


        elif opcao == "5":
            listar_contas(contas)


        elif opcao == "6":
            criar_usuario(usuarios)


        elif opcao == "0":
            sim_ou_nao = (input("""\nTem certeza que deseja sair? \nAo finalizar a sessão todos os seus dados serão apagados.
                            \nDigite [1] para sair ou qualquer outra tecla para continuar usando nosso sistema: """))
            if sim_ou_nao == "1":
                print("""
                                    Santo André
                Cuidamos do seu dinheiro para você cuidar do resto.
                  """)
                break
            else:
                opcao    



        else:
            print("Opção inválida, por favor selecione uma opção a seguir:")


main()
