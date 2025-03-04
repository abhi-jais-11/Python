import numpy as np

arr=np.array([41,24,42,43,54,49,22])
filter_arr=[]

#using array direct without using loop

filter_arr=arr>24 #adding the true for the greater the 24 value and put it inside the arr[filter_array]


print("Greater Than 24 :",arr[filter_arr])

print('--------------------------------')

#even filter 
arr=np.array([41,24,42,43,54,49,22,23,5,7,6])
filter_arr=[]

#using array direct without using loop

filter_arr=arr%2==0


print("Even Array",arr[filter_arr])

print('--------------------------------')

#odd filter 
arr=np.array([41,24,42,43,54,49,22,23,5,7,6])
filter_arr=[]

#using array direct without using loop

filter_arr=arr%2!=0 


print("Odd Array:",arr[filter_arr])



#positive filter
print('--------------------------------')
arr=np.array([41,-24,42,-43,54,49,-22,23,5,-7,6])
filter_arr=[]

#using array direct without using loop

filter_arr=arr>0 


print("Positive Array:",arr[filter_arr])


#negative filter

print('--------------------------------')
arr=np.array([41,-24,42,-43,54,49,-22,23,5,-7,6])
filter_arr=[]

#using array direct without using loop

filter_arr=arr<0 

print("Negative Array:",arr[filter_arr])



