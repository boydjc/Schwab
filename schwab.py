import requests
import json
from auth import Auth
from dataclasses import fields, is_dataclass
from enum import Enum

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

    def sendPostRequest(self, urlIn, headersIn={}, paramsIn={}):

        if self.auth.checkAccessExpire():
            self.auth.createAccessToken()

        headers = headersIn


        # add auth token to headers
        headers["Authorization"] = "Bearer " + self.auth.getAccessToken()

        params=self.toPayload(paramsIn)


        try:

            res = requests.post(urlIn, headers=headers, json=params)

            if res.status_code == 201:

                return "Success"
            
            else:
                print("Failed POST request on endpoint: ", urlIn)
                print(res.text)
                print("Status Code: ", res.status_code)
                print("Headers")
                for header, value in headers.items():
                    print(header + " : " + value)
                print("Parameters")
                for param, value in params.items():
                    print(param + " : " + value)
        except Exception as e:
            print(e)

    def toPayload(self, obj):
        if obj is None:
            return None

        if isinstance(obj, Enum):
            return obj.value

        if is_dataclass(obj):
            result = {}

            for field in fields(obj):
                value = getattr(obj, field.name)

                if value is not None:
                    result[field.name] = self.toPayload(value)

            return result

        if isinstance(obj, list):
            return [self.toPayload(item) for item in obj if item is not None]

        if isinstance(obj, dict):
            return {
                key: self.toPayload(value)
                for key, value in obj.items()
                if value is not None
            }

        return obj

