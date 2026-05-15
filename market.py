from datetime import datetime
import requests
import json
import pandas as pd
from schwab import Schwab, RequestType

'''
    This class handles all of the market data endpoints
'''
class Market():

    def __init__(self, schwab: Schwab):
        self.schwab = schwab

    def getPriceHistory(self, ticker: str, startDate: str = None, endDate: str = None):

        # the date passed here to the url has to be in unix milliseconds

        if startDate == None and endDate == None:

            todayDate = int(datetime.now().timestamp()) * 1000

            reqUrl = "https://api.schwabapi.com/marketdata/v1/pricehistory?symbol=" + ticker + \
            "&periodType=year&period=20&frequencyType=daily&endDate=" + str(todayDate) + "&needPreviousClose=true"

        else:

            endDate = int(datetime.strptime(endDate, "%Y-%m-%d").timestamp()) * 1000
            startDate = int(datetime.strptime(startDate, "%Y-%m-%d").timestamp()) * 1000

            reqUrl = "https://api.schwabapi.com/marketdata/v1/pricehistory?symbol=" + ticker + \
            "&startDate=" + str(startDate) + "&endDate=" + str(endDate) + "&periodType=year&frequencyType=daily"


        res = self.schwab.sendRequest(RequestType.GET, reqUrl)

        return res

    def getQuote(self, 
                 ticker, 
                 includeQuote=False, 
                 includeFundamental=False,
                 includeExtended=False,
                 includeReference=False,
                 includeRegular=False):

        '''
            Request for subset of data by passing coma separated list of root nodes, 
            possible root nodes are quote, fundamental, extended, reference, regular. Sending quote, 
            fundamental in request will return quote and fundamental data in response. 
            Dont send this attribute for full response.
        '''

        if self.auth.checkAccessExpire():
            self.auth.createAccessToken()

        fields = []

        if includeQuote:
            fields.append("quote")
            
        if includeFundamental:
            fields.append("fundamental")
            
        if includeExtended:
            fields.append("extended")
            
        if includeReference:
            fields.append("reference")
            
        if includeRegular:
            fields.append("regular")

        subsetString = ""
        if fields:
            subsetString = "?fields=" + ",".join(fields)


        reqUrl = f"https://api.schwabapi.com/marketdata/v1/{ticker}/quotes{subsetString}"

        headers = {
            "accept": "application/json",
            "Authorization" : "Bearer " + self.auth.getAccessToken()
        }

        try:
            res = requests.get(reqUrl, headers=headers)

            if res.status_code == 200:

                resJson = json.loads(res.text)

                return resJson
            else:
                print("Status code: ", res.status_code)

        except Exception as e:
            print(e)

        
