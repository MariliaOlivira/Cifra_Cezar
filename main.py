from curses.ascii import isdigit
import string
alfa = list(string.ascii_lowercase) 

encode = input("Digite uma letra coisa linda: ")
key = int(input("Digite a chave: "))

answer = ''

for i in encode:
    if i == ' ':
        answer += ' '
        continue
    index = alfa.index(i)
    answer += alfa[index + (key)]


import tkinter as tk
from tkinter import messagebox

def cifra_cesar_encode(texto: str, chave: int) -> str:
    resultado = ""
    for letra in texto:
        if letra.isalpha():
            indice = (ord(letra) - 97 + chave) % 26
            resultado += chr(indice + 97)
        else:
            resultado += letra
    return resultado


def cifra_cesar_decode(texto: str, chave: int) -> str:
    resultado = ""
    for letra in texto:
        if letra.isalpha():
            indice = (ord(letra) - 97 - chave) % 26
            resultado += chr(indice + 97)
        else:
            resultado += letra
    return resultado


class CifraCesarApp:
    def __init__(self, master):
        self.master = master
        master.title("Cifra de César")

        self.label1 = tk.Label(master, text="Digite o texto:")
        self.label1.grid(row=0, column=0)

        self.texto_entry = tk.Entry(master, width=50)
        self.texto_entry.grid(row=0, column=1)

        self.label2 = tk.Label(master, text="Digite a chave (entre 1 e 25):")
        self.label2.grid(row=1, column=0)

        self.chave_entry = tk.Entry(master, width=5)
        self.chave_entry.grid(row=1, column=1)

        self.encode_button = tk.Button(master, text="Codificar", command=self.encode)
        self.encode_button.grid(row=2, column=0)

        self.decode_button = tk.Button(master, text="Decodificar", command=self.decode)
        self.decode_button.grid(row=2, column=1)

    def encode(self):
        texto = self.texto_entry.get()
        chave = self.chave_entry.get()
        try:
            chave = int(chave)
            if chave < 1 or chave > 25:
                raise ValueError
        except ValueError:
            messagebox.showerror("Erro", "A chave deve ser um número inteiro entre 1 e 25.")
            return
        texto_codificado = cifra_cesar_encode(texto, chave)
        messagebox.showinfo("Texto codificado", texto_codificado)

    def decode(self):
        texto = self.texto_entry.get()
        chave = self.chave_entry.get()
        try:
            chave = int(chave)
            if chave < 1 or chave > 25:
                raise ValueError
        except ValueError:
            messagebox.showerror("Erro", "A chave deve ser um número inteiro entre 1 e 25.")
            return
        texto_decodificado = cifra_cesar_decode(texto, chave)
        messagebox.showinfo("Texto decodificado", texto_decodificado)


root = tk.Tk()
app = CifraCesarApp(root)
root.mainloop()






