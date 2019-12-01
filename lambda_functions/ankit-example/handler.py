import json

# For any additional packages make sure pipenv shell is enabled then run 
# pipenv install <package-name> for each package
# import alpaca_trade_api as tradeapi

def hello(event, context):
    return {
        "statusCode": 200,
        "body": f"Hello world from {event['name']} lambda function"
    }