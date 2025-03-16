sys = True
saldo = 0
valor_maximo = 500
depositos = []
qtd_saques = 0
LIMITE_SAQUE = 3

def deposita(valor, saldo, depositos):
    if valor <= 0:
        return f'Valor inválido', saldo

    saldo += valor
    depositos.append({'Depósito': valor})
    return f'\nDepósito realizado com sucesso!\n', saldo

def saca(saldo_atual, valor_saque, saques, saldo_excedido, maximo_excedido, qtd_saques_execedido, depositos):
    global qtd_saques  # Indica que estamos usando a variável global qtd_saques
    if saldo_excedido:
        print('Saldo Insuficiente.')
        return saldo_atual  # Retorna o saldo sem alterações
    elif maximo_excedido:
        print('Valor máximo de saque excedido.')
        return saldo_atual  # Retorna o saldo sem alterações
    elif qtd_saques_execedido:
        print('Quantidade saques diários excedidos.')
        return saldo_atual  # Retorna o saldo sem alterações
    elif valor_saque > 0:
        saldo_atual -= valor_saque
        depositos.append({'Saque': valor_saque})
        qtd_saques += 1  # Incrementa a quantidade de saques
        print('\nSaque realizado com sucesso\n')
        return saldo_atual  # Retorna o novo saldo
    else:
        return saldo_atual # retorna o saldo caso o valor do saque não seja válido.

def extrato(saldo_atual, depositos):
    print('\n##################################')
    print(f'Valor em conta: R${saldo_atual:.2f}\n')
    print('Depósitos realizados:\n')

    for i in depositos:
        for k, v in i.items():
            print(f'{k}: R${v:.2f}')
    print('##################################\n')

def execute_sys():
    opcao = int(input('--- Digite uma operação ---\n\n"1" para Depósitos \n"2" para Saque \n"3" para Visualizar Extrato \n"4" para Sair\n\n:: '))
    return opcao

while sys:
    opcao = execute_sys()

    if opcao == 1:
        valor = float(input('\nDigite o valor que deseja depositar: '))
        mensagem, saldo = deposita(valor, saldo, depositos)
        print(mensagem)

    elif opcao == 2:
        saque = float(input('\nDigite o valor que deseja sacar: '))

        saldo_excedido = saque > saldo

        maximo_excedido = saque > valor_maximo

        qtd_saques_execedido = qtd_saques >= LIMITE_SAQUE

        saldo = saca(saldo, saque, qtd_saques, saldo_excedido, maximo_excedido, qtd_saques_execedido, depositos) # Atualiza o saldo

    elif opcao == 3:
        extrato(saldo, depositos)

    elif opcao == 4:
        sys = False

    else:
        print('Valor inválido')
        continue
