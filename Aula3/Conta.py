class Conta: 
    def __init__(self, numero, titulo, saldo, limite):
        print('contruindo objeto...{}'.format(self))
        self.numero = numero
        self.titulo = titulo
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print("Saldo {} do titular {}".format(self.saldo, self.titulo))        
    def depositar(self, valor):
        self.saldo += valor
    def sacar(self, valor):
        self.saldo -= valor


