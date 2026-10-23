class Pedido:
    def __init__(self, picole,quantidade):
          self.picole = picole
          self.quantidade = quantidade
        
    def calcular_subtotal(self):
        return self.picole.preco * self.quantidade
    
    def exibir_resumo(self):
        subtotal = self.calculartotal()
        print(f"Você comprou {self.quantidade} picolé(s) de {self.picole.nome}.")
        print(f"Valor a pagar: R${subtotal:.2f}")