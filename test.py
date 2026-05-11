from auth import Auth
from schwab import Schwab
from market import Market
from accounts import Accounts
from trade import Trade

from schemas.dataclasses.account import *

class Test():

    def __init__(self):
        self.auth = Auth()
        self.schwab = Schwab(self.auth)


        #self.market = Market(self.schwab)
        self.accounts = Accounts(self.schwab)
        #self.trade = Trade(self.schwab)

    # Market Tests

    def getQuote(self):
        print(self.market.getQuote("AAPL"))

    def getHistorical(self):
        print(self.market.getPriceHistory("AAPL"))

    # Account Tests

    def getAccountNumber(self):
        print(self.accounts.getAccountNumber())

    def getAccountInfo(self):
        
        accountNumber: AccountNumberHash = self.accounts.getAccountNumber()

        if accountNumber.hashValue:
            print(self.accounts.getAccountInfo(accountNumber.hashValue))
        else:
            print("ERROR: No hashValue returned in account number call")


if __name__ == "__main__":

    test = Test()

    #test.getQuote()
    #test.getHistorical()
    #test.getAccountNumber()
    test.getAccountInfo()
    