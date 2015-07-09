from pandas.io.data import _yahoo_codes
from pandas.io.common import urlopen
import pandas.compat as compat
from collections import defaultdict

sym_list = 'APT'
_yahoo_codes.update({'MarketCap' : 'j1'})
request = ''.join(compat.itervalues(_yahoo_codes))  # code request string
header = list(_yahoo_codes.keys())
print header
data = defaultdict(list)

url_str = 'http://finance.yahoo.com/d/quotes.csv?s=%s&f=%s' % (sym_list, request)

with urlopen(url_str) as url:
    lines = url.readlines()
    print lines
