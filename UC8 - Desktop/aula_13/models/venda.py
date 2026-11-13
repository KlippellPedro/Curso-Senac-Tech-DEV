import datetime
class Venda:
    def __init__(self, id_venda: str, id_usuario_caixa: str, nome_caixa: str, itens_simplificados: list, valor_bruto: float, valor_liquido: float, forma_pagamento: str, data_hora: str=None, status: str="Concluída"):
        self.id_venda = id_venda
        self.id_usuario_caixa = id_usuario_caixa
        self.nome_caixa = nome_caixa
        self.itens_simplificados = itens_simplificados
        self.valor_bruto = valor_bruto
        self.valor_liquido = valor_liquido
        self.forma_pagamento = forma_pagamento
        self.data_hora = data_hora if data_hora else datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.status = status
    
    def cancelar_transacao(self) -> bool:
        if self.status == "Cancelada":
            return False
        self.status = "Cancelada"
        return True
    
    def to_dict(self) -> dict:
        return {
            "id_venda": self.id_venda,
            "id_usuario_caixa": self.id_usuario_caixa,
            "nome_caixa": self.nome_caixa,
            "itens_simplificados": self.itens_simplificados,
            "valor_bruto": self.valor_bruto,
            "valor_liquido": self.valor_liquido,
            "forma_pagamento": self.forma_pagamento,
            "data_hora": self.data_hora,
            "status": self.status
        }
    
    @classmethod
    def from_dict(cls, dados: dict):
        return cls(
            id_venda=dados["id_venda"],
            id_usuario_caixa=dados["id_usuario_caixa"],
            nome_caixa=dados["nome_caixa"],
            itens_simplificados=dados["itens_simplificados"],
            valor_bruto=dados["valor_bruto"],
            valor_liquido=dados["valor_liquido"],
            forma_pagamento=dados["forma_pagamento"],
            data_hora=dados["data_hora"],
            status=dados["status"]
        )
    