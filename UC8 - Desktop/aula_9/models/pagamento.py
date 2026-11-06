class Pagamento:
    FORMAS = {
        "Dinheiro": -10,
        "PIX": -10,
        "Débito": -5,
        "Crédito 1x": 0,
        "Crédito 2x": 5,
        "Crédito 3x": 10
    }

    @classmethod
    def calcular_total(cls, subtotal, forma_pagamento):
        percentual = cls.FORMAS[forma_pagamento]
        valor_final = subtotal + (subtotal * percentual / 100)
        return valor_final
    
    @classmethod
    def obter_percentual(cls, forma_pagamento):
        return cls.FORMAS[forma_pagamento]