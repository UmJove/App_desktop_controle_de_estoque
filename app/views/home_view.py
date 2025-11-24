import customtkinter as ctk


class HomeView(ctk.CTkFrame):
    # def __init__(self, user, parent, controller):
    def __init__(self, controller, parent, username):
        super().__init__(parent)
        self.controller = controller
        self.parent = parent
        self.configure(fg_color="transparent")

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=0)
        self.rowconfigure((0, 2), weight=0)
        self.rowconfigure(1, weight=1)
        
        # Divisões pricipais da janela

        # Frame - Menu no topo 
        self.top_menu_fr = ctk.CTkFrame(self, width=200, fg_color="transparent")
        self.top_menu_fr.grid(row=0, column=0, stick="ns")
        
        # Frame - Conteúdo 
        self.conteudo_fr = ctk.CTkFrame(self, fg_color='transparent')
        self.conteudo_fr.grid(row=1, column=0, stick="nsew")


        if "@adm" in self.controller.username:
            self.show_top_menu_adm()
        elif not "@adm" in self.controller.username:
            self.show_top_menu_geral()
        
        self.show_rg_lote()
       
        # Frame - Rodapé 
        self.rodape_fr = ctk.CTkFrame(self, fg_color="transparent" , border_width=2, border_color='magenta')
        self.rodape_fr.grid(row=2, column=0, stick="nsew")

        self.btn_rg_lote = ctk.CTkButton(self.rodape_fr, text="Sair", command=self.sair)
        self.btn_rg_lote.pack(padx=10, pady=5, side="right", expand=True)



    # MENU GERAL (FUNCIONÁRIOS)
    def show_top_menu_geral(self):
        self.btn_rg_lote = ctk.CTkButton(self.top_menu_fr, text="Registrar\n novo lote", command=self.show_rg_lote)
        self.btn_rg_lote.pack(padx=10, pady=5, side="left", expand=True)
        
        self.btn_ger_produtos = ctk.CTkButton(self.top_menu_fr, text="Gerenciar\nProdutos", command=self.show_ger_produtos)
        self.btn_ger_produtos.pack(padx=10, pady=5, side="left", expand=True)
        
        self.btn_ger_lotes = ctk.CTkButton(self.top_menu_fr, text="Gerenciar\nLotes", command=self.show_ger_estoque)
        self.btn_ger_lotes.pack(padx=10, pady=5, side="left", expand=True)
        
        
    # MENU ADMINISTRADOR  
    def show_top_menu_adm(self):
        self.show_top_menu_geral()
        
        self.btn_adm_funcs = ctk.CTkButton(self.top_menu_fr, text="Administrar\nFuncionários", command=self.show_adm_funcs)
        self.btn_adm_funcs.pack(padx=10, pady=5, side="left", expand=True)
        
        
        
    # limpar frame de conteúdo
    def limpar_conteudo_fr(self):
        self.controller.limpar_frame(self.conteudo_fr)
             
    
    def show_rg_lote(self):        
        self.controller.show_rg_lote(self.conteudo_fr)

        
    def show_ger_produtos(self):
        self.controller.show_ger_produtos(self.conteudo_fr)
  

    def show_ger_estoque(self):
        self.controller.show_ger_estoque(self.conteudo_fr)        
        
        
    def show_adm_funcs(self):
        self.controller.show_adm_funcs(self.conteudo_fr)

    

            
            
    def sair(self):
        self.controller.sair_show_login()
