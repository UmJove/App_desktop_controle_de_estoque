import customtkinter as ctk
from tkinter import ttk


class AdmFuncView(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.parent = parent

        self.configure(fg_color='transparent', border_width=2, border_color='yellow')

        self.geral_fr = ctk.CTkFrame(self, fg_color='transparent' , border_width=2, border_color='magenta')
        self.geral_fr.pack(padx=35, fill='both', expand=True)



    # Frames e Grid
        self.geral_fr.columnconfigure(0, weight=1)
        self.geral_fr.rowconfigure((0,1), weight=0)
        self.geral_fr.rowconfigure((2), weight=1)

        self.titulo_fr = ctk.CTkFrame(self.geral_fr, fg_color='transparent' , border_width=2, border_color='magenta')
        self.titulo_fr.grid(row=0, column=0, padx=20, pady=(5), sticky='nsew')
        
        self.sub_menu_fr = ctk.CTkFrame(self.geral_fr, fg_color='transparent' , border_width=2, border_color='red')
        self.sub_menu_fr.grid(row=1, column=0, padx=20, pady=(5), sticky='ns')

        self.conteudo_adm_fr = ctk.CTkFrame(self.geral_fr, fg_color='transparent' , border_width=2, border_color='blue')
        self.conteudo_adm_fr.grid(row=2, column=0, sticky='nsew')


    # Título da página
        titulo_pagina = ctk.CTkLabel(self.titulo_fr, text='Gerenciamento de Funcionários')
        titulo_pagina.pack()        
    
    # Sub Menu Adm
        btn_editar_prod = ctk.CTkButton(self.sub_menu_fr, text='Visualizar Funcionários', command=self.show_func_treeview)
        btn_editar_prod.pack(padx=10, pady=5, side='left', expand=True)

        btn_editar_prod = ctk.CTkButton(self.sub_menu_fr, text='Cadastrar',  command=self.show_func_cadastro)
        btn_editar_prod.pack(padx=10, pady=5, side='left', expand=True)

        btn_editar_prod = ctk.CTkButton(self.sub_menu_fr, text='Editar dados',command=lambda: self.show_func_edicao(id_funcionario=None))
        btn_editar_prod.pack(padx=10, pady=5, side='left', expand=True)

   

    def show_func_treeview(self):
        self.controller.limpar_frame(self.conteudo_adm_fr)

        self.func_cadastro_fr = ctk.CTkFrame(self.conteudo_adm_fr, border_width=2, border_color='#00ffff')
        self.func_cadastro_fr.pack(padx=5, pady=5, fill='both', expand=True)

        self.func_cadastro_fr.columnconfigure(0, weight=1)
        self.func_cadastro_fr.rowconfigure((0,1,3), weight=0)
        self.func_cadastro_fr.rowconfigure((2), weight=1)
   
    # Treeview de produtos       
        # Titulo Seção
        titulo_secao = ctk.CTkLabel(self.func_cadastro_fr, text='Funcionários Registrados')
        titulo_secao.grid(row=0, column=0)

        # Filtro de ordenação
        ordenacao_fr = ctk.CTkFrame(self.func_cadastro_fr, border_width=2)
        ordenacao_fr.grid(row=1, column=0, sticky='nsew')

        ordenacao_lbl = ctk.CTkLabel(ordenacao_fr, text='Ordenar por:')
        ordenacao_lbl.pack(padx=(5,0), side='left')      

        self.ordenacao_var = ctk.StringVar(value='opções')
        ordenacao_opmenu = ctk.CTkOptionMenu(ordenacao_fr, 
                                            values=['op1','op2','op3'], 
                                            variable=self.ordenacao_var,
                                            width=60, 
                                            height=20)
        ordenacao_opmenu.pack(padx=(5,0), side='left')      

        # Tabela Treeview
        tabela = ttk.Treeview(self.func_cadastro_fr, 
                              columns=('id', 
                                       'nome_produto', 
                                       'qtd_estoque', 
                                       'lotes_atv', 
                                       'a', 
                                       'observacao'), 
                              show='headings')
        tabela.grid(row=2, column=0, padx=5, sticky='nsew')
        
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
        
        # Botão
        editar_prod_btns_fr = ctk.CTkFrame(self.func_cadastro_fr, border_width=2)
        editar_prod_btns_fr.grid(row=3, column=0, sticky='nsew')

        id_funcionario = ''
        btn_editar_prod = ctk.CTkButton(editar_prod_btns_fr, text='Editar dados', command=lambda: self.show_func_edicao(id_funcionario))
        btn_editar_prod.pack()        



    def show_func_cadastro(self):
        self.controller.limpar_frame(self.conteudo_adm_fr)
        
        self.func_cadastro_fr = ctk.CTkFrame(self.conteudo_adm_fr, border_width=2, border_color="#11ff11")
        self.func_cadastro_fr.grid(row=0, column=0, padx=150, pady=5, sticky='new')
        
        self.conteudo_adm_fr.columnconfigure((0), weight=1)
        self.conteudo_adm_fr.rowconfigure((0), weight=1)

        self.func_cadastro_fr.columnconfigure((0), weight=0)
        self.func_cadastro_fr.columnconfigure((1), weight=1)
       
    # CADASTRO DE FUNCIONÁRIO - FORMULÁRIO
        # título    
        cad_func_lbl = ctk.CTkLabel(self.func_cadastro_fr, text='Cadastro de Funcionário')
        cad_func_lbl.grid(row=0, padx=(35, 10), columnspan=3, pady=5)

        
        nome_func_lbl = ctk.CTkLabel(self.func_cadastro_fr, text='Nome:')
        nome_func_lbl.grid(row=1, column=0, padx=(35, 10), pady=10, sticky='e')

        self.nome_func_entry = ctk.CTkEntry(self.func_cadastro_fr, placeholder_text='Digite o nome do funcionário')
        self.nome_func_entry.grid(row=1, column=1, padx=(0,35), pady=10, sticky='ew')
        
        user_func_lbl = ctk.CTkLabel(self.func_cadastro_fr, text='Username:')
        user_func_lbl.grid(row=2, column=0, padx=(35, 10), pady=10, sticky='e')

        self.user_func_entry = ctk.CTkEntry(self.func_cadastro_fr, placeholder_text='Crie um nome de usuário')
        self.user_func_entry.grid(row=2, column=1, padx=(0,35), pady=10, sticky='ew')

        senha_func_lbl = ctk.CTkLabel(self.func_cadastro_fr, text='Senha:')
        senha_func_lbl.grid(row=3, column=0, padx=(35, 10), pady=10, sticky='e')

        self.senha_func_entry = ctk.CTkEntry(self.func_cadastro_fr, placeholder_text='Crie uma senha')
        self.senha_func_entry.grid(row=3, column=1, padx=(0,35), pady=10, sticky='ew')

        cargo_func_lbl = ctk.CTkLabel(self.func_cadastro_fr, text='Cargo:')
        cargo_func_lbl.grid(row=4, column=0, padx=(35, 10), pady=10, sticky='e')

        self.cargo_func_entry = ctk.CTkEntry(self.func_cadastro_fr, placeholder_text='Digite o cargo do funcionário')
        self.cargo_func_entry.grid(row=4, column=1, padx=(0,35), pady=10, sticky='ew')

        # botão salvar
        btn_cadastrar_func = ctk.CTkButton(self.func_cadastro_fr, text='Cadastrar', command=self.cadastrar_func)
        btn_cadastrar_func.grid(row=5, column=1, padx=35, pady=15, sticky='e')        
    

    def show_func_edicao(self, id_funcionario):
        self.controller.limpar_frame(self.conteudo_adm_fr)

    def cadastrar_func(self):
        ...



