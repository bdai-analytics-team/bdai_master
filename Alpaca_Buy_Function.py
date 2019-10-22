#!/usr/bin/env python
# coding: utf-8

import alpaca_trade_api as tradeapi

API_KEY = "PKL0QGF1MJDFXNFEPUDI"
API_SECRET = "L0XZ2u3KrWIa2w3iPnRvXpuojn6tLr5jel9GfnCs"
APCA_API_BASE_URL = "https://paper-api.alpaca.markets"

# requires package import alpaca_trade_api as tradeapi
    # must figure out way to put this into function

# required arguments 
    # @symbolCompany
    # @quantity
    # @typeW
    # @API_KEY_buy
    # @API_SECRET_buy
    
# @params
# @symbolCompany = abbreviation of company whose stock is being bought (str)
# @quantity = number of shares to buy (int)
# @side = buy (str)
# @typeW = {market, limit, limit_price, stop} (str)
    # market = purchases at market price 
    # limit = purhcases at specified price
    # if you select limit/limit_price, you must specify a @price (unless you want default value of $100)
# @time_force = {day, gtc, opg, cls, ioc, fok} (str)
    # day = day order. available only when stock market is open. (default)
    # gtc = the order is good until canceled
# @price = price to purchase only used if typeW is limit. default = $100 (ie 20.50 = $20.50) (float/decimal)
# @API_KEY_buy = Alpaca's API key with our acct. Resets when Alpaca webpage is refreshed (str)
# @API_SECRET_buy = Alpaca's secret API key with our acct. Resets when Alpaca webpage is refreshed (str)
# @APCA_API_BASE_URL_buy = default is "https://paper-api.alpaca.markets" (str)
# @api_v = default is 'v2' (str)

# You can buy and sell stocks using the same API multiple times without refreshing the webpage. 
# Alpaca's webpage will update in near real-time to these scripts

# required: symbol of company to purchase stock from, quantity to purchase, type of purchase, time_force, 
def buyStock(symbolCompany, quantity, typeW, API_KEY_buy, API_SECRET_buy, price = 100, time_force = 'day', APCA_API_BASE_URL_buy = "https://paper-api.alpaca.markets", api_v = 'v2', buy = 'buy'): 
    # checks if limit_price argument is needed. 
    api = tradeapi.REST(API_KEY_buy, API_SECRET_buy, APCA_API_BASE_URL_buy, api_version = api_v)
    portfolio = api.list_positions()
    qty_stock = 0
    for position in portfolio:
        if (position.symbol == symbolCompany):
            qty_stock = position.qty
    qty_stock = int(qty_stock)
    equity = float(api.get_account().equity)
    symbol_bars = api.get_barset(symbolCompany, 'minute', 1).df.iloc[0]
    symbol_price = symbol_bars[symbolCompany]['high']
    symbol_price = float(symbol_price)
    if (api.get_asset(symbolCompany).tradable):
        newNumStock = qty_stock + quantity
        if (symbol_price*quantity <= equity):
            if (typeW=='limit' or typeW=='stop_limit'):
                api.submit_order(
                    symbol = symbolCompany,
                    qty = quantity, 
                    side = buy, 
                    type = typeW,
                    time_in_force= time_force, 
                    limit_price = price)
                print("Success! You bought {} shares of {} at the price ${}.".format(quantity, symbolCompany, price))
                print("You now have {} shares of {}.".format(newNumStock, symbolCompany))
            else:
                api.submit_order(
                    symbol = symbolCompany,
                    qty = quantity, 
                    side = buy, 
                    type = typeW,
                    time_in_force= time_force)
                print("Success! You bought {} shares of {} at the market price.".format(quantity, symbolCompany))
                print("You now have {} shares of {}.".format(newNumStock, symbolCompany))
        else:
            print("You do not have the equity to complete this transaction.")
            print("You have ${} in equity and this action costs ${}.".format(equity, symbol_price*quantity))
    else:
        print("{} is not tradeable at this time.".format(symbolCompany))
    return

# buyStock('HAS', 5, 'market', API_KEY, API_SECRET)
