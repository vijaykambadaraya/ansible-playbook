import pandas as pd
DTIndex = pd.date_range(start='1-Sep-2017', end='15-Sep-2017', name='dates')
print(DTIndex[2])
datelist = ['14-Sep-2017', '9-Sep-2017']
dates_to_be_searched=pd.to_datetime(datelist)
#print(dates_to_be_searched)
#print(DTIndex.isin(dates_to_be_searched))
print(dates_to_be_searched.isin(DTIndex))
#print(DTIndex)
#result=DTIndex[DTIndex['dates'].isin(dates_to_be_searched)]
arraylist = [['classA']*5 + ['classB']*5, ['s1', 's2', 's3','s4', 's5']*2]
#print(arraylist)

mi_index = pd.MultiIndex.from_arrays(arraylist, names=['classA', 'classB'])
print(mi_index)