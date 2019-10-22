#!/usr/bin/env python
# coding: utf-8

import alpaca_trade_api as tradeapi

API_KEY = "PK3BBYKKGDXAYHIA14BK"
API_SECRET = "G22TxTmJV5x/TQqRY3FkHGLWfCOSG9UvE8dFzGt9"
APCA_API_BASE_URL = "https://paper-api.alpaca.markets"

# company symbols
# quantity
# side = {buy, sell}
# typeW = {market, limit, limit_price, stop}
    # market = purchases at market price
    # limit = purhcases at specified price 
# time_force = {day, gtc, opg, cls, ioc, fok}
    # day = day order. available only when stock market is open
    # gtc = the order is good until canceled
    # opg = 
    # cls = 
    # ioc = 
    # fok = 
# price = price to purchase only used if typeW is limit (ie 20.50 = $20.50)

# required: symbol of company to purchase stock from, quantity to purchase, type of purchase, time_force, 
def sellStock(symbolCompany, quantity, typeW, time_force, price, API_KEY_sell, API_SECRET_sell, APCA_API_BASE_URL_sell, api_v = 'v2', sell = 'sell'): 
    # checks if limit_price argument is needed. 
    api = tradeapi.REST(API_KEY_sell, API_SECRET_sell, APCA_API_BASE_URL_sell, api_version=api_v)
    portfolio = api.list_positions()
    qty_stock = 0
    for position in portfolio:
        if (position.symbol == 'AAPL'):
            qty_stock = position.qty
    qty_stock = int(qty_stock)
    if (quantity <= qty_stock):
        shares_left = qty_stock - quantity
        if (typeW=='limit' or typeW=='stop_limit'):
            api.submit_order(
                symbol = symbolCompany,
                qty = quantity, 
                side = sell, 
                type = typeW,
                time_in_force= time_force, 
                limit_price = price)
            print("Success! You sold {} shares of {} at the price ${}.".format(quantity, symbolCompany, price))
            print("You have {} shares of {} remaining.".format(shares_left, symbolCompany))
        else:
            api.submit_order(
                symbol = symbolCompany,
                qty = quantity, 
                side = sell, 
                type = typeW,
                time_in_force= time_force)
            print("Success! You sold {} shares of {} at the market price.".format(quantity, symbolCompany))
            print("You have {} shares of {} remaining.".format(shares_left, symbolCompany))
    else:
        print("ERROR! You only have {} shares of {}, and you are trying to sell {} shares of {}.".format(qty_stock, symbolCompany, quantity, symbolCompany))
    return
