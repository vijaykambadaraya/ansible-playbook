
import pandas as pd
import numpy as np
import random
data={'s1':176.2,'s2':158.4,'s3':167.6,'s4':156.2,'s5':161.4}
heights_A = pd.Series(data,index=['s1','s2','s3','s4','s5'])
print(heights_A[1])
print(heights_A[1:4])
data1={'s1':85.1,'s2':90.2,'s3':76.8,'s4':80.4,'s5':78.9}
weights_A = pd.Series(data1,index=['s1','s2','s3','s4','s5'])

frame1 = {'Student_height': heights_A, 'Student_weight': weights_A}

df_A=pd.DataFrame(frame1)
df_A.to_csv('classA.csv')
df_A2=pd.read_csv('classA.csv')
df_A3=pd.read_csv('classA.csv',index_col=0)


labels = ['s1','s2','s3','s4','s5']
np.random.seed(100)

my_list = np.random.normal(170.0,25.0,5)
heights_B=pd.Series(data = my_list,index = labels)

#print(heights_B.mean())
np.random.seed(100)
my_list1 = np.random.normal(75.0,12.0,5)
weights_B=pd.Series(data = my_list1,index = labels)
#print(weights_B)
frame2 = {'h1':heights_B,'w1':weights_B}
df_B=pd.DataFrame(frame2)
df_B.rename(columns={'h1':'Student_height',
                          'w1':'Student_weight'},inplace=True)
df_B.to_csv('classB.csv',index=False)
df_B2=pd.read_csv('classB.csv')
print(df_B2)
df_B3=pd.read_csv('classB.csv',header=None)
print(df_B3)
df_B4=pd.read_csv('classB.csv',header=None,skiprows=2)
print(df_B4)