import tkinter as tk
from tkinter import messagebox

class ConversorDeMoeda:
    def __init__(self, master):
        self.master= master
        self.master.title("Conversor de moeda TabajaraCorp")
        self.master.geometry("500x400")
        self.master.resizable(False,False)
        """Desabilita o dedimensionamento da janela tanto na largura quato na altura, impedindo o usuario de alterar seu tamanho"""
        
        self.reais= tk.StringVar()
        self.cotacao_dolar= tk.StringVar()
        self.cotacao_euro= tk.StringVar()

        self.valor_em_dolar= 0.0
        self.valor_em_euro= 0.0

        tk.Label(master, text="Valor em reais R$:").grid(row=0, column=0, sticky="w", padx=10, pady=10)
        tk.Entry(master, textvariable=self.reais).grid(row=0, column=1, padx=10, pady=10)

        tk.Label(master, text="Valor em Dólar $:").grid(row=1, column=0, sticky="w", padx=10, pady=10)
        tk.Entry(master, textvariable=self.cotacao_dolar).grid(row=1, column=1, padx=10, pady=10)

        tk.Label(master, text="Valor em euro €:").grid(row=2, column=0, sticky="w", padx=10, pady=10)
        tk.Entry(master, textvariable=self.cotacao_euro).grid(row=2, column=1, padx=10, pady=10)

        tk.Button(master, text="Calcular Conversão", command=self.calcular_conversao). grid(row=3, column=0, columnspan=2, pady=15)
        tk.Button(master, text="Exibir resultado", command=self.exibir_resultado). grid(row=4, column=0, columnspan=2, pady=5)

    def calcular_conversao(self):
        try:
            reais_float=float(self.reais.get().replace(",",","))
            dolar_float=float(self.cotacao_dolar.get().replace(",",","))
            euro_float=float(self.cotacao_euro.get().replace(",",","))
            """Converte o valor em reais para dolar e euro. Permite digitar com virgula (ex: 5,60) e converte para ponto"""
            self.valor_em_dolar=reais_float/dolar_float
            self.valor_em_euro=reais_float/euro_float
        except ValueError:
            messagebox.showerror("Erro", "Por favor,insira números válidos! Use virgula ou ponto para decimais")

    def exibir_resultado(self):
        janela_resultado= tk.Toplevel(self.master)
        janela_resultado.title("Resultado da conversão")
        janela_resultado.geometry("400x200")

        tk.Label(janela_resultado, text=f"Valor em reais R$ {self.reais.get()}").grid(row=0, column=0, sticky="w", padx=10, pady=5)
        tk.Label(janela_resultado, text=f"Valor convertido em dolar $ {self.valor_em_dolar:.2f}").grid(row=1, column=0, sticky="w", padx=10, pady=5)
        tk.Label(janela_resultado, text=f"Valor convertido em euro € {self.valor_em_euro:.2f}").grid(row=2, column=0, sticky="w", padx=10, pady=5)

if __name__=="__main__":
    root=tk.Tk()
    app=ConversorDeMoeda(root)
    root.mainloop()