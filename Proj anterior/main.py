from Produto import Produto
# instanciação de produtos para testes # enquanto não há permanencia de dados
p1 = Produto(1, "Rosas Brancas", 24.90, 20)
p2 = Produto(2, "Rosas Vermelhas", 29.90, 10)
p3 = Produto(3, "Tulipa", 34.90, 9)
p4 = Produto(4, "Girassol", 14.90, 5)
p5 = Produto(5, "Orquídia", 34.90, 4)
p6 = Produto(6, "Rosa Cor de Rosa", 21.90, 1)
p7 = Produto(7, "Muda de Jasmim", 9.90, 0)

produtos = [p1,p2,p3,p4,p5,p6,p7] 
estoque_dados = {} # dados tratados para implementação de salvamento 

def menu(): 
    while True:
        print("\n--- Menu ---")
        print("1. Listar produtos em estoque")
        print("2. Cadastrar novo produto")
        print("3. Editar produto")     
        print("4. Excluir produto")
        print("5. Registrar recebimento de insumos")
        print("6. Calcular valor promocional")
        print("7. Verificar estoque de produto")
        print("8. Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            listar_produtos()
        elif opcao == "2":
            cadastrar_produto()
        elif opcao == "3":
            editar_produto()
        elif opcao == "4":
            excluir_produto()
        elif opcao == "5":
            registrar_recebimento_insumo()
        elif opcao == "6":
            calc_promocao()
        elif opcao == "7":
            verificar_estoque()
        elif opcao == "8":
            sair()
        else:
            print("Opção inválida. Tente novamente.")

def listar_produtos():
    print("\nProdutos disponíveis em estoque:")
    for produto in produtos:
        print(f"ID {produto.id} - {produto.nome} - R$ {produto.preco:.2f} - {produto.quantidade} unidades")

def cadastrar_produto():
    print("\n--- Cadastro de Novo Produto ---")
    try:
        nome = input("Nome do produto: ").strip()
        preco = float(input("Preço do produto (ex: 19.90): "))
        quantidade = int(input("Quantidade em estoque: "))

        # Gerar novo ID automático baseado no maior ID atual
        novo_id = ((produtos[-1]).get_id()) + 1
        novo_produto = Produto(novo_id, nome, preco, quantidade)
        
        produtos.append(novo_produto)

        # dados tratados para implementação de salvamento # Uppar dados (posteriormente em json)
        estoque_dados[novo_produto.id] = {"nome":novo_produto.nome, "preço":novo_produto.preco, "quantidade":novo_produto.quantidade}
        print(f"\nProduto cadastrado \nID {novo_produto.id} - {estoque_dados[novo_produto.id]}!")

    except ValueError:
        print("Erro: Entrada inválida. Tente novamente com os dados corretos.")

def editar_produto():
    listar_produtos()
    try:
        id_input = int(input("\nID do produto que deseja editar: "))
        for produto in produtos:
            if produto.id == id_input:
                print(f"Editando produto: ID {produto.id} - {produto.nome}")
                novo_nome = input("Novo nome (deixe em branco para manter o atual): ").strip()
                novo_preco = input("Novo preço (deixe em branco para manter o atual): ").strip()
                nova_qtd = input("Nova quantidade (deixe em branco para manter a atual): ").strip()

                if novo_nome:
                    produto.nome = novo_nome
                if novo_preco:
                    produto.preco = float(novo_preco)
                if nova_qtd:
                    produto.quantidade = int(nova_qtd)

                print("Produto atualizado com sucesso.")

    except ValueError:
        print("Entrada inválida. Tente novamente.")



def excluir_produto():
    listar_produtos()
    try:
        id_input = int(input("\nID do produto que deseja excluir: "))
        for produto in produtos:
            if produto.id == id_input:
                confirmacao = input(f"\nTem certeza que deseja excluir '{produto.nome}'? (S/N): ")
                if confirmacao.lower() == 's':
                    produto_exluido = produtos.pop((produto.get_id())-1)
                    print(f"Produto {produto_exluido.get_nome()} excluído com sucesso.")
                else:
                    print("Operação cancelada.")

    except ValueError:
        print("Entrada inválida.")

def registrar_recebimento_insumo():
    id_input = int(input("\nID do produto que deseja registrar: "))
    for produto in produtos:
        if id_input == produto.id:
            confimacao = input(f"\nConfirme produto: \nID - {produto.get_id()} - {produto.get_nome()} (S/N): ")
            if confimacao.lower() == "n":
                return
            elif confimacao.lower() =="s":
                data_recebimento = input("Data: ")
                quantidade_recebida = int(input("Quantidade recebida: "))
                produto.rg_chegada_de_insumo(data_recebimento, quantidade_recebida)
            else:
                print("Opção invalida")
                registrar_recebimento_insumo() # modificar para try except
    
def calc_promocao():
    id_input = int(input("\nID do produto: "))
    for produto in produtos:
        if id_input == produto.id:
            if produto.confirmar_produto() == True:
                porcentagem_desconto = float(input("\nDigite a porcentagem a ser descontada: "))
                print(f"{produto.get_nome()}\nDesconto: - R$ {(produto.preco - produto.promocao(porcentagem_desconto)):.2f} \nPreço promocional: R$ {produto.promocao(porcentagem_desconto)}")
            else:
                calc_promocao() # modificar para try except (?)

def verificar_estoque():
    while True:
        try:
            id_input = int(input("\nID do produto: "))  
            produto_encontrado = None
            for produto in produtos:
                if id_input == produto.get_id():
                    produto_encontrado = produto
                    break
            if produto_encontrado:
                if produto.confirmar_produto() == True:
                    print(produto.verificar_estoque())
                    return
            else:
                raise ValueError("ID não encontrado. Tente novamente.")
        except ValueError as e:
            print(f"\nErro: {e}")
            continue

def inicio():
    print("\nCONTROLE DE ESTOQUE")
    menu()
    
def sair():
    print("Encerrando o sistema. Até logo!")
    exit()

# Iniciar o sistema
inicio()
