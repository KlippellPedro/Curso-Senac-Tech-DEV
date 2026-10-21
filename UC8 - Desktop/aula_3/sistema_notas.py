import tkinter as tk
from tkinter import messagebox

class SistemaDeNotas:
    def __init__(self,master):
        self.master=master
        self.master.title("Sistemas de notas TabajaraCorp")
        self.master.geometry("500x400")
        self.master.resizable(False,False)
        self.nome=tk.StringVar()
        self.turma=tk.StringVar()
        self.n1=tk.StringVar()
        self.n2=tk.StringVar()
        self.n3=tk.StringVar()
        self.n4=tk.StringVar()
        self.n5=tk.StringVar()
        self.media=tk.StringVar()

        tk.Label(master, text="Nome:").grid(row=0, column=0, sticky="w", padx=10, pady=10)
        tk.Entry(master, textvariable=self.nome).grid(row=0, column=1, padx=10, pady=10)
        
        tk.Label(master, text="Turma:").grid(row=1, column=0, sticky="w", padx=10, pady=10)
        tk.Entry(master, textvariable=self.turma).grid(row=1, column=1, padx=10, pady=10)

        tk.Label(master, text="Valor da nota 1:").grid(row=2, column=0, sticky="w", padx=10, pady=10)
        tk.Entry(master, textvariable=self.n1).grid(row=2, column=1, padx=10, pady=10)

        tk.Label(master, text="Valor da nota 2:").grid(row=3, column=0, sticky="w", padx=10, pady=10)
        tk.Entry(master, textvariable=self.n2).grid(row=3, column=1, padx=10, pady=10)

        tk.Label(master, text="Valor da nota 3:").grid(row=4, column=0, sticky="w", padx=10, pady=10)
        tk.Entry(master, textvariable=self.n3).grid(row=4, column=1, padx=10, pady=10)

        tk.Label(master, text="Valor da nota 4:").grid(row=5, column=0, sticky="w", padx=10, pady=10)
        tk.Entry(master, textvariable=self.n4).grid(row=5, column=1, padx=10, pady=10)

        tk.Label(master, text="Valor da nota 5:").grid(row=6, column=0, sticky="w", padx=10, pady=10)
        tk.Entry(master, textvariable=self.n5).grid(row=6, column=1, padx=10, pady=10)

        tk.Button(master, text="Calcular média", command=self.calcular_media). grid(row=7, column=0, columnspan=2, pady=15)
        tk.Button(master, text="Exibir média", command=self.exibir_media). grid(row=8, column=0, columnspan=2, pady=5)

    def calcular_media(self):
        try:
            n1_float=int(self.n1.get())
            n2_float=int(self.n2.get())
            n3_float=int(self.n3.get())
            n4_float=int(self.n4.get())
            n5_float=int(self.n5.get())
            self.media=int(n1_float+n2_float+n3_float+n4_float+n5_float)/5
        except ValueError:
            messagebox.showerror("Erro", "Por favor,insira números válidos e inteiros!")

    def exibir_media(self):
        janela_resultado= tk.Toplevel(self.master)
        janela_resultado.title(f"Resultado da média final")
        janela_resultado.geometry("400x200")

        tk.Label(janela_resultado, text=f"Nome do aluno: {self.nome.get()}").grid(row=0, column=0, sticky="w", padx=10, pady=5)
        tk.Label(janela_resultado, text=f"Turma: {self.turma.get()}").grid(row=1, column=0, sticky="w", padx=10, pady=5)
        tk.Label(janela_resultado, text=f"Valor da nota 1: {self.n1.get()}").grid(row=2, column=0, sticky="w", padx=10, pady=5)
        tk.Label(janela_resultado, text=f"Valor da nota 2: {self.n2.get()}").grid(row=3, column=0, sticky="w", padx=10, pady=5)
        tk.Label(janela_resultado, text=f"Valor da nota 3: {self.n3.get()}").grid(row=4, column=0, sticky="w", padx=10, pady=5)
        tk.Label(janela_resultado, text=f"Valor da nota 4: {self.n4.get()}").grid(row=5, column=0, sticky="w", padx=10, pady=5)
        tk.Label(janela_resultado, text=f"Valor da nota 5: {self.n5.get()}").grid(row=6, column=0, sticky="w", padx=10, pady=5)
        tk.Label(janela_resultado, text=f"Valor da média final: {self.media}").grid(row=7, column=0, sticky="w", padx=10, pady=5)

if __name__=="__main__":
    root=tk.Tk()
    app=SistemaDeNotas(root)
    root.mainloop()