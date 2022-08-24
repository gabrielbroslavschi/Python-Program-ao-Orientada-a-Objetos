class Conta: 
    def __init__(self, numero, titulo, saldo, limite):
        print('contruindo objeto...{}'.format(self))
        self.__numero = numero
        self.__titulo = titulo
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo {} do titular {}".format(self.__saldo, self.__titulo))
        
    def depositar(self, valor):
        self.__saldo += valor
        
    def sacar(self, valor):
        self.__saldo -= valor

    def transfere (self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)

        
