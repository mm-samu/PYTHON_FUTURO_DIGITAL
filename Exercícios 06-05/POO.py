# contas = []
#
# def criar_conta(nome, saldo):
#     contas.append({"nome": nome, "saldo": saldo})
#
# def depositar(nome, valor):
#     for c in contas:
#         if c["nome"] == nome:
#             c["saldo"] += valor
#
# # 🧩 ORIENTADO A OBJETOS
# class Conta:
#     def __init__(self, nome, saldo=0):
#         self.nome = nome
#         self.saldo = saldo
#
#     def depositar(self, valor):
#         self.saldo += valor
#
# conta = Conta("Ana", 100)
# conta.depositar(50)  # ✅ Mais organizado e intuitivo
from operator import length_hint


class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = []

class Estoque:
    def __init__(self, produto):
        self.produto = {}
        self.contador = 0

def adicionar_produto(self,produto):
    self.produto.append(produto)
    self.contador += 1

def total_em_stock(self):
    return len(self.produto)

def soma (self, quantidade, preco):
    return

