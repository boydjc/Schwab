from auth import Auth
from schwab import Schwab
from schemas.dataclasses.account import *

from datetime import datetime, timezone, timedelta

'''
    Handles the accounts and trading endpoints
'''
class Accounts():

    def __init__(self, schwab: Schwab):
        self.schwab = schwab

    def getAccountNumber(self) -> AccountNumberHash:
        # this function assumes there is only one account

        url = "https://api.schwabapi.com/trader/v1/accounts/accountNumbers"

        results = self.schwab.sendGetRequest(url)

        return AccountNumberHash(**results[0])


    def getAccountInfo(self, accountNumberHash) -> Account:

        url = f"https://api.schwabapi.com/trader/v1/accounts/{accountNumberHash}"

        results = self.schwab.sendGetRequest(url)

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


    def getOrders(self, accountNumberHash: str, fromEnteredDateTime: str = None, toEnteredDateTime: str = None, maxResults: str = "3000", status: Status = Status.WORKING):


        if not fromEnteredDateTime:

            fromEnteredDateTime = (datetime.now(timezone.utc) - timedelta(hours=1)).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"

        if not toEnteredDateTime:

            toEnteredDateTime = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"


        url = f"https://api.schwabapi.com/trader/v1/accounts/{accountNumberHash}/orders"

        params = {
            "accountNumber" : accountNumberHash,
            "fromEnteredTime" : fromEnteredDateTime,
            "toEnteredTime" : toEnteredDateTime,
            "maxResults" : maxResults,
            "status" : status
        }

        results = self.schwab.sendGetRequest(url, paramsIn=params)

        if len(results) != 0:
            return Order(**results)

        return None
