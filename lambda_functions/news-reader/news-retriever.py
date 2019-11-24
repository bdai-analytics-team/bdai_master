#!/usr/bin/env python

import feedparser
import pandas as pd

a ="http://feeds.marketwatch.com/marketwatch/marketpulse/"
feed = feedparser.parse( a)

"""Add a dictionary of stocks to get relevancy"""

stocks = {"Uber":"UBER US","Xylem": "XYL US","Wabtec": "WAB US","WPP": "WPP LN","Vodafone Group": "VOD LN","Teva Pharmaceutical Industries": "TEVA IT","Tesla": "TSLA US","Tableau Software": "DATA US","Synchrony Financial": "SYF US","SoftBank Group": "9984 JP","Rosneft Oil": "ROSN LI","Range Resources": "RRC US","Pyxus International": "PYX US","Prudential": "PRU LN","Petrobras": "PETR4 BZ","Osram Licht": "OSR GR","Nike": "NKE US","NXP Semiconductors": "NXPI US","McDermott International": "MDR US","Marathon Petroleum": "MPC US","Manulife Financial": "MFC CN","Lennar": "LEN US","L Brands": "LB US","Kroger": "KR US","Knight-Swift Transportation Holdings": "KNX US","Kering": "KER FP","Johnson Controls International": "JCI US","Iqvia Holdings": "IQV US","InterGlobe Aviation": "INDIGO IN","ITV": "ITV LN","Harley-Davidson": "HOG US","Hammerson": "HMSO LN","Gilead Sciences": "GILD US","General Electric": "GE US","Ford Motor": "F US","Fast Retailing": "9983 JP","Fannie Mae/Freddie Mac": "FNMA US/FMCC US","Energy Transfer": "ET US","Deutsche Bank": "DBK GR","Dell Technologies": "DELL US","Comcast": "CMCSA US","Cheniere Energy": "LNG US","Centrica": "CNA LN","Canopy Growth": "CGC US","CK Asset Holdings": "1113 HK","CBS": "CBS US","Boston Properties": "BXP US","Bausch Health": "BHC US","Barclays": "BARC LN","Anthem": "ANTH US","Anheuser-Busch InBev": "ABI BB","Amazon": "AMZN","Google": "GOOG","Microsoft": "MSFT","Apple": "AAPL","Facebook": "FB","Netflix": "NFLX","JP Morgan": "JPM","Bank of America": "BAC"}

"""basically get relevant stocks"""

def rss_processor(feed):
  title =feed.feed.title
  #retrival_time = feed.feed.time
  colTitle = []
  colPublished = []
  colTicker =[]
  colArticle = []
  colDescription= []
  for i in feed.entries:
    for key in stocks:
      if key in i.title:
        print(stocks.get(key))
        ticker = stocks.get(key)
      else:
        ticker=None
    
    
    colTitle.append(title)
    colPublished.append(i.published)
    colTicker.append(ticker)
    colArticle.append(i.title)
    colDescription.append(i.description)
    print(title+"   |    "+i.published+"   |    " + i.title + "\n" + i.description+ "\n \n \n")

  data = {'Source':colTitle,'Time':colPublished,'Ticker Symbol':colTicker,'Title':colArticle,'Full Article':colDescription}
  df = pd.DataFrame(data)
  print(df)
  
 