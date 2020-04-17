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
height=df_A['Student_height']
print(type(height))
df_s1s2=df_A.loc[['s1','s2']]
print(df_s1s2)
df_s2s5s1=df_A.loc[['s2','s5','s2']]
print(df_s2s5s1)
df_s1s4=df_A.loc[(df_A.index.str.endswith('1') | df_A.index.str.endswith('4'))]
print(df_s1s4)