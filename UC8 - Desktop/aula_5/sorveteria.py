import tkinter as tk
from tkinter import messagebox, PhotoImage
from menu import Menu
from pedido import Pedido

class Sorveteria:
    def __init__(self, master):
        self.master = master
        self.master.title("Sorveteria TabajaraCorp")
        self.master.geometry("800x600")
        self.master.configure(bg="#ffeadb")
        self.logo_img=PhotoImage(file="logotabajara.png")
        tk.Label(self.master, image=self.logo_img, bg="#ffeadb").pack(pady=10)
        self.menu = Menu()
        self.pedidos = []
        
        self.codigo = tk.StringVar(value="")
        self.quantidade = tk.StringVar(value="")
        self.total_acumulado = tk.DoubleVar(value=0.0)
        
        self.frame_menu = tk.Frame(self.master, bg="#ffeadb", padx=20, pady=20)
        self.frame_menu.pack()
        tk.Label(self.frame_menu, text="=== Menu de opções ===", font=("Helvetica", 16,"bold"), bg="#ffeadb").pack(pady=10)
        
        menu_texto = "\n".join([f"[{p.codigo}] Picolé de {p.nome} R$ {p.preco:.2f}" for p in self.menu.opcoes])
        tk.Label(self.frame_menu, text=menu_texto, font=("Courier", 12), justify="left", bg="#ffeadb", pady=10).pack()
        
        self.frame_imputs = tk.Frame(master, bg="#ffeadb", pady=10)
        self.frame_imputs.pack()
        
        tk.Label(self.frame_imputs, text="Digite o código do picolé:", font=("Helvetica", 12), bg="#ffeadb").pack(side=tk.LEFT, padx=5)
        self.entry_codigo = tk.Entry(self.frame_imputs, textvariable=self.codigo, font=("Helvetica", 12), width=5)
        self.entry_codigo.pack(side=tk.LEFT, padx=5)
        
        tk.Label(self.frame_imputs, text="Digite a quantidade:", font=("Helvetica", 12), bg="#ffeadb").pack(side=tk.LEFT, padx=5)
        self.entry_quantidade = tk.Entry(self.frame_imputs, textvariable=self.quantidade, font=("Helvetica", 12), width=5)
        self.entry_quantidade.pack(side=tk.LEFT, padx=5)
        
        tk.Button(self.frame_imputs, text="Adicionar ao pedido", command=self.adicionar_pedido, font=("Helvetica", 12), bg="#ffeadb").pack(side=tk.LEFT, padx=10)
        
        self.label_total = tk.Label(self.master, text=f"Total acumulado: R$ {self.total_acumulado.get():.2f}", font=("Helvetica", 14,"bold"), bg="#ffeadb")
        self.label_total.pack(pady=10)
        
        tk.Button(master, text="Finalizar pedido", command=self.exibir_resumo_final, font=("Helvetica", 12, "bold"), bg="#ffeadb", fg="black").pack(pady=5)
        
    def adicionar_pedido(self):
        try:
            codigo = int(self.codigo.get())
            quantidade = int(self.quantidade.get())
            picole = self.menu.obter_picole_por_codigo(codigo)
            
            if picole is None:
                messagebox.showerror("Erro", "Código de picolé inválido!")
                return
            if quantidade <= 0:
                messagebox.showerror("Erro", "A quantidade deve ser maior que zero!")
                return
                
            pedido = Pedido(picole, quantidade)
            self.pedidos.append(pedido)

            novo_total = self.total_acumulado.get() + pedido.calcular_subtotal()
            self.total_acumulado.set(novo_total)
            self.label_total.config(text=f"Total acumulado: R$ {self.total_acumulado.get():.2f}")
            messagebox.showinfo("Sucesso", f"Pedido adicionado: {quantidade} picolé(s) de {picole.nome}.")
            
            self.codigo.set("")
            self.quantidade.set("")
        except ValueError:
            messagebox.showerror("Erro", "Digite valores válidos para código e quantidade!")
            
    def calcular_quantidade_total(self):
        return sum(p.quantidade for p in self.pedidos)
        
    def exibir_resumo_final(self):
        total_unidades = self.calcular_quantidade_total()
        total_valor = self.total_acumulado.get()
        mensagem = (f"Resumo do pedido:\nTotal de unidades: {total_unidades}\nValor total: R$ {total_valor:.2f}\nObrigado por comprar na Sorveteria TabajaraCorp!")
        messagebox.showinfo("Resumo final do Pedido", mensagem)
        self.master.destroy()