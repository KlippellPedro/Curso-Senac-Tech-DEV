class Pagamento:
    def __init__(self, total):
        self.total = total
        self.parcelamento = 0.0
        self.descricao = ""

    def aplicar_pagamento(self, opcao):
        if opcao == 1:
            self.total *= 0.90
            self.descricao = "Desconto de 10% - Dinheiro ou PIX"
        elif opcao == 2:
            self.total *= 0.95
            self.descricao = "Desconto de 5% - Cartão de débito"
        elif opcao == 3:
            self.descricao = "Pagamento no cartão de crédito 1x - mesmo valor" 
        elif opcao == 4:
            self.total *= 1.05
            self.parcelamento = self.total / 2
            self.descricao = (
                f"Acréscimo de 5%. "
                f"Parcelado em 2x de R$ {self.parcelamento:.2f}"
            )   
        elif opcao == 5:
            self.total *= 1.10
            self.parcelamento = self.total / 3
            self.descricao = (
                f"Acréscimo de 10%. "
                f"Parcelado em 3x de R$ {self.parcelamento:.2f}"
            )  
        elif opcao == 6:
            self.total *= 1.15
            self.parcelamento = self.total / 4
            self.descricao = (
                f"Acréscimo de 15%. "
                f"Parcelado em 4x de R$ {self.parcelamento:.2f}"
            )  

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
        