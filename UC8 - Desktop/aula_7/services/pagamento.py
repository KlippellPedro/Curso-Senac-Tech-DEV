class Pagamento:
    def __init__(self, total):
        self.total = total
        self.parcelamento = 0.0
        self.descricao = ""

    def aplicar_pagamento(self, opcao):
        if opcao == 1:
            self.total *= 0.87
            self.descricao = "Desconto de 13% - Dinheiro ou PIX"
        elif opcao == 2:
            self.total *= 0.92
            self.descricao = "Desconto de 8% - Cartão de débito"
        elif opcao == 3:
            self.descricao = "Pagamento no cartão de crédito 1x - mesmo valor" 
        elif opcao == 4:
            self.total *= 1.07
            self.parcelamento = self.total / 2
            self.descricao = (f"Acréscimo de 7% - Parcelado em 4x de R$ {self.parcelamento:.2f}") 
        elif opcao == 5:
            self.total *= 1.09
            self.parcelamento = self.total / 3
            self.descricao = (f"Acréscimo de 9% - Parcelado em 4x de R$ {self.parcelamento:.2f}") 
        elif opcao == 6:
            self.total *= 1.12
            self.parcelamento = self.total / 4
            self.descricao = (f"Acréscimo de 12% - Parcelado em 4x de R$ {self.parcelamento:.2f}")  

    def exibir_total(self):
        print(f"Valor total da compra R$ {self.total:.2f}")

    def obter_resumo_texto(self):
        resumo = f"Descrição do pagamento: {self.descricao}\n"
        resumo += f"Valor final: R$ {self.total:.2f}"

        if self.parcelamento > 0:
            resumo += (
                f"\nValor da parcela R$ "
                f"{self.parcelamento:.2f}"
            )                          
        return resumo         
        