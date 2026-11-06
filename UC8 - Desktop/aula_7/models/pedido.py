class Pedido:
    def __init__(self, pizza, quantidade):
        self.pizza = pizza
        self.quantidade = quantidade

    def calcular_subtotal(self):
        return self.pizza.preco * self.quantidade

    def exibir_resumo(self):
        print(f"{self.quantidade}x Pizzas de {self.pizza.nome} - R$ {self.calcular_subtotal():.2f}")   

    def obter_resumo_texto(self):
        return f"{self.quantidade}x Pizzas de {self.pizza.nome} - R$ {self.calcular_subtotal():.2f}"    

        