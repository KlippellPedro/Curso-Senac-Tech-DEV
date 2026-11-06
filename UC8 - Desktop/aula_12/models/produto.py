class Produto:
    def __init__(self, nome:str, preco:float, estoque:int= 10):
        self._nome = nome
        self._preco = float(preco)
        self._estoque = int(estoque)
    
    @property
    # Define uma propriedade chamada nome para permitir o acesar o nome do produto
    def nome(self):
        return self._nome
    @property
    def preco(self):
        return self._preco
    @property
    def estoque(self):
        return self._estoque
    
    def reduzir_estoque(self, quantidade:int):
        if quantidade <= 0:
            raise ValueError("A quantidade deve ser maior que zero.")
        if quantidade > self._estoque:
            raise ValueError("Quantidade solicitada maior que o estoque disponível.")
        self._estoque -= quantidade
    
    def aumentar_estoque(self, quantidade:int):
        if quantidade <= 0:
            raise ValueError("A quantidade deve ser maior que zero.")
        self._estoque += quantidade
    
    def __str__(self):
        # Define o método especial __str__, utilizado para representar o objeto como uma string, útil para exibir informações do produto.
        return f"Produto: {self._nome} - R${self._preco:.2f} - (Estoque: {self._estoque})"