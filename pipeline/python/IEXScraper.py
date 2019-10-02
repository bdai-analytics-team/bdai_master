from iexfinance.stocks import get_historical_data
from iexfinance.stocks import Stock
from datetime import date, timedelta
from iexfinance.refdata import get_symbols


def get_last_business_day(adate):
    adate -= timedelta(days=1)
    while adate.weekday() > 4:  # Mon-Fri are 0-4
        adate -= timedelta(days=1)
    return adate


def get_stocks_last_days_data(stock_name):
    start = get_last_business_day(date.today())
    return get_historical_data(
        stock_name, start, end=None, output_format='pandas')


print(get_stocks_last_days_data('AAPL'))


def get_ticker_list(file_name):
    nyse_file = open(file_name)
    target_pairs = nyse_file.readlines()
    target_tickers = []
    available_tickers = []
    available_companies = get_symbols()
    for company in available_companies:
        if company['isEnabled'] is True:
            available_tickers.append(company['symbol'])
    for pair in target_pairs:
        if pair.split()[0] in available_tickers:
            target_tickers.append(pair.split()[0])

    return target_tickers

# TODO: Make a separate file for helper methods like these two
# Takes python date and returns a string formatted in the manner used by IEX in JSON


def format_date(date):
    year = str(date.year)
    month = str(date.month)
    day = str(date.day)
    if len(day) == 1:
        day = '0' + day
    if len(month) == 1:
        month = '0' + month
    return year + '-' + month + '-' + day


def get_month_length(month, year):
    month_lengths = {1: 31, 2: 28 + int(year / 4), 3: 31, 4: 30, 5: 31, 6: 30,
                     7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    return month_lengths[month]
