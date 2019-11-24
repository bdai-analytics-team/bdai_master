import json
from news-retriever import rss_processor

# For any additional packages make sure pipenv shell is enabled then run 
# pipenv install <package-name> for each package
#import alpaca_trade_api as tradeapi

def hello(event, context):
    message = rss_processor(**event)

    return {
        "statusCode": 201,
        "body": "hello world YOTE"
    }