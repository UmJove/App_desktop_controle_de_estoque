import customtkinter as ctk
from tkinter import ttk




class GerProdView(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.parent = parent

        self.configure(fg_color='transparent')# , border_width=2, border_color='magenta')

        self.geral_fr = ctk.CTkFrame(self, fg_color='transparent' , border_width=2, border_color='magenta')
        self.geral_fr.pack(padx=35, fill='both', expand=True)



    # Frames e Grid
        self.geral_fr.columnconfigure(0, weight=1)
        self.geral_fr.rowconfigure((0), weight=0)
        self.geral_fr.rowconfigure((1,2), weight=1)

        self.titulo_fr = ctk.CTkFrame(self.geral_fr, fg_color='transparent' , border_width=2, border_color='magenta')
        self.titulo_fr.grid(row=0, column=0, padx=20, pady=(5), sticky='nsew')

        self.prod_treeview_fr = ctk.CTkFrame(self.geral_fr)
        self.prod_treeview_fr.grid(row=1, padx=20, pady=(5), sticky='nsew')

        self.prod_treeview_fr.columnconfigure(0, weight=1)
        self.prod_treeview_fr.rowconfigure((0,1,3), weight=0)
        self.prod_treeview_fr.rowconfigure((2), weight=1)

        self.cad_prod_fr = ctk.CTkFrame(self.geral_fr, )
        self.cad_prod_fr.grid(row=2, column=0, padx=20, pady=(5), sticky='ns')
        
        self.cad_prod_fr.columnconfigure((0,1,2), weight=1)

    # Título da página

        titulo_pagina = ctk.CTkLabel(self.titulo_fr, text='Gerenciamento de Produtos')
        titulo_pagina.pack()        
    
    # Treeview de produtos        
        # Titulo Seção
        titulo_secao = ctk.CTkLabel(self.prod_treeview_fr, text="Produtos Registrados")
        titulo_secao.grid(row=0, column=0)

        # Filtro de ordenação
        ordenacao_fr = ctk.CTkFrame(self.prod_treeview_fr, border_width=2)
        ordenacao_fr.grid(row=1, column=0, sticky='nsew')

        ordenacao_lbl = ctk.CTkLabel(ordenacao_fr, text='Ordenar por:')
        ordenacao_lbl.pack(padx=(5,0), side="left")      

        self.ordenacao_var = ctk.StringVar(value="opções")
        ordenacao_opmenu = ctk.CTkOptionMenu(ordenacao_fr, 
                                            values=["op1","op2","op3"], 
                                            variable=self.ordenacao_var,
                                            width=60, 
                                            height=20)
        ordenacao_opmenu.pack(padx=(5,0), side="left")      

        # Tabela Treeview
        self.tabela = ttk.Treeview(self.prod_treeview_fr, 
                              columns=('id', 
                                       'nome_produto', 
                                       'qtd_estoque', 
                                    #    'lotes_atv', 
                                    #    'a', 
                                    #    'observacao'
                                       ), 
                              show='headings')
        self.tabela.grid(row=2, column=0, padx=5, sticky='nsew')
        
            # Topos
        self.tabela.heading('#0', text='')
        self.tabela.heading('id', text='ID')
        self.tabela.heading('nome_produto', text='Produto')
        self.tabela.heading('qtd_estoque', text='Estoque')
        # self.tabela.heading('lotes_atv', text='Lote(s) ativo(s)')
        # self.tabela.heading('a', text='a')
        # self.tabela.heading('observacao', text='OBS')

            # Colunas
        self.tabela.column('#0', width=0, minwidth=0)
        self.tabela.column('id', anchor='center', width=25)
        self.tabela.column('nome_produto', anchor='center', width=180)
        self.tabela.column('qtd_estoque', anchor='center', width=80)
        # self.tabela.column('lotes_atv', anchor='center', width=100)
        # self.tabela.column('a', anchor='center', width=15)
        # self.tabela.column('observacao', anchor='center', width=150)   
        
        # Botão
        editar_prod_btns_fr = ctk.CTkFrame(self.prod_treeview_fr, border_width=2)
        editar_prod_btns_fr.grid(row=3, column=0, sticky='nsew')

        btn_editar_prod = ctk.CTkButton(editar_prod_btns_fr, text="Editar prod", )# command=self....)
        btn_editar_prod.pack()        
    
    
    # CADASTRO DE PRODUTO - Formulário        
        
        cad_prod_lbl = ctk.CTkLabel(self.cad_prod_fr, text='Cadastro de produto')
        cad_prod_lbl.grid(row=0, padx=10, columnspan=3, pady=5)

        
        nome_prod_lbl = ctk.CTkLabel(self.cad_prod_fr, text='Produto:')
        nome_prod_lbl.grid(row=1, column=0, padx=10, pady=10, sticky='e')

        self.nome_prod_entry = ctk.CTkEntry(self.cad_prod_fr, placeholder_text='Digite o nome do produto')
        self.nome_prod_entry.grid(row=1, column=1,  columnspan=2,padx=(0,15), pady=10, sticky='ew')
        
        
        qtd_estoq_lbl = ctk.CTkLabel(self.cad_prod_fr, text='Estoque:')
        qtd_estoq_lbl.grid(row=2, column=0, padx=10, pady=10, sticky='e')

        self.qtd_estoq_entry = ctk.CTkEntry(self.cad_prod_fr, placeholder_text='Qtd inicial', width=80)
        self.qtd_estoq_entry.grid(row=2, column=1, padx=0, pady=10, sticky='w')

        # botão salvar
        btn_salvar_rg = ctk.CTkButton(self.cad_prod_fr, text='Cadastrar', command=self.cadastrar_prod)
        btn_salvar_rg.grid(row=2, column=2, columnspan=2, padx=10, pady=15)   
    
    
    
    
        self.listar_treeview()

    def listar_treeview(self):
        # Limpar células
        for record in self.tabela.get_children(): 
            self.tabela.delete(record)
            
            
        produtos = self.controller.listar_produtos()
        
           
        for produto in produtos:
            self.tabela.insert(parent="",
                               index="end", 
                               tex="", 
                               values=(produto[0], produto[1], produto[2], #    "",     "",    "",
                                       )
                                )
            
    def cadastrar_prod(self):
        nome_prod = self.nome_prod_entry.get()
        qtd_estoque = int(self.qtd_estoq_entry.get())
        self.controller.inserir_produto(nome_prod, qtd_estoque)
        self.listar_treeview()
        

    
    # CRUD Produtos
        # FALTA : Excluir produtos

# class CadastroProd(ctk.CTkFrame):
#     def __init__(self, parent, controller):
#         super().__init__(parent)
#         self.controller = controller
        
#         self.configure(border_width=1)
#         self.columnconfigure((0,1,2), weight=1)
#         ### CADASTRO DE PRODUTO - Form        
        
#         cad_prod_lbl = ctk.CTkLabel(self, text='Cadastro de produto')
#         cad_prod_lbl.grid(row=0, padx=10, columnspan=3, pady=5)

        
#         nome_prod_lbl = ctk.CTkLabel(self, text='Produto:')
#         nome_prod_lbl.grid(row=1, column=0, padx=10, pady=10, sticky='e')

#         self.nome_prod_entry = ctk.CTkEntry(self, placeholder_text='Digite o nome do produto')
#         self.nome_prod_entry.grid(row=1, column=1,  columnspan=2,padx=(0,15), pady=10, sticky='ew')
        
        
#         qtd_estoq_lbl = ctk.CTkLabel(self, text='Estoque:')
#         qtd_estoq_lbl.grid(row=2, column=0, padx=10, pady=10, sticky='e')

#         self.qtd_estoq_entry = ctk.CTkEntry(self, placeholder_text='Qtd inicial', width=80)
#         self.qtd_estoq_entry.grid(row=2, column=1, padx=0, pady=10, sticky='w')

#         # botão salvar
#         btn_salvar_rg = ctk.CTkButton(self, text='Cadastrar', command=self.cadastrar_prod)
#         btn_salvar_rg.grid(row=2, column=2, columnspan=2, padx=10, pady=15)        
    
    def cadastrar_prod(self):
        nome_prod = self.nome_prod_entry.get()
        qtd_estoque = int(self.qtd_estoq_entry.get())
        self.controller.inserir_produto(nome_prod, qtd_estoque)