import datetime
class Caixa:
    def __init__(self):
        self.total_dia=0.0
        self.itens_vendidos=0

    def registrar_venda(self, total_compra:float, itens_vendidos:int):
        self.total_dia += total_compra
        self.itens_vendidos += itens_vendidos
    
    def fechamento(self):
        print("--- Fechamento do Caixa ---")
        print(f"Total do dia: R${self.total_dia:.2f}")
        print(f"Total de itens vendidos: {self.itens_vendidos}")
        agora=datetime.datetime.now().strtime("%Y/%m/%d - %H:%M:%S")
        filename=f"fechamento_caixa_{agora}.txt"

        with open(filename, "w", encoding="utf-8") as f:
            f.write("--- Fechamento do Caixa ---\n")
            f.write(f"Total do dia: R${self.total_dia:.2f}\n")
            f.write(f"Total de itens vendidos: {self.itens_vendidos}\n")

        print(f"Relatório salvo em: {filename}")