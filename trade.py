class Trade():

    def __init__(self, auth: Auth):
        pass

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