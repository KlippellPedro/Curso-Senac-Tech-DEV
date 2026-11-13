import datetime
class Caixa:
    def __init__(self):
        self.total_dia = 0.0
        self.itens_vendidos = 0

    def registrar_venda(self, total_compra: float, itens_vendidos: int):
        self.total_dia += total_compra
        self.itens_vendidos += itens_vendidos

    def fechamento(self):
        print("### Fechamento do caixa ###")
        print(f"Total arrecadado no dia R$ {self.total_dia:.2f}")
        print(f"Total de itens vendidos: {self.itens_vendidos}")
        agora = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"fechamento_caixa{agora}.txt"

        with open(filename, "w", encoding="utf-8") as f:
            f.write("### Fechamento do caixa ###\n")
            f.write(f"Total arrecadado no dia R$ {self.total_dia:.2f}\n")
            f.write(f"Total de itens vendidos: {self.itens_vendidos}\n")

        print(f"Relatório salvo em: {filename}")            