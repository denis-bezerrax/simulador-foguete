import customtkinter as ctk

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


class Aplicativo(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Simulador de decolagem de foguete")
        self.geometry("900x600")

        # Divisão da tela
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Parte lateral
        self.barra_lateral = ctk.CTkFrame(self, width=300)
        self.barra_lateral.grid(row=0, column= 0, sticky="nswe", padx=(10, 10), pady=(10, 10))
        # Parte principal
        self.barra_principal = ctk.CTkFrame(self, width=400)
        self.barra_principal.grid(row=0, column=1, sticky="nswe", padx=(0, 10), pady=(10, 10))
        
        self.construir_abalateral()
        self.construir_abaprincipal()

    def construir_abalateral(self):
        
        self.titulo_lateral = ctk.CTkLabel(self.barra_lateral, 
                                   text="Foguete",
                                   font=ctk.CTkFont(size=24, weight="bold"))
                                   
        self.titulo_lateral.pack(pady=(30, 30), padx=(125, 125))

    def construir_abaprincipal(self):
        self.titulo_principal = ctk.CTkLabel(self.barra_principal,
                                   text="Simulador de decolagem",
                                   font=ctk.CTkFont(size=24, weight="bold"))
        self.titulo_principal.pack(pady=(20, 20), padx=(20, 20))

        # Combustivel
        self.subtitulo_combustivel = ctk.CTkLabel(self.barra_principal,
                                                  text="Combustível")
        self.subtitulo_combustivel.pack()
        self.campo_combustivel = ctk.CTkEntry(self.barra_principal)
        self.campo_combustivel.pack()

        # Carga inicial
        self.subtitulo_energia_inicial = ctk.CTkLabel(self.barra_principal,
                                                      text="Energia inicial")
        self.subtitulo_energia_inicial.pack()
        self.campo_energia_inicial = ctk.CTkEntry(self.barra_principal)
        self.campo_energia_inicial.pack()

        # Temperatura Interna
        self.subtitulo_temperatura_interna_inicial = ctk.CTkLabel(self.barra_principal,
                                                                  text="Temperatura interna inicial")
        self.subtitulo_temperatura_interna_inicial.pack()
        self.campo_temperatura_interna_inicial = ctk.CTkEntry(self.barra_principal)
        self.campo_temperatura_interna_inicial.pack()

        # Temperatura Externa
        self.subtitulo_temperatura_externa_inicial = ctk.CTkLabel(self.barra_principal,
                                                                  text="Temperatura externa inicial")
        self.subtitulo_temperatura_externa_inicial.pack()
        self.campo_temperatura_externa_inicial = ctk.CTkEntry(self.barra_principal)
        self.campo_temperatura_externa_inicial.pack()

        
        
        # Botão de iniciar decolagem
        def resultado():
            

        self.button_iniciar = ctk.CTkButton(self.barra_principal, text="Iniciar decolagem", command=resultado)
        self.button_iniciar.pack(pady=(30, 30))

        # Status do foguete
        self.status_do_foguete = ctk.CTkLabel(self.barra_principal,
                                              text="Status: O foguete está no chão",
                                              font=ctk.CTkFont(weight="bold"))
        self.status_do_foguete.pack()

        # Descrição do estado
        self.subtitulo_descricao = ctk.CTkLabel(self.barra_principal,
                                                text="Descrição",
                                                font=ctk.CTkFont(weight="bold"))
        self.subtitulo_descricao.pack(pady=20)
        self.texto_descricao = ctk.CTkLabel(self.barra_principal,
                                            text=""
                                            )


janela = Aplicativo()
janela.mainloop()