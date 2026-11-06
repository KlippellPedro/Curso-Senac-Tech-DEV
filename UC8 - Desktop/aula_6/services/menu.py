from models.picole import Picole
class Menu:
    def __init__(self):
        self.sabores = [
            Picole(1, "CPU", 5.00),
            Picole(2, "HD", 10.00),
            Picole(3, "SSD", 15.00),
            Picole(4, "GPU", 20.00),
            Picole(5, "1080P", 25.00)
        ]

    def exibir_menu_picole(self):
        print("### Sorveteria TabajaraNerd ###")
        print("== Menu de sabores ==")

        for picole in self.sabores:
            print(f"{picole.codigo} - {picole.nome} - R$ {picole.preco:.2f}")

    def obter_picole_por_codigo(self, codigo):
        for picole in self.sabores:
            if picole.codigo == codigo:
                return picole
        return None

    def exibir_menu_pagamento(self):
        print("### Menu de opções de pagamento ###")
        print("1 - A vista em dinheiro ou PIX - 10% de desconto") 
        print("2 - Cartão de débito - 5% de desconto") 
        print("3 - Cartão de crédito 1x - mesmo valor") 
        print("4 - Cartão de crédito 2x - 5% de acréscimo")
        print("5 - Cartão de crédito 3x - 10% de acréscimo")
        print("6 - Cartão de crédito 4x - 15% de acréscimo")

    def get_opcoes_pagamento(self):
        return [
            (1, "1 - A vista em dinheiro ou PIX - 10% de desconto"),
            (2, "2 - Cartão de débito - 5% de desconto"),
            (3, "3 - Cartão de crédito 1x - mesmo valor"),
            (4, "4 - Cartão de crédito 2x - 5% de acréscimo"),
            (5, "5 - Cartão de crédito 3x - 10% de acréscimo"),
            (6, "6 - Cartão de crédito 4x - 15% de acréscimo")
        ]                 