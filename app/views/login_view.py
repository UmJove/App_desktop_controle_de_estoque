import customtkinter as ctk
from PIL import Image

class LoginView(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller


        # Pegar imagens
        login_image = ctk.CTkImage(light_image=Image.open("./assets/imgs/img-login.png"), dark_image=Image.open("./assets/imgs/img-login.png"), size=(350, 350))
        

        # Criar frames
        self.frame = ctk.CTkFrame(self, corner_radius=10, fg_color='transparent')
        self.frame.pack(pady=(100,0))

        self.frame_image = ctk.CTkFrame(self.frame, fg_color='transparent')
        self.frame_image.grid(row=0, column=0)

        self.frame_form = ctk.CTkFrame(self.frame, fg_color='transparent') 
        self.frame_form.grid(row=0, column=1, padx=(50, 0))

        footer_label = ctk.CTkLabel(self.frame, text="Sistema de Gestão de Funcionários | Desenvolvido por @UmJove | 2025")
        footer_label.grid(row=1, column=0, columnspan=2, pady=(100,0))

        # Adicionar os widgets
        label_image = ctk.CTkLabel(self.frame_image, image=login_image, text='')
        label_image.pack()

        self.title = ctk.CTkLabel(self.frame_form, text="Faça login", font=("arial bold", 20))
        self.title.pack()

        self.username_entry = ctk.CTkEntry(self.frame_form, placeholder_text="nome de usuário", width=200)
        self.username_entry.pack(pady=(20, 20))

        self.password_entry = ctk.CTkEntry(self.frame_form, placeholder_text="senha", width=200, show="*")
        self.password_entry.pack(pady=(10, 20))

        self.error_label = ctk.CTkLabel(self.frame_form, text=" ")
        self.error_label.pack()

        self.login_button = ctk.CTkButton(self.frame_form, text="Login", width=200, command=self.attempt_login)
        self.login_button.pack(pady=(10, 20))

    # Função do botão de login
    def attempt_login(self):
        print("botão clicado")
        username = self.username_entry.get()
        password = self.password_entry.get()
        self.controller.login(username, password)