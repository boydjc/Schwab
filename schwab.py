import requests
import json
from auth import Auth

'''
    Handles sending web requests and other misc things
'''

class Schwab():

    def __init__(self, auth: Auth):

        self.auth = auth


    def sendGetRequest(self, urlIn, headersIn={}):

        if self.auth.checkAccessExpire():
            self.auth.createAccessToken()

        headers = headersIn


        # add auth token to headers
        headers["Authorization"] = "Bearer " + self.auth.getAccessToken()

        try:

            res = requests.get(urlIn, headers=headers)

            if res.status_code == 200:

                resJson = json.loads(res.text)

                return resJson
            
            else:
                print("Failed GET request on endpoint: ", urlIn)
                print(res)
                print("Status Code: ", res.status_code)

        except Exception as e:
            print(e)
