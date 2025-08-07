from datetime import datetime

dinheiro_disponivel_conta = 0.0
LIMITE_VALOR_SAQUE = 500
saques_realizados = 0
extrato = []

def sacar():
    global dinheiro_disponivel_conta, LIMITE_VALOR_SAQUE, saques_realizados

    valor_sacado = float(input('Digite o valor do saque: '))
    if saques_realizados == 3:
        print("Limite de saques diários atingido, tente novamente amanha.")

    elif valor_sacado > dinheiro_disponivel_conta:
        print("Saldo insuficiente para saque.")

    elif valor_sacado > LIMITE_VALOR_SAQUE:
        print("Limite máximo de saque de R$500,00 ultrapassado.")

    else:
        dinheiro_disponivel_conta -= valor_sacado
        print(f"Saldo disponível na conta: R${dinheiro_disponivel_conta:.2f}")
        data_modificada = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        extrato.append(f"Saque de R${valor_sacado:.2f} realizado em {data_modificada}")
        saques_realizados += 1

def mostra_extrato():
    for item in extrato:
        print(f"{item}")

def depositar():
    global dinheiro_disponivel_conta
    valor_depositado = float(input("Digite a quantia a ser depositada: "))

    if valor_depositado > 0:
        dinheiro_disponivel_conta += valor_depositado
        data_modificada = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        extrato.append(f"Deposito de R${valor_depositado:.2f} realizado em {data_modificada} ")
        print(f"Saldo disponível na conta: R${dinheiro_disponivel_conta:.2f}")

    else:
        print("Valor inválido para deposito.")

while True:

    opcao = int(input("""
------ Boas Vindas ao Banco DIO ------

[1] Depositar
[2] sacar
[3] Visualizar Extrato
[4] Sair

Selecione a opção que deseja realizar: """))

    if opcao == 1:
        depositar()

    if opcao == 2:
        sacar()

    if opcao == 3:
        mostra_extrato()

    if opcao == 4:
        break


