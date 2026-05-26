from datetime import datetime
import requests
import json
import pandas as pd
from schwab import Schwab, RequestType
from schemas.enums import *

'''
    This class handles all of the market data endpoints
'''
class Market():

    def __init__(self, schwab: Schwab):
        self.schwab = schwab

    def getQuotes(self, 
                symbols: str, 
                fields: str = None,
                indicative: bool = False):

        if fields:
            subsetString = "&fields=" + ",".join(fields)
        else:
            subsetString = ""

        reqUrl = f"https://api.schwabapi.com/marketdata/v1/quotes?symbols={symbols}{subsetString}"

        if indicative:
            reqUrl = reqUrl + "&indicative=true"
        else:
            reqUrl = reqUrl + "&indicative=false"

        res = self.schwab.sendRequest(RequestType.GET, reqUrl)

        return res
    
    def getQuote(self,
                 symbol_id: str,
                 fields: str = None):
        
        if fields:
            subsetString = "?fields=" + ",".join(fields)
        else:
            subsetString = ""

        reqUrl = f"https://api.schwabapi.com/marketdata/v1/{symbol_id}/quotes{subsetString}"

        res = self.schwab.sendRequest(RequestType.GET, reqUrl)

        return res



    """

        if the periodType is
        • day - valid values are 1, 2, 3, 4, 5, 10
        • month - valid values are 1, 2, 3, 6
        • year - valid values are 1, 2, 3, 5, 10, 15, 20
        • ytd - valid values are 1

        If the period is not specified and the periodType is
        • day - default period is 10.
        • month - default period is 1.
        • year - default period is 1.
        • ytd - default period is 1.
    """
    def getPriceHistory(self, 
                        ticker: str, 
                        periodType: PeriodType, # day, month, year, ytd
                        period: int,
                        str, startDate: str = None, endDate: str = None):

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
        

    # def getOptionChain(self,
    #                    symbol: str,
    #                    contractType: ContractType,
    #                    strikeCount: int,
    #                    includeUnderlyingQuote: bool,
    #                    strategy: Strategy,
    #                    interval: float,
    #                    strike: float,
    #                    range: Range,
    #                    fromDate: str,
    #                    toDate: str,
    #                    volatility: float,
    #                    underlyingPrice: float,
    #                    interestRate: float,
    #                    daysToExpiration: int,
    #                    expMonth: str,
    #                    optionType: str,
    #                    entitlement: str)