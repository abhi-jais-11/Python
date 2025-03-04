'''
Normal Distribution.
    -The normal destribution is one of the most important distribution.
    -It is also called the Gaussian Distribution after German mathematician Carl Friendrich Gauss.
    -It fits the probabality distribution of many events..eg. IQ Score Heartbeat etc..... 
    - normal() is use for normal destribution
    


'''

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

arr=random.normal(loc=10,scale=20.5,size=(100,100))

sns.distplot(arr)
#it take the three parameter -> size , loc ,scale 
'''
-size is the shape of the array
-loc  (mean) where the peak of the bell exists.
-scale (standard deviation) how flate the graph distribution should be

'''
plt.show()

