import datetime
import tkinter as tk
from PIL import Image,ImageTk

janela = tk.Tk()
janela.geometry("680x780")
janela.title("Calculador de Idade")

nome = tk.Label(text="Nome:")
nome.grid(column=0,row=1)
ano = tk.Label(text="Ano")
ano.grid(column=0,row=2)


