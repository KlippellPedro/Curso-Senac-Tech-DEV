class Carrinho:
    def __init__(self):
        self._itens = []

    @property
    def itens(self):
        return self._itens

    def adicionar(self, produto):
        self._itens.append(produto)

    def remover(self, indice):
        if 0 <= indice < len(self._itens):
            self._itens.pop(indice)

    def limpar(self):
        self._itens.clear()

    def calcular_total(self):
        total = 0
        for item in self._itens:
            total += item.subtotal

        return total

    def quantidade_itens(self):
        return len(self._itens)                        