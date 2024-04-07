g_num_saques = 0
seq_conta = 1
conta = []
usuario = []

def deposito(valor, saldo, extrato, i):
    saldo += valor
    extrato = 'Deposito = R${:.2f}\n'.format(valor)
    conta[i]['deposito'] = valor
    return(historico(extrato = extrato, saldo = saldo, i = i ))

def historico(extrato = '', saldo = 0, i = 0 ):
    conta[i]['saldo'] = str(saldo)
    conta[i]['extrato'] += extrato
   
    
def imp_ext(i):
    if test_ext(i):
        print('*' *35)
        print('{:^35}'.format('   OPERAÇÃO EXTRATO    ' ))
        print('*' *35)
        print(f'Numero da conta: {conta[i]["num_conta"]}')
        print(f'Numero da agencia: {conta[i]["agencia"]}')
        print(f'Nome do usuario: {conta[i]["usuario"]["nome"]}')
        print('*' *35)
        print (conta[i]['extrato'])
        print ('Saldo = {:.2f}'.format(float(conta[i]['saldo'])))
    
def test_valor():
    valor = float(input('Valor do deposito/saque: ')) 
    if valor > 0:
        return(valor)
    else:
        print('Somente são aceitos valores positivos.')
        return(0)
        
def test_ext(i):
    if  conta[i]['extrato'] == '':
        print('Nao foram realizadas movimentações')
        print('saldo = R${:.2f}'.formafloat)
    else:
        return(True)
    
def test_saques(valor):
    if 0 < valor <= 500 and float(conta[i]["saldo"]) >= valor and  g_num_saques < 3:
            return(valor)
    else:
        print('Não foi possivel executar a operação saque.')
        print('Saldo insuficiente.')if float(conta[i]["saldo"]) < valor else ''
        print('Numero de saques excessivo')if g_num_saques >= 3 else ''
        print('Valor acima do limite (R$500,00)')if valor > 500 else ''  
        return(0)
        
def saque(valor):
    global g_num_saques
    saldo_atu =  float(conta[i]["saldo"]) - valor
    g_num_saques += 1
    conta[i]['saque'] = valor
    print(f'Efetuado saque de R${valor:.2f}\nSaldo atualizado: R${saldo_atu:.2f}')
    extrato = 'Saque = R${:.2f}\n'.format(valor)
    return(historico(extrato = extrato, saldo = saldo_atu))

def cadastrar_usu():
    usu = [{'nome':'', 'data_nasc':'','cpf':'', 'end':{'logradouro':'', 'numero':'', 'bairro':'', 'cidade': '', 'estado':''} } ]
    cpf = str(input('Digite o cpf do usuario: ')).replace(' ', '')
    if not test_usu(cpf):
        usu[0]['cpf'] = cpf
        usu[0]['nome'] = input('Digite o nome do usuario: ')
        usu[0]['data_nasc'] = input('Digite a data de nascimento do usuario: ')
        usu[0]['end']['logradouro'] = input('Digite o logradouro: ')
        usu[0]['end']['numero'] = input('Digite o numero: ')
        usu[0]['end']['bairro'] = input('Digite o bairro: ')
        usu[0]['end']['cidade'] = input('Digite a cidade: ')
        usu[0]['end']['estado'] = input('Digite o estado: ')
        usuario.extend(usu)
        print('\nUsuario cadastrado com sucesso!.')
        usu = []
    
        
def test_usu(cpf):
    for cpf_cad in (usuario):
        if cpf == cpf_cad['cpf']:
            print('Usuario já cadastrado')
            return(True)
 
def test_cont(cpf):
    for indice, cpf_cad in enumerate(usuario):
        if cpf == cpf_cad['cpf']:
            return(indice)    
      
def criar_conta():
    global seq_conta
    cont = [{'agencia': '0001', 'num_conta':'', 'usuario':'', 'deposito':'', 'saque':'', 'extrato':'', 'saldo':''}]
    cpf = str(input('Digite o cpf do usuario a criar conta: ')).replace(' ', '')
    if test_usu(cpf):
        cont[0]['num_conta'] = str(seq_conta)
        seq_conta += 1
        x = test_cont(cpf)
        cont[0]['usuario'] = usuario[x]
        conta.extend(cont)
        print('\nConta cadastrada com sucesso!.')
    else:
         print('\nCPF não cadastrado como usuario.')
        

    
def listar_contas():
    for i in range (len(conta)):
        print(f' Numero da conta: {conta[i]["num_conta"]}')
        print(f' Numero da agencia: {conta[i]["agencia"]}')
        print(f' Nome do usuario: {conta[i]["usuario"]["nome"]}')
        print(f' Data de nascimento: {conta[i]["usuario"]["data_nasc"]}')
        print(f' CPF: {conta[i]["usuario"]["cpf"]}')
        print(f' Logradouro: {conta[i]["usuario"]["end"]["logradouro"]}')
        print(f' Numero: {conta[i]["usuario"]["end"]["numero"]}')
        print(f' Bairro: {conta[i]["usuario"]["end"]["bairro"]}')
        print(f' Cidade: {conta[i]["usuario"]["end"]["cidade"]}')
        print(f' Estado: {conta[i]["usuario"]["end"]["estado"]}')
        print('*' *35)
         
    
        
def listar_usuarios():
    for i in range (len(usuario)):
        print(f' Nome do usuario: {usuario[i]["nome"]}')
        print(f' Data de nascimento: {usuario[i]["data_nasc"]}')
        print(f' CPF: {usuario[i]["cpf"]}')
        print(f' Logradouro: {usuario[i]["end"]["logradouro"]}')
        print(f' Numero: {usuario[i]["end"]["numero"]}')
        print(f' Bairro: {usuario[i]["end"]["bairro"]}')
        print(f' Cidade: {usuario[i]["end"]["cidade"]}')
        print(f' Estado: {usuario[i]["end"]["estado"]}')
        print('*' *35)
        
def test_dep_saque():
    cpf = input('Informe o CPF: ')
    if test_usu(cpf):
        i = test_cont(cpf)
        print(f'Numero da conta: {conta[i]["num_conta"]}')
        print(f'Numero da agencia: {conta[i]["agencia"]}')
        print(f'Nome do usuario: {conta[i]["usuario"]["nome"]}')
        print('*' *35)
        return(i)
    else:
        print('Não foi possivel executar a operação.')
        print('CPF confirmado não tem conta.')
        print('*' *35)
        return(-1)
              
def test_conf():
    
    conf = input('Confirma dados [S/N]: \n').upper()
    if conf == 'S':        
        return(True)
    else:
        print('Não foi possivel executar a operação.')
        print('*' *35)

print('*' *35)
print('{:^35}'.format('   BANCO DO PAULÃO    ' ))
print('*' *35)
menu = '''
[d] depositar
[s] sacar
[e] extrato
[u] cadastrar usuario
[c] criar conta
[l] listar contas
[x] listar usuarios
[q] sair

=> '''
    
while True:
    opcao = input(menu)
    if opcao == 'd':
        print('*' *35)
        print('{:^35}'.format('   OPERAÇÃO DEPÓSITO    ' ))
        print('*' *35)
        i = test_dep_saque()
        if test_conf():
            valor = test_valor()
            if valor > 0:
                    deposito(valor, 0, '', i)
                    print(f'Efetuado deposito de R${valor:.2f}')
                    print('*' *35)
        else:
           print('Não foi possivel executar a operação deposito.')
           print('*' *35) 
    elif opcao == 's':
        print('*' *35)
        print('{:^35}'.format('   OPERAÇÃO SAQUE    ' ))
        print('*' *35)
        i = test_dep_saque()
        if test_conf():
            valor = test_saques(test_valor())
            if valor > 0:
                saque(valor = valor)
            print('*' *35)
    elif opcao == 'e':
        print('*' *35)
        print('{:^35}'.format('   OPERAÇÃO EXTRATO    ' ))
        print('*' *35)
        i = test_dep_saque()
        if i != -1:
            if test_conf():
                imp_ext(i)
                print('*' *35)
        
    elif opcao == 'u':
        print('*' *35)
        print('{:^35}'.format('   OPERAÇÃO CADASTRAR USUARIO    ' ))
        print('*' *35)
        cadastrar_usu()
        print('*' *35)
        
    elif opcao == 'c':
        print('*' *35)
        print('{:^35}'.format('   OPERAÇÃO CRIAR CONTA   ' ))
        print('*' *35)
        criar_conta()
        print('*' *35)
        
    elif opcao == 'l':
        print('*' *35)
        print('{:^35}'.format('   OPERAÇÃO LISTAR CONTAS    ' ))
        print('*' *35)
        listar_contas()
        print('*' *35)
        
    elif opcao == 'x':
        print('*' *35)
        print('{:^35}'.format('   OPERAÇÃO LISTAR USUARIOS    ' ))
        print('*' *35)
        listar_usuarios()
        print('*' *35)
            
    elif opcao == 'q':
        print('*' *35)
        print('{:^35}'.format('   OBRIGADO. FIM DA OPERAÇÃO    ' ))
        print('*' *35)
        break
    else:
        print('Opção invalida. Por favor selecione novamente a opção desejada')

            
        
                    