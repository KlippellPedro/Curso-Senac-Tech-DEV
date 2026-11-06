from models.pizza import Pizza
class Menu:
    def __init__(self):
        self.sabores = [
            Pizza(1, "Marguerita", 500.00),
            Pizza(2, "Portuguesa", 67.00),
            Pizza(3, "Frango com catupiry", 83.00),
            Pizza(4, "Calabresa", 99.00),
            Pizza(5, "Chocolate", 1024.00)
        ]

    def exibir_menu_pizza(self):
        print("### Fazbear Pizzaria ###")
        print("== Menu de sabores ==")

        for pizza in self.sabores:
            print(f"{pizza.codigo} - {pizza.nome} - R$ {pizza.preco:.2f}")

    def obter_pizza_por_codigo(self, codigo):
        for pizza in self.sabores:
            if pizza.codigo == codigo:
                return pizza
        return None

    def exibir_menu_pagamento(self):
        print("### Menu de opções de pagamento ###")
        print("1 - A vista em dinheiro ou PIX - 13% de desconto") 
        print("2 - Cartão de débito - 8% de desconto") 
        print("3 - Cartão de crédito 1x - mesmo valor") 
        print("4 - Cartão de crédito 2x - 7% de acréscimo")
        print("5 - Cartão de crédito 3x - 9% de acréscimo")
        print("6 - Cartão de crédito 4x - 12% de acréscimo")

    def get_opcoes_pagamento(self):
        return [
            (1, "1 - A vista em dinheiro ou PIX - 13% de desconto"),
            (2, "2 - Cartão de débito - 8% de desconto"),
            (3, "3 - Cartão de crédito 1x - mesmo valor"),
            (4, "4 - Cartão de crédito 2x - 7% de acréscimo"),
            (5, "5 - Cartão de crédito 3x - 9% de acréscimo"),
            (6, "6 - Cartão de crédito 4x - 12% de acréscimo")
        ]                 