class Funcionario:
    def __init__(self, id, nome, senha):
        self._id = id
        self._nome = nome
        self._senha = senha
    
    def login(self, id_input, senha_input):
        if id_input == self.id and senha_input == self.senha:
            return True
        else:
            return False

    ## Getters e setters
    def get_id(self):
        return self._id
    
    def get_nome(self):
        return self._nome
    
    def get_senha(self):
        return self._senha
    
    def set_id(self, novo_id):
        self.id = novo_id
        return True
    
    def set_nome(self, novo_nome):
        self.nome = novo_nome
        return True
    
    def set_senha(self, nova_senha):
        self.senha = nova_senha
        return True
    
class Gerente(Funcionario):
    def __init__(self, id, nome, senha, cargo):
        super().__init__(id, nome, senha)
        self.cargo = "Gerente"
    def cadastrar_funcionario(self):
        pass





### testes
if __name__ == "__main__":
    funcionario_1 = Funcionario("001", "Angelo", "Abc1")
    while True:
        try:
            print("\n### LOGIN ###")
            id_input = input("\nID do funcionário: ")
            senha_input = input("Senha: ")

            if funcionario_1.login(id_input,senha_input) == True:
                print("\n>> Acesso autorizado")
                break
            else:
                raise ValueError("ID ou senha invalido(s)!")
        except ValueError as e:
            print(f"\n>> Acesso negado!\
                  \nErro: {e}")
            continue