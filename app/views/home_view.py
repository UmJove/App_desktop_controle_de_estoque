import customtkinter as ctk


class HomeView(ctk.CTkFrame):
    # def __init__(self, user, parent, controller):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        # self.user = user
        
        # Menu lateral (widgets)
        self.side_menu = ctk.CTkFrame(self, width=200)
        self.side_menu.pack(side='left', fill='y', padx=10, pady=10)

        #Botões para o menu lateral
        self.btn_home = ctk.CTkButton(self.side_menu, text="Home", command=self.show_home)
        self.btn_home.pack(pady=10, padx=10)

    # A função para mostrar a homepage
    def show_adm_view(self):
        self.clear_content()
        # if "adm" in self.user:
        welcome_label = ctk.CTkLabel(self.content_frame, text="Adm home!", font=('Arial bold', 20))
        welcome_label.pack(pady=20)
    
    def show_func_view(self):
        self.clear_content()
        welcome_label = ctk.CTkLabel(self.content_frame, text="Funcionario home!", font=('Arial bold', 20))
        welcome_label.pack(pady=20)
