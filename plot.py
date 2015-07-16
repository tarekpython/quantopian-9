import pandas as pd
import numpy as np
import talib
import datetime
import matplotlib.pyplot as plt
"""get_ipython().magic(u'matplotlib inline')
pd.set_option('display.notebook_repr_html', False)
pd.set_option('display.max_columns', 15)
pd.set_option('display.max_rows', 100)
pd.set_option('precision', 3)
"""
import pandas.io.data as web

    
rate = pd.DataFrame().from_csv("rate.csv")
quarter = pd.DataFrame().from_csv("quarter.csv")
volume = pd.DataFrame().from_csv("avg_volume.csv")
tran =  volume.transpose()
cc = []
for column in tran.columns.values[2:]:
    ss = tran.ix[1:,1:column].sort([column],ascending=[0])
    
    cc.append(list(ss.iloc[:50].index))
    
    
xx =pd.Series(cc[0])    

for dd in cc[1:]:
    xx2 = pd.Series(dd)
    xx =  pd.Series(np.intersect1d(xx,xx2))
    print xx.to_dict()



#.sort([1],ascending=[0])



#aaa = rate[rate.columns[:10]]
#aaa.plot()
#aaa
#aaa.plot(figsize=(30,30))

#quarter = pd.DataFrame().from_csv("quarter.csv")    
#quarter.plot(figsize=(30,30))     


#bbb = quarter[quarter.columns[:10]]
#bbb
