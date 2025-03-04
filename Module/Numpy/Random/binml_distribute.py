'''
Binomial Distribution :
    - Binomial distribution is a descreate distribution.
    - It describe the outcomes of the binary scenarios eg. toss of coin --
    - It has three parameters 
    
    n-> number of the trials .
    p-> probabiliy of occuurence of each trial .
    size -> shape of the rteurn array.

    

'''

from numpy import random 
import seaborn as sns
import matplotlib.pyplot as plt 

arr=random.binomial(n=10,p=0.5, size=100)

sns.distplot(arr,hist=True,kde=False,label="binomial")

plt.show()
