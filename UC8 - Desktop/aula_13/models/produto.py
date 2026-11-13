class Produto:
    def __init__(self, id_produto: str ,nome: str, preco_base: float, estoque: int, icone: str):
        self.id_produto = id_produto
        self.nome = nome
        self.preco_base = preco_base
        self.estoque = estoque
        self.icone = icone

    def atualizar_estoque(self, quantidade: int) -> bool:
        """Modifica a quantidade de itens no estoque, aceitando valores positivos (entrada) ou negativos (saída). Retorna True se a operação foi bem-sucedida, False caso contrário."""
        if self.estoque + quantidade < 0:
            return False
        self.estoque += quantidade
        return True
    
    def tem_estoque_disponivel(self, quantidade_desejada: int) -> bool:
        """Verifica se há estoque suficiente para a quantidade desejada."""
        return self.estoque >= quantidade_desejada
    
    def to_dict(self) -> dict:
        """Retorna uma representação do produto como um dicionário para permitir a serialização em formato JSON."""
        return {
            "id_produto": self.id_produto,
            "nome": self.nome,
            "preco_base": self.preco_base,
            "estoque": self.estoque,
            "icone": self.icone
        }
    
    @classmethod
    def from_dict(cls, dados: dict):
        """Método de classe que recontrói um objeto Produto a partir de um dicionário, útil para desserialização de JSON."""
        return cls(
            id_produto=dados["id_produto"],
            nome=dados["nome"],
            preco_base=dados["preco_base"],
            estoque=dados["estoque"],
            icone=dados["icone"]
        )
    