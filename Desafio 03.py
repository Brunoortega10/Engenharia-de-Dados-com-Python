import textwrap

class Cliente:
    def __init__(self, nome, data_nascimento, cpf, endereco):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco

    def __str__(self):
        return f"{self.nome} ({self.cpf})"

class Conta:
    def __init__(self, agencia, numero_conta, cliente):
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.cliente = cliente
        self.saldo = 0
        self.limite = 500
        self.extrato = ""
        self.numero_saques = 0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato += f"Depósito:\tR$ {valor:.2f}\n"
            print("\n=== Depósito realizado com sucesso! ===")
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    def sacar(self, valor, limite_saques, LIMITE_SAQUES):
        excedeu_saldo = valor > self.saldo
        excedeu_limite = valor > self.limite
        excedeu_saques = self.numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")
        elif excedeu_limite:
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")
        elif excedeu_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")
        elif valor > 0:
            self.saldo -= valor
            self.extrato += f"Saque:\t\tR$ {valor:.2f}\n"
            self.numero_saques += 1
            print("\n=== Saque realizado com sucesso! ===")
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    def exibir_extrato(self):
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not self.extrato else self.extrato)
        print(f"\nSaldo:\t\tR$ {self.saldo:.2f}")
        print("==========================================")

class Banco:
    def __init__(self):
        self.usuarios = []
        self.contas = []
        self.LIMITE_SAQUES = 3
        self.AGENCIA = "0001"

    def criar_usuario(self):
        cpf = input("Informe o CPF (somente número): ")
        if any(usuario.cpf == cpf for usuario in self.usuarios):
            print("\n@@@ Já existe usuário com esse CPF! @@@")
            return

        nome = input("Informe o nome completo: ")
        data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
        endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

        novo_usuario = Cliente(nome, data_nascimento, cpf, endereco)
        self.usuarios.append(novo_usuario)
        print("=== Usuário criado com sucesso! ===")

    def criar_conta(self):
        cpf = input("Informe o CPF do usuário: ")
        cliente = next((usuario for usuario in self.usuarios if usuario.cpf == cpf), None)

        if cliente:
            numero_conta = len(self.contas) + 1
            nova_conta = Conta(self.AGENCIA, numero_conta, cliente)
            self.contas.append(nova_conta)
            print("\n=== Conta criada com sucesso! ===")
            return nova_conta

        print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")

    def listar_contas(self):
        for conta in self.contas:
            linha = f"""\ 
                Agência:\t{conta.agencia}
                C/C:\t\t{conta.numero_conta}
                Titular:\t{conta.cliente.nome}
            """
            print("=" * 100)
            print(textwrap.dedent(linha))

def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))

def main():
    banco = Banco()
    while True:
        opcao = menu()

        if opcao == "d":
            numero_conta = int(input("Informe o número da conta: "))
            conta = next((c for c in banco.contas if c.numero_conta == numero_conta), None)
            if conta:
                valor = float(input("Informe o valor do depósito: "))
                conta.depositar(valor)
            else:
                print("Conta não encontrada.")

        elif opcao == "s":
            numero_conta = int(input("Informe o número da conta: "))
            conta = next((c for c in banco.contas if c.numero_conta == numero_conta), None)
            if conta:
                valor = float(input("Informe o valor do saque: "))
                conta.sacar(valor, banco.LIMITE_SAQUES, banco.LIMITE_SAQUES)
            else:
                print("Conta não encontrada.")

        elif opcao == "e":
            numero_conta = int(input("Informe o número da conta: "))
            conta = next((c for c in banco.contas if c.numero_conta == numero_conta), None)
            if conta:
                conta.exibir_extrato()
            else:
                print("Conta não encontrada.")

        elif opcao == "nu":
            banco.criar_usuario()

        elif opcao == "nc":
            banco.criar_conta()

        elif opcao == "lc":
            banco.listar_contas()

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()
