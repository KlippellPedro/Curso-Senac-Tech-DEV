class Pagamento:
    def __init__(self,total:float):
        self.total= float(total)

    def calcular_pagamento(self, opcao:int):
        if opcao == 1:
            return self.total *0.90, "Dinheiro ou Pix - 10% de desconto"
        elif opcao == 2:
            return self.total * 0.95, "Cartão de débito - 5% de desconto"
        elif opcao == 3:
            return self.total, "Cartão de crédito 1x - mesmo valor"
        elif opcao == 4:
            return self.total * 1.05, "Cartão de crédito 2x - 5% de acrescimo"
        elif opcao == 5:
            return self.total * 1.10, "Cartão de crédito 3x - 10% de acrescimo"
        elif opcao == 6:
            return self.total * 1.15, "Cartão de crédito 4x - 15% de acrescimo"
        else:
            raise ValueError("Opção de pagamento inválida.")