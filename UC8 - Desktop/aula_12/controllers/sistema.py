import datetime
from models.produto import Produto
from models.carrinho import Carrinho
from models.pagamento import Pagamento
from models.caixa import Caixa

class Sistema:
    def __init__(self):
        self.produtos = [
            Produto("Arroz 1Kg", 5.00),
            Produto("Feijão 1Kg", 6.00),
            Produto("Leite 1L", 4.00),
            Produto("Café 500g", 25.00),
        ]
        self.caixa=Caixa()
    
    def exibir_produtos(self):
        print("--- Produtos Disponíveis ---")
        for idx, produto in enumerate(self.produtos, start=1):
            print(f"{idx}. {produto}")
        print("[0] Remover item do carrinho")
        print("[9] Finalizar compra")
    
    def escolher_produto(self, opcao):
        if opcao < 1 or opcao > len(self.produtos):
            return self.produtos[opcao - 1] # Retorna o produto selecionado com base na opção escolhida pelo usuário.
        return None
    
    def processo_compra(self):
        carrinho=Carrinho()
        while True:
            self.exibir_produtos()
            try:
                opcao = int(input("Escolha a opção: "))
            except ValueError:
                print("Opção inválida. Digite um número.")
                continue
            if opcao == 9:
                if carrinho.vazio():
                    print("Carrinho vazio. Adicione produtos antes de finalizar.")
                    continue
                else:
                    break
            elif opcao == 0:
                if carrinho.vazio():
                    print("Carrinho vazio. Não há itens para remover.")
                    continue
                else:
                    self.remover_item_carrinho(carrinho)
                    continue
            produto = self.escolher_produto(opcao)
            if produto:
                try:
                    qtd=int(input(f"Digite a quantidade de {produto.nome} que deseja adicionar ao carrinho: "))
                    carrinho.adicionar(produto, qtd)
                    print(f"{qtd} unidade(s) de {produto.nome} adicionada(s) ao carrinho.")
                except ValueError as e:
                    print(e)
            else:
                print("Opção inválida. Tente novamente.")
        self.finalizar_compra(carrinho)
    
    def remover_do_carrinho(self, carrinho:Carrinho):
        if carrinho.vazio():
            print("Carrinho vazio. Não há itens para remover.")
            return
        print("--- Itens no Carrinho ---")
        itens=list(carrinho.listar_itens())
        for idx, (produto,qtd) in enumerate(itens, start=1):
            print(f"[{idx}] {produto.nome} - {qtd} unidade(s)")
        try:
            opcao=int(input("Escolha o item que deseja remover: "))
            if 1 < opcao <= len(itens):
                produto,qtd_no_carrinho=itens[opcao-1]
                qtd_remover=int(input(f"Digite a quantidade de {produto.nome} que deseja remover: "))
                if qtd_remover>0:
                    carrinho.remover(produto, qtd_remover)
                    print(f"{qtd_remover}x de {produto.nome} removido(s) do carrinho.")
                else:
                    print("Quantidade inválida. A quantidade deve ser maior que zero.")
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Opção inválida. Digite um número.")
    
    def finalizar_compra(self, carrinho:Carrinho):
        total=carrinho.calcular_total()
        print(f"Total da compra: R${total:.2f}")
        print("--- Opções de Pagamento ---")
        print("[1] Dinheiro ou Pix - 10% de desconto")
        print("[2] Cartão de débito - 5% de desconto")
        print("[3] Cartão de crédito 1x - mesmo valor")
        print("[4] Cartão de crédito 2x - 5% de acréscimo")
        print("[5] Cartão de crédito 3x - 10% de acréscimo")
        print("[6] Cartão de crédito 4x - 15% de acréscimo")
        while True:
            try:
                opcao=int(input("Escolha a opção de pagamento: "))
                pagamento=Pagamento(total)
                valor_final, forma= pagamento.calcular_pagamento(opcao)
                break
            except (ValueError, Exception):
                print("Opção inválida. Tente novamente.")