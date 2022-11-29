
import datetime
import tkinter as tk
from PIL import Image, ImageTk

janela = tk.Tk()
janela.geometry("680x780")
janela.title("Calculador de Idade")


nome = tk.Label(text="Nome:")
nome.grid(column=0,row=1)
ano = tk.Label(text="Ano")
ano.grid(column=0,row=2)
mes = tk.Label(text="Mês")
mes.grid(column=0,row=3)
dia = tk.Label(text='Dia')
dia.grid(column=0,row=4)

nomeEntry = tk.Entry()
nomeEntry.grid(column=1,row=1)
anoEntry = tk.Entry()
anoEntry.grid(column=1,row=2)
mesEntry = tk.Entry()
mesEntry.grid(column=1,row=3)
diaEntry = tk.Entry()
diaEntry.grid(column=1,row=4)

def getInput():
    nome=nomeEntry.get()
    dados = Pessoa(nome,datetime.date(int(anoEntry.get()),int(mesEntry.get()),int(diaEntry.get())))

    textArea = tk.Text(master=janela,height=10,width=25)
    textArea.grid(column=1,row=6)
    resposta = f"Coé {dados.nome}!!!, Sua Idade é {dados.idade()}\nUse produtos da AVON "
    textArea.insert(tk.END,resposta)

botao = tk.Button(janela,text='Calcular Idade',command=getInput,bg="red")
botao.grid(column=1,row=5)

class Pessoa:
    def __init__(self,nome,aniversario):
        self.nome = nome
        self.aniversario = aniversario


    def idade(self):
        hoje = datetime.date.today()
        idade = hoje.year - self.aniversario.year
        return idade


foto = Image.open("imagem.jpg")
foto.thumbnail((300,300),Image.ANTIALIAS)
photo = ImageTk.PhotoImage(foto)
foto_label = tk.Label(image=photo)
foto_label.grid(column=1,row=0)





janela.mainloop()


