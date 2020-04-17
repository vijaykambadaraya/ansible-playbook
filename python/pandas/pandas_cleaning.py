import pandas as pd
import numpy as np
import random
data={'s1':176.2,'s2':158.4,'s3':167.6,'s4':156.2,'s5':161.4}
heights_A = pd.Series(data,index=['s1','s2','s3','s4','s5'])
print(heights_A[0])
print(heights_A.shape)
data1={'s1':85.1,'s2':90.2,'s3':76.8,'s4':80.4,'s5':78.9}
weights_A = pd.Series(data1,index=['s1','s2','s3','s4','s5'])
#labels = ['s1','s2','s3','s4','s5']
frame1 = {'Student_height': heights_A, 'Student_weight': weights_A}
df_A = pd.DataFrame(frame1) 
#df_A = pd.DataFrame(frame1,index=labels) 
print(df_A.loc['s3'])

df_A.loc['s3'] = np.nan

df_A.loc['s5'].Student_weight = np.nan
df_A2=df_A.dropna()
print(df_A2)