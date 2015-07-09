import pandas as pd
import sys
import numpy as np
import talib
import datetime
import matplotlib.pyplot as plt
#get_ipython().magic(u'matplotlib inline')
#pd.set_option('display.notebook_repr_html', False)
#pd.set_option('display.max_columns', 15)
#pd.set_option('display.max_rows', 8)
#pd.set_option('precision', 3)

import pandas.io.data as web
ticker_list = "companylist-healthcare.csv"

start = datetime.datetime(2012, 1, 1)
end = datetime.datetime(2012, 06, 30)

full_health_data = pd.DataFrame()
full_health_rate =  pd.DataFrame()


T1 = pd.read_csv(ticker_list)

for ticker in T1["Symbol"]:

    try:
         
        data = web.DataReader(ticker, 'yahoo', start, end)
        

        data["quarter"] = data["Adj Close"].index.quarter
        data["year"] = data["Adj Close"].index.year
        quarter = data.groupby(["year","quarter"], as_index=False).first()
        count = 0
        last = 0
        rate = []
        filter_price=0
         
        for item in quarter["Adj Close"]:
            if count == 0:
                rate.append(0)
                last = item
                if float(item) < 1:
                   filter_price = 1
            else:
                rate.append((item-last)/last*100)
                last = item
            count=count + 1
        if filter_price == 1:
            continue
        full_health_data[ticker]= quarter["Adj Close"]
        
        full_health_rate[ticker]= rate
        full_health_data.to_csv("quarter.csv")
        full_health_rate.to_csv("rate.csv")

    except:
        print "Unexpected error:", sys.exc_info()[0]
        continue
    
