#!/usr/bin/env python
# coding: utf-8

import alpaca_trade_api as tradeapi

### MUST BE REGENERATED
API_KEY = "PKL0QGF1MJDFXNFEPUDI"
API_SECRET = "L0XZ2u3KrWIa2w3iPnRvXpuojn6tLr5jel9GfnCs"
APCA_API_BASE_URL = "https://paper-api.alpaca.markets"

# requires package import alpaca_trade_api as tradeapi
    # must figure out way to put this into function

# required arguments 
    # @symbolCompany
    # @quantity
    # @typeW
    # @API_KEY_sell
    # @API_SECRET_sell
    
# @params
# @symbolCompany = abbreviation of company whose stock is being sold (str)
# @quantity = number of shares to sell (int)
# @side = sell (str)
# @typeW = {market, limit, limit_price, stop} (str)
    # market = sells at market price 
    # limit = sells at specified price
    # if you select limit/limit_price, you should specify a @price (unless you want default value of $100)
# @time_force = {day, gtc, opg, cls, ioc, fok} (str)
    # day = day order. available only when stock market is open. (default)
    # gtc = the order is good until canceled
# @price = price to sell at. should be used if typeW is limit/limit price. default = $100 (ie 20.50 = $20.50) (int/float/decimal)
# @API_KEY_sell = Alpaca's API key with our acct. Resets when Alpaca webpage is refreshed (str)
# @API_SECRET_sell = Alpaca's secret API key with our acct. Resets when Alpaca webpage is refreshed (str)
# @APCA_API_BASE_URL_sell = default is "https://paper-api.alpaca.markets" (str)
# @api_v = default is 'v2' (str)

# You can buy and sell stocks using the same API multiple times without refreshing the webpage. 
# Alpaca's webpage will update in near real-time to these scripts

# required: symbol of company to purchase stock from, quantity to purchase, type of purchase, time_force, 
def sellStock(symbolCompany, quantity, typeW, API_KEY_sell, API_SECRET_sell, price = 100, time_force = 'day', APCA_API_BASE_URL_sell = "https://paper-api.alpaca.markets", api_v = 'v2', sell = 'sell'): 
    api = tradeapi.REST(API_KEY_sell, API_SECRET_sell, APCA_API_BASE_URL_sell, api_version=api_v)
    portfolio = api.list_positions()
    qty_stock = 0
    for position in portfolio:
        if (position.symbol == symbolCompany):
            qty_stock = position.qty
    qty_stock = int(qty_stock)
    if (api.get_asset(symbolCompany).tradable):
        if (quantity <= qty_stock):
            shares_left = qty_stock - quantity
            if (typeW == 'limit' or typeW == 'stop_limit'):
                api.submit_order(
                    symbol = symbolCompany,
                    qty = quantity, 
                    side = sell, 
                    type = typeW,
                    time_in_force = time_force, 
                    limit_price = price)
                message = "Success! You sold {} shares of {} at the price ${}.".format(quantity, symbolCompany, price)
                message = "You have {} shares of {} remaining.".format(shares_left, symbolCompany)
            else:
                api.submit_order(
                    symbol = symbolCompany,
                    qty = quantity, 
                    side = sell, 
                    type = typeW,
                    time_in_force = time_force)
                message = "Success! You sold {} shares of {} at the market price.".format(quantity, symbolCompany)
                message = "You have {} shares of {} remaining.".format(shares_left, symbolCompany)
        else:
            message = "ERROR! You have {} shares of {}, and you are trying to sell {} shares of {}.".format(qty_stock, symbolCompany, quantity, symbolCompany)
    else:
        message = "{} is not tradeable at this time.".format(symbolCompany)
    return message
