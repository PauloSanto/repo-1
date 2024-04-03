print('*' *35)
print('{:^35}'.format('   BANCO DO PAULÃO    ' ))
print('*' *35)
menu = '''
[d] depositar
[s] sacar
[e] extrato
[q] sair

=> '''

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = int(3)
num = 0
cont = 0
while True:
    
    opcao = input(menu)
    
    if opcao == 'd':
        print('*' *35)
        print('{:^35}'.format('   OPERAÇÃO DEPÓSITO    ' ))
        print('*' *35)
        num = float(input('Valor do deposito: ')) 
        if num > 0:
            saldo += num
            cont += 1
        else:
            print('Somente são aceitos valores positivos para deposito.')
            
        extrato += f'{str(cont)} - deposito = R${num:.2f}\n'
        
    elif opcao == 's':
        print('*' *35)
        print('{:^35}'.format('   OPERAÇÃO SAQUE    ' ))
        print('*' *35)
        num = float(input('Valor do saque: ')) 
        if 0 < num <= 500 and saldo >= num and  numero_saques < LIMITE_SAQUES:
            saldo -= num
            cont += 1
            numero_saques += 1
            print(f'Efetuado saque de R${num:.2f}\nSaldo atualizado: R${saldo:.2f}')
            extrato += f'{str(cont)} - saque = R${num:.2f}\n'
        else:
            print('Não foi possivel executar a operação saque.')
            print('Saldo insuficiente.')if saldo < num else ''
            print('Numero de saques excessivo')if numero_saques >= LIMITE_SAQUES else ''
            print('Valor acima do limite (R$500,00)')if num > 500 else ''  
            print('Valor negativo ou zerado')if num <= 0 else''  
    elif opcao == 'e':
        print('*' *35)
        print('{:^35}'.format('   OPERAÇÃO EXTRATO    ' ))
        print('*' *35)
        print('Nao foram realizadas movimentações' if not extrato else extrato)
        print('saldo = R${:.2f}'.format(saldo))
        print('*' *35)

    elif opcao == 'q':
        print('*' *35)
        print('{:^35}'.format('   OBRIGADO. FIM DA OPERAÇÃO    ' ))
        print('*' *35)
        break
    
    else:
        print('Opção invalida. Por favor selecione novamente a opção desejada')
                    