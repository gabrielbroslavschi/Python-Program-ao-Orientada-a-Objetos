class Conta: 
    def __init__(self, numero, titulo, saldo, limite):
        print('contruindo objeto...{}'.format(self))
        self.__numero = numero
        self.__titulo = titulo
        self.__saldo = saldo
        self.__limite = limite
    
    def get_numero(self):
        return self.__numero
    def get_titulo(self):
        return self.__titulo
    def get_saldo(self):
        return self.__saldo
    def get_limite(self):
        return self.__limite

    def set_numero(self , numero):
        self.__numero = numero
    def set_numero(self , titulo):
       self.__titulo = titulo
    def set_numero(self , saldo):
        self.__saldo = saldo
    def set_numero(self , limite):
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

        
