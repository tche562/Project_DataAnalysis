import pandas as pd
import numpy as np
import csv
import datetime
import time

pd.set_option('display.max_rows', 50)
data = pd.read_csv('melb_data.csv')
#print(data.ioc[1])#row
#print(data['Suburb'])#colume





#data.to_csv('./test.csv',sep=',',header = True, index = True)

#print(data['Date'])#colume

data['Date'] = pd.to_datetime(data['Date'],format='%d/%m/%Y')
data['Year'] = data['Date'].dt.year
data['Month'] = data['Date'].dt.month
# for item in data['Date']:
#     print(item)
#     date_time = datetime.datetime.strptime(item, '%d/%m/%Y')
#     print(date_time)
#     data['Year'] = date_time

new = np.unique(data['Year'])
print(new)

a = data.isnull().sum().sort_values(ascending = False)
# a = a.sort_value(axis=1,ascending = False)
print(a)
# print(data)

#data.to_csv('./test.csv',sep=',',header = True, index = True)