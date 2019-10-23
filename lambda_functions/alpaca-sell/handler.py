import json
from Alpaca_Sell_Function import sellStock

# For any additional packages make sure pipenv shell is enabled then run 
# pipenv install <package-name> for each package
import alpaca_trade_api as tradeapi

def sell(event, context):
    message = sellStock(**event)

    return {
        "statusCode": 201,
        "body": message
    }