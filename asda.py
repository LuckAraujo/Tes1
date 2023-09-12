import tkinter as tk
import re

def validar_email():
    email = entrada_email.get()
    padrao_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if re.match(padrao_email, email):
        resultado.config(text="E-mail válido")
    else:
        resultado.config(text="E-mail inválido")

# Crie uma janela
janela = tk.Tk()
janela.title("Campo de E-mail")

# Crie um rótulo para o campo de e-mail
rotulo = tk.Label(janela, text="E-mail:")
rotulo.pack()

# Crie um campo de entrada para e-mail
entrada_email = tk.Entry(janela)
entrada_email.pack()

# Crie um botão para validar o e-mail
botao_validar = tk.Button(janela, text="Validar E-mail", command=validar_email)
botao_validar.pack()

# Crie um rótulo para exibir o resultado da validação
resultado = tk.Label(janela, text="")
resultado.pack()

# Inicie o loop principal
janela.mainloop()