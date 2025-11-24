import customtkinter as ctk
from tkinter import ttk

from app.controllers.font_controller import Fontes


class GerEstoqueView(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.parent = parent
        
        self.ft = Fontes()


        self.configure(fg_color='transparent', border_width=2, border_color='magenta')

        self.geral_fr = ctk.CTkFrame(self, fg_color='transparent' , border_width=2, border_color='magenta')
        self.geral_fr.pack(padx=35, fill='both', expand=True)



    # Frames e Grid
        self.geral_fr.columnconfigure(0, weight=1)
        self.geral_fr.rowconfigure((0,2), weight=0)
        self.geral_fr.rowconfigure((1), weight=1)

        self.titulo_fr = ctk.CTkFrame(self.geral_fr, fg_color='transparent' , border_width=2, border_color='magenta')
        self.titulo_fr.grid(row=0, column=0, padx=20, pady=(5), sticky='nsew')

        self.lotes_treeview_fr = ctk.CTkFrame(self.geral_fr)
        self.lotes_treeview_fr.grid(row=1, padx=20, pady=(5), sticky='nsew')

        self.lotes_treeview_fr.columnconfigure(0, weight=1)
        self.lotes_treeview_fr.rowconfigure((0,1,3), weight=0)
        self.lotes_treeview_fr.rowconfigure((2), weight=1)                

    # Título da página
        titulo_pagina = ctk.CTkLabel(self.titulo_fr, text='Gerenciamento de Lotes', font=self.ft.titulo, text_color=self.ft.txt_claro)
        titulo_pagina.pack(pady=(0,10))
        
    # Treeview de lotes
        cont_row = 0
        
        # Titulo Seção
        titulo_secao = ctk.CTkLabel(self.lotes_treeview_fr, text="Lotes Registrados")
        titulo_secao.grid(row=cont_row, column=0)

        cont_row += 1

        # Filtro de ordenação
        ordenacao_fr = ctk.CTkFrame(self.lotes_treeview_fr, border_width=2)
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
  
        tabela = ttk.Treeview(self.lotes_treeview_fr, 
                              columns=('id_lote', 
                                       'id_produto', 
                                       'nome_produto', 
                                       'data_fabri', 
                                       'data_valid', 
                                       'rg_por', 
                                       'data_rg'), 
                              show='headings')
        tabela.grid(row=cont_row, column=0, padx=5, sticky='nsew')
        
        cont_row += 1

        # Topos
        tabela.heading('#0', text='')

        tabela.heading('id_lote', text='Lote(ID)')
        tabela.heading('id_produto', text='Prod(ID)')
        tabela.heading('nome_produto', text='Produto')

        tabela.heading('data_fabri', text='Fabricação')
        tabela.heading('data_valid', text='Validade')
        
        tabela.heading('rg_por', text='Registrado por')
        tabela.heading('data_rg', text='Registro')


        # Colunas
        tabela.column('#0', width=0, minwidth=0)

        tabela.column('id_lote', anchor='center', width=20)
        tabela.column('id_produto', anchor='center', width=20)
        tabela.column('nome_produto', anchor='center', width=200)

        tabela.column('data_fabri', anchor='center', width=60)
        tabela.column('data_valid', anchor='center', width=60)
        
        tabela.column('rg_por', anchor='center', width=100)   
        tabela.column('data_rg', anchor='center', width=60)  


        editar_prod_btns_fr = ctk.CTkFrame(self.lotes_treeview_fr, border_width=2)
        editar_prod_btns_fr.grid(row=cont_row, column=0, sticky='nsew')

        btn_editar_prod = ctk.CTkButton(editar_prod_btns_fr, text="Editar lote", )# command=self....)
        btn_editar_prod.pack()  

    # CRUD Produtos
