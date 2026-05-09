from auth import Auth
from .dataclasses.accountDataClasses import AccountNumberHash

import requests
import json

'''
    Handles the accounts and trading endpoints
'''
class Accounts():

    def __init__(self, auth: Auth):
        self.auth = auth

    def getAccountNumber(self):
    # this function assumes there is only one account numbers

        if self.auth.checkAccessExpire():
            self.auth.createAccessToken()

        accountUrl = "https://api.schwabapi.com/trader/v1/accounts/accountNumbers"

        headers = {
            "Authorization" : "Bearer " + self.auth.getAccessToken()
        }

        try:
            res = requests.get(accountUrl, headers=headers)

            if res.status_code == 200:

                resJson = json.loads(res.text)

                return resJson[0]
            else:
                print(res)
                print("Status code: ", res.status_code)

        except Exception as e:
            print(e)

    def getAccountInfo(self, accountNumberHash):


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

                print(resJson)

                return resJson
            else:
                print(res)
                print("Status code: ", res.status_code)

        except Exception as e:
            print(e)