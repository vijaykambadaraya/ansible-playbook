
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

df_A['Gender'] = ['M', 'F', 'M', 'M', 'F']

s=pd.Series([165.4, 82.7, 'F'], index=['Student_height', 'Student_weight', 'Gender'],name='s6')

df_AA=df_A.append(s)

print(df_AA)

labels = ['s1','s2','s3','s4','s5']
np.random.seed(100)
my_list = np.random.normal(170.0,25.0,5)
heights_B=pd.Series(data = my_list,index = labels)
np.random.seed(100)
my_list1 = np.random.normal(75.0,12.0,5)
weights_B=pd.Series(data = my_list1,index = labels)

frame2 = {'Student_height': heights_B, 'Student_weight': weights_B}

df_B = pd.DataFrame(frame2) 

df_B=df_B.rename(index={'s1':'s7','s2':'s8','s3':'s9','s4':'s10','s5':'s11'})

df_B['Gender']=['F', 'M', 'F', 'F', 'M']

df = pd.concat([df_AA, df_B])

print(df)