import pandas as pd
import numpy as np
import random
data={'s1':176.2,'s2':158.4,'s3':167.6,'s4':156.2,'s5':161.4}
heights_A = pd.Series(data,index=['s1','s2','s3','s4','s5'])
print(heights_A[0])
print(heights_A.shape)
data1={'s1':85.1,'s2':90.2,'s3':76.8,'s4':80.4,'s5':78.9}
weights_A = pd.Series(data1,index=['s1','s2','s3','s4','s5'])

print(weights_A.dtype)

frame1 = {'Student_height': heights_A, 'Student_weight': weights_A}

result1 = pd.DataFrame(frame1) 

print(result1.shape)

labels = ['s1','s2','s3','s4','s5']
np.random.seed(100)

my_list = np.random.normal(170.0,25.0,5)

heights_B=pd.Series(data = my_list,index = labels)

print(heights_B.mean())

my_list1 = np.random.normal(75.0,12.0,5)

weights_B=pd.Series(data = my_list1,index = labels)

print(weights_B)

frame2 = {'Student_height': heights_B, 'Student_weight': weights_B}

result2 = pd.DataFrame(frame2) 

print(result2.columns)

data2 = {'item1':result1, 'item2':result2} 

dataflair_pan = pd.Panel(data2)
print(dataflair_pan.shape)