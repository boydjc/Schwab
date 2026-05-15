from auth import Auth
from schwab import Schwab
from market import Market
from accounts import Accounts
from trade import Trade

from time import sleep

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

    def getUserPreferences(self):
        print(self.accounts.getUserPreferences())

    def getAccountNumber(self):
        print(self.accounts.getAccountNumber())

    def getAccountInfo(self):
        
        accountNumber: AccountNumberHash = self.accounts.getAccountNumber()

        if accountNumber.hashValue:
            print(self.accounts.getAccountInfo(accountNumber.hashValue))
        else:
            print("ERROR: No hashValue returned in account number call")

    def getOrders(self):

        accountNumber: AccountNumberHash = self.accounts.getAccountNumber()

        if accountNumber.hashValue:
            orders: list[Order] = self.accounts.getOrders(accountNumber.hashValue)

            for order in orders:
                print(order.status)

        else:
            print("ERROR: No hashValue returned in account number call")

    def sendOrder(self):

        accountNumber: AccountNumberHash = self.accounts.getAccountNumber()

        if accountNumber.hashValue:
            self.accounts.placeOrder(
                                     Instruction.BUY,
                                     symbol="HUMA",
                                     quantity=1.00,
                                     price=1.00,
                                     stopPrice=0.90,
                                     targetPrice=1.10,
                                     accountNumber=accountNumber.hashValue,
                                     dryRun=False
                                    )
            
    def deleteOrders(self):

        accountNumber: AccountNumberHash = self.accounts.getAccountNumber()

        orders: list[Order] = self.accounts.getOrders(accountNumber.hashValue)

        for order in orders:
            if order.status == Status.WORKING or order.status == Status.PENDING_ACTIVATION:
                self.accounts.deleteOrder(accountNumber.hashValue, order.orderId)

    def replaceOrder(self):

        accountNumber: AccountNumberHash = self.accounts.getAccountNumber()

        print("Placing initial order")
        self.accounts.placeOrder(
                                Instruction.BUY,
                                symbol="HUMA",
                                quantity=1.00,
                                price=1.00,
                                stopPrice=0.90,
                                targetPrice=1.10,
                                accountNumber=accountNumber.hashValue,
                                dryRun=False
                                )
        
        sleep(2)

        orders: list[Order] = self.accounts.getOrders(accountNumber.hashValue)

        for order in orders:
            if order.status == Status.WORKING or order.status == Status.PENDING_ACTIVATION:
                print("Placing replace order")
                self.accounts.placeOrder(
                                Instruction.BUY,
                                symbol="HUMA",
                                quantity=3.00,
                                price=1.25,
                                stopPrice=1.00,
                                targetPrice=1.50,
                                accountNumber=accountNumber.hashValue,
                                replace=True,
                                replaceOrderId=order.orderId,
                                dryRun=False
                                )
                
        # sleep(2)

        # orders: list[Order] = self.accounts.getOrders(accountNumber.hashValue)

        # for order in orders:
        #     if order.status == Status.WORKING:
        #         self.accounts.deleteOrder(accountNumber.hashValue, order.orderId)
        


if __name__ == "__main__":

    test = Test()

    # Account endpoints
    #test.getAccountNumber()
    #test.getAccountInfo()
    #test.sendOrder()
    #test.getOrders()
    test.deleteOrders()
    #test.getUserPreferences()
    #test.replaceOrder()

    