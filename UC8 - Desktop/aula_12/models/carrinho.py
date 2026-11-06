from models.produto import Produto
class Carrinho:
    def __init__(self):
        self.__itens = {}
        """Cria um dicionário privado chamado __itens para armazenar os produtos e suas quantidades no carrinho de compras."""
    
    def adicionar(self,produto:Produto, quantidade:int):
        """Adiciona um produto ao carrinho de compras."""
        if quantidade <= 0:
            raise ValueError("A quantidade deve ser maior que zero.")
        if quantidade > produto.estoque:
            raise ValueError(f"Estoque insuficiente disponível: {produto.estoque}")
        if produto.nome in self.__itens:
            self.__itens[produto]+= quantidade
        else:
            self.__itens[produto]=quantidade
    
    def remover(self,produto:Produto, quantidade:int):
        """Remove um produto do carrinho de compras."""
        if quantidade <= 0:
            raise ValueError("A quantidade deve ser maior que zero.")
        if produto.nome in self.__itens:
            qtd_no_carrinho=self.__itens[produto]
            if quantidade >= qtd_no_carrinho:
                produto.aumentar_estoque(qtd_no_carrinho)
                del self.__itens[produto]
                # Remove o produto do carrinho se a quantidade a ser removida for maior ou igual à quantidade no carrinho.
            else:
                self.__itens[produto]-=quantidade
                produto.aumentar_estoque(quantidade)
    
    def listar_itens(self):
        return self.__itens.items()
    """Retorna uma visão dos pares de chaves e valor do dicionario. Cada par contêm o objeto produto e a quantidade correspondente no carrinho de compras."""

    def calcular_total(self):
        return sum(p.preco * quantidade for p, quantidade in self.__itens.items())
    
    def total_itens(self):
        return sum(qtd for qtd in self.__itens.values())
    
    def vazio(self):
        return len(self.__itens) == 0
    """Retorna True se o carrinho estiver vazio, caso contrário, retorna False."""
    