usu = [{'nome':'', 'data_nasc':'', 'cpf':'1', 'end':{'logradouro':'', 'numero':'', 'bairro':'', 'cidade': '', 'estado':''} } ]
cpf = input('Digite o cpf do usuario: ')

for cpf_cad in (usu):
    if cpf == cpf_cad['cpf']:
        print('Usuario já cadastrado')
    else:
        print('sem cadastro')
    
        

        
