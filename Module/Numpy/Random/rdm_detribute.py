from numpy import random 

'''

Random Destribution:
        - P(X = xi) = pi for x = xi and P(X = xi) = 0 for x ≠ xi.
        - X is tha data set with x1,x2,x3.........xi
        - P is the probbality density  function for the data set. p1,p2,...pi sum(pi)=1
    
'''

arr=random.choice([3,5,9,7],p=[0.5,0.3,0.0,0.2],size=(10))
print("Random Distribution:\n",arr)

print('---------------------------------')
arr=random.choice([3,5,9,7],p=[0.5,0.3,0.0,0.2],size=(4,4))
print("Random Distribution:\n",arr)