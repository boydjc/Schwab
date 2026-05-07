'''
    Class for handling active streams of data through the streaming service
'''
class Stream():

    def __init__(self, auth: Auth):
        
        self.streamServiceRequestId = 0 # incremented on each stream call
        self.streamServiceQueues = {} # set of queues for storing streaming data to be consumed later
        self.streamStopEvent = asyncio.Event()
        self.streamUrl = "wss://streamer-api.schwab.com/ws"
        self.streamWebSocket = None

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