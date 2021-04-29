import pandas as pd
import numpy
import csv

pd.set_option('display.max_rows', 20)
data = pd.read_csv('melb_data.csv')
#print(data.ioc[1])#row
#print(data['Suburb'])#colume

print(data)



#data.to_csv('./test.csv',sep=',',header = True, index = True)

#print(data['Date'])#colume

for item in data['Date']:
    print(item)
