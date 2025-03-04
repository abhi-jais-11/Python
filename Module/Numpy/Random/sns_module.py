'''
    import the pyplot object of the matplotlib module .
    import the seaborn module 
'''

'''
Displot is use for distribution plote.
    - It takes an array input and plote the curve corresponding to the distribution of thepoints of array.

'''


import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot([0,1,2,3,4,5],hist=False)

plt.show()