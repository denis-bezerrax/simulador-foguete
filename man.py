import tkinter as tk
janela = tk.Tk()
janela.title("Programa do sistema de foguete")
janela.geometry("500x300")
janela.configure(bg="white")


mensagem = 'O foguete está no chão'
# Título
titulo = tk.Label(janela,
            text='Simulador de decolagem\n',
            font=("Arial", 16, "bold"),
            bg="white",
            fg="#1a1a2e")
titulo.pack()

tk.Label(janela, text='KWH').pack()
kwh_entry = tk.Entry(janela)
kwh_entry.pack()

tk.Label(janela, text='Energia em %').pack()
energia_entry = tk.Entry(janela)
energia_entry.pack()

tk.Label(janela, text='Temperatura interna em °C').pack()
temperatura_interna_entry = tk.Entry(janela)
temperatura_interna_entry.pack()

tk.Label(janela, text='Temperatura externa em °C').pack()
temperatura_externa_entry = tk.Entry()
temperatura_externa_entry.pack()


        

def resposta_botao():
    energia = int(energia_entry.get())
    kwh = int(kwh_entry.get())
    interna = int(temperatura_interna_entry.get())
    externa = int(temperatura_externa_entry.get())
    if energia >= 75 and kwh >= 500000 and interna >= 15 and interna <= 40 and externa >= -15 and externa <= 2000:
        status_tela['text'] = '\nO foguete está decolando!'
        descricao_do_foguete['text'] = '\n'

    elif energia <= 75 and kwh >= 500000 and interna >= 15 and interna <= 40 and externa >= -15 and externa <= 2000:
        status_tela['text'] = '\nO foguete não está pronto para decolar'
        descricao_do_foguete['text'] = '\nA quantidade de energia está a baixo do recomendado de 75%. É muito arriscado com essa quantidade de energia, imprevistos acontecem.'
    elif energia >= 75 and kwh <= 500000 and interna >= 15 and interna <= 40 and externa >= -15 and externa <= 2000:
        status_tela['text'] = '\nO foguete não está pronto para decolar'
        descricao_do_foguete['text'] = '\nÉ necessário uma quantidade mínima de 500000 quilos de combustível para decolar.'
    elif energia >= 75 and kwh <= 500000 and interna <= 15 or interna >= 40 and externa >= -15 and externa <= 2000:
        status_tela['text'] = '\nO foguete não está pronto para decolar'
        descricao_do_foguete['text'] = '\nA temperatura está inadequada para decolagem. A temperatura segura interna do foguete de início deve estar entre 15°C até 40°C.'
    elif energia >= 75 and kwh >= 500000 and interna >= 15 and interna <= 40 and externa <= -15 or externa >= 2000:
        status_tela['text'] = '\nO foguete não está pronto para decolar'
        descricao_do_foguete['text'] = '\nA temperatura está inadequada para decolagem. A temperatura externa do foguete de início deve estar entre -15°C até 2000°C.'
    else:
        status_tela['text'] = '\nO foguete não está pronto para decolar'

tk.Button(janela, text='Iniciar decolagem', command=resposta_botao).pack()


status_tela = tk.Label(janela, text=f'\nStatus: O foguete está no chão')
status_tela.pack()

descricao_do_foguete = tk.Label(janela, text=f'\n')
descricao_do_foguete.pack()


tempo_de_decolagem = tk.Label(janela, text=f'\nDuração da decolagem:')
tempo_de_decolagem.pack()

janela.mainloop()
