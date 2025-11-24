import customtkinter as ctk

from app.models.funcionarios_model import FuncionariosModel
from app.models.produtos_model import ProdutosModel

from app.views.login_view import LoginView
from app.views.home_view import HomeView

from app.views.rg_lote_view import RgLoteView
from app.views.ger_produtos_view import GerProdView
from app.views.ger_estoque_view import GerEstoqueView
from app.views.adm_funcionarios_view import AdmFuncView


class AppController:
    def __init__(self):
        ctk.set_default_color_theme("assets/themes/meu_tema1.json")
        ctk.set_appearance_mode("light")
        
        self.funcionarios_model = FuncionariosModel()
        self.produtos_model = ProdutosModel()
        self.root = ctk.CTk()
        self.root.geometry("900x650")
        self.show_login_view()
    

    def show_login_view(self):
        self.login_view = LoginView(self.root, self)
        self.login_view.pack(fill="both", expand=True)        
        
    # Controle de login do usuário
    def login(self, username, password):
        self.username = "@adm"
        password = None
        self.show_home(username)
                
    # Mostrar a tela inicial
    def show_home(self, username):
        self.login_view.destroy()
        self.home_view = HomeView(self, self.root, username)
        self.home_view.pack(fill="both", expand=True)
        
    def limpar_frame(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

    def show_rg_lote(self, conteudo_fr):
        self.limpar_frame(conteudo_fr)

        self.rg_lote_view = RgLoteView(conteudo_fr, self)
        self.rg_lote_view.pack(fill="both", expand=True) 

    def show_ger_produtos(self, conteudo_fr):
        self.limpar_frame(conteudo_fr)

        self.ger_produtos_view = GerProdView(conteudo_fr, self)
        self.ger_produtos_view.pack(fill="both", expand=True) 

    def show_adm_funcs(self, conteudo_fr):
        self.limpar_frame(conteudo_fr)

        self.adm_funcs_view = GerEstoqueView(conteudo_fr, self)
        self.adm_funcs_view.pack(fill="both", expand=True) 

    def show_adm_funcs(self, conteudo_fr):
        self.limpar_frame(conteudo_fr)

        self.rg_adm_funcs = AdmFuncView(conteudo_fr, self)
        self.rg_adm_funcs.pack(fill="both", expand=True) 


    def sair_show_login(self):
        self.root.destroy()
        
        self.root = ctk.CTk()
        self.root.geometry("900x650")
        self.show_login_view()

        self.run()



    # CRUD Produto
    # Create produto
    def inserir_produto(self, nome_prod, qtd_estoque):
        self.produtos_model.inserir_produto(nome_prod, qtd_estoque)
    
    # Read listar produtos
    def listar_produtos(self):
        produtos = self.produtos_model.listar_produtos()
        return produtos
    
    # Read selecionar produto
    def selecionar_produto(self, produto_id):
        produto_selecionado = self.produtos_model(produto_id)
        return produto_selecionado
    
    # Update produto
    def atualizar_produto(self, produto_id, novo_nome, nova_qtd_estoque):
        self.produtos_model.atualizar_produto(produto_id, novo_nome, nova_qtd_estoque)

    # Delete produto
    def excluir_produto(self, id_prod):
        self.produtos_model.excluir_produto(id_prod)
    
    # CRUD Lote
    # C lote
    def inserir_lote(self, produto_id, qtd_lote, fabricacao, validade, registro, responsavel):
        self.produtos_model.inserir_lote(produto_id, qtd_lote, fabricacao, validade, registro, responsavel)

    # CRUD Func




    def run(self):
        self.root.mainloop()
