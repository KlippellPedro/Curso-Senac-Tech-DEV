import tkinter as tk
from tkinter import messagebox, PhotoImage
import os
from services.menu import Menu
from models.pedido import Pedido
from services.pagamento import Pagamento

class Sorveteria:
    def __init__(self,master):
        self.master=master
        self.master.title("Sorveteria TabajaraCorp")
        self.master.geometry("600x400")
        self.master.configure(bg="#fdf5e6")

        try:
            """Obtém o caminho da pasta, onde este arquivo sorveteria_gui.py está localizada. __file__ representa o próprio arquivo Python.
            os.path.abspath(__file__) retorna o caminho absoluto do arquivo atual.
            os.path.dirname() retorna o diretório pai do caminho fornecido, ou seja, a pasta onde o arquivo está localizado."""
            pasta_projeto=os.path.dirname(os.path.abspath(__file__))
            """Mostra o caminho completo até o arquivo da logo. 
            os.path.join() é usado para criar um caminho de arquivo de forma independente do sistema operacional, unindo a pasta do projeto com o nome do arquivo da logo."""
            caminho_logo=os.path.join(pasta_projeto,"logotabajara.png")

            """Carrega a imagem da logo da sorveteria. O caminho completo é utilizado para evitar problemas quando o programa é executado por uma IDE"""
            self.logo_img=PhotoImage(file=caminho_logo)
            tk.Label(master,image=self.logo_img,bg="#fdf5e6").pack(pady=10)
        except tk.TclError as erro:
            """Captura um erro do Tkinter relacionado ao carregamento da iamgem"""
            print("Erro: Não foi possível carregar o arquivo da imagem")
            print(erro)
            """Mostra o caminho que o programa tentou utilizar"""
            print("Caminho procurado:")
            print(caminho_logo)

            """Como a imagem não pode ser carregada, ele cria um Label de texto no lugar do logo. Dessa forma a aplicação continua funcionando, mesmo sem a imagem."""
            tk.Label(master,text="Sorveteria TabajaraCorp",font=("Arial",24,"bold"),bg="#fdf5e6").pack(pady=10)
        
        self.menu.Menu()
        self.pedidos=[]
        self.total_acumulado=0.0
        self.codigo=tk.StringVar(value="")
        self.quantidade=tk.StringVar(value="")
        self.opcao_pagamento=tk.IntVar()
        self.frame_menu=tk.Frame(master,bg="#fdf5e6", padx=20, pady=20)
        self.frame_menu.pack()
        tk.Label(self.frame_menu,text="### MENU DE PICOLÉS ###",font=("Helvetica",16,"bold"),bg="#fdf5e6", fg="#8b4513").pack(pady=10)
        menu_texto="\n".join([f"[{p.codigo}] - {p.nome} - R$ {p.preco:.2f}" for p in self.menu.sabores])
        tk.Label(self.frame_menu,text=menu_texto,font=("Courier",12), justify="left", bg="#fdf5e6").pack()
        self.frame_inputs=tk.Frame(master,bg="#fdf5e6", pady=10)
        self.frame_inputs.pack()
        tk.Label(self.frame_inputs,text="Código:", font=("Helvetica", 12), bg="#fdf5e6").pack(side=tk.LEFT, padx=5)
        self.entry_codigo=tk.Entry(self.frame_inputs,textvariable=self.codigo, font=("Helvetica", 12), width=5, relief="solid", bd=1)
        self.entry_codigo.pack(side=tk.LEFT, padx=5)
        tk.Label(self.frame_inputs,text="Quantidade:", font=("Helvetica", 12), bg="#fdf5e6").pack(side=tk.LEFT, padx=5)
        
        self.entry_quantidade=tk.Entry(self.frame_inputs,textvariable=self.quantidade, font=("Helvetica", 12), width=5, relief="solid", bd=1)
        self.entry_quantidade.pack(side=tk.LEFT, padx=5)
        tk.Button(self.frame_inputs,text="Adicionar ao pedido", command=self.adicionar_pedido, font=("Helvetica", 12), bg="#ffcc88", fg="333", relief="raised", bd=3).pack(side=tk.LEFT, padx=10)
        self.label_total=tk.Label(master,text=f"Total acumulado R$ {self.total_acumulado:.2f}", font=("Helvetica", 14, "bold"), bg="#fdf5e6", fg="#4a148c")
        self.label_total.pack(pady=10)
        tk.Button(master,text="Finalizar compra",command=self.abrir_menu_pagamento,font=("Helvetica", 12), bg="#ff8c00", fg="white", relief="raised", bd=4).pack(pady=10)
    
    def adicionar_pedido(self):
        try:
            codigo=int(self.codigo.get())
            quantidade=int(self.quantidade.get())
            picole=self.menu.obter_picole_por_codigo(codigo)
            if picole is None:
                messagebox.showerror("Erro","Código de picolé inválido!")
                return
            if quantidade<=0:
                messagebox.showerror("Erro", "Quantidade deve ser maior que zero.")
                return
            pedido=Pedido(picole,quantidade)
            self.pedidos.append(pedido)
            self.total_acumulado+=(pedido.calcular_subtotal())
            self.label_total.config(text=f"Total acumulado R$ {self.total_acumulado:.2f}")
            messagebox.showinfo("Sucesso", f"{quantidade}x picolé(s) de {picole.nome} adicionado(s) ao pedido!")
            self.codigo.set("")
            self.quantidade.set("")
        except ValueError:
            messagebox.showerror("Entrada inválida", "Por favor, insira valores válidos para código e quantidade.")
    
    def abrir_menu_pagamento(self):
        if not self.pedidos:
            messagebox.showwarning("Aviso", "O carrinho está vazio. Adicione produtos.")
            return

        janela_pagamento=tk.Toplevel(self.master)
        janela_pagamento.title("Menu de pagamento")
        janela_pagamento.geometry("500x400")
        janela_pagamento.configure(bg="#fdf5e6")
        tk.Label(janela_pagamento,text="=== Opções de pagamento ===",font=("Helvetica",16,"bold"),bg="#fdf5e6", fg="#8b4513").pack(pady=10)
        opcoes=self.menu_get_opcaoes_pagamento()
        self.opcao_pagamento.set()
        for valor, texto in opcoes:
            tk.Radiobutton(janela_pagamento,text=texto,variable=self.opcao_pagamento,value=valor,font=("Helvetica",12),bg="#fdf5e6", fg="#333", relief="raised", bd=2).pack(anchor="w", padx=30, pady=5)
        tk.Button(janela_pagamento,text="Pagar",command=self.processar_pagamento,font=("Helvetica",14,"bold"), bg="#4caf50", fg="white", relief="raised", bd=4).pack(pady=20)

    

          