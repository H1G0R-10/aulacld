class CadastroCliente:  
    def __init__(self):  
        self.cadastro = []  

    def cadastrar_cliente(self, cliente):  
        if len(cliente.nome) < 3:
            return "Cadastro não realizado, nome sem 3 caracteres"
        self.cadastro.append(cliente)  
        if len(self.cadastro) > 0:  # Verifica se há clientes cadastrados  
            return "Cadastro ok, criado"  # Mensagem corrigida  