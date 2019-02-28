import time
from datetime import datetime
from datetime import date
import pymongo
from pymongo import MongoClient
from iexfinance.stocks import get_historical_data
from iexfinance.refdata import get_symbols
import IEXScraper

TICKER_FILE = 'NYSE.txt'

#TODO: Separate into methods to check if EOD exists for ticker on date, retrieve and format the JSON, and upload to db
def insert_if_exists(database, ticker, start_date):
    json = get_historical_data(ticker, start_date, start_date)
    string_date = IEXScraper.format_date(start_date)
    if IEXScraper.format_date(start_date) in json:
        json = json[IEXScraper.format_date(start_date)]
        json['name'] = ticker
        database[string_date].insert(json)
        return True
    return False


#Uploads the EOD data for available NYSE companies on the given date
def upload_single_day_eod(database, date):
    if str(date.today()) not in database.collection_names():
        database.create_collection(str(date))
        database[str(date)].create_index('name')
    tickers = IEXScraper.get_ticker_list(TICKER_FILE)
    for ticker in tickers:
        insert_chart = insert_if_exists(database, ticker, date)
        if insert_chart:
            print('Insert succeeded on: ' + ticker)
        else:
            print('Insert failed on: ' + ticker)
        time.sleep(0.01)

#Uploads the EOD data for available NYSE companies in the given date range.
def upload_range_eod(database, start_date, end_date):
    #TODO 0: Factor code in this method to a daterange() method
    day = start_date.day
    month = start_date.month
    year = start_date.year
    while day != end_date.day and month != end_date.month and year != end_date.year:
        upload_single_day_eod(database, date(year, month, day))
        day = (day % IEXScraper.get_month_length(month, year)) + 1
        if day == 1:
            month = (month % (365 + int(year / 4))) + 1
            if month == 1:
                year += 1


def get_company_eod_data(database, ticker, date):
    return database[date].find(name=ticker)

#connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
#TODO: take user input for dates
client = MongoClient()
db=client.BDAI
upload_range_eod(db, date(2018, 12, 19), date(2019, 2, 18))