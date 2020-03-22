class CheckingAccount:
    def __init__(self, name, address, accountNo, balance = 0):
        self.name = name
        self.address = address
        self.accountNo = accountNo
        self.balance = float(balance)
        
    def getBalance(self):
        print('\nChecking Account Balance: \n${0:.2f}\n'.format(self.balance))
    
    def getAmount(self, question):
        amount = float(input(question))
        return amount 
    
    def deposit(self):
        amount = self.getAmount('How much would you like to deposit today? ')
        self.balance += amount
        print('\nNew Account Balance: \n${0:.2f}\n'.format(self.balance))
    
    def withdraw(self):
        amount = self.getAmount('How much would you like to withdrawal today? ')
        if amount > self.balance:
            print ('\nYou do not have sufficient funds. Your current balance is ${0:.2f}\n'.format(self.balance))
            self.withdraw()
        else:
            self.balance -= amount
            print('\nNew Account Balance: \n${0:.2f}\n'.format(self.balance))
    
        
myAcc = CheckingAccount ('hannahTaylor', '123 spring st', '121212000', '10')
myAcc.getBalance()
myAcc.deposit ()
myAcc.getBalance()
myAcc.withdraw()
