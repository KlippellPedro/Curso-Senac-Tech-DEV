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
           bg="FF6B6B",
           height=120 
        )    
        self.frame_topo.pack(fill="x")

        #Logo
        try:
            imagem = Image.open("assets/logotabajara.png")
            imagem = imagem.resize(100, 90)
            self.logo = ImageTk.PhotoImage(imagem)
            self.lbl_logo = tk.Label(
                self.frame_topo,
                image=self.logo,
                bg="#FF6B6B"
            )
            self.lbl_logo.place(x=20, y=15)

        except:
            pass

        # Título
        self.lbl_titulo = tk.Label(
            self.frame_topo,
            text="Sorveteria geladinho",
            font=("Arial", 24, "bold"),
            bg="#FF6B6B",
            fg="white"
        )    
        self.lbl_titulo.pack(pady=35)

        # Frame principal
        self.frame_principal = tk.Frame(self.root, bg="#FFF5E4")
        self.frame_principal.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=15
        )
        # Lado esquerdo
        self.frame_esquerdo = tk.LabelFrame(
            self.frame_principal,
            text="Escolha seu picolé",
            bg="#FFF5E4",
            font=("Arial", 12, "bold")
        )
        self.frame_esquerdo.grid(
            row=0, column=0, padx=10, sticky="n"
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
            values=list(self.sabores.keys())
        )
        self.combo_sabor.pack(pady=5)
        self.combo_sabor.current(0)

        # Quantidade 
        # Continuamos amanhã......
        