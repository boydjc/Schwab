from auth import Auth
from schwab import Schwab, RequestType
from schemas.dataclasses.account import AccountNumberHash, \
                                        Account, Instrument, \
                                        OrderLegCollection, \
                                        SecuritiesAccount, \
                                        CashAccount, \
                                        MarginAccount, \
                                        OrderRequest, \
                                        AccountsInstrument, \
                                        AccountEquity, \
                                        Order

from schemas.enums.account import Duration, \
                                  Instruction, \
                                  OrderTypeRequest, \
                                  RequestedDestination, \
                                  Session, \
                                  Status, \
                                  OrderLegType, \
                                  AssetType, \
                                  OrderStrategyType, \
                                  StopType

from datetime import datetime, timezone, timedelta
from dataclasses import asdict

'''
    Handles the accounts and trading endpoints
'''
class Accounts():

    def __init__(self, schwab: Schwab):
        self.schwab = schwab

    def getAccountNumber(self) -> AccountNumberHash:
        # this function assumes there is only one account

        url = "https://api.schwabapi.com/trader/v1/accounts/accountNumbers"

        results = self.schwab.sendRequest(RequestType.GET, url)

        return AccountNumberHash(**results[0])


    def getAccountInfo(self, accountNumberHash) -> Account:

        url = f"https://api.schwabapi.com/trader/v1/accounts/{accountNumberHash}"

        results = self.schwab.sendRequest(RequestType.GET, url)

        if "securitiesAccount" in results.keys():

            securitiesData = results["securitiesAccount"]

            if securitiesData["type"] == "CASH":
                securitiesAccount = SecuritiesAccount(
                    cashAccount=CashAccount(**securitiesData)
                )
            else:
                securitiesAccount = SecuritiesAccount(
                    marginAccount=MarginAccount(**securitiesData)
                )
            
            account = Account(
                securitiesAccount = securitiesAccount
            )

            return account
    
        return None
    
    def getUserPreferences(self):

        url = f"https://api.schwabapi.com/trader/v1/userPreference"

        results = self.schwab.sendRequest(RequestType.GET, url)

        return results

    def getOrders(self, accountNumberHash: str, fromEnteredDateTime: str = None, toEnteredDateTime: str = None, maxResults: str = "3000", status: Status = Status.WORKING):


        if not fromEnteredDateTime:

            fromEnteredDateTime = (datetime.now(timezone.utc) - timedelta(hours=1)).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"

        if not toEnteredDateTime:

            toEnteredDateTime = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"

        print("From datetime: ", fromEnteredDateTime)
        print("To datetime: ", toEnteredDateTime)


        url = f"https://api.schwabapi.com/trader/v1/accounts/{accountNumberHash}/orders"

        params = {
            "accountNumber" : accountNumberHash,
            "fromEnteredTime" : fromEnteredDateTime,
            "toEnteredTime" : toEnteredDateTime,
            "maxResults" : maxResults
        }

        results = self.schwab.sendRequest(RequestType.GET, url, paramsIn=params)

        if len(results) != 0:
            return [Order(**order) for order in results]

        return None

    # we'll  assume that we are buying equities and manually build the orderLegCollection and childOrders for target & stoploss
    def placeOrder(self,
        instruction: Instruction,
        symbol: str,
        quantity: float,
        price: float,
        stopPrice: float,
        targetPrice: float,
        accountNumber: str,
        session: Session = Session.NORMAL,
        duration: Duration = Duration.DAY,
        orderType: OrderTypeRequest = OrderTypeRequest.LIMIT,
        dryRun: bool = True # default to not actually sending the order to schwab. True for testing and paper trading strategies
    ):
        

        # building the main order
        orderLegCollection = OrderLegCollection(
            orderLegType=OrderLegType.EQUITY,
            quantity=quantity,
            instruction=Instruction.BUY if instruction == Instruction.BUY else Instruction.SELL,
            instrument=Instrument(
                assetType=AssetType.EQUITY,
                symbol=symbol
            )
        )

        # building the two child orders that are OCO target price sell and stop loss sell

        childOrders = [
            OrderRequest(
                orderStrategyType=OrderStrategyType.OCO,
                childOrderStrategies= [
                    OrderRequest( # target price sell
                        session=session,
                        duration=Duration.GOOD_TILL_CANCEL,
                        orderType=orderType,
                        price=targetPrice,
                        orderStrategyType=OrderStrategyType.SINGLE,
                        orderLegCollection=[
                            OrderLegCollection(
                                orderLegType=OrderLegType.EQUITY,
                                quantity=quantity,
                                instruction=Instruction.SELL if instruction == Instruction.BUY else Instruction.BUY,
                                instrument=Instrument(
                                    assetType=AssetType.EQUITY,
                                    symbol=symbol
                                )
                            )
                        ]
                    ),

                    OrderRequest( # stop loss sell
                        session=session,
                        duration=Duration.GOOD_TILL_CANCEL,
                        orderType=OrderTypeRequest.STOP,
                        stopPrice=stopPrice,
                        stopType=StopType.STANDARD,
                        orderStrategyType=OrderStrategyType.SINGLE,
                        orderLegCollection=[
                            OrderLegCollection(
                                orderLegType=OrderLegType.EQUITY,
                                quantity=quantity,
                                instruction="SELL" if instruction == Instruction.BUY else "BUY",
                                instrument=Instrument(
                                    assetType=AssetType.EQUITY,
                                    symbol=symbol
                                )
                            )
                        ]
                    )
                ]
            )

            
        ]

        order = OrderRequest(
            session=session,
            duration=duration,
            orderType=orderType,
            price=price,
            orderStrategyType=OrderStrategyType.TRIGGER,
            orderLegCollection=[orderLegCollection],
            childOrderStrategies=childOrders
        )

        url = f"https://api.schwabapi.com/trader/v1/accounts/{accountNumber}/orders"

        params = order

        if not dryRun:
            res = self.schwab.sendRequest(RequestType.POST, url, paramsIn=params)
            print(res)
        else:
            print("Dry Run Flag is True")
            print(self.schwab.toPayload(params))


    def deleteOrder(self, accountNumber: str, orderId: str):

        url = f"https://api.schwabapi.com/trader/v1/accounts/{accountNumber}/orders/{orderId}"

        params = {
            "accountNumber" : accountNumber,
            "orderId" : orderId
        }

        res = self.schwab.sendRequest(RequestType.DELETE, url, paramsIn=params)

        print(res)
