import customtkinter as ctk
from PIL import Image
from datetime import datetime

from app.controllers.font_controller import Fontes




class RgLoteView(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.parent = parent
        
        self.ft = Fontes()

        
        self.configure(fg_color='transparent')# , border_width=2, border_color='magenta')
        self.geral_fr = ctk.CTkFrame(self, fg_color='transparent')# , border_width=2, border_color='magenta')
        self.geral_fr.pack(fill='both', expand=True)

        self.produtos = self.controller.listar_produtos()
        self.dias = []
        self.meses = []
        for dia in range(1, 32):
            self.dias.append(str(dia).zfill(2))
        for mes in range(1, 13):
            self.meses.append(str(mes).zfill(2))

        # Imagem
        image_lateral = ctk.CTkImage(light_image=Image.open('./assets/imgs/img-rg-lateral.png'), dark_image=Image.open('./assets/imgs/img-rg-lateral.png'), size=(150, 200))

        # Frames e grid
        self.geral_fr.columnconfigure((0), weight=0)
        self.geral_fr.columnconfigure((1), weight=1)
        self.geral_fr.rowconfigure(0, weight=0)
        self.geral_fr.rowconfigure(1, weight=1)

        self.titulo_fr = ctk.CTkFrame(self.geral_fr, fg_color='transparent')# , border_width=2, border_color='magenta')
        self.titulo_fr.grid(row=0, column=0, columnspan=2, padx=20, pady=(5), sticky='nsew')

        
        self.imagem_fr = ctk.CTkFrame(self.geral_fr, fg_color='transparent')
        self.imagem_fr.grid(row=1, column=0, sticky='nsew')


        self.rg_lote_form_fr = ctk.CTkFrame(self.geral_fr)
        self.rg_lote_form_fr.grid(row=1, column=1, padx=(0,170), pady=(0,15), sticky='new')
        
        self.rg_lote_form_fr.columnconfigure((0,1), weight=1)


        # Título da página
        titulo_pagina = ctk.CTkLabel(self.titulo_fr, text='Registro de Lotes', font=self.ft.titulo, text_color=self.ft.txt_claro)
        titulo_pagina.pack(pady=(0,10))
        
        # Imagem lateral
        label_image = ctk.CTkLabel(self.imagem_fr, image=image_lateral, text='')
        label_image.pack(padx=10, pady=10, side='bottom')

        ### REGISTRO DE LOTE - Formuário        
        # Label Seção
        rg_lote_lbl = ctk.CTkLabel(self.rg_lote_form_fr, text='Formulário de recebimento')
        rg_lote_lbl.grid(row=0, column=0, padx=10, columnspan=2, pady=5)

        
        # Selecionar produto
        self.atualizar_opcoes_prod()
        
        selecionar_prod_lbl = ctk.CTkLabel(self.rg_lote_form_fr, text='Produto')
        selecionar_prod_lbl.grid(row=1, column=0, padx=10, pady=10)

        self.selecionar_prod_var = ctk.StringVar(value='Selecionar produto')
        self.selecionar_prod_combb = ctk.CTkComboBox(self.rg_lote_form_fr, values=self.produto_opcoes, variable=self.selecionar_prod_var)
        self.selecionar_prod_combb.grid(row=1, column=1, padx=(5,25), pady=10, sticky='ew')


        # Quantidade
        qtd_lbl = ctk.CTkLabel(self.rg_lote_form_fr, text='Quantidade')
        qtd_lbl.grid(row=2, column=0, padx=10, pady=10)

        self.qtd_entry = ctk.CTkEntry(self.rg_lote_form_fr, placeholder_text='Quantidade recebida')
        self.qtd_entry.grid(row=2, column=1, padx=(5,25), pady=10, sticky='ew')



        self.check_val_var = ctk.StringVar(value='off')
        check_val_chkbox = ctk.CTkCheckBox(self.rg_lote_form_fr, 
                                           text='Produto com validade?',
                                           variable=self.check_val_var, 
                                           onvalue='on', 
                                           offvalue='off',
                                           command=self.checar_validade)
        check_val_chkbox.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
        

        # Frame para informar data de fabricação e validade
        self.validade_fr = ctk.CTkFrame(self.rg_lote_form_fr, fg_color='transparent', height=10)
        self.validade_fr.grid(row=4, column=0, columnspan=2,  padx=10, pady=10)

        
        # botão salvar
        btn_salvar_rg = ctk.CTkButton(self.rg_lote_form_fr, text='Salvar Registro', command=self.registrar_lote_recebido)
        btn_salvar_rg.grid(row=5, column=0, columnspan=2, padx=10, pady=10)



    def checar_validade(self):
        precisa_validade = self.check_val_var.get()
        self.controller.limpar_frame(self.validade_fr)

        if precisa_validade == 'on':
            print('Precisa')
            
            # Fabricação
            fabr_lbl = ctk.CTkLabel(self.validade_fr, text='Fabricação:')
            fabr_lbl.grid(row=0, column=0, padx=10, pady=3)
            
            
            data_fabr_fr = ctk.CTkFrame(self.validade_fr,)
            data_fabr_fr.grid(row=1, column=0, padx=10, pady=(0,3))
            
            self.fabr_dia_var = ctk.StringVar(value='dia')
            fabr_dia_combb = ctk.CTkComboBox(data_fabr_fr, 
                                             values=self.dias, 
                                             variable=self.fabr_dia_var,
                                             width=60, 
                                             height=20)
            fabr_dia_combb.pack(padx=10, pady=(0,3), side='left', fill='x')

            self.fabr_mes_var = ctk.StringVar(value='mês')
            fabr_mes_combb = ctk.CTkComboBox(data_fabr_fr, 
                                             values=self.meses, 
                                             variable=self.fabr_mes_var,
                                             width=60,  
                                             height=20)
            fabr_mes_combb.pack(padx=10, pady=(0,3), side='left', fill='x')

            self.fabr_ano_entry = ctk.CTkEntry(data_fabr_fr, 
                                          placeholder_text='ano', 
                                          width=60, 
                                          height=20)
            self.fabr_ano_entry.pack(padx=10, pady=(0,3), side='left', fill='x')


            # Validade


            valid_lbl = ctk.CTkLabel(self.validade_fr, text='Validade:')
            valid_lbl.grid(row=2, column=0, padx=10, pady=(0,3))


            data_valid_fr = ctk.CTkFrame(self.validade_fr,)
            data_valid_fr.grid(row=3, column=0, padx=10, pady=(0,3))

            self.valid_dia_var = ctk.StringVar(value='dia')
            valid_dia_combb = ctk.CTkComboBox(data_valid_fr, 
                                             values=self.dias, 
                                             variable=self.valid_dia_var,
                                             width=60, 
                                             height=20)
            valid_dia_combb.pack(padx=10, pady=(0,3), side='left', fill='x')

            self.valid_mes_var = ctk.StringVar(value='mês')
            valid_mes_combb = ctk.CTkComboBox(data_valid_fr, 
                                             values=self.meses, 
                                             variable=self.valid_mes_var,
                                             width=60,  
                                             height=20)
            valid_mes_combb.pack(padx=10, pady=(0,3), side='left', fill='x')

            self.valid_ano_entry = ctk.CTkEntry(data_valid_fr, 
                                          placeholder_text='ano', 
                                          width=60, 
                                          height=20)
            self.valid_ano_entry.pack(padx=10, pady=(0,3), side='left', fill='x')


            # ctk.CTkEntry(self.rg_lote_form_fr, placeholder_text=)
        elif precisa_validade == 'off':
            print('Não Precisa')
            self.validade_fr.configure(height=10)

    def registrar_lote_recebido(self):
        produto = self.selecionar_prod_combb.get()
        produto_id = self.dic_produto_opcoes[produto]
        qtd_lote = self.qtd_entry.get()

        fabricacao = f"{self.fabr_ano_entry.get()}-{self.fabr_mes_var.get()}-{self.fabr_dia_var.get()}"
        validade = f"{self.valid_ano_entry.get()}-{self.valid_mes_var.get()}-{self.valid_dia_var.get()}"
        registro = str(datetime.now())
        responsavel = self.controller.username

        
        # Create novo lote
        self.controller.inserir_lote(produto_id, qtd_lote, fabricacao, validade, registro, responsavel)
        


        



    def atualizar_opcoes_prod(self):
        self.dic_produto_opcoes = {}        
        self.produto_opcoes = []
        for produto in self.produtos:
            self.dic_produto_opcoes[produto[1]] = produto[0]
            self.produto_opcoes.append(produto[1])

    