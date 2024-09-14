# Importação de módulos necessários para obter o horário dos saques
from datetime import datetime
import pytz

# Opções do menu
menu = """

Selecione uma opção.

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>"""

# Declaração de algumas variáveis e constantes necessárias
LIMITE = 500
quantidade_saques = 0
saldo = 0
lista_saques = []
LIMITE_SAQUES = 3 # 3

while True:
    opcao = input(menu).lower() # Obter a opção do usuário

    # Opção de depósito
    if opcao == 'd':
        while True:
            valor_base = input('Insira um valor a depositar: R$')
            valor_base = valor_base.replace(',', '.')

            # Checa se o valor contém números para converter para float
            if valor_base.replace('.', '', 1).isdigit():
                valor_a_depositar = float(valor_base)

                if valor_a_depositar > 0:
                    saldo += valor_a_depositar

                    print(f'O valor de RS{valor_a_depositar:.2f} foi depositado!')
                    break
                print('Erro! Insira um valor positivo.')

            else:
                print('Erro! Insira apenas números!')
                break

    elif opcao == 's': # Opção de saque
        valor_base_saque = input('Insira um valor para ser sacado: R$')
        valor_base_saque = valor_base_saque.replace(',', '.')

         # Checa se o valor contém números para converter para float
        if valor_base_saque.replace('.', '', 1).isdigit():
            valor_a_sacar = float(valor_base_saque)

            # Sequência de if/elif/else para realizar as operações necessárias
            # e tratar os erros
            if saldo > 0 and valor_a_sacar > 0:
                if valor_a_sacar <= saldo and LIMITE_SAQUES > 0 and valor_a_sacar <= LIMITE:
                    saldo -= valor_a_sacar
                    LIMITE_SAQUES -= 1
                    quantidade_saques += 1

                    lista_saques.append({
                        'Valor Sacado': valor_a_sacar,
                        'Data do Saque': datetime.now(pytz.timezone('America/Sao_Paulo')).strftime('%d/%m/%Y, %H:%M')
                    })

                    print(f'Saque realizado! Novo saldo R${saldo:.2f}')

                elif LIMITE_SAQUES == 0:
                    print('Você atingiu seu LIMITE diário de saques! Tente amanhã')

                elif valor_a_sacar >= LIMITE:
                    print(f'Não é possível sacar um valor maior que seu LIMITE atual de R${LIMITE:.2f}')

                else:
                    print('Saldo insuficiente!')

            else:
                print('Erro! Saldo insuficiente ou valor a sacar inválido!')

        else:
            print('Erro! Valor a sacar inválido!')

    elif opcao == 'e': # Opção de extrato
        print('===Extrato da conta bancária===')
        print(f'Saldo disponível R${saldo:.2f}')
        print(f'Quantidade de saques realizados: {quantidade_saques}')
        print()

        if not lista_saques:
            print('Não houveram movimentações')

        for extratos in lista_saques:
            print('-' * 30)

            for chave, valor in extratos.items():
                if chave == 'Valor Sacado':
                    print(f'{chave}: R${valor:.2f}')
                else:
                    print(f'{chave}: {valor}')

            print('-' * 30)

    elif opcao == 'q': # Opção de sair do sistema
        print('Saindo da conta! Obrigado por nos acessar!')
        break

    else:
        print('Operação inválida etc...')
