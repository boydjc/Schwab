from auth import Auth
from schemas.dataclasses.account import *

import requests
import json

'''
    Handles the accounts and trading endpoints
'''
class Accounts():

    def __init__(self, auth: Auth):
        self.auth = auth

    def getAccountNumber(self) -> AccountNumberHash:
    # this function assumes there is only one account numbers

        if self.auth.checkAccessExpire():
            self.auth.createAccessToken()

        accountUrl = "https://api.schwabapi.com/trader/v1/accounts/accountNumbers"

        headers = {
            "Authorization" : "Bearer " + self.auth.getAccessToken()
        }

        result: AccountNumberHash = None

        try:
            res = requests.get(accountUrl, headers=headers)

            if res.status_code == 200:

                result = json.loads(res.text)

                return AccountNumberHash(**result[0])
            else:
                print(res)
                print("Status code: ", res.status_code)

        except Exception as e:
            print(e)

    def getAccountInfo(self, accountNumberHash) -> Account:


        if self.auth.checkAccessExpire():
            self.auth.createAccessToken()

        accountUrl = f"https://api.schwabapi.com/trader/v1/accounts/{accountNumberHash}"

        headers = {
            "Authorization" : "Bearer " + self.auth.getAccessToken()
        }

        try:
            res = requests.get(accountUrl, headers=headers)

            if res.status_code == 200:

                resJson = json.loads(res.text)

                if "securitiesAccount" in resJson.keys():

                    securitiesData = resJson["securitiesAccount"]

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
            
            else:
                print(res)
                print("Status code: ", res.status_code)

        except Exception as e:
            print(e)