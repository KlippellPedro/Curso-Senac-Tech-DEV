class Pedido:
    def __init__(self, picole, quantidade):
        self.picole = picole
        self.quantidade = quantidade

    def calcular_subtotal(self):
        return self.picole.preco * self.quantidade

    def exibir_resumo(self):
        print(f"{self.quantidade}x Picolé de {self.picole.nome} - R$ {self.calcular_subtotal():.2f}")   

    def obter_resumo_texto(self):
        return f"{self.quantidade}x Picolé de {self.picole.nome} - R$ {self.calcular_subtotal():.2f}"    

        