class ContaBancaria:
    """
Cria uma conta bancária, e permite fazer saques e depósitos. 
    """
    def __init__(self, id, nome, saldo = 0):
        self.id = id
        self.titular = nome
        self.saldo = saldo
        print(f'Conta n°{self.id} em nome de {self.titular} criada com sucesso. \nSaldo atual de R${self.saldo:.2f}')


    def __str__(self):
        return f"Conta = {self.id}\nNome = {self.titular}\nSaldo = R${self.saldo:.2f}"


    def depositar(self, valor):
        self.saldo += valor
        print(f'Depósito de R${valor:.2f} autorizado com sucesso na conta {self.id}')


    def sacar(self, valor):
        if valor > self.saldo:
            print(f'Saque não autorizado. Valor solicitado maior que o saldo em conta!')
        else:    
            self.saldo -= valor
            print(f'Saque de R${valor:.2f} autorizado com sucesso na conta {self.id}')

c1 = ContaBancaria(112, "Richard Ariel Klann", 3800)
c1.depositar(500)
c1.sacar(5000)
print(c1)