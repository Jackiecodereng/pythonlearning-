# object oriented programming

class Account:
    def __init__(self, full_name, acc_num, balance, phone):
        self.full_name = full_name  # a special function used to setup(constructor)
        self.acc_num = acc_num
        self.balance = balance
        self.phone = phone

    def deposit(self, amount):
        self.balance += amount
        print(f'amount ${amount} deposited succesfully to account ${self.acc_num}')  # f means format the sentence #

    def withdraw(self, amount):
        if self.balance < amount:
            print(f'insufficient funds.balance is ${self.balance}')
        else:
            self.balance -= amount
            print(f'amount {amount} withdrawn succesfully from account {self.acc_num}')

    



    def check_balance(self):
         print(f'balance for account  {self.acc_num} is :{self.balance}')





# create accounts
kevo_acc = Account('kelvin maina', '0010', 12000, '075410000')
sara_acc = Account('sara hassan', '0010', 5000, '0715445522')
willy_account = Account(balance=8000, acc_num='003', full_name='will jones', phone='+987654321')
kevo_acc.deposit(2000)
kevo_acc.check_balance()
kevo_acc.withdraw(500)
kevo_acc.check_balance()
