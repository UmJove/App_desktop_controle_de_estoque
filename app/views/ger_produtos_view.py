import customtkinter as ctk



class GerProdView(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        titulo_pagina = ctk.CTkLabel(self, text="GER PRODUTOS")
        titulo_pagina.pack()        

    # Adicionar novo produto
    # Editar produtos
    # Excluir produtos
    # CRUD Produtos

class CadastroProd(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        self.configure(border_width=1)
        self.columnconfigure((0,1,2), weight=1)
        ### CADASTRO DE PRODUTO - Form        
        cont_row2 = 0
        
        cad_prod_lbl = ctk.CTkLabel(self, text="Cadastro de produto")
        cad_prod_lbl.grid(row=cont_row2, padx=10, columnspan=3, pady=5)

        cont_row2 += 1
        
        nome_prod_lbl = ctk.CTkLabel(self, text="Produto:")
        nome_prod_lbl.grid(row=cont_row2, column=0, padx=10, pady=10, sticky="e")

        self.nome_prod_entry = ctk.CTkEntry(self, placeholder_text="Digite o nome do produto")
        self.nome_prod_entry.grid(row=cont_row2, column=1,  columnspan=2,padx=(0,15), pady=10, sticky="ew")
        
        cont_row2 += 1
        
        qtd_estoq_lbl = ctk.CTkLabel(self, text="Estoque:")
        qtd_estoq_lbl.grid(row=cont_row2, column=0, padx=10, pady=10, sticky="e")

        self.qtd_estoq_entry = ctk.CTkEntry(self, placeholder_text="Qtd inicial", width=80)
        self.qtd_estoq_entry.grid(row=cont_row2, column=1, padx=0, pady=10, sticky="w")

        # botão salvar
        btn_salvar_rg = ctk.CTkButton(self, text="Cadastrar", command=self.cadastrar_prod)
        btn_salvar_rg.grid(row=cont_row2, column=2, columnspan=2, padx=10, pady=15)        
    
    def cadastrar_prod(self):
        ...