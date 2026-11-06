class Produto:
    def __init__(self, nome, preco, quantidade):
        self._nome = nome
        self._preco = preco
        self._quantidade = quantidade

    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, valor):
        self._nome = valor

    @property
    def preco(self):
        return self._preco
    @preco.setter
    def preco(self, valor):
        self._preco = valor

    @property
    def quantidade(self):
        return self._quantidade
    @quantidade.setter
    def quantidade(self, valor):
        self._quantidade = valor

    @property
    def subtotal(self):
        return self.preco * self.quantidade

    def __str__(self):
        '''Exibe as informações do produto'''
        return (
            f"{self.nome} | "
            f"Qtd: {self.quantidade} | "
            f"Preço R$ {self.preco:.2f}"
        )                
        