import customtkinter as ctk
from PIL import Image
import random
import os
import sys

def caminho_recurso(nome):
    if getattr(sys, "frozen", False):
        pasta = sys._MEIPASS
    else:
        pasta = os.path.dirname(os.path.abspath(__file__))

    return os.path.join(pasta, nome)

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class Aplicativo(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Missão Aurora")
        self.geometry("600x600")

        # Divisão da tela
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Parte lateral
        self.barra_lateral = ctk.CTkFrame(self, width=(300))
        self.barra_lateral.grid(row=0, column=0, sticky="nswe", padx=(10, 10), pady=(10, 10))
        # Parte principal           
        self.barra_principal = ctk.CTkFrame(self, width=300)
        self.barra_principal.grid(row=0, column=1, sticky="nswe", padx=(0, 10), pady=(10, 10))
        self.barra_principal.grid_columnconfigure(0, weight=1)
        self.barra_principal.grid_rowconfigure(0, weight=1)
        
        self.construir_abalateral()
        self.construir_abaprincipal()

        self.simulacao_id = None
        self.queda_id = None
        self.cronometro_id = None

    def construir_abalateral(self):
        self.tela_frame_lateral = ctk.CTkFrame(self.barra_lateral,)
        self.tela_frame_lateral.pack()

        # Foto do foguete
        self.img_I = ctk.CTkImage(dark_image=Image.open(caminho_recurso("foguete_1.png")), size=(300,300))
        self.img_II = ctk.CTkImage(dark_image=Image.open(caminho_recurso("foguete_2.png")), size=(300,300))
        self.img_III = ctk.CTkImage(dark_image=Image.open(caminho_recurso("foguete_3.png")), size=(300,300))
        self.img_IV = ctk.CTkImage(dark_image=Image.open(caminho_recurso("foguete_4.png")), size=(300,300))
        self.img_V = ctk.CTkImage(dark_image=Image.open(caminho_recurso("foguete_5.png")), size=(300,300))
        self.img_VI = ctk.CTkImage(dark_image=Image.open(caminho_recurso("foguete_6.png")), size=(300,300))
        self.img_VII = ctk.CTkImage(dark_image=Image.open(caminho_recurso("foguete_7.png")), size=(300,300))
        self.img_VIII = ctk.CTkImage(dark_image=Image.open(caminho_recurso("foguete_8.png")), size=(300,300))
        self.img_IX = ctk.CTkImage(dark_image=Image.open(caminho_recurso("foguete_9.png")), size=(300,300))
        self.img_X = ctk.CTkImage(dark_image=Image.open(caminho_recurso("foguete_10.png")), size=(300,300))
        self.img_XI = ctk.CTkImage(dark_image=Image.open(caminho_recurso("foguete_11.png")), size=(300,300))
        self.img_XII = ctk.CTkImage(dark_image=Image.open(caminho_recurso("foguete_12.png")), size=(300,300))
        self.imge = ctk.CTkImage(dark_image=Image.open(caminho_recurso("foguete_sem.png")), size=(300,300))
        self.imge_I = ctk.CTkImage(dark_image=Image.open(caminho_recurso("efoguete_1.png")), size=(300,300))
        self.imge_II = ctk.CTkImage(dark_image=Image.open(caminho_recurso("foguete_caindo.png")), size=(300,300))
        self.imge_III = ctk.CTkImage(dark_image=Image.open(caminho_recurso("foguete_chao.png")), size=(300,300))

        self.imagem_foguete = ctk.CTkLabel(self.tela_frame_lateral,
                                            image=self.img_I,
                                            text="",
                                            fg_color="transparent"
                                            )  

        self.imagem_foguete.grid(row=0, column=0)

        # Tempo
        self.tempo = 0
        self.minutos = 0
        self.segundos = 0
        self.label_tempo = ctk.CTkLabel(self.tela_frame_lateral,
                                           text="TEMPO:\n00:00")
        self.label_tempo.grid(row=1, column=0)
        

        # Altura do foguete
        self.altura = 0
        self.velocidade = 0
        self.mostrador_altura_e_velocidade = ctk.CTkLabel(self.barra_lateral,
                                             text=(f"Altura: {self.altura} quilômetros | Velocidade {self.velocidade} Km/s"))
        self.mostrador_altura_e_velocidade.pack()

        # Integridade do foguete
        self.integridade_do_foguete = ctk.CTkLabel(self.barra_lateral,
                                                   text="INTEGRIDADE ESTRUTURAL",
                                                   font=ctk.CTkFont(weight="bold"))
        self.integridade_do_foguete.pack()

        self.button_integridade = ctk.CTkButton(self.barra_lateral,
                                                       text="INDISPONÍVEL")
        self.button_integridade.pack()

        # Módulos críticos
        self.navegacao = "N/a"
        self.comunicacao = "N/a"
        self.motores = "N/a"
        self.subtitulo_modulos = ctk.CTkLabel(self.barra_lateral,
                                              text="MÓDULOS CRÍTICOS",
                                              font=ctk.CTkFont(weight="bold"))
        self.subtitulo_modulos.pack()
        self.button_modulos = ctk.CTkButton(self.barra_lateral,
                                            text=f"Navegação: {self.navegacao}\n Comunicação: {self.comunicacao}\n Motores: {self.motores}")
        self.button_modulos.pack()

        # Combustível - barra lateral
        self.mostrador_combustivel_lateral = ctk.CTkLabel(self.barra_lateral,
                                                          text="COMBUSTÍVEL",
                                                          font=ctk.CTkFont(weight="bold"))
        self.mostrador_combustivel_lateral.pack()
        self.button_combustivel_lateral = ctk.CTkButton(self.barra_lateral,
                                                        text="0 quilos")
        self.button_combustivel_lateral.pack()

        # Energia - barra lateral
        self.mostrador_energia_lateral = ctk.CTkLabel(self.barra_lateral,
                                                      text="ENERGIA",
                                                      font=ctk.CTkFont(weight="bold"))
        self.mostrador_energia_lateral.pack()
        self.button_energia_lateral = ctk.CTkButton(self.barra_lateral,
                                                   text="0%")
        self.button_energia_lateral.pack()
        # Temperatura interna - barra lateral
        self.mostrador_temperatura_interna_lateral = ctk.CTkLabel(self.barra_lateral,
                                                              text="TEMPERATURA INTERNA",
                                                              font=ctk.CTkFont(weight="bold"))
        self.mostrador_temperatura_interna_lateral.pack()
        self.button_temperatura_interna_lateral = ctk.CTkButton(self.barra_lateral,
                                                              text="0℃")
        self.button_temperatura_interna_lateral.pack()
        
        # Temperatura externa - barra lateral
        self.mostrador_temperatura_externa_lateral = ctk.CTkLabel(self.barra_lateral,
                                                                  text="TEMPERATURA EXTERNA",
                                                                  font=ctk.CTkFont(weight="bold"))
        self.mostrador_temperatura_externa_lateral.pack()
        self.button_temperatura_externa_lateral = ctk.CTkButton(self.barra_lateral,
                                                                text="0℃")
        self.button_temperatura_externa_lateral.pack()
        # Pressão dos tanques - barra lateral
        self.mostrador_pressao_dos_tanques_lateral = ctk.CTkLabel(self.barra_lateral,
                                                                  text="PRESSÃO DOS TANQUES",
                                                                  font=ctk.CTkFont(weight="bold"))
        self.mostrador_pressao_dos_tanques_lateral.pack()
        self.button_pressao_dos_tanques_lateral = ctk.CTkButton(self.barra_lateral,
                                                                text="0 bar")
        self.button_pressao_dos_tanques_lateral.pack()

    # Aba que o usuário insere as informações
    def construir_abaprincipal(self):
        self.tela_frame = ctk.CTkFrame(self.barra_principal, fg_color="transparent")
        self.tela_frame.grid(row=0, column=0, sticky="snwe")
        self.tela_frame.grid_columnconfigure(0, weight=1)
        self.tela_frame.grid_columnconfigure(1, weight=1)
        self.titulo_principal = ctk.CTkLabel(self.tela_frame,
                                   text="SIMULADOR DE DECOLAGEM",
                                   font=ctk.CTkFont(size=24, weight="bold")
                                   )
        self.titulo_principal.grid(row=0, column=0, columnspan=2, pady=10)
        
        # Função que verifica se é um número a informação inserida pelo usuário
        def validacao(valor):
            if valor in ("", "-", "."):
                return True

            if valor.count(".") > 1:
                return False

            if valor.startswith("-"):
                valor = valor[1:]

            return valor.replace(".", "").isdigit()

        # Integridade Estrutural
        
        self.subtitulo_integridade_estrutual = ctk.CTkLabel(self.tela_frame,
                                                                    text="Integridade estrutural")
        self.subtitulo_integridade_estrutual.grid(row=1,column=0, columnspan=2)
        self.integridade = ctk.IntVar(value=0)

        # Verificação da estrutura do foguete
        def verificar_integridade():
            if self.integridade.get() == 1:
                self.button_integridade.configure(text="ÍNTEGRO", fg_color="green", hover_color="green")
                self.motores = "Ok"
                self.comunicacao = "Ok"
                self.navegacao = "Ok"
                self.button_modulos.configure(text=f"Navegação: {self.navegacao}\n Comunicação: {self.comunicacao}\n Motores: {self.motores}",
                                              fg_color="green",
                                              hover_color="green")
            else:
                self.motores = "Falha"
                self.comunicacao = "Falha"
                self.navegacao = "Falha"
                self.button_modulos.configure(text=f"Navegação: {self.navegacao}\n Comunicação: {self.comunicacao}\n Motores: {self.motores}",
                                              fg_color="red",
                                              hover_color="red")
                self.button_integridade.configure(text="DANIFICADO", fg_color="red", hover_color="red")
        self.aleatorio_integridade = 0
        self.integridadeon = ctk.CTkRadioButton(self.tela_frame,
                                                        text="Íntegro",
                                                        variable=self.integridade,
                                                        value=1,
                                                        command=verificar_integridade)
        self.integridadeon.grid(row=2,column=0, columnspan=2)
        self.integridadeof = ctk.CTkRadioButton(self.tela_frame, 
                                                        text="Danificado",
                                                        variable=self.integridade,
                                                        value=2, 
                                                        command=verificar_integridade)
        self.integridadeof.grid(row=3,column=0, columnspan=2)

        # Combustivel
        self.subtitulo_combustivel_inicial = ctk.CTkLabel(self.tela_frame,
                                                  text="Combustível ")
        self.subtitulo_combustivel_inicial.grid(row=4,column=0, columnspan=2)

        self.campo_combustivel_inicial = ctk.CTkEntry(self.tela_frame, 
                                                      validate="key",
                                                      validatecommand=(self.register(validacao), "%P"))
        self.campo_combustivel_inicial.grid(row=5,column=0, columnspan=2)

        # Carga inicial
        self.subtitulo_energia_inicial = ctk.CTkLabel(self.tela_frame,
                                                      text="Energia inicial")
        self.subtitulo_energia_inicial.grid(row=6,column=0, columnspan=2)
        self.campo_energia_inicial = ctk.CTkEntry(self.tela_frame, 
                                                      validate="key",
                                                      validatecommand=(self.register(validacao), "%P"))
        self.campo_energia_inicial.grid(row=7, column=0, columnspan=2)

        # Temperatura Interna
        self.subtitulo_temperatura_interna_inicial = ctk.CTkLabel(self.tela_frame,
                                                                  text="Temperatura interna inicial")
        self.subtitulo_temperatura_interna_inicial.grid(row=8,column=0, columnspan=2)
        self.campo_temperatura_interna_inicial = ctk.CTkEntry(self.tela_frame, 
                                                      validate="key",
                                                      validatecommand=(self.register(validacao), "%P"))
        self.campo_temperatura_interna_inicial.grid(row=9,column=0, columnspan=2)

        # Temperatura Externa
        self.subtitulo_temperatura_externa_inicial = ctk.CTkLabel(self.tela_frame,
                                                                  text="Temperatura externa inicial ")
        self.subtitulo_temperatura_externa_inicial.grid(row=10,column=0, columnspan=2)
        self.campo_temperatura_externa_inicial = ctk.CTkEntry(self.tela_frame, 
                                                      validate="key",
                                                      validatecommand=(self.register(validacao), "%P"))
        self.campo_temperatura_externa_inicial.grid(row=11,column=0, columnspan=2)

        # Pressão dos tanques

        self.subtitulo_pressao_dos_tanques_inicial = ctk.CTkLabel(self.tela_frame,
                                                                  text="Pressão dos tanques")
        self.subtitulo_pressao_dos_tanques_inicial.grid(row=12,column=0, columnspan=2) 
        self.campo_pressao_dos_tanques_inicial = ctk.CTkEntry(self.tela_frame, 
                                                      validate="key",
                                                      validatecommand=(self.register(validacao), "%P"))
        self.campo_pressao_dos_tanques_inicial.grid(row=13,column=0, columnspan=2)

        def informacoes_do_usuario():
            self.combustivel = float(self.campo_combustivel_inicial.get())
            self.energia = float(self.campo_energia_inicial.get())
            self.t_interna = float(self.campo_temperatura_interna_inicial.get())
            self.t_externa = float(self.campo_temperatura_externa_inicial.get())
            self.pressao_tanques = float(self.campo_pressao_dos_tanques_inicial.get())

        def verificacao_das_variaveis():
            # Verificação do combustível
            if self.combustivel <= 0:
                self.status_do_foguete.configure(text="Status: O foguete cairá!")
                self.texto_descricao.configure(text="O foguete está sem combustível, ele perderá velocidade e cairá")
                self.button_combustivel_lateral.configure(fg_color="darkred", hover_color="darkred")
                self.imagem_foguete.configure(image=self.imge)
                if self.combustivel <= 0:
                      self.combustivel = 0
                      self.pressao_tanques = 0
                self.after_cancel(self.simulacao_id)
                self.simulacao_id = None
                queda()

                
            elif self.combustivel <= 15000:
                self.status_do_foguete.configure(text="Status: O foguete está com problemas")
                self.texto_descricao.configure(text="O foguete está ficando sem combustível")
                self.button_combustivel_lateral.configure(fg_color="red", hover_color="red")
            elif self.combustivel <= 35000:
                self.button_combustivel_lateral.configure(fg_color="darkorange", hover_color="darkorange")
            else:
                self.button_combustivel_lateral.configure(fg_color="green", hover_color="green")

            # Verificação da energia
            if self.energia <= 0:
                self.status_do_foguete.configure(text="Status: O foguete explodiu!")
                self.texto_descricao.configure(text="O foguete está sem energia. Não podendo se auto-regular.")
                self.button_energia_lateral.configure(fg_color="darkred", hover_color="darkred")
                self.imagem_foguete.configure(self.imagem_foguete.configure(image=self.imge_I))
                foguete_para()
            elif self.energia <= 20:
                self.status_do_foguete.configure(text="Status: O foguete está com problemas")
                self.texto_descricao.configure(text="O foguete está ficando sem energia")
                self.button_energia_lateral.configure(fg_color="red", hover_color="red")
            elif self.energia <= 35:
                self.button_energia_lateral.configure(fg_color="darkorange", hover_color="darkorange")
            else:
                self.button_energia_lateral.configure(fg_color="green", hover_color="green")

            # Verificação da temperatura interna
            if self.t_interna >= 50:
                self.status_do_foguete.configure(text="Status: O foguete explodiu pela temperatura!")
                self.texto_descricao.configure(text="A temperatura interna atingiu um ponto que danificou a carga e que comprometeu os sistemas.")
                self.button_temperatura_interna_lateral.configure(fg_color="darkred", hover_color="darkred")
                self.imagem_foguete.configure(image=self.imge_I)
                foguete_para()
            elif self.t_interna >= 40:
                self.status_do_foguete.configure(text="Status: O foguete está com problemas")
                self.texto_descricao.configure(text="A temperatura interna está ficando alta.")
                self.button_temperatura_interna_lateral.configure(fg_color="red", hover_color="red")
            elif self.t_interna >= 35:
                self.button_temperatura_interna_lateral.configure(fg_color="darkorange", hover_color="darkorange")
            else:
                self.button_temperatura_interna_lateral.configure(fg_color="green", hover_color="green")

            # Verificação da temperatura externa
            if self.t_externa >= 1500:
                self.status_do_foguete.configure(text="Status: O foguete explodiu pela temperatura!")
                self.texto_descricao.configure(text="A temperatura externa atingiu um ponto que afetou o sistema como também todo o seu combustível e sua estrutura.")
                self.button_temperatura_externa_lateral.configure(fg_color="darkred", hover_color="darkred")
                self.imagem_foguete.configure(image=self.imge_I)
                foguete_para()
            elif self.t_externa >= 1000:
                self.status_do_foguete.configure(text="Status: O foguete está com problemas")
                self.texto_descricao.configure(text="A temperatura externa está ficando muito alta.")
                self.button_temperatura_externa_lateral.configure(fg_color="red", hover_color="red")
            elif self.t_externa >= 600:
                self.button_temperatura_externa_lateral.configure(fg_color="darkorange", hover_color="darkorange")
            elif self.t_externa >= 300:
                            self.button_temperatura_externa_lateral.configure(fg_color="orange", hover_color="orange")
            else:
                self.button_temperatura_externa_lateral.configure(fg_color="green", hover_color="green")

            # Verificação da pressão dos tanques
            if self.pressao_tanques >= 35:
                self.status_do_foguete.configure(text="Status: O foguete explodiu pela pressão!")
                self.texto_descricao.configure(text="A pressão dos tanques ficou muito alta.")
                self.button_pressao_dos_tanques_lateral.configure(fg_color="darkred", hover_color="darkred")
                self.imagem_foguete.configure(image=self.imge_I)
                foguete_para()
            elif self.pressao_tanques >= 30:
                self.status_do_foguete.configure(text="Status: O foguete está com problemas")
                self.texto_descricao.configure(text="A pressão dos tanques está crítica.")
                self.button_pressao_dos_tanques_lateral.configure(fg_color="red", hover_color="red")
            elif self.pressao_tanques >= 25:
                self.button_pressao_dos_tanques_lateral.configure(fg_color="orange", hover_color="orange")
            else:
                self.button_pressao_dos_tanques_lateral.configure(fg_color="green", hover_color="green")

            # Verificação da integridade estrutural e dos módulos
            if self.aleatorio_integridade >= 298:
                self.navegacao = "Falha"
                self.button_modulos.configure(fg_color="orange", hover_color="orange")
                self.button_integridade.configure(text="DANIFICADO", fg_color="red", hover_color="red")
                self.texto_descricao.configure(text="O foguete apresentou danos a sua estrutura")
            elif self.aleatorio_integridade >= 295:
                self.comunicacao = "Falha"
                self.button_modulos.configure(fg_color="orange", hover_color="orange")
                self.button_integridade.configure(text="DANIFICADO", fg_color="red", hover_color="red")
                self.texto_descricao.configure(text="O foguete apresentou danos a sua estrutura")
            elif self.aleatorio_integridade >= 292:
                self.motores = "Falha"
                self.button_modulos.configure(fg_color="orange", hover_color="orange")
                self.button_integridade.configure(text="DANIFICADO", fg_color="red", hover_color="red")
                self.texto_descricao.configure(text="O foguete apresentou danos a sua estrutura")

            if self.navegacao == "Falha" and self.comunicacao == "Falha" and self.motores == "Falha":
                self.button_modulos.configure(fg_color="darkred", hover_color="darkred")
                self.status_do_foguete.configure(text="Status: O foguete explodiu!")
                self.texto_descricao.configure(text="Todos os módulos do foguete pararam de funcionar.")
                self.imagem_foguete.configure(image=self.imge_I)
                atualizar_mostradores()
                foguete_para()

            if self.altura >= 130:
                self.status_do_foguete.configure(text="O foguete chegou no espaço!")
                self.texto_descricao.configure(text="Parabéns por ter conseguido chegar ao espaço.")
                foguete_para()

            

        def atualizar_mostradores():
            self.mostrador_altura_e_velocidade.configure(text=f"Altura: {self.altura:.2f} quilômetros | Velocidade {self.velocidade:.2f}Km/s")
            self.button_combustivel_lateral.configure(text=f"{self.combustivel} quilos")
            self.button_energia_lateral.configure(text=f"{self.energia}%")
            self.button_temperatura_interna_lateral.configure(text=f"{self.t_interna:.1f}℃")
            self.button_temperatura_externa_lateral.configure(text=f"{self.t_externa:.1f}℃")
            self.button_pressao_dos_tanques_lateral.configure(text=f"{self.pressao_tanques:.1f} bar")
            self.label_tempo.configure(text=f"TEMPO\n{self.minutos:02d}:{self.segundos:02d}")
            self.button_modulos.configure(text=f"Navegação: {self.navegacao}\n Comunicação: {self.comunicacao}\n Motores: {self.motores}")

        def atualizar_imagens_foguete():
            if self.altura <= 0.5 and self.altura <= 1.99:
                self.imagem_foguete.configure(image=self.img_II)
            elif self.altura >= 2 and self.altura <= 4.99:
                self.imagem_foguete.configure(image=self.img_III)
                self.status_do_foguete.configure(text="Status: Voando!")
            elif self.altura >= 5 and self.altura <= 9.99:
                            self.imagem_foguete.configure(image=self.img_IV)
            elif self.altura >= 10 and self.altura <= 19.99:
                            self.imagem_foguete.configure(image=self.img_V)
            elif self.altura >= 20 and self.altura <= 29.99:
                            self.imagem_foguete.configure(image=self.img_VI)
            elif self.altura >= 30 and self.altura <= 44.99:
                            self.imagem_foguete.configure(image=self.img_VII)
            elif self.altura >= 45 and self.altura <= 59.99:
                            self.imagem_foguete.configure(image=self.img_VIII)
            elif self.altura >= 60 and self.altura <= 74.99:
                            self.imagem_foguete.configure(image=self.img_IX)
            elif self.altura >= 75 and self.altura <= 89.99:
                            self.imagem_foguete.configure(image=self.img_X)
            elif self.altura >= 90 and self.altura <= 99.99:
                            self.imagem_foguete.configure(image=self.img_XI)
            elif self.altura >= 100 and self.altura < 10000:
                            self.imagem_foguete.configure(image=self.img_XII)
            
              
        
        # Simulação
        def simulacao():
            self.altura += self.velocidade
            self.velocidade += 0.03
            self.combustivel -= 1129
            self.energia -= 0.5
            self.t_interna += (self.velocidade * 60) * 0.003
            self.t_externa += (self.velocidade * 60) * 0.1
            self.pressao_tanques += 0.3
            self.aleatorio_integridade = random.randint(1,300)

            

            atualizar_mostradores()
            atualizar_imagens_foguete()
            
            self.simulacao_id = self.after(1000, simulacao)
            verificacao_das_variaveis()

        # Função de queda do foguete
        def queda():
            self.altura += self.velocidade
            self.velocidade -= 0.00981
            self.t_interna += (self.velocidade * 60) * 0.0010
            self.t_externa += (self.velocidade * 60) * 0.08

            if self.velocidade <= 0:
                self.imagem_foguete.configure(image=self.imge_II)
                self.status_do_foguete.configure(text="Status: O foguete está caindo!")
                self.texto_descricao.configure(text="O foguete explodirá quando atingir o chão.")
            if self.altura <= 0:
                self.altura = 0

            atualizar_mostradores()
            self.queda_id = self.after(1000, queda)
            if self.altura <= 0:
                foguete_para()
                self.imagem_foguete.configure(image=self.imge_III)
                self.status_do_foguete.configure(text="Status: O foguete explodiu!")
                self.texto_descricao.configure(text="O foguete atingiu o chão.")

        # Resetar as variaveis
        def reset():
            self.altura = 0
            self.velocidade = 0
            self.tempo = 0
            self.minutos = 0
            self.segundos = 0
            self.motores = "Ok"
            self.comunicacao = "Ok"
            self.navegacao = "Ok"
            self.button_modulos.configure(fg_color="green", hover_color="green")
            informacoes_do_usuario()
            atualizar_mostradores()

            
        
        def parar_simulacao():
            if self.simulacao_id is not None:
                self.after_cancel(self.simulacao_id)
                self.simulacao_id = None
            if self.cronometro_id is not None:
                self.after_cancel(self.cronometro_id)
                self.cronometro_id = None
            if self.queda_id is not None:
                self.after_cancel(self.queda_id)
                self.queda_id = None
            self.imagem_foguete.configure(image=self.img_I)
            self.button_integridade.configure(text="ÍNTEGRO", fg_color="green", hover_color="green")
            self.status_do_foguete.configure(text="Status: O foguete está no chão!")
            self.texto_descricao.configure(text="")
            mudar_button_parar()
            reset()

        def foguete_para():
            if self.simulacao_id is not None:
                self.after_cancel(self.simulacao_id)
                self.simulacao_id = None
            if self.cronometro_id  is not None:
                self.after_cancel(self.cronometro_id)
                self.cronometro_id = None
            if self.queda_id is not None:
                self.after_cancel(self.queda_id)
                self.queda_id = None

        def cronometro():
            self.tempo += 1
            self.minutos = self.tempo // 60
            self.segundos = self.tempo % 60
            self.label_tempo.configure(text=f"TEMPO:\n{self.minutos:02d}:{self.segundos:02d}")

            self.cronometro_id = self.after(1000, cronometro)
            
        def mudar_button_iniciar():
                  self.button_iniciar.configure(command=None, fg_color="#304566", hover_color="#304566")
                  self.button_parar.configure(command=parar_simulacao, fg_color="#2761a7", hover_color="#304566")
        def mudar_button_parar():
              self.button_parar.configure(command=None, fg_color="#304566", hover_color="#304566")
              self.button_iniciar.configure(command=resultado, fg_color="#2761a7", hover_color="#304566")

        # Botão de iniciar decolagem
        def resultado():
            try:
                combustivel = float(self.campo_combustivel_inicial.get())
                energia = float(self.campo_energia_inicial.get())
                t_interna = float(self.campo_temperatura_interna_inicial.get())
                t_externa = float(self.campo_temperatura_externa_inicial.get())
                pressao_tanques = float(self.campo_pressao_dos_tanques_inicial.get())
                integridade = self.integridade.get()
            except:
                self.texto_descricao.configure(text="Insira valores nos campos vazios.")
                return

            # Verificação das informações inseridas pelo usuário
            if combustivel < 35000 or combustivel > 1000000:
                self.status_do_foguete.configure(text="Status: DECOLAGEM ABORTADA!")
                self.texto_descricao.configure(text="O combustível exigido para uma decolagem é 35000 quilogramas, sendo o máximo 1000000 de quilogramas.")
                
            elif energia < 35 or energia > 100:
                self.status_do_foguete.configure(text="Status: DECOLAGEM ABORTADA!")
                self.texto_descricao.configure(text="Quantidade de energia inadequada para uma decolagem segura. O nível exigido é de 35% até 100%.")

            elif not 15 <= t_interna <= 30:
                self.status_do_foguete.configure(text="Status: DECOLAGEM ABORTADA!"
            )
                self.texto_descricao.configure(text="A temperatura interna deve estar entre 15℃ e 30℃.")

            elif not -60 <= t_externa <= 50:
                self.status_do_foguete.configure(text="Status: DECOLAGEM ABORTADA!")
                self.texto_descricao.configure(text="A temperatura externa deve estar entre -60℃ e 50.")

            elif not 2.5 <= pressao_tanques <= 4.0:
                self.status_do_foguete.configure(text="Status: DECOLAGEM ABORTADA!")
                self.texto_descricao.configure(text="A pressão inicial dos tanques para decolagem deve estar entre 2.5 e 4.0.")


            elif integridade == 2 or integridade == 0:
                self.status_do_foguete.configure(text="Status: DECOLAGEM ABORTADA!")
                self.texto_descricao.configure(text="O foguete deve estar íntegro para iniciar a decolagem.")

            else:
                self.status_do_foguete.configure(text="Status: DECOLANDO!")
                self.texto_descricao.configure(text="O foguete não apresenta nenhuma anomalia.")
                self.imagem_foguete.configure(image=self.img_II)
                informacoes_do_usuario()
                simulacao()
                cronometro()
                mudar_button_iniciar()

        # Botão de ínicio de decolagem
        
        self.botoes_tela = ctk.CTkFrame(self.tela_frame, fg_color="transparent")
        self.botoes_tela.grid(row=14, column=0, columnspan=2, pady=20)
        self.button_iniciar = ctk.CTkButton(self.botoes_tela, text="Iniciar", command=resultado, fg_color="#2761a7", hover_color="#304566")
        self.button_iniciar.grid(row=0, column=0, padx=5)
        self.button_parar = ctk.CTkButton(self.botoes_tela, text="Parar", fg_color="#304566", hover_color="#304566", command=None)
        self.button_parar.grid(row=0, column=1, padx=0)


        # Status do foguete
        self.status_do_foguete = ctk.CTkLabel(self.tela_frame,
                                              text=f"Status: O foguete está no chão",
                                              font=ctk.CTkFont(weight="bold"))
        self.status_do_foguete.grid(row=15, column=0, columnspan=2)

        # Descrição do estado
        self.subtitulo_descricao = ctk.CTkLabel(self.tela_frame,
                                                text="Descrição",
                                                font=ctk.CTkFont(weight="bold"))
        self.subtitulo_descricao.grid(row=16, column=0, padx=0, columnspan=2)
        self.texto_descricao = ctk.CTkLabel(self.tela_frame,
                                            text=""
                                            )
        self.texto_descricao.grid(row=17, column=0, columnspan=2)


janela = Aplicativo()
janela.mainloop()