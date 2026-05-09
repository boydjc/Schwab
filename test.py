from auth import Auth
from market import Market
from accounts import Accounts
<<<<<<< HEAD
from trade import Trade
=======
>>>>>>> main

class Test():

    def __init__(self):
        self.auth = Auth()
        self.market = Market(self.auth)
        self.accounts = Accounts(self.auth)
<<<<<<< HEAD
        self.trade = Trade()
=======
>>>>>>> main

    # Market Tests

    def getQuote(self):
        print(self.market.getQuote("AAPL"))

    def getHistorical(self):
        print(self.market.getPriceHistory("AAPL"))

    # Account Tests

    def getAccountNumber(self):
        print(self.accounts.getAccountNumber())

    def getAccountInfo(self):
        
        accountNumber = self.accounts.getAccountNumber()

        if 'hashValue' in accountNumber.keys():
            print(self.accounts.getAccountInfo(accountNumber['hashValue']))
        else:
            print("ERROR: No hashValue returned in account number call")


if __name__ == "__main__":

    test = Test()

    #test.getQuote()
    #test.getHistorical()
<<<<<<< HEAD
    #accountNumber = test.getAccountNumber()
    #test.getAccountInfo()
=======
    #test.getAccountNumber()
    test.getAccountInfo()
>>>>>>> main
    