import time
import sys
from datetime import datetime
from datetime import date
import pymongo
from pymongo import MongoClient
from iexfinance.stocks import get_historical_data
from iexfinance.refdata import get_symbols
import IEXScraper

TICKER_FILE = sys.argv[1]
print("Reading stock data from " + TICKER_FILE)

def format_EOD_json(json, ticker, date):
    for eod_item in json:
        json[eod_item]['ticker'] = ticker
        json[eod_item]['date'] = date
    return json

def return_EOD_range_if_exists(ticker, start_date, end_date):
    json = get_historical_data(ticker, start_date, end_date)
    string_date = IEXScraper.format_date(start_date)
    if string_date in json:
        formatted_json = format_EOD_json(json, ticker, string_date)
        return formatted_json
    return {}

def daterange(start_date, end_date):
    date_range = []
    day = start_date.day
    month = start_date.month
    year = start_date.year
    while day != end_date.day and month != end_date.month and year != end_date.year:
        day = (day % IEXScraper.get_month_length(month, year)) + 1
        if day == 1:
            month = (month + 1) % 12
            if month == 1:
                year += 1
        date_range.append(IEXScraper.format_date(date(month, day, year)))
    return date_range

def upload_range_eod_single_company(database, ticker, start_date, end_date):
    eod_json = return_EOD_range_if_exists(ticker, start_date, end_date)
    collection_name = 'EOD'
    print(f"Inserting data for {ticker}")
    if collection_name not in database.list_collection_names():
        database.create_collection(collection_name)
    if len(eod_json) > 0:
        for eod_day in eod_json:
            database[collection_name].insert_one(eod_json[eod_day])

#Uploads the EOD data for available NYSE companies in the given date range.
def upload_range_eod_total_companies(database, start_date, end_date):
    tickers = IEXScraper.get_ticker_list(TICKER_FILE)
    for ticker in tickers:
        upload_range_eod_single_company(database, ticker, start_date, end_date)

#Gets the EOD data for company specified by ticker on given date
def get_company_eod_data(database, ticker, date):
    return database['EOD'].find_one({'ticker': ticker})

#connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
#TODO: take user input for dates
client = MongoClient("mongodb+srv://admin:admin@bdaidatabase-l1mg5.mongodb.net/test?retryWrites=true")
db=client.BDAI_EOD
upload_range_eod_total_companies(db, date(2015, 4, 10), date(2019, 4, 10))
print("Finished!")