import requests
import json
from auth import Auth

'''
    Handles sending web requests and other misc things
'''

class Schwab():

    def __init__(self, auth: Auth):

        self.auth = auth


    def sendGetRequest(self, urlIn, headersIn={}, paramsIn={}):

        if self.auth.checkAccessExpire():
            self.auth.createAccessToken()

        headers = headersIn


        # add auth token to headers
        headers["Authorization"] = "Bearer " + self.auth.getAccessToken()

        try:

            res = requests.get(urlIn, headers=headers, params=paramsIn)

            if res.status_code == 200:

                resJson = json.loads(res.text)

                return resJson
            
            else:
                print("Failed GET request on endpoint: ", urlIn)
                print(res.text)
                print("Status Code: ", res.status_code)
                print("Headers")
                for header, value in headers.items():
                    print(header + " : " + value)
                print("Parameters")
                for param, value in paramsIn.items():
                    print(param + " : " + value)
        except Exception as e:
            print(e)
