
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from PIL import Image
from PIL import ImageTk

from models.produto import Produto
from models.carrinho import Carrinho
from models.pagamento import Pagamento
from utils.formatador import moeda


class TelaPrincipal:

    def __init__(self, root):
        self.root = root
        self.root.title("Sorveteria Geladinho")
        self.root.geometry("1200x700")

        # Impede redimensionamento
        self.root.resizable(False, False)
        self.root.configure(bg="#FFF5E4")

        self.carrinho = Carrinho()

        self.sabores = {
            "Chocolate": 4.50,
            "Morango": 4.00,
            "Baunilha": 4.00,
            "Coco": 4.50,
            "Limão": 3.50,
            "Uva": 4.00
        }

        self.criar_interface()

    def criar_interface(self):

        # Cabeçalho
        self.frame_topo = tk.Frame(
            self.root,
            bg="#FF6B6B",
            height=120
        )
        self.frame_topo.pack(fill="x")

        # Logo
        try:
            imagem = Image.open("assets/logotabajara.png")
            imagem = imagem.resize((100, 90))

            self.logo = ImageTk.PhotoImage(imagem)

            self.lbl_logo = tk.Label(
                self.frame_topo,
                image=self.logo,
                bg="#FF6B6B"
            )
            self.lbl_logo.place(x=20, y=15)

        except (FileNotFoundError, OSError):
            pass

        # Título
        self.lbl_titulo = tk.Label(
            self.frame_topo,
            text="Sorveteria Geladinho",
            font=("Arial", 24, "bold"),
            bg="#FF6B6B",
            fg="white"
        )
        self.lbl_titulo.pack(pady=35)

        # Frame principal
        self.frame_principal = tk.Frame(
            self.root,
            bg="#FFF5E4"
        )
        self.frame_principal.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=15
        )

        # ==================================
        # LADO ESQUERDO - ESCOLHA DO PRODUTO
        # ==================================

        self.frame_esquerdo = tk.LabelFrame(
            self.frame_principal,
            text="Escolha seu picolé",
            bg="#FFF5E4",
            font=("Arial", 12, "bold")
        )
        self.frame_esquerdo.grid(
            row=0,
            column=0,
            padx=10,
            sticky="n"
        )

        # Label sabor
        self.lbl_sabor = tk.Label(
            self.frame_esquerdo,
            text="Sabores",
            bg="#FFF5E4",
            font=("Arial", 11, "bold")
        )
        self.lbl_sabor.pack(pady=10)

        # ComboBox sabores
        self.combo_sabor = ttk.Combobox(
            self.frame_esquerdo,
            width=25,
            values=list(self.sabores.keys()),
            state="readonly"
        )
        self.combo_sabor.pack(pady=5)
        self.combo_sabor.current(0)

        # Quantidade
        self.lbl_quantidade = tk.Label(
            self.frame_esquerdo,
            text="Quantidade",
            bg="#FFF5E4",
            font=("Arial", 11)
        )
        self.lbl_quantidade.pack(pady=5)

        self.entry_quantidade = tk.Entry(
            self.frame_esquerdo,
            width=10,
            justify="center"
        )
        self.entry_quantidade.pack(pady=5)

        # Insere quantidade inicial
        self.entry_quantidade.insert(0, "1")

        # Botão adicionar
        self.btn_adicionar = tk.Button(
            self.frame_esquerdo,
            text="Adicionar ao Carrinho",
            bg="#1DD1A1",
            fg="white",
            font=("Arial", 11, "bold"),
            width=22,
            command=self.adicionar_item
        )
        self.btn_adicionar.pack(pady=20)

        # ==================================
        # ÁREA CENTRAL - CARRINHO
        # ==================================

        self.frame_centro = tk.LabelFrame(
            self.frame_principal,
            text="Carrinho",
            bg="#FFF5E4",
            font=("Arial", 12, "bold")
        )
        self.frame_centro.grid(
            row=0,
            column=1,
            padx=10
        )

        # ListBox
        self.lista_carrinho = tk.Listbox(
            self.frame_centro,
            width=60,
            height=20,
            font=("Consolas", 10)
        )
        self.lista_carrinho.pack(
            padx=10,
            pady=10
        )

        # Botões do carrinho
        self.frame_botoes = tk.Frame(
            self.frame_centro,
            bg="#FFF5E4"
        )
        self.frame_botoes.pack(pady=10)

        # Botão remover
        self.btn_remover = tk.Button(
            self.frame_botoes,
            text="Remover Item",
            width=15,
            bg="#FF6B6B",
            fg="white",
            font=("Arial", 10, "bold"),
            command=self.remover_item
        )
        self.btn_remover.pack(
            side="left",
            padx=5
        )

        # Botão limpar
        self.btn_limpar = tk.Button(
            self.frame_botoes,
            text="Limpar Carrinho",
            width=15,
            bg="#FFA502",
            fg="white",
            font=("Arial", 10, "bold"),
            command=self.limpar_carrinho
        )
        self.btn_limpar.pack(
            side="left",
            padx=5
        )

        # ==================================
        # LADO DIREITO - PAGAMENTO
        # ==================================

        self.frame_direito = tk.LabelFrame(
            self.frame_principal,
            text="Pagamento",
            bg="#FFF5E4",
            font=("Arial", 12, "bold")
        )
        self.frame_direito.grid(
            row=0,
            column=2,
            padx=10,
            sticky="n"
        )

        # Label subtotal
        self.lbl_subtotal = tk.Label(
            self.frame_direito,
            text="Subtotal R$ 0,00",
            bg="#FFF5E4",
            font=("Arial", 12, "bold")
        )
        self.lbl_subtotal.pack(pady=10)

        # Forma de pagamento
        self.lbl_pagamento = tk.Label(
            self.frame_direito,
            text="Forma de pagamento",
            bg="#FFF5E4",
            font=("Arial", 11)
        )
        self.lbl_pagamento.pack()

        # Combo pagamento
        self.combo_pagamento = ttk.Combobox(
            self.frame_direito,
            width=20,
            values=list(Pagamento.FORMAS.keys()),
            state="readonly"
        )
        self.combo_pagamento.pack(pady=10)

        # Seleciona a primeira forma de pagamento
        if self.combo_pagamento["values"]:
            self.combo_pagamento.current(0)

        # Atualiza valores ao trocar a forma de pagamento
        self.combo_pagamento.bind(
            "<<ComboboxSelected>>",
            lambda evento: self.atualizar_totais()
        )

        # Label do desconto
        self.lbl_desconto = tk.Label(
            self.frame_direito,
            text="Desconto/Acréscimo R$ 0,00",
            bg="#FFF5E4",
            font=("Arial", 11)
        )
        self.lbl_desconto.pack(pady=10)

        # Label total
        self.lbl_total = tk.Label(
            self.frame_direito,
            text="Total R$ 0,00",
            bg="#FFF5E4",
            fg="#1DD1A1",
            font=("Arial", 16, "bold")
        )
        self.lbl_total.pack(pady=20)

        # Botão finalizar
        self.btn_finalizar = tk.Button(
            self.frame_direito,
            text="Finalizar Compra",
            width=20,
            height=2,
            bg="#1DD1A1",
            fg="white",
            font=("Arial", 11, "bold"),
            command=self.finalizar_compra
        )
        self.btn_finalizar.pack(pady=20)

    # ==================================
    # ADICIONAR ITEM AO CARRINHO
    # ==================================

    def adicionar_item(self):

        try:
            # Obter o sabor selecionado
            sabor = self.combo_sabor.get()

            if not sabor:
                messagebox.showwarning(
                    "Aviso",
                    "Selecione um sabor."
                )
                return

            # Obter a quantidade
            quantidade = int(self.entry_quantidade.get())

            if quantidade <= 0:
                raise ValueError

            # Busca o preço
            preco = self.sabores[sabor]

            # Cria um objeto produto
            produto = Produto(
                sabor,
                preco,
                quantidade
            )

            # Adiciona ao carrinho
            self.carrinho.adicionar(produto)

            # Atualiza a tela
            self.atualizar_lista()

            # Limpa o campo quantidade
            self.entry_quantidade.delete(0, tk.END)
            self.entry_quantidade.insert(0, "1")

        except ValueError:
            messagebox.showerror(
                "Erro",
                "Informe uma quantidade inteira válida e maior que zero."
            )

    # ==================================
    # REMOVER ITEM DO CARRINHO
    # ==================================

    def remover_item(self):

        # Verifica se existe item selecionado
        selecao = self.lista_carrinho.curselection()

        if not selecao:
            messagebox.showwarning(
                "Aviso",
                "Selecione um item."
            )
            return

        indice = selecao[0]

        self.carrinho.remover(indice)

        self.atualizar_lista()

    # ==================================
    # LIMPAR CARRINHO
    # ==================================

    def limpar_carrinho(self):

        self.carrinho.limpar()

        self.atualizar_lista()

    # ==================================
    # ATUALIZAR LISTA
    # ==================================

    def atualizar_lista(self):

        # Limpa o listbox
        self.lista_carrinho.delete(0, tk.END)

        # Percorre os itens
        for item in self.carrinho.itens:

            texto = (
                f"{item.nome} | "
                f"Qtd: {item.quantidade} | "
                f"Unitário: {moeda(item.preco)} | "
                f"Subtotal: {moeda(item.subtotal)}"
            )

            self.lista_carrinho.insert(
                tk.END,
                texto
            )

        self.atualizar_totais()

    # ==================================
    # ATUALIZAR TOTAIS
    # ==================================

    def atualizar_totais(self):

        # Obtém o subtotal do carrinho
        subtotal = self.carrinho.calcular_total()

        # Obtém a forma de pagamento selecionada
        forma = self.combo_pagamento.get()

        # Calcula o total considerando desconto/acréscimo
        total = Pagamento.calcular_total(
            subtotal,
            forma
        )

        diferenca = total - subtotal

        # Atualiza o subtotal na tela
        self.lbl_subtotal.config(
            text=f"Subtotal: {moeda(subtotal)}"
        )

        # Se houver desconto
        if diferenca < 0:

            self.lbl_desconto.config(
                text=(
                    f"Desconto: "
                    f"{moeda(abs(diferenca))}"
                )
            )

        # Se houver acréscimo
        elif diferenca > 0:

            self.lbl_desconto.config(
                text=(
                    f"Acréscimo: "
                    f"{moeda(diferenca)}"
                )
            )

        else:

            self.lbl_desconto.config(
                text="Desconto/Acréscimo: R$ 0,00"
            )

        # Atualiza o total final
        self.lbl_total.config(
            text=f"Total: {moeda(total)}"
        )

    # ==================================
    # FINALIZAR COMPRA
    # ==================================

    def finalizar_compra(self):

        # Verifica se o carrinho está vazio
        if len(self.carrinho.itens) == 0:

            messagebox.showwarning(
                "Carrinho vazio",
                "Adicione produtos antes de finalizar."
            )
            return

        # Obtém o subtotal
        subtotal = self.carrinho.calcular_total()

        # Obtém a forma de pagamento
        forma = self.combo_pagamento.get()

        if not forma:
            messagebox.showwarning(
                "Aviso",
                "Selecione uma forma de pagamento."
            )
            return

        # Obtém o percentual
        percentual = Pagamento.obter_percentual(forma)

        # Obtém o valor final
        total = Pagamento.calcular_total(
            subtotal,
            forma
        )

        # Monta o recibo
        recibo = ""

        recibo += "\n"
        recibo += "=" * 40
        recibo += "\n"
        recibo += "    Sorveteria Geladinho\n"
        recibo += "=" * 40
        recibo += "\n\n"

        recibo += "Itens da compra\n\n"

        # Percorre os itens
        for item in self.carrinho.itens:

            recibo += (
                f"{item.nome}"
                f" | Qtd: {item.quantidade}"
                f" | {moeda(item.subtotal)}\n"
            )

        recibo += "\n"
        recibo += "-" * 40
        recibo += "\n"

        recibo += (
            f"Subtotal: "
            f"{moeda(subtotal)}\n"
        )

        recibo += (
            f"Pagamento: "
            f"{forma}\n"
        )

        # Desconto
        if percentual < 0:

            recibo += (
                f"Desconto: "
                f"{abs(percentual)}%\n"
            )

        # Acréscimo
        elif percentual > 0:

            recibo += (
                f"Acréscimo: "
                f"{percentual}%\n"
            )

        else:

            recibo += "Sem desconto/acréscimo\n"

        recibo += "\n"

        recibo += (
            f"Total: "
            f"{moeda(total)}\n"
        )

        recibo += "\n"
        recibo += "Obrigado pela preferência!\n"
        recibo += "\n"
        recibo += "=" * 40

        # Exibe o recibo
        messagebox.showinfo(
            "Compra finalizada",
            recibo
        )

        # Limpa o sistema
        self.carrinho.limpar()

        self.atualizar_lista()

        self.combo_pagamento.current(0)

        self.entry_quantidade.delete(0, tk.END)
        self.entry_quantidade.insert(0, "1")
