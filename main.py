import os
from alpaca_trade_api.rest import REST

# Connect to Alpaca
API_KEY = os.getenv("APCA_API_KEY_ID")
API_SECRET = os.getenv("APCA_API_SECRET_KEY")
BASE_URL = "https://paper-api.alpaca.markets"

api = REST(API_KEY, API_SECRET, BASE_URL)

# Check account status
account = api.get_account()
print(f"Account status: {account.status}")

# Place a market BUY order for 1 share of AAPL
order = api.submit_order(
    symbol="AAPL",
    qty=1,
    side="buy",
    type="market",
    time_in_force="gtc"
)

print("Order submitted successfully:")
print(order)
