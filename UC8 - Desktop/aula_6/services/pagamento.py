class Pagamento:
    def __init__(self,total):
        self.total=total
        self.parcelamento=0.0
        self.descricao=""
    
    def aplicar_pagamento(self,opcao):
        if opcao == 1:
            self.descricao = "Desconto de 10% - Dinheiro ou PIX"
            self.total *= 0.90
        elif opcao == 2:
            self.descricao = "Desconto de 5% - Débito"
            self.total *= 0.95
        elif opcao == 3:
            self.descricao = "Parcelado no crédito 1x - mesmo valor"
        elif opcao == 4:
            self.descricao = f"Parcelado em 2x de R$ {self.parcelamento:.2f}- 5% de acrescimo"
            self.total *= 1.05
            self.parcelamento = self.total / 2
        elif opcao == 5:
            self.descricao = f"Parcelado em 3x de R$ {self.parcelamento:.2f}- 10% de acrescimo"
            self.total *= 1.10
            self.parcelamento = self.total / 3
        elif opcao == 6:
            self.descricao = f"Parcelado em 4x de R$ {self.parcelamento:.2f}- 15% de acrescimo"
            self.total *= 1.15
            self.parcelamento = self.total / 4
        else:
            raise ValueError("Opção de pagamento inválida.")
    
    def exibir_total(self):
        print(f"Valor total da compra R$ {self.total:.2f}")

    def obter_resumo_texto(self):
        resumo= f"Descrição do pagamento: {self.descricao}\n"
        resumo+= f"Valor final: R$ {self.total:.2f}"

        if self.parcelamento > 0:
            resumo+= f"\nValor da parcela: R$ {self.parcelamento:.2f}"
        return resumo