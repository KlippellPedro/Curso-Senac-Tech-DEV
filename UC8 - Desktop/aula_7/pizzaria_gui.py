import tkinter as tk
from tkinter import messagebox, PhotoImage
import os
from services.menu import Menu
from models.pedido import Pedido
from services.pagamento import Pagamento

class PizzariaGui:
    def __init__(self, master):
        self.master = master
        self.master.title("Fazbear Pizzaria")
        self.master.geometry("800x800")
        self.master.configure(bg="#fdf5e6")

        try:
            pasta_projeto = os.path.dirname(os.path.abspath(__file__))
            caminho_logo = os.path.join(pasta_projeto, "fazbear.png")
            self.logo_img = PhotoImage(file = caminho_logo)
            tk.Label(master, image=self.logo_img, bg="#fdf5e6").pack(pady=10)
        except tk.TclError as erro:
            print("Erro: Não foi possível carregar o arquivo da imagem")
            print(erro)
            print("Caminho procurado:")
            print(caminho_logo)
            tk.Label(master, text="Fazbear Pizzaria", font=("Arial",24,"bold"),bg="#fdf5e6").pack(pady=10)

        self.menu = Menu()  
        self.pedidos = []
        self.total_acumulado = 0.0

        self.codigo = tk.StringVar(value="")
        self.quantidade = tk.StringVar(value="")
        self.opcao_pagamento = tk.IntVar()
        self.frame_menu = tk.Frame(master, bg="#fdf5e6", padx=20, pady=20)
        self.frame_menu.pack()
        tk.Label(self.frame_menu, text=" Menu de Pizzas ",font=("Helvetica", 16, "bold"), bg="#fdf5e6", fg="#8b4513").pack(pady=10)
        menu_texto = "\n".join([f"[{p.codigo}] - {p.nome} - R$ {p.preco:.2f}"for p in self.menu.sabores]) 
        tk.Label(self.frame_menu, text=menu_texto, font=("Courier", 12), justify="left", bg="#fdf5e6").pack()
        self.frame_inputs = tk.Frame(master, bg="#fdf5e6", pady=10)
        self.frame_inputs.pack()
        tk.Label(self.frame_inputs, text="Código", font=("Helvetica", 12, "bold"), bg="#fdf5e6", fg="#102914").pack(side=tk.LEFT, padx=5)
        self.entry_codigo = tk.Entry(self.frame_inputs, textvariable=self.codigo,font=("Helvetica", 12), width=5, relief="solid", bd=1)
        self.entry_codigo.pack(side=tk.LEFT, padx=5)
        tk.Label(self.frame_inputs, text="Quantidade:", font=("Helvetica", 12, "bold"),bg="#fdf5e6", fg="#102914").pack(side=tk.LEFT, padx=5)
        
        self.entry_quantidade = tk.Entry(self.frame_inputs, textvariable=self.quantidade,font=("Helvetica", 12), width=5, relief="solid", bd=1)
        self.entry_quantidade.pack(side=tk.LEFT, padx=5)
        tk.Button(self.frame_inputs, text="Adicionar ao pedido", command=self.adicionar_pedido, font=("Helvetica", 12, "bold"),bg="#d1832c", fg="#fff", relief="raised", bd=3).pack(side=tk.LEFT, padx=10)
        self.label_total = tk.Label(master, text=f"Total acumulado R$ {self.total_acumulado:.2f}", font=("Helvetica", 14, "bold"),bg="#fdf5e6", fg="#4a148c")
        self.label_total.pack(pady=10)

        tk.Button(master, text="Finalizar compra", command=self.abrir_menu_pagamento, font=("Helvetica", 14, "bold"), bg="#4ce05a", fg="white", relief="raised", bd=4).pack(pady=5)
        
    def adicionar_pedido(self):
        try:
            codigo = int(self.codigo.get())
            quantidade = int(self.quantidade.get())
            pizza = self.menu.obter_pizza_por_codigo(codigo)

            if pizza is None:
                messagebox.showerror("Erro", "Opção de picolé inválido!")
                return

            if quantidade <= 0:
                messagebox.showerror("Erro", "Quantidade deve ser maior que zero.")
                return

            pedido = Pedido(pizza, quantidade)
            self.pedidos.append(pedido)
            self.total_acumulado +=(pedido.calcular_subtotal())
            self.label_total.config(
                text=f"Total acumulado R$ {self.total_acumulado:.2f}")
            messagebox.showinfo("Sucesso", 
                                f"{quantidade}x {pizza.nome} adicionado(s) ao pedido!")
            self.codigo.set("")
            self.quantidade.set("")

        except ValueError:
            messagebox.showerror("Entrada inválida", "Por favor, digite números válidos!")

    def abrir_menu_pagamento(self):
        if not self.pedidos:
            messagebox.showwarning("Aviso", "O carrinho está vazio. Adicione produtos.")
            return

        janela_pagamento = tk.Toplevel(self.master)
        janela_pagamento.title("Menu de pagamento")
        janela_pagamento.geometry("500x400")
        janela_pagamento.configure(bg="#fdf5e6")
        tk.Label(janela_pagamento, text="### Menu de pagamento ###", 
                 font=("Helvetica", 16, "bold"), bg="#fdf5e6", fg="#8b4513").pack(
                    pady=10 
                 )         
        opcoes = self.menu.get_opcoes_pagamento()
        self.opcao_pagamento.set(3)
        for valor, texto in opcoes:
            tk.Radiobutton(janela_pagamento, text=texto, variable=self.opcao_pagamento,
                           value=valor, font=("Helvetica", 11), bg="#fdf5e6", 
                           fg="#333", relief="raised", bd=2).pack(
                               anchor="w", padx=30, pady=5)
        tk.Button(janela_pagamento, text="Pagar", command=self.processar_pagamento,
                    font=("Helvetica", 14, "bold"), bg="#4caf50", fg="white", 
                    relief="raised", bd=4).pack(pady=20)

    # Continuamos amanhã
    def processar_pagamento(self):
        try:
            opcao_escolhido = self.opcao_pagamento.get()
            pagamento = Pagamento(self.total_acumulado)
            pagamento.aplicar_pagamento(opcao_escolhido)
            mensagem = ("Compra finalizada com sucesso!\n")
            mensagem += (pagamento.obter_resumo_texto())
            messagebox.showinfo("Compra finalizada", mensagem)

            '''Preparar o sistema para uma nova compra'''
            self.total_acumulado = 0.0
            self.pedidos = []

            self.label_total.config(text=f"Total acumulado R$ {self.total_acumulado:.2f}")

        except ValueError:
            messagebox.showerror("Erro de pagamento", "Opção de pagamento inválida.")    
        

