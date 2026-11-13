import datetime
from models.produto import Produto
from models.carrinho import Carrinho
from models.pagamento import Pagamento
from models.caixa import Caixa

class Sistema:
    def __init__(self):
        self.produtos = [
            Produto("Arroz 1kg", 5.00),
            Produto("Feijão 1kg", 6.00),
            Produto("Leite 1lt", 4.00),
            Produto("Café 500gm", 25.00)
        ]
        self.caixa = Caixa()

    def exibir_menu_produtos(self):
        print("==== Produtos disponíveis ====")
        for idx, produto in enumerate(self.produtos, start=1):
            print(f"[{idx}] {produto}")
        print("[0] Remover item do carrinho")
        print("[9] Finalizar compra")

    def escolher_produto(self, opcao):
        if 1 <= opcao <= len(self.produtos):
            return self.produtos[opcao - 1]# Retorna o objeto Produto correspondente
        return None            
    
    def processo_compra(self):
        carrinho = Carrinho()
        while True:
            self.exibir_menu_produtos()
            try:
                opcao = int(input("Escolha a opção: "))
            except ValueError:
                print("Digite um número válido")
                continue

            if opcao == 9:
                if carrinho.vazio():
                    print("O carrinho está vazio!")
                    continue
                else:
                    break
            elif opcao == 0:
                self.remover_do_carrinho(carrinho)
                continue
            produto = self.escolher_produto(opcao)
            if produto:
                try:
                    qtd = int(input(f"Quantos '{produto.nome}' deseja adicionar?"))
                    carrinho.adicionar(produto, qtd)
                    print(f"{qtd}x '{produto.nome}' adicionado ao carrinho")
                except ValueError as e:
                    print(e)
            else:
                print("Opção inválida!")

        self.finalizar_compra(carrinho)
    def remover_do_carrinho(self, carrinho: Carrinho):
        if carrinho.vazio():
            print("O carrinho está vazio.")
            return
        print("==== Itens no carrinho ====")
        itens = list(carrinho.listar_itens())
        for idx, (produto, qtd) in enumerate(itens, start=1):
            print(f"[{idx}] {produto.nome} - {qtd} unidade(s)")
        try:
            opcao = int(input("Escolha o item que deseja remover: "))
            if 1 < opcao <= len(itens):
                produto, qtd_no_carrinho = itens[opcao - 1]
                qtd_remover = int(input(f"Quantas unidades deseja remover de '{produto.nome}'?"))
                if qtd_remover > 0:
                    carrinho.remover(produto, qtd_remover)
                    print(f"{qtd_remover}x '{produto.nome}' removido do carrinho.")
                else:
                    print("Quantidade inválida.")
            else:
                print("Opção inválida.")
        except ValueError:
            print("Digite um número válido.")

    def finalizar_compra(self, carrinho: Carrinho):
        total = carrinho.calcular_total()
        print("===== Forma de pagamento =====")
        print("[1] - Dinheiro ou PIX - 10% de desconto")  
        print("[2] - Cartão de débito - 5% de desconto")
        print("[3] - Cartão de crédito 1x - mesmo valor") 
        print("[4] - Cartão de crédito 2x - 5% de acréscimo") 
        print("[5] - Cartão de crédito 3x - 10% de acréscimo")
        print("[6] - Cartão de crédito 4x - 15% de acréscimo")

        while True:
            try:
                opcao = int(input("Escolha a forma de pagamento: "))
                pagamento = Pagamento(total) 
                valor_final, forma = pagamento.calcular_pagamento(opcao)
                break
            except (ValueError, Exception):
                print("Opção inválida, tente novamente.")

        # Continuamos na segunda 
        print("=== Resumo da compra ===")
        # Exibe os iténs do carrinho
        for produto, qtd in carrinho.listar_itens():
            print(f"{qtd}x {produto.nome} - R$ {produto.preco * qtd:.2f}")
        print(f"Forma de pagamento: {forma}")
        print(f"Total a pagar R$ {valor_final:.2f}")

        '''Registra no caixa o valor do dia.
        O caixa registra o valor final e o total de itens vendidos.'''
        self.caixa.registrar_venda(valor_final, carrinho.total_itens)

        # Gera nota fiscal individual
        agora = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"nota_{agora}.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write("====== Nota fiscal ======\n")
            # Escreve cada item do carrinho e o valor no arquivo
            for produto, qtd in carrinho.listar_itens():
                f.write(f"{qtd}x {produto.nome} - R$ {produto.preco * qtd:.2f}\n")
            f.write(f"Forma de pagamento: {forma}\n")
            f.write(f"Total a pagar R$ {valor_final:.2f}\n")
            f.write("=======================\n")
        print(f"Nota fiscal salva em: {filename}")

    def fechamento_dia(self):
        self.caixa.fechamento()                                       



