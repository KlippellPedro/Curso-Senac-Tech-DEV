class Estoque:
    @staticmethod
    def possui_estoque(produto, quantidade):
        """Verifica se há estoque suficiente para a quantidade desejada de um produto."""
        return produto["estoque"] >= quantidade        
    
    @staticmethod
    def baixar(produto, quantidade):
        """Reduz a quantidade de um produto no estoque, se houver estoque suficiente."""
        produto["estoque"] -= quantidade

    @staticmethod
    def repor(produto, quantidade):
        """Aumenta a quantidade de um produto no estoque."""
        produto["estoque"] += quantidade