class Conta: 
    def __init__(self, numero, titulo, saldo, limite):
        print('contruindo objeto...{}'.format(self))
        self.__numero = numero
        self.__titulo = titulo
        self.__saldo = saldo
        self.__limite = limite
        self.__codigo_banco = "001"

    @property
    def get_numero(self):
        return self.__numero
    @property
    def get_titulo(self):
        return self.__titulo
    @property
    def get_saldo(self):
        return self.__saldo
    @property
    def get_limite(self):
        return self.__limite
    @staticmethod
    def codigo_banco():
        return "001"
        
    def set_numero(self , numero):
        self.__numero = numero
    def set_titulo(self , titulo):
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
        valorDoSaque = self.__saldo - valor
        if(valorDoSaque < -1000):
            print("voce chegou ao seu limite")
            self.extrato()
        else:
            self.__saldo -= valor
            self.extrato()
        
    def transfere (self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)

        
