class CheckingAccount:
    def __init__(self, name, address, accountNo, balance = 0):
        self.name = name
        self.address = address
        self.accountNo = accountNo
        self.__balance = float(balance)
        
    def getBalance(self):
        print('\nChecking Account Balance: \n${0:.2f}\n'.format(self.__balance))
    
    def getAmount(self, question):
        amount = float(input(question))
        return amount 
    
    def deposit(self):
        amount = self.getAmount('How much would you like to deposit today? ')
        self.__balance += amount
        print('\nNew Account Balance: \n${0:.2f}\n'.format(self.__balance))
    
    def withdraw(self):
        amount = self.getAmount('How much would you like to withdrawal today? ')
        if amount > self.__balance:
            print ('\nYou do not have sufficient funds. Your current balance is ${0:.2f}\n'.format(self.__balance))
            self.withdraw()
        else:
            self.__balance -= amount
            print('\nNew Account Balance: \n${0:.2f}\n'.format(self.__balance))
    
        

