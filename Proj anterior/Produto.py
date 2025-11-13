import time

class Produto:
    def __init__ (self, id, nome, preco, quantidade):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    # Métodos
    def rg_chegada_de_insumo(self, data_recebimento, quantidade_recebida):
        self.quantidade += quantidade_recebida
        print(f"\nQuantidade de atualizada \nID {self.id} - {self.nome}: {self.quantidade} unidades -- RG {data_recebimento}")
        return
    
    def promocao(self, porcentagem_desconto):
        preco_promocao = self.preco - (porcentagem_desconto*self.preco/100)
        return float(f"{preco_promocao:.2f}")

    def verificar_estoque(self):
        if self.quantidade >= 10:
            return f"\n>> {self.quantidade} unidades de {self.nome} em estoque."
        elif self.quantidade < 10 and self.quantidade >= 5:
            return f"\n>> Estoque baixo!\n- {self.quantidade} unidade(s) de {self.nome}."
        elif self.quantidade < 5 and self.quantidade > 0:
            return f"\n>> Estoque muito baixo!\n- {self.quantidade} unidade(s) de {self.nome}."
        else:
            return f"\n>> ESTOQUE VAZIO!\n- Reposição imediata recomendada!"
        
    def confirmar_produto(self):
        confimacao = input(f"\nConfirme produto: \nID - {self.id} - {self.nome} (S/N): ") #transformação em método
        if confimacao.lower() == "n":
            return False
        elif confimacao.lower() =="s":
            return True
        else:
            print("\nOpção invalida")
            


    # Getters e Setters
    def get_id(self):
        return self.id
    
    def set_id(self, novo_id):
        try:
            self.id = int(novo_id)
            return True
        except ValueError:
            print ("id inválido, use apenas números inteiros")
            return False
        
    def get_nome(self):
        return self.nome
    
    def set_nome(self, novo_nome):
        self.nome = novo_nome
        return True

    def get_preco(self):
        return self.preco
    
    def set_preco(self, novo_preco):
        self.preco = novo_preco
        return True

    def get_quantidade(self):
        return self.quantidade
    
    def set_quantidade(self, novo_quantidade):
        self.quantidade = novo_quantidade
        return True



class Flor(Produto):
    def __init__(self, id, nome, preco, quantidade,tempo_vida,data_colheita):
        super().__init__(id, nome, preco, quantidade)
        self.tempo_vida = tempo_vida
        self.data_colheita = data_colheita
        

    def verificar_viabilidade_entrega(self, data_entrega):
        colheita = time.strptime(self.data_colheita,"%d/%m/%Y")
        colheita_segundos = time.mktime(colheita)
        validade_segundos = colheita_segundos+((self.tempo_vida)*60*60*24)
        entrega = time.strptime(data_entrega,"%d/%m/%Y")
        entrega_segundos = time.mktime(entrega)
        if entrega_segundos > validade_segundos:
            print("\nNão é possivel fazer a entregar")
        else:
            dias=int((validade_segundos-entrega_segundos)/(60*60*24))
            print(f"\nA entregar viável dias {dias}")

    def get_tempo_vida(self):
        return f"{self.tempo_vida} dias"

    def set_tempo_vida(self, novo_tempo_vida):
        self.tempo_vida = novo_tempo_vida
        return True

    def get_data_colheita(self):
        return self.data_colheita

    def set_data_colheita(self, novo_data_colheita):
        self.data_colheita = novo_data_colheita
        return True

# Testes de código
if __name__ == "__main__":
    #instanciando objeto para teste
    f1 = Flor(1, "Rosa Vermelha", 10.90, 5, 10, "05/08/2025")
            # id, nome,           preco, qtd, vida, colheita

    
    # testando getters e setters
    # herdados
    print(f"\nID - {f1.get_id()}\
          \n{f1.get_nome()}\
          \n{f1.get_preco():.2f}\
          \n{f1.get_quantidade()} unidades")
    
    
    print("\nAntes")
    print("colheita:",f1.get_data_colheita())
    print("vida:",f1.get_tempo_vida())
    
    # método específico
    f1.verificar_viabilidade_entrega("16/08/2025")
    
    f1.set_data_colheita("06/08/2025")
    f1.set_tempo_vida(15)
    
    print("\nDepois")
    print("colheita:",f1.get_data_colheita())
    print("vida:",f1.get_tempo_vida())

    f1.verificar_viabilidade_entrega("16/08/2025")


    print(f"\n{"-"*10}fim{"-"*10}\n")
