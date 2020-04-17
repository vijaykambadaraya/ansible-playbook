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

df_A_filter1=df_A[(df_A.Student_height >= 160.0) & (df_A.Student_weight < 80.0)]
print(df_A_filter1)

df_A_filter2=df_A.loc[(df_A.index.str.endswith('5'))]
print(df_A_filter2)

df_A['Gender'] = ['M', 'F', 'M', 'M', 'F']
df_groups=df_A.groupby('Gender').mean()

print(df_groups)