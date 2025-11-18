import customtkinter as ctk
from app.views.rg_lote_view import RgLoteView


class HomeView(ctk.CTkFrame):
    # def __init__(self, user, parent, controller):
    def __init__(self, controller, parent, username):
        super().__init__(parent)
        self.controller = controller
        self.parent = parent
        self.user = username
        
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        
        # Menu no topo 
        self.top_menu_fr = ctk.CTkFrame(self, width=200)
        self.top_menu_fr.grid(row=0, column=0, stick="nsew")
        
        # Frame de conteúdo das "abas"
        self.conteudo_fr = ctk.CTkFrame(self, fg_color="gray")
        self.conteudo_fr.grid(row=1, column=0, stick="nsew")
        
        if "@adm" in username:
            self.show_top_menu_adm()
        elif not "@adm" in username:
            self.show_top_menu_geral()
        
       
        # criar self.btn_sair



    # MENU GERAL (FUNCIONÁRIOS)
    def show_top_menu_geral(self):
        self.btn_rg_lote = ctk.CTkButton(self.top_menu_fr, text="Registrar\n novo lote", command=self.show_rg_lote)
        self.btn_rg_lote.pack(padx=10, pady=10, expand=True, side="left")
        
        self.btn_ger_produtos = ctk.CTkButton(self.top_menu_fr, text="Gerenciar\nProdutos", command=self.show_ger_produtos)
        self.btn_ger_produtos.pack(padx=10, pady=10, expand=True, side="left")
        
        self.btn_ger_lotes = ctk.CTkButton(self.top_menu_fr, text="Gerenciar\nLotes", command=self.show_ger_lotes)
        self.btn_ger_lotes.pack(padx=10, pady=10, expand=True, side="left")
        
        
    # MENU ADMINISTRADOR  
    def show_top_menu_adm(self):
        self.show_top_menu_geral()
        
        self.btn_adm_funcs = ctk.CTkButton(self.top_menu_fr, text="Administrar\nFuncionários", command=self.show_adm_funcs)
        self.btn_adm_funcs.pack(padx=10, pady=10, expand=True, side="left")
        
        
        
    # limpar frame de conteúdo
    def limpar_conteudo_fr(self):
        self.controller.limpar_frame(self.conteudo_fr)

                       
    
    def show_rg_lote(self):
        self.limpar_conteudo_fr()
        
        self.rg_lote_view = RgLoteView(self.conteudo_fr, self.controller)
        self.rg_lote_view.pack(padx=10, pady=10, fill="both", expand=True)      
        
        
        
    def show_ger_produtos(self):
        self.limpar_conteudo_fr()
        titulo_sessao = ctk.CTkLabel(self.conteudo_fr, text="GER PRODUTOS")
        titulo_sessao.pack()
        
    def show_ger_lotes(self):
        self.limpar_conteudo_fr()

        titulo_sessao = ctk.CTkLabel(self.conteudo_fr, text="GER LOTES")
        titulo_sessao.pack()
        
    def show_adm_funcs(self):
        self.limpar_conteudo_fr()
    
        titulo_sessao = ctk.CTkLabel(self.conteudo_fr, text="ADM FUNCIONÁRIOS")
        titulo_sessao.pack()
            
            
    