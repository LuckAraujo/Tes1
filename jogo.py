import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import os
from tkinter import PhotoImage


class Tela():
    def __init__(self, master):
        self.janela = master
        self.janela.geometry('800x600')
        self.janela.title('Tela De Play')
        self.janela.configure(bg='#3D89E1')
        
        pastaAPP = os.path.dirname(__file__)
        img_path = os.path.join(pastaAPP, "imagem", "Logo.png")
        imgLogo = PhotoImage(file=img_path)
        l_logo = ttk.Label(self.janela, image=imgLogo, background="#3D89E1")
        l_logo.image = imgLogo
        l_logo.grid(row=0, columnspan= 2, column=0,pady=(40, 0), padx=(20,0))

        btn1 = ttk.Button(self.janela, text="Entrar", bootstyle=OUTLINE, width=40,  command=self.abrir_categorias)
        btn1.grid(row=1, column= 0,padx= 20, pady=20)
        btn2 = ttk.Button(self.janela, text="Cadastrar", bootstyle=OUTLINE, width=40, command=self.abrir_categorias)
        btn2.grid(row=1, column= 1,padx= 20, pady=20)
        btn3 = ttk.Button(self.janela, text="Visitante", bootstyle=OUTLINE, width=40, command=self.abrir_categorias)
        btn3.grid(row=2, columnspan= 2, column=0,padx= 20, pady=20)

        self.janela.columnconfigure(0, weight=5)
        self.janela.columnconfigure(1, weight=5)
        self.janela.columnconfigure(2, weight=1)

    def abrir_categorias(self):
            for widget in self.janela.winfo_children():
                widget.destroy()
            
            self.janela = self.janela
            self.janela.geometry('800x600')
            self.janela.title('Escolha uma Categoria')
            self.janela.configure(bg='#3D89E1')
            
            style = ttk.Style()
            style.configure("LetraButton.TButton", padding=10, font=("Helvetica", 12))
            
            letraA = ttk.Button(self.janela, text="FDS", style="LetraButton.TButton")
            letraA.pack()

app = ttk.Window(themename='lumen')
Tela(app)
app.mainloop()