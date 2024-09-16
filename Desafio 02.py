# Dados iniciais
clientes = {}
contas = {}
LIMITE_SAQUES = 3

# Função para exibir o menu principal
def exibir_menu():
    menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    => """
    return input(menu)

# Função para criar um cliente
def criar_cliente():
    nome = input("Informe o nome do cliente: ")
    cpf = input("Informe o CPF do cliente: ")
    if cpf in clientes:
        print("Cliente já cadastrado.")
    else:
        clientes[cpf] = nome
        print(f"Cliente {nome} cadastrado com sucesso!")

# Função para criar uma conta corrente e associar a um cliente
def criar_conta_corrente():
    cpf = input("Informe o CPF do cliente para vincular a conta: ")
    if cpf not in clientes:
        print("Cliente não encontrado. Cadastre o cliente primeiro.")
        return
    
    numero_conta = input("Informe um número para a conta: ")
    if numero_conta in contas:
        print("Conta já cadastrada.")
    else:
        contas[numero_conta] = {
            'cpf': cpf,
            'saldo': 0,
            'limite': 500,
            'extrato': "",
            'numero_saques': 0
        }
        print(f"Conta {numero_conta} cadastrada com sucesso!")

# Função para realizar um depósito
def depositar(conta):
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        contas[conta]['saldo'] += valor
        contas[conta]['extrato'] += f"Depósito: R$ {valor:.2f}\n"
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
    else:
        print("Operação falhou! O valor informado é inválido.")

# Função para realizar um saque
def sacar(conta):
    valor = float(input("Informe o valor do saque: "))
    saldo = contas[conta]['saldo']
    limite = contas[conta]['limite']
    numero_saques = contas[conta]['numero_saques']

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        contas[conta]['saldo'] -= valor
        contas[conta]['extrato'] += f"Saque: R$ {valor:.2f}\n"
        contas[conta]['numero_saques'] += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
    else:
        print("Operação falhou! O valor informado é inválido.")

# Função para visualizar o extrato da conta
def exibir_extrato(conta):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not contas[conta]['extrato'] else contas[conta]['extrato'])
    print(f"\nSaldo: R$ {contas[conta]['saldo']:.2f}")
    print("==========================================")

# Função principal do sistema bancário
def sistema_bancario():
    while True:
        opcao = exibir_menu()
        if opcao == "d":
            conta = input("Informe o número da conta: ")
            if conta in contas:
                depositar(conta)
            else:
                print("Conta não encontrada.")

        elif opcao == "s":
            conta = input("Informe o número da conta: ")
            if conta in contas:
                sacar(conta)
            else:
                print("Conta não encontrada.")

        elif opcao == "e":
            conta = input("Informe o número da conta: ")
            if conta in contas:
                exibir_extrato(conta)
            else:
                print("Conta não encontrada.")

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

# Função principal do menu inicial
def menu_inicial():
    while True:
        print("\n=== Sistema Bancário ===")
        print("[c] Criar Cliente")
        print("[b] Criar Conta Corrente")
        print("[p] Entrar no sistema bancário")
        print("[q] Sair")
        
        escolha = input("Escolha uma opção: ")

        if escolha == "c":
            criar_cliente()
        elif escolha == "b":
            criar_conta_corrente()
        elif escolha == "p":
            sistema_bancario()
        elif escolha == "q":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu_inicial()
