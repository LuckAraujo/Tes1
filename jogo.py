import tkinter as tk
import os
from tkinter import PhotoImage


class Tela():
    def __init__(self, master):
        self.janela = master
        self.janela.geometry('800x600')
        self.janela.title('Tela De Play')
        self.janela.configure(bg='#3D89E1')


        self.telaInicial()

    def telaInicial(self):
        
        self.janela.title('Tela De Play')
        pastaAPP = os.path.dirname(__file__)
        img_path = os.path.join(pastaAPP, "imagem", "Logo.png")
        imgLogo = PhotoImage(file=img_path)
        l_logo = tk.Label(self.janela, image=imgLogo, background="#3D89E1")
        l_logo.image = imgLogo
        l_logo.pack(pady=(40, 0), padx=(20,0))

        btn1 = tk.Button(self.janela, text="Entrar",  height=2 ,width=20,  command=self.entrar,
        bg="#FF8000", activebackground="#FF8000", font=("Arial Black", 10))
        
        btn1.pack(padx= 20, pady=20)
        
        btn2 = tk.Button(self.janela, text="Cadastrar", height=2 ,width=20, command=self.cadastrar,
        bg="#FF9933", activebackground="#FF9933", font=("Arial Black", 10))
        
        btn2.pack(padx= 20, pady=20)
        
        btn3 = tk.Button(self.janela, text="Visitante", height=2 ,width=20, command=self.visitante, 
        bg="#FFB266", activebackground="#FFB266",font=("Arial Black", 10))
        
        btn3.pack(padx= 20, pady=20)

        
    def abrir_categorias(self):
            for widget in self.janela.winfo_children():
                widget.destroy()
            
            self.janela = self.janela
            self.janela.geometry('800x600')
            self.janela.title('Escolha uma Categoria')
            self.janela.configure(bg='#3D89E1')
            
            letraA = tk.Button(self.janela, text="FDS")
            letraA.pack()
    
    def entrar(self):
            for widget in self.janela.winfo_children():
                widget.destroy()
            
            self.janela = self.janela
            self.janela.geometry('800x600')
            self.janela.title('Entrar')
            self.janela.configure(bg='#3D89E1')

            botV = tk.Button(self.janela, text="Voltar", command= self.volta)
            botV.grid(row=0, column=0, padx= 5, pady= 5)


    
    def cadastrar(self):
            for widget in self.janela.winfo_children():
                widget.destroy()
            
            self.janela = self.janela
            self.janela.geometry('800x600')
            self.janela.title("Cadastrar")
            self.janela.configure(bg='#3D89E1')

            botV = tk.Button(self.janela, text="Voltar", command= self.volta)
            botV.grid(row=0, column=0, padx= 5, pady= 5)
    
    def visitante(self):
            for widget in self.janela.winfo_children():
                widget.destroy()
            
            self.janela = self.janela
            self.janela.geometry('800x600')
            self.janela.title('Visitante')
            self.janela.configure(bg='#3D89E1')

            botV = tk.Button(self.janela, text="Voltar", command= self.volta)
            botV.grid(row=0, column=0, padx= 5, pady= 5)
    
    def volta(self):
        for widget in self.janela.winfo_children():
                widget.destroy()
        self.telaInicial()
        
app = tk.Tk()
Tela(app)
app.mainloop()