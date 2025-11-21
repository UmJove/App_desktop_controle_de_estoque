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

        self.cad_prod_fr = CadastroProd(self.geral_fr, self.controller)
        self.cad_prod_fr.grid(row=2, column=0, padx=20, pady=(5), sticky='ns')

    # Título da página

        titulo_pagina = ctk.CTkLabel(self.titulo_fr, text='Gerenciamento de Produtos')
        titulo_pagina.pack()        
    
    # Treeview de produtos
        cont_row = 0
        
        # Titulo Seção
        titulo_secao = ctk.CTkLabel(self.prod_treeview_fr, text="Produtos Registrados")
        titulo_secao.grid(row=cont_row, column=0)

        cont_row += 1

        # Filtro de ordenação
        ordenacao_fr = ctk.CTkFrame(self.prod_treeview_fr, border_width=2)
        ordenacao_fr.grid(row=cont_row, column=0, sticky='nsew')

        ordenacao_lbl = ctk.CTkLabel(ordenacao_fr, text='Ordenar por:')
        ordenacao_lbl.pack(padx=(5,0), side="left")      

        self.ordenacao_var = ctk.StringVar(value="opções")
        ordenacao_opmenu = ctk.CTkOptionMenu(ordenacao_fr, 
                                            values=["op1","op2","op3"], 
                                            variable=self.ordenacao_var,
                                            width=60, 
                                            height=20)
        ordenacao_opmenu.pack(padx=(5,0), side="left")      

        cont_row += 1

        tabela = ttk.Treeview(self.prod_treeview_fr, 
                              columns=('id', 
                                       'nome_produto', 
                                       'qtd_estoque', 
                                       'lotes_atv', 
                                       'a', 
                                       'observacao'), 
                              show='headings')
        tabela.grid(row=cont_row, column=0, padx=5, sticky='nsew')
        
        cont_row += 1

        # Topos
        tabela.heading('#0', text='')
        tabela.heading('id', text='ID')
        tabela.heading('nome_produto', text='Produto')
        tabela.heading('qtd_estoque', text='Estoque')
        tabela.heading('lotes_atv', text='Lote(s) ativo(s)')
        tabela.heading('a', text='a')
        tabela.heading('observacao', text='OBS')

        # Colunas
        tabela.column('#0', width=0, minwidth=0)
        tabela.column('id', anchor='center', width=25)
        tabela.column('nome_produto', anchor='center', width=180)
        tabela.column('qtd_estoque', anchor='center', width=80)
        tabela.column('lotes_atv', anchor='center', width=100)
        tabela.column('a', anchor='center', width=15)
        tabela.column('observacao', anchor='center', width=150)   

        editar_prod_btns_fr = ctk.CTkFrame(self.prod_treeview_fr, border_width=2)
        editar_prod_btns_fr.grid(row=cont_row, column=0, sticky='nsew')

        btn_editar_prod = ctk.CTkButton(editar_prod_btns_fr, text="Editar prod", )# command=self....)
        btn_editar_prod.pack()        



    # CRUD Produtos
        # FALTA : Excluir produtos

class CadastroProd(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        self.configure(border_width=1)
        self.columnconfigure((0,1,2), weight=1)
        ### CADASTRO DE PRODUTO - Form        
        cont_row2 = 0
        
        cad_prod_lbl = ctk.CTkLabel(self, text='Cadastro de produto')
        cad_prod_lbl.grid(row=cont_row2, padx=10, columnspan=3, pady=5)

        cont_row2 += 1
        
        nome_prod_lbl = ctk.CTkLabel(self, text='Produto:')
        nome_prod_lbl.grid(row=cont_row2, column=0, padx=10, pady=10, sticky='e')

        self.nome_prod_entry = ctk.CTkEntry(self, placeholder_text='Digite o nome do produto')
        self.nome_prod_entry.grid(row=cont_row2, column=1,  columnspan=2,padx=(0,15), pady=10, sticky='ew')
        
        cont_row2 += 1
        
        qtd_estoq_lbl = ctk.CTkLabel(self, text='Estoque:')
        qtd_estoq_lbl.grid(row=cont_row2, column=0, padx=10, pady=10, sticky='e')

        self.qtd_estoq_entry = ctk.CTkEntry(self, placeholder_text='Qtd inicial', width=80)
        self.qtd_estoq_entry.grid(row=cont_row2, column=1, padx=0, pady=10, sticky='w')

        # botão salvar
        btn_salvar_rg = ctk.CTkButton(self, text='Cadastrar', command=self.cadastrar_prod)
        btn_salvar_rg.grid(row=cont_row2, column=2, columnspan=2, padx=10, pady=15)        
    
    def cadastrar_prod(self):
        ...