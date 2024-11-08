from cliente import Cliente  
from cadastrar_cliente import CadastroCliente  

def test_cadastro_cliente_com_sucesso():  
    cliente = Cliente('will', 20, 'will@teste.com')  
    cadastro_cliente = CadastroCliente()  
    resposta = cadastro_cliente.cadastrar_cliente(cliente)  
    assert resposta == "Cadastro ok, criado"  

def test_cadastro_cliente_com_nome_menor_que_tres_caracteres():  
    cliente = Cliente('wi', 20, 'will@teste.com')  
    cadastro_cliente = CadastroCliente()  
    resposta = cadastro_cliente.cadastrar_cliente(cliente)  
    assert resposta == "Cadastro não realizado, nome sem 3 caracteres"  