import requests # type: ignore
import json
from datetime import datetime, timedelta, timezone
import pandas as pd # type: ignore
from typing import Optional
import asyncio
import websockets # type: ignore

class Schwab():

    def __init__(self):

        self.secretsPath = './secrets.json'

        self.loadSecrets()

        self.streamServiceRequestId = 0 # incremented on each stream call
        self.streamServiceQueues = {} # set of queues for storing streaming data to be consumed later
        self.streamStopEvent = asyncio.Event()
        self.streamUrl = "wss://streamer-api.schwab.com/ws"
        self.streamWebSocket = None

        if self.checkAccessExpire() and not self.checkRefreshExpire():
            self.createAccessToken()

    def loadSecrets(self):

        with open(self.secretsPath) as f:

            self.secrets = json.load(f)

            self.accessToken = self.secrets['schwab']['access-token']
            self.accessTokenCreationDate = self.secrets['schwab']['access-token-creation-date']
            self.appKey = self.secrets['schwab']['app-key']
            self.appKeyBase64 = self.secrets['schwab']['app-key-base64']
            self.appKeySecretBase64 = self.secrets['schwab']['app-key-secret-base64']
            self.appSecret = self.secrets['schwab']['app-secret']
            self.appSecretBase64 = self.secrets['schwab']['app-secret-base64']
            self.authCode = self.secrets['schwab']['auth-code']
            self.redirectUrl = self.secrets['schwab']['redirect-url']
            self.refreshToken = self.secrets['schwab']['refresh-token']
            self.refreshTokenCreationDate = self.secrets['schwab']['refresh-token-creation-date']
            self.streamerInfo = self.secrets['schwab']['user-preferences']['streamer-info'][0]

    def saveSecrets(self):

        with open(self.secretsPath, 'w') as file:
            json.dump(self.secrets, file, indent=4)

    def checkAccessExpire(self):

        currentUnixTimestamp = int(datetime.now().timestamp()) * 1000

        accessExpiredDate = self.accessTokenCreationDate + 1800000 # 30 minutes

        if currentUnixTimestamp > accessExpiredDate:
            return True
        
        return False
    
    def checkRefreshExpire(self):

        currentUnixTimestamp = int(datetime.now().timestamp()) * 1000

        # Calculate 7 days in milliseconds (7 days * 24 hours/day * 60 minutes/hour * 60 seconds/minute * 1000 ms/second)
        sevenDaysInMs = 7 * 24 * 60 * 60 * 1000

        refreshExpiredDate = self.refreshTokenCreationDate + sevenDaysInMs

        if currentUnixTimestamp > refreshExpiredDate:
            print("Info: Your schwab refresh token will expire in 1 day.")
            return True
        
        return False
    
    def checkDirtySecrets(self):

        with open(self.secretsPath) as f:

            testConfig = json.load(f)

        if json.dumps(testConfig, sort_keys=True) != json.dumps(self.secrets, sort_keys=True):
            print("Dirty Secrets Detected. Reloading secrets..")
            self.loadSecrets()

    def createAccessToken(self, generateRefreshToken=False):

        # NOTE TO SELF: The auth code that you get to first get a refresh token expires very quickly. 
        # eg. 30 seconds or less 

        tokenUrl = "https://api.schwabapi.com/v1/oauth/token"

        postData = {}

        if generateRefreshToken:
            postData = {
                "grant_type": "authorization_code",
                "code": self.authCode,
                "redirect_uri": self.redirectUrl
            }
        else:
            postData = {
                "grant_type": "refresh_token",
                "refresh_token": self.refreshToken
            }

        headers = {
            "Accept-Encoding": "gzip",
            "Accept-Language": "en-US",
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization" : "Basic " + self.appKeySecretBase64
        }

        res = requests.post(tokenUrl, headers=headers, data=postData)

        if res.status_code == 200:
            dirtySecrets = False
            resJson = json.loads(res.text)

            try:
                if 'refresh_token' in resJson.keys():
                    self.secrets['schwab']['refresh-token'] = resJson['refresh_token']
                    self.secrets['schwab']['refresh-token-creation-date'] = int(datetime.now().timestamp()) * 1000
                    dirtySecrets = True
                
                if 'access_token' in resJson.keys():
                    self.secrets['schwab']['access-token'] = resJson['access_token']
                    self.secrets['schwab']['access-token-creation-date'] = int(datetime.now().timestamp()) * 1000
                    dirtySecrets = True

                if dirtySecrets:
                    self.saveSecrets()
                    self.loadSecrets()

            except Exception as e:
                print("Error when trying to generate tokens")
                print(res.text)
                print(e)

    def getAccountNumber(self):
    # this function assumes there is only one account numbers

        if self.checkAccessExpire():
            self.createAccessToken()

        accountUrl = "https://api.schwabapi.com/trader/v1/accounts/accountNumbers"

        headers = {
            "Authorization" : "Bearer " + self.accessToken
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


        if self.checkAccessExpire():
            self.createAccessToken()

        accountUrl = f"https://api.schwabapi.com/trader/v1/accounts/{accountNumberHash}"

        headers = {
            "Authorization" : "Bearer " + self.accessToken
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

    def getAllOrders(self, accountNumberHash, status=None):

        if self.checkAccessExpire():
            self.createAccessToken()

        fromEnteredTime = (datetime.now(timezone.utc) - timedelta(hours=1)).strftime("%Y-%m-%dT%H:%M:%S.000Z")

        toEnteredTime = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.000Z")

        accountUrl = f"https://api.schwabapi.com/trader/v1/accounts/{accountNumberHash}/orders?accountNumber={accountNumberHash}&fromEnteredTime={fromEnteredTime}&toEnteredTime={toEnteredTime}"
        
        if status:
            accountUrl += f"&status={status}"

        headers = {
            "Authorization" : "Bearer " + self.accessToken
        }
    
        try:
            res = requests.get(accountUrl, headers=headers)

            if res.status_code == 200:

                resJson = json.loads(res.text)

                return resJson
            
            else:
                print(res)
                print("Status code: ", res.status_code)

        except Exception as e:
            print(e)


    def getPriceHistory(self, ticker, startDate=None, endDate=None):

        if self.checkAccessExpire():
            self.createAccessToken()
            
        candleList = []

        # the date passed here to the url has to be in unix milliseconds

        reqUrl = ""

        if startDate == None and endDate == None:

            todayDate = int(datetime.now().timestamp()) * 1000

            reqUrl = "https://api.schwabapi.com/marketdata/v1/pricehistory?symbol=" + ticker + \
            "&periodType=year&period=20&frequencyType=daily&endDate=" + str(todayDate) + "&needPreviousClose=true"

        else:

            endDate = int(datetime.strptime(endDate, "%Y-%m-%d").timestamp()) * 1000
            startDate = int(datetime.strptime(startDate, "%Y-%m-%d").timestamp()) * 1000

            reqUrl = "https://api.schwabapi.com/marketdata/v1/pricehistory?symbol=" + ticker + \
            "&startDate=" + str(startDate) + "&endDate=" + str(endDate) + "&periodType=year&frequencyType=daily"


        headers = {
            "Authorization" : "Bearer " + self.accessToken
        }

        try:
            res = requests.get(reqUrl, headers=headers)

            if res.status_code == 200:

                resJson = json.loads(res.text)

                if 'candles' in resJson.keys():
                    candles = resJson['candles']

                    for candle in candles:
                        formatedCandle = [
                                            datetime.fromtimestamp(candle['datetime']/1000).strftime("%Y-%m-%d"),
                                            round(candle['open'], 2),
                                            round(candle['high'], 2),
                                            round(candle['low'], 2),
                                            round(candle['close'], 2),
                                            candle['volume']
                                        ]
                        
                        candleList.append(formatedCandle)

            
            if not len(candleList) == 0:
                stockDf = pd.DataFrame(candleList, columns=['Date', 'Open', 'High', 'Low', 'Close', 'Volume'])

                return stockDf
            
            # return empty dataframe
            return pd.DataFrame()
        except Exception as e:
            print("Error getting historical data for ticker: ", ticker)
            print(e)

    def getQuote(self, ticker):

        if self.checkAccessExpire():
            self.createAccessToken()

        reqUrl = f"https://api.schwabapi.com/marketdata/v1/{ticker}/quotes"

        headers = {
            "Authorization" : "Bearer " + self.accessToken
        }

        try:
            res = requests.get(reqUrl, headers=headers)

            if res.status_code == 200:

                resJson = json.loads(res.text)

                return resJson

        except Exception as e:
            print(e)

    def cancelOrder(self, accountNumberHash, orderId):

        orderUrl = f"https://api.schwabapi.com/trader/v1/accounts/{accountNumberHash}/orders/{orderId}"

        headers = {
            "Authorization" : "Bearer " + self.accessToken
        }

        try:
            res = requests.delete(orderUrl, headers=headers)

            if res.status_code == 200:
                return True
            else:
                print("Failed to cancel order: ", orderId)
                return False

        except Exception as e:
            print(e)

        return False

    def cancelAllOrders(self, accountNumberHash):

        orders = self.getAllOrders(accountNumberHash, 'PENDING_ACTIVATION')

        orders += self.getAllOrders(accountNumberHash, 'QUEUED')

        orders += self.getAllOrders(accountNumberHash, 'WORKING')

        for order in orders:
            self.cancelOrder(accountNumberHash, order['orderId'])

    def placeEquityOrder(self, accountNumberHash, 
                                symbol,
                                orderType,
                                instruction,
                                orderLegType,
                                quantity,
                                legId,
                                assetType,
                                price: Optional[str] = None,
                                positionEffect = "OPENING",
                                session="NORMAL",
                                duration="DAY",
                                complexOrderStrategyType="NONE",
                                taxLotMethod="FIFO",
                                orderStrategyType="SINGLE"):
        
        orderUrl = f"https://api.schwabapi.com/trader/v1/accounts/{accountNumberHash}/orders"

        postOrderJson = {
            "price": price,
            "session": session,
            "duration": duration,
            "orderType": orderType,
            "complexOrderStrategyType": complexOrderStrategyType,
            "quantity": quantity,
            "taxLotMethod": taxLotMethod,
            "orderLegCollection": [
                {
                    "orderLegType": orderLegType,
                    "legId": legId,
                    "instrument": {
                        "symbol": symbol,
                        "assetType": assetType,
                    },
                    "instruction": instruction,
                    "positionEffect": positionEffect,
                    "quantity": quantity,
                }
            ],
            "orderStrategyType": orderStrategyType,
        }

        headers = {
            "Authorization" : "Bearer " + self.accessToken
        }
    
        try:
            res = requests.post(orderUrl, headers=headers, json=postOrderJson)

            if res.status_code == 201:

                return True

            else:
                print("error placing order")
                print(res.text)
                print("Status code: ", res.status_code)

                return False
        
        except Exception as e:
            print(e)

        return False
    
    async def initializeStreamingQueues(self):
        """Initialize queue inside the correct event loop."""
        # NOTE: each service needs to have its own queue
        self.streamServiceQueues['ADMIN'] = asyncio.Queue()
        self.streamServiceQueues['HEARTBEAT'] = asyncio.Queue()
        self.streamServiceQueues['NASDAQ_BOOK'] = asyncio.Queue()
        self.streamServiceQueues['TIME_AND_SALES'] = asyncio.Queue()

    async def streamReceiver(self):
        """Single WebSocket receiver that distributes messages to the appropriate queues."""

        try:
            while True:
                message = await self.streamWebSocket.recv()  # Only one `recv()` call running
                response = json.loads(message)
                
                # Determine the type of message and add to the appropriate queue
                # as per schwab documentation, there should only be 3 types of responses
                # 1. Response
                # 2. Data
                # 3. Notify (this is basically heartbeat)
                # each response from the stream should only have one of these labels so we 
                # can filter here based on what kind of response it is
                response = response[list(response.keys())[0]][0]

                if "service" in response.keys():
                    if response['service'] == "NASDAQ_BOOK":
                        await self.streamServiceQueues["NASDAQ_BOOK"].put(response)
                    elif response['service'] == "LEVELONE_EQUITIES":  # TIME_AND_SALES
                        await self.streamServiceQueues["TIME_AND_SALES"].put(response)
                    elif response['service'] == "ADMIN":
                        await self.streamServiceQueues["ADMIN"].put(response)
                elif "heartbeat" in response.keys():
                    await self.streamServiceQueues["HEARTBEAT"].put(response)
                else:
                    print(f"Unknown message type: {response}")
                

        except websockets.exceptions.ConnectionClosedError:
            print("WebSocket connection closed unexpectedly.")
        
    
    async def streamLogin(self):
        if self.streamWebSocket:
            print("WebSocket connection already active.")
            return

        headers = {"Authorization": "Bearer " + self.accessToken}

        try:
            self.streamWebSocket = await websockets.connect(self.streamUrl, additional_headers=headers)
            # print("Connected to WebSocket!")

            msgDict = {
                        "service": "ADMIN", # ADMIN, LEVELONE_FOREX, NASDAQ_BOOK, etc..
                        "command": "LOGIN",
                        "requestid": self.streamServiceRequestId,
                        "SchwabClientCustomerId": self.streamerInfo['schwab-client-customer-id'],
                        "SchwabClientCorrelId": self.streamerInfo['schwab-client-correl-id'],
                        "parameters": {
                            "Authorization": self.accessToken,
                            "SchwabClientChannel": "N9",
                            "SchwabClientFunctionId": "APIAPP"
                        }
                    }
        
            self.streamServiceRequestId += 1
            await self.streamWebSocket.send(json.dumps(msgDict))

        except websockets.ConnectionClosed as e:
            print(f"WebSocket connection closed unexpectedly: {e}")
        except Exception as e:
            print(f"Error during WebSocket login: {e}")
        
    
    async def streamLogout(self):

        msgDict = {
                    "service": "ADMIN", # ADMIN, LEVELONE_FOREX, NASDAQ_BOOK, etc..
                    "command": "LOGOUT",
                    "requestid": self.streamServiceRequestId,
                    "SchwabClientCustomerId": self.streamerInfo['schwab-client-customer-id'],
                    "SchwabClientCorrelId": self.streamerInfo['schwab-client-correl-id'],
                    "parameters": {
                        "Authorization": self.accessToken,
                        "SchwabClientChannel": "N9",
                        "SchwabClientFunctionId": "APIAPP"
                    }
                }
        
        try:
            self.streamServiceRequestId += 1
            await self.streamWebSocket.send(json.dumps(msgDict))
            await asyncio.sleep(1)  # Small delay to ensure logout message is sent
            await self.streamWebSocket.close()
            print("WebSocket connection closed.")
        except websockets.ConnectionClosed:
            print("WebSocket was already closed.")
        except Exception as e:
            print(f"Error during WebSocket logout: {e}")
        finally:
            self.streamWebSocket = None  # Reset the WebSocket reference
        
    
    async def streamBookData(self, ticker, book="NASDAQ", timeoutSeconds=5):
    
        if not self.streamWebSocket:
            print("Error: streamWebSocket is not connected")
            return

        msgDict = {
                    "service": book + "_BOOK",
                    "command": "SUBS",
                    "requestid": self.streamServiceRequestId,
                    "SchwabClientCustomerId": self.streamerInfo['schwab-client-customer-id'],
                    "SchwabClientCorrelId": self.streamerInfo['schwab-client-correl-id'],
                    "parameters": {
                        "keys": ticker,
                        "fields": "0,1,2,3"
                    }
                }
    
        self.streamServiceRequestId += 1       

        # Send the subscription request
        await self.streamWebSocket.send(json.dumps(msgDict))
        # print(f"Sent subscription request: {reqMessage}")

    async def streamTimeAndSales(self, ticker, timeoutSeconds=5):
    
        if not self.streamWebSocket:
            print("Error: streamWebSocket is not connected")
            return

        msgDict = {
                    "service": "LEVELONE_EQUITIES",
                    "command": "SUBS",
                    "requestid": self.streamServiceRequestId,
                    "SchwabClientCustomerId": self.streamerInfo['schwab-client-customer-id'],
                    "SchwabClientCorrelId": self.streamerInfo['schwab-client-correl-id'],
                    "parameters": {
                        "keys": ticker,
                        "fields": "3, 9, 35"
                    }
                }
    
        self.streamServiceRequestId += 1        
        # Sending a message

        # Send the subscription request
        await self.streamWebSocket.send(json.dumps(msgDict))
        # print(f"Sent subscription request: {reqMessage}")


if __name__ == '__main__':

    testSchwab = Schwab()

    print("Schwab Api")

    userChoice = ""

    while userChoice != "0":
        if userChoice == "0":
            break

        print("1. Generate Refresh Token")
        print("2. Generate Access Token")
        print("3. Get Historical")
        print("4. Get Quote")
        print("5. Get Account Numbers")
        print("6. Get Account Info")
        print("7. Get All Orders")
        print("8. Place Buy Order")
        print("9. Cancel All Orders")
        print("10. Test Web Socket")
        print("0. Exit")
        userChoice = input(":")
        if userChoice == "1":
            testSchwab.createAccessToken(True)
        elif userChoice == "2":
            testSchwab.createAccessToken()
        elif userChoice == "3":
            print(testSchwab.getPriceHistory("%24NDX"))
        elif userChoice == "4":
            testSchwab.getQuote("AAPL")
        elif userChoice == "5":
            testSchwab.getAccountNumber()
        elif userChoice == "6":
            accountNumber = testSchwab.getAccountNumber()
            testSchwab.getAccountInfo(accountNumber['hashValue'])
        elif userChoice == "7":
            accountNumber = testSchwab.getAccountNumber()
            testSchwab.getAllOrders(accountNumber['hashValue'])
        elif userChoice == "8":

            accountNumber = testSchwab.getAccountNumber()

            symbol = input("Enter ticker: ")

            success = testSchwab.placeEquityOrder(
                                        accountNumber['hashValue'], 
                                        symbol,
                                        orderType="LIMIT",
                                        price=f"4.50",
                                        instruction="BUY",
                                        quantity=f"1",
                                        legId=f"1",
                                        orderLegType="EQUITY",
                                        assetType="EQUITY"
                                        )

            if success:
                print("Order Submitted Successfully")
        elif userChoice == "9":

            accountNumber = testSchwab.getAccountNumber()

            testSchwab.cancelAllOrders(accountNumber['hashValue'])
        elif userChoice == "10":

            asyncio.run(testSchwab.testWebSocket())

        
