import pandas as pd
import sys
import numpy as np
import talib as ta
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
end = datetime.datetime(2015, 6, 1)

full_health_data = pd.DataFrame()
full_health_rate =  pd.DataFrame()
full_health_avg_volume = pd.DataFrame()



T1 = pd.read_csv(ticker_list)

for ticker in T1["Symbol"]:
    try:
        
        data = web.DataReader(ticker, 'yahoo', start, end)
        
        data["rsi"] =  ta.RSI(np.array(data["Adj Close"])) 
#        print ta.RSI(data["Adj Close"])
#        print data
        
        data["quarter"] = data["Adj Close"].index.quarter
        data["year"] = data["Adj Close"].index.year
      
        data2 = data

        data2["quarter"] = data["Volume"].index.quarter
        data2["year"] = data["Volume"].index.year

        data.to_csv(ticker+".csv")
        
        quarter = data.groupby(["year","quarter"], as_index=False).first()
        mean = data2.groupby(["year","quarter"], as_index=False).mean()

        
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
        full_health_avg_volume[ticker] = mean["Volume"]
    except:
        print "Unexpected error:", sys.exc_info()[0]
        continue
full_health_avg_volume.to_csv("avg_volume.csv")
full_health_data.to_csv("quarter.csv")
full_health_rate.to_csv("rate.csv")
   
