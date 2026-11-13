from models.produto import Produto

class ItemCarrinho:
    def __init__(self, produto: Produto, quantidade: int):
        self.produto = produto
        self.quantidade = quantidade
    
    @property
    def subtotal(self) -> float:
        """Calcula o subtotal do item no carrinho."""
        return self.produto.preco_base * self.quantidade
    
class Carrinho:
    def __init__(self):
        self.itens= {}
    
    def adicionar_produto(self, produto: Produto, quantidade: int = 1) -> bool:
        quantidade_atual_no_carrinho=0
        if produto.id_produto in self.itens:
            quantidade_atual_no_carrinho = self.itens[produto.id_produto].quantidade
        
        quantidade_total_solicitada = quantidade_atual_no_carrinho + quantidade
        if not produto.tem_estoque_disponivel(quantidade_total_solicitada):
            return False
        
        if produto.id_produto in self.itens:
            self.itens[produto.id_produto].quantidade += quantidade
        
        else:
            self.itens[produto.id_produto] = ItemCarrinho(produto, quantidade)
        
        return True
    
    def remover_ou_decrementar_produto(self, id_produto: str, quantidade: int = 1):
        if id_produto not in self.itens:
            if self.itens[id_produto].quantidade <= quantidade:
                del self.itens[id_produto]
            else:
                self.itens[id_produto].quantidade -= quantidade
    
    def limpar_carrinho(self):
        self.itens.clear()

    @property
    def total_base(self) -> float:
        """Calcula o total base do carrinho, somando os subtotais de todos os itens."""
        return sum(item.subtotal for item in self.itens.values())