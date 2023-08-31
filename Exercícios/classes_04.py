# Defina uma classe BankAccount com atributos privados balance e account_number.
# Crie métodos deposit e withdraw para manipular o saldo.

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposito(self, valor):
        self.balance += valor
        return self.balance

    def saque(self, valor):
        if valor < self.balance:
            self.balance -= valor
            return self.balance
        else:
            print("Você não tem o valor em saldo")

operation = BankAccount("002", 5000)
print(f"Your account {operation.account_number} have: {operation.balance}")
choice = str(input(f"Olá conta {operation.account_number}! Escolha sua operação, digite S para Saque e D para Depósito: "))
if choice == 'd':
   print(f"Your account {operation.account_number} now it has: {operation.deposito(100)}")
elif choice == 's':
    print(f"Your account {operation.account_number} now it has: {operation.saque(100)}")
else:
    print("Caracter invalido")