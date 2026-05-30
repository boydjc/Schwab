from datetime import datetime
import requests
import json
import pandas as pd
from schemas.dataclasses.market import CandleList, ExpirationChain, OptionChain, QuoteResponse
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
                indicative: bool = False) -> QuoteResponse:

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
                 fields: str = None) -> QuoteResponse:
        
        if fields:
            subsetString = "?fields=" + ",".join(fields)
        else:
            subsetString = ""

        reqUrl = f"https://api.schwabapi.com/marketdata/v1/{symbol_id}/quotes{subsetString}"

        res = self.schwab.sendRequest(RequestType.GET, reqUrl)

        return res
    
    """
    Params:
        symbol: str - ticker symbol

        contractType: ContractType

        strikeCount: int - The number of strikes to return above or below the at-the-money price

        includeUnderlyingQuote: boolean - Underying quotes to be included

        strategy: Strategy - OptionChain strategy. Default is SINGLE. ANALYTICAL allows the use of
            volatility, underlyingPrice, interestRate, and daysToExpiration params to calculate theoretical values
            Avaiable values: SINGLE, ANALYTICAL, CONVERED, VERTICAL, CALENDAR, STRANGLE, STRADDLE, BUTTERFLY,
            CONDOR, DIAGONAL, COLLAR, ROLL

        interval: int - Strike interval for spread strategy chains (see strategy param)

        strike: float - Strike Price

        range: Range - Range(ITM/NTM/OTM etc.)

        fromDate: str - From date(pattern: yyyy-MM-dd)

        toDate: str - To date(pattern: yyyy-MM-dd)

        volatility: float - Volatility to use in calculations. Applies only to ANALYTICAL strategy chains

        underlyingPrice: float - Underlying price to use in calculations. Applies only to ANALYTICAL strategy chains

        interestRate: float - Interest rate to use in calculations. Appliees only to ANALYTICAL strategy chains

        daysToExpirations: int - Days to expiration to use in calculations. Applies only to ANALYTICAL chains

        expMonth: str - Expiration month Avaiable values: JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT
            NOV, DEC, ALL

        optionType: str - Option Type

        entitlement: str - Applicable only if its retail token, entitlement of client 
            PP - PayingPro, NP - NonPro and PN - NonPayingPro
    """
    def getOptionChain(self,
                       symbol: str,
                       contractType: ContractType = ContractType.ALL,
                       strikeCount: int = 4,
                       includeUnderlyingQuote: bool = False,
                       strategy: Strategy = Strategy.SINGLE,
                       interval: float=None,
                       strike: float=None,
                       range: Range=Range.ITM,
                       fromDate: str=None,
                       toDate: str=None,
                       volatility: float=None,
                       underlyingPrice: float=None,
                       interestRate: float=None,
                       daysToExpiration: int=0,
                       expMonth: str=None,
                       optionType: str=None,
                       entitlement: str="NP") -> OptionChain:
        
        reqUrl = f"https://api.schwabapi.com/marketdata/v1/chains?symbol={symbol}&contractType={contractType.value}&strikeCount={strikeCount}&includeUnderlyingQuote={includeUnderlyingQuote}&strategy={strategy.value}&entitlement={entitlement}"

        print(reqUrl)

        if interval:
            reqUrl += f"&interval={interval}"
        
        if strike:
            reqUrl += f"&strike={strike}"
        
        if range:
            reqUrl += f"&range={range}"

        if fromDate:
            reqUrl += f"&fromDate={fromDate}"
        
        if toDate: 
            reqUrl += f"&toDate={toDate}"

        if volatility:
            reqUrl += f"&volatility={volatility}"
        
        if underlyingPrice:
            reqUrl += f"&underlyingPrice={underlyingPrice}"

        if interestRate:
            reqUrl += f"&interestRate={interestRate}"

        if daysToExpiration:
            reqUrl += f"&daysToExpiration={daysToExpiration}"

        if expMonth:
            reqUrl += f"&expMonth={expMonth}"

        if optionType:
            reqUrl += f"&optionType={optionType}"
        
        res = self.schwab.sendRequest(RequestType.GET, reqUrl)

        return res
    
    def getExpirationChain(self, symbol: str) -> ExpirationChain:

        reqUrl = f"https://api.schwabapi.com/marketdata/v1/expirationchain?symbol={symbol}"

        res = self.schwab.sendRequest(RequestType.GET, reqUrl)

        return res
        

    def getPriceHistory(self, 
                        symbol: str, 
                        periodType: PeriodType, # day, month, year, ytd
                        period: int,
                        frequencyType: str,
                        frequency: int,
                        startDate: int = None,
                        endDate: int = None,
                        needExtendedHoursData: bool = False,
                        needPreviousClose: bool = False) -> CandleList:

        # the date passed here to the url has to be in unix milliseconds

        if startDate == None and endDate == None:

            todayDate = int(datetime.now().timestamp()) * 1000

            reqUrl = f"https://api.schwabapi.com/marketdata/v1/pricehistory?symbol={symbol}&periodType={periodType}&period={period}&frequencyType={frequencyType}&frequency={frequency}&endDate={todayDate}&needExtendedHoursData={needExtendedHoursData}&needPreviousClose={needPreviousClose}"

        else:

            reqUrl = f"https://api.schwabapi.com/marketdata/v1/pricehistory?symbol={symbol}&periodType={periodType}&period={period}&frequencyType={frequencyType}&frequency={frequency}&startDate={startDate}&endDate={todayDate}&needExtendedHoursData={needExtendedHoursData}&needPreviousClose={needPreviousClose}"


        res = self.schwab.sendRequest(RequestType.GET, reqUrl)

        return res
        
    '''
    Params:
        symbol_id: MarketIndex - Index Symbol
        sort: MarketIndexSort - Sort by a particular attribute
        frequency: int - To return movers with the specified directions of up or down
    '''
    def getMovers(self,
                  index: MarketIndex,
                  sort: MarketIndexSort,
                  frequency: int = 0):
        
        params={
                "sort": sort.value,
                "frequency": frequency,
            }
        
        res = self.schwab.sendRequest(RequestType.GET,  f"https://api.schwabapi.com/marketdata/v1/movers/{index.value}", {}, params)

        return res