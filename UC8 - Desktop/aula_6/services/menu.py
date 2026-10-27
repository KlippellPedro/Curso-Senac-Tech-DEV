from models.picole import Picole

class Menu:
    def __init__(self):
        self.sabores = [
            Picole(1, "CPU", 5.00),
            Picole(2, "HD", 10.00),
            Picole(3, "SSD", 15.00),
            Picole(4, "GPU", 20.00),
            Picole(5, "1080p", 25.00)
        ]
    def exibir_menu_picole(self):
        print("=== Bem-vindo a Sorveteria TabajaraCorp ===")
        print("--- Menu de opções ---")
        for picole in self.sabores:
            print(f"{picole.codigo} - Picolé de {picole.nome} - R${picole.preco:.2f}")
    def obter_picole_por_codigo(self, codigo):
        for picole in self.sabores:
            if picole.codigo == codigo:
                return picole
        return None
    def exibir_menu_pagamento(self):
        print("=== Opções de pagamento ===")
        print("1 - A vista em dinheiro ou PIX - 10% de desconto")
        print("2 - A vista no débito - 5% de desconto")
        print("3 - Parcelado no crédito 1x - mesmo valor")
        print("4 - Parcelado no crédito 2x - 5% de acrescimo")
        print("5 - Parcelado no crédito 3x - 10% de acrescimo")
        print("6 - Parcelado no crédito 4x - 15% de acrescimo")
    def get_opcoes_pagamento(self):
        return [
            (1, "A vista em dinheiro ou PIX - 10% de desconto"),
            (2, "A vista no débito - 5% de desconto"),
            (3, "Parcelado no crédito 1x - mesmo valor"),
            (4, "Parcelado no crédito 2x - 5% de acrescimo"),
            (5, "Parcelado no crédito 3x - 10% de acrescimo"),
            (6, "Parcelado no crédito 4x - 15% de acrescimo")
        ]