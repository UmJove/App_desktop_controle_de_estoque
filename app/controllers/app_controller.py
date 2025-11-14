import customtkinter as ctk

from app.models.funcionarios_model import FuncionariosModel
from app.models.produtos_model import ProdutosModel

from app.views.login_view import LoginView
from app.views.home_view import HomeView


class AppController:
    def __init__(self):
        self.funcionarios = FuncionariosModel()
        self.produtos = ProdutosModel()
        self.root = ctk.CTk()
        self.root.geometry("800x600")

        # Tela de login
        self.login_view = LoginView(self.root, self)
        self.login_view.pack(fill="both", expand=True)        
        
    # Controle de login do usuário
    def login(self, username, password):
        username = None
        password = None
        self.show_home()
                
    # Mostrar a tela inicial
    def show_home(self):
        
        self.login_view.destroy()
        self.home_view = HomeView(self.root, self)
        self.home_view.pack(fill="both", expand=True)
        
        
    def run(self):
        self.root.mainloop()
        

