import customtkinter as ctk
from app.views.ger_produtos_view import CadastroProd


class RgLoteView(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(fg_color="transparent")
        
        self.produtos = self.controller.listar_produtos()
        self.dias = []
        self.meses = ["jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez"]
        for dia in range(1, 32):
            self.dias.append(str(dia))


        # DIVISÃO DE SEÇÕES (organização de frames)
        self.columnconfigure((0), weight=1)
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)

        self.titulo_fr = ctk.CTkFrame(self, corner_radius=10)
        self.titulo_fr.grid(row=0, column=0, padx=5, pady=(0,5), columnspan=2)

        self.rg_lote_form_fr = ctk.CTkFrame(self)
        self.rg_lote_form_fr.grid(row=1, column=0, padx=50, pady=(0,15), sticky="nsew")
        
        self.rg_lote_form_fr.columnconfigure((0,1), weight=1)


        
        titulo_pagina = ctk.CTkLabel(self.titulo_fr, text="TÍTULO DA PÁGINA")
        titulo_pagina.pack()
        
        ### REGISTRO DE LOTE - Form
        cont_row = 0
        
        rg_lote_lbl = ctk.CTkLabel(self.rg_lote_form_fr, text="Registro de lote")
        rg_lote_lbl.grid(row=cont_row, padx=10, columnspan=2, pady=5)

        cont_row += 1
        
        # Selecionar produto
        self.atualizar_opcoes_prod()
        
        selecionar_prod_lbl = ctk.CTkLabel(self.rg_lote_form_fr, text="Produto")
        selecionar_prod_lbl.grid(row=cont_row, column=0, padx=10, pady=10)

        self.selecionar_prod_var = ctk.StringVar(value="Selecionar produto")
        selecionar_prod_combb = ctk.CTkComboBox(self.rg_lote_form_fr, values=self.produto_opcoes, variable=self.selecionar_prod_var)
        selecionar_prod_combb.grid(row=cont_row, column=1, padx=(5,25), pady=10, sticky="ew")

        cont_row += 1
        # Quantidade
        qtd_lbl = ctk.CTkLabel(self.rg_lote_form_fr, text="Quantidade")
        qtd_lbl.grid(row=cont_row, column=0, padx=10, pady=10)

        self.qtd_entry = ctk.CTkEntry(self.rg_lote_form_fr, placeholder_text="Quantidade recebida")
        self.qtd_entry.grid(row=cont_row, column=1, padx=(5,25), pady=10, sticky="ew")

        cont_row += 1

        # Checkbox de reg fabricação e validade
        # check_val_lbl = ctk.CTkLabel(self.rg_lote_form_fr, text="Produto com validade?")
        # check_val_lbl.grid(row=cont_row, column=0, padx=10, pady=10)

        self.check_val_var = ctk.StringVar(value="off")
        check_val_chkbox = ctk.CTkCheckBox(self.rg_lote_form_fr, 
                                           text="Produto com validade?",
                                           variable=self.check_val_var, 
                                           onvalue="on", 
                                           offvalue="off",
                                           command=self.checar_validade)
        check_val_chkbox.grid(row=cont_row, column=0, columnspan=2, padx=10, pady=10)
        
        cont_row += 1

        # Frame para informar data de fabricação e validade
        self.validade_fr = ctk.CTkFrame(self.rg_lote_form_fr, fg_color="transparent", height=10)
        self.validade_fr.grid(row=cont_row, column=0, columnspan=2,  padx=10, pady=10)

        cont_row += 1
        
        # botão salvar
        btn_salvar_rg = ctk.CTkButton(self.rg_lote_form_fr, text="Salvar Registro", command=self.registrar_lote_recebido)
        btn_salvar_rg.grid(row=cont_row, column=0, columnspan=2, padx=10, pady=10)

        cont_row += 2
        
        # Cadastrar de Produto
        cadastro_prod_fr = CadastroProd(self.rg_lote_form_fr, self.controller)
        cadastro_prod_fr.grid(row=cont_row, column=1, padx=25, pady=15, sticky="se") 


    def checar_validade(self):
        precisa_validade = self.check_val_var.get()
        self.controller.limpar_frame(self.validade_fr)

        if precisa_validade == "on":
            print("Precisa")
            cont_row = 0
            
            # Fabricação
            fabr_lbl = ctk.CTkLabel(self.validade_fr, text="Fabricação:")
            fabr_lbl.grid(row=cont_row, column=0, padx=10, pady=3)
            
            cont_row += 1
            
            data_fabr_fr = ctk.CTkFrame(self.validade_fr,)
            data_fabr_fr.grid(row=cont_row, column=0, padx=10, pady=(0,3))
            
            self.fabr_dia_var = ctk.StringVar(value="dia")
            fabr_dia_combb = ctk.CTkComboBox(data_fabr_fr, 
                                             values=self.dias, 
                                             variable=self.fabr_dia_var,
                                             width=60, 
                                             height=20)
            fabr_dia_combb.pack(padx=10, pady=(0,3), side="left", fill="x")

            self.fabr_mes_var = ctk.StringVar(value="mês")
            fabr_mes_combb = ctk.CTkComboBox(data_fabr_fr, 
                                             values=self.meses, 
                                             variable=self.fabr_mes_var,
                                             width=60,  
                                             height=20)
            fabr_mes_combb.pack(padx=10, pady=(0,3), side="left", fill="x")

            fabr_ano_entry = ctk.CTkEntry(data_fabr_fr, 
                                          placeholder_text="ano", 
                                          width=60, 
                                          height=20)
            fabr_ano_entry.pack(padx=10, pady=(0,3), side="left", fill="x")


            cont_row += 1


            valid_lbl = ctk.CTkLabel(self.validade_fr, text="Validade:")
            valid_lbl.grid(row=cont_row, column=0, padx=10, pady=(0,3))

            cont_row += 1

            data_valid_fr = ctk.CTkFrame(self.validade_fr,)
            data_valid_fr.grid(row=cont_row, column=0, padx=10, pady=(0,3))

            self.valid_dia_var = ctk.StringVar(value="dia")
            valid_dia_combb = ctk.CTkComboBox(data_valid_fr, 
                                             values=self.dias, 
                                             variable=self.valid_dia_var,
                                             width=60, 
                                             height=20)
            valid_dia_combb.pack(padx=10, pady=(0,3), side="left", fill="x")

            self.valid_mes_var = ctk.StringVar(value="mês")
            valid_mes_combb = ctk.CTkComboBox(data_valid_fr, 
                                             values=self.meses, 
                                             variable=self.valid_mes_var,
                                             width=60,  
                                             height=20)
            valid_mes_combb.pack(padx=10, pady=(0,3), side="left", fill="x")

            valid_ano_entry = ctk.CTkEntry(data_valid_fr, 
                                          placeholder_text="ano", 
                                          width=60, 
                                          height=20)
            valid_ano_entry.pack(padx=10, pady=(0,3), side="left", fill="x")


            # ctk.CTkEntry(self.rg_lote_form_fr, placeholder_text=)
        elif precisa_validade == "off":
            print("Não Precisa")
            self.validade_fr.configure(height=10)

    def registrar_lote_recebido(self):
        ...


    def atualizar_opcoes_prod(self):
        self.produto_opcoes = []
        for produto in self.produtos:
            self.produto_opcoes.append(produto[1])
        print(self.produto_opcoes)
    
    # WRITE (INSERT) - lote
    # def inserir_lote(self, produto_id: int, qtd_lote: int, fabricacao:str, validade:str, registro:str, responsavel:str):        
        # self.cursor.execute(
        #     """
        #         INSERT INTO lote (produto_id, 
        #                              qtd_lote, 
        #                              fabricacao,
        #                              validade,
        #                              registro,
        #                              responsavel) 
        #                              VALUES (?, ?, ?, ?, ?, ?)  
        #     """,
        #     (produto_id, qtd_lote, fabricacao, validade, registro, responsavel)
        # )
        
        # self.conn.commit()
        # self.conn.close()