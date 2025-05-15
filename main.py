import os
from alpaca_trade_api.rest import REST

# Use environment variables for security
API_KEY = os.getenv("APCA_API_KEY_ID")
API_SECRET = os.getenv("APCA_API_SECRET_KEY")
BASE_URL = "https://paper-api.alpaca.markets"

api = REST(API_KEY, API_SECRET, BASE_URL)

# Test the connection
account = api.get_account()
print(f"Account status: {account.status}")
