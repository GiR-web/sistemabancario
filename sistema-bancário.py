import sys

saldo = 0.0
extrato = []
num_saques = 0
LIMITE_SAQUES = 3
LIMITE_VALOR_SAQUE = 500

while True:
    print("""
========= MENU =========
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
========================
""")
    opcao = input("Escolha a opção: ").strip().lower()

    if opcao == "d":
        try:
            valor = float(input("Informe o valor do depósito: R$"))
            if valor <= 0:
                print("Valor inválido! O depósito deve ser positivo.")
            else:
                saldo += valor
                extrato.append(f"Depósito: + R${valor:.2f}")
                print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        except ValueError:
            print("Entrada inválida! Informe um valor numérico.")
            
    elif opcao == "s":
        if num_saques >= LIMITE_SAQUES:
            print("Limite de saques diários atingido!")
        else:
            try:
                valor = float(input("Informe o valor do saque: R$"))
                if valor <= 0:
                    print("Valor inválido! O saque deve ser positivo.")
                elif valor > LIMITE_VALOR_SAQUE:
                    print(f"O limite por saque é de R${LIMITE_VALOR_SAQUE:.2f}.")
                elif valor > saldo:
                    print("Saldo insuficiente para saque.")
                else:
                    saldo -= valor
                    extrato.append(f"Saque: - R${valor:.2f}")
                    num_saques += 1
                    print(f"Saque de R${valor:.2f} realizado com sucesso.")
            except ValueError:
                print("Entrada inválida! Informe um valor numérico.")
                
    elif opcao == "e":
        print("\n======= EXTRATO =======")
        if not extrato:
            print("Não foram realizadas movimentações.")
        else:
            for movimento in extrato:
                print(movimento)
        print(f"\nSaldo atual: R${saldo:.2f}")
        print("========================\n")
        
    elif opcao == "q":
        print("Saindo do sistema. Obrigado!")
        sys.exit()
        
    else:
        print("Operação inválida! Por favor, escolha uma opção válida.")
