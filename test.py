from auth import Auth
from market import Market

if __name__ == "__main__":

    auth = Auth()
    market = Market(auth)

    print("Hello from test")

    print(market.getQuote("AAPL", True))