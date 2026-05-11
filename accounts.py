from auth import Auth
from schwab import Schwab
from schemas.dataclasses.account import *

import requests
import json

'''
    Handles the accounts and trading endpoints
'''
class Accounts():

    def __init__(self, schwab: Schwab):
        self.schwab = schwab

    def getAccountNumber(self) -> AccountNumberHash:
        # this function assumes there is only one account

        accountUrl = "https://api.schwabapi.com/trader/v1/accounts/accountNumbers"

        results = self.schwab.sendGetRequest(accountUrl)

        return AccountNumberHash(**results[0])


    def getAccountInfo(self, accountNumberHash) -> Account:

        accountUrl = f"https://api.schwabapi.com/trader/v1/accounts/{accountNumberHash}"

        results = self.schwab.sendGetRequest(accountUrl)

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


    def getOrders(self, accountNumberHash: str, maxResults: int, fromEnteredDateTime: str, toEnteredDateTime: str, status: Status):


        if self.auth.checkAccessExpire():
            self.auth.createAccessToken()

        accountUrl = f"https://api.schwabapi.com/trader/v1/accounts/{accountNumberHash}"

        headers = {
            "Authorization" : "Bearer " + self.auth.getAccessToken()
        }
