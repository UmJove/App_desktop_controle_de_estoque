import customtkinter as ctk

from app.models.funcionarios_model import FuncionariosModel
from app.models.produtos_model import ProdutosModel

from app.views.login_view import LoginView
from app.views.home_view import HomeView


class AppController:
    def __init__(self):
        ctk.set_default_color_theme("assets/themes/meu_tema1.json")
        ctk.set_appearance_mode("light")
        
        self.funcionarios_model = FuncionariosModel()
        self.produtos_model = ProdutosModel()
        self.root = ctk.CTk()
        self.root.geometry("900x650")

        # TELA INICIAL - Tela de login
        self.login_view = LoginView(self.root, self)
        self.login_view.pack(fill="both", expand=True)        
        
    # Controle de login do usuário
    def login(self, username, password):
        password = None
        self.show_home(username)
                
    # Mostrar a tela inicial
    def show_home(self, username):
        self.login_view.destroy()
        self.home_view = HomeView(self, self.root, username)
        self.home_view.pack(fill="both", expand=True)
        
    def limpar_frame(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()


    def listar_produtos(self):
        produtos = self.produtos_model.listar_produtos()
        return produtos


    def run(self):
        self.root.mainloop()
        