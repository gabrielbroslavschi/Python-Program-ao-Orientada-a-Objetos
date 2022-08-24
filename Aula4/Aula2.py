import Conta as ct
def listarConta(conta):
       print('Numero: ', conta.numero,' Titulo: ', conta.titulo,' Saldo: ', conta.saldo,' limite: ', conta.limite )
def depositar(conta, valor):
    conta["saldo"] += valor

def sacar(conta, valor):
    conta["saldo"] -= valor

def extrato(conta):
    print("saldo é ", format(conta["saldo"]), "R$")


conta = ct.Conta(321, "gabriel", 100.0, 1000.0)
conta2 = ct.Conta(100, "teste", 150.0, 1000.0)

conta2.transfere(10.0, conta)


conta.extrato()
conta2.extrato()
