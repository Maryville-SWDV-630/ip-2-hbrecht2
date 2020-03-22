from CheckingAccount import *

def main ():
    myAcc = CheckingAccount ('hannahTaylor', '123 spring st', '121212000', '10')
    myAcc.getBalance()
    myAcc.deposit ()
    myAcc.withdraw()
    
main ()