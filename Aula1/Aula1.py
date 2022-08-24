def cria_conta(numero, titular, saldo, limite):
    conta= {"numero": numero,"titular":"titular","saldo":saldo, "limite":limite}
    print("conta criada")
    return conta

def depositar(conta, valor):
    conta["saldo"] += valor

def sacar(conta, valor):
    conta["saldo"] -= valor

def extrato(conta):
    print("saldo é ", format(conta["saldo"]), "R$")


contaG = cria_conta(123, "gabriel", 100.0, 1000.0)
depositar(contaG, 100.0)
extrato(contaG)
sacar(contaG, 50.0)
extrato(contaG)

