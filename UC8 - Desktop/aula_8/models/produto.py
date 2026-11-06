class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self,valor):
        self._nome = valor
    
    @property
    def preco(self):
        return self._preco
    @preco.setter
    def preco(self,valor):
        self._preco = valor

    @property
    def quantidade(self):
        return self._quantidade
    @quantidade.setter
    def quantidade(self,valor):
        self._quantidade = valor
    
    @property
    def subtotal(self):
        return self.preco * self.quantidade
    
    def __str__(self):
        """Exibe as informações do produto em uma string formatada."""
        return f"{self.nome} - R$ {self.preco:.2f} - Quantidade: {self.quantidade} - Subtotal: R$ {self.subtotal:.2f}"