# #Create the independent data set
# for day in df_days:
#     days.append([int(day.split('-')[4])])
# #Create the dependent data set (adj close prices)
# for adj_close_price in df_adj_close:
#     adj_close_prices.append( float(adj_close_price))
from pandas._libs.tslibs.timestamps import Timestamp

time = Timestamp()
print(time)
