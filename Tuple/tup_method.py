'''
1.Tuple Built-In Methods
    -Tuples support only a few methods due to their immutable nature.
    -The two most commonly used methods are count() and index()

'''

#simple tuple 1-10
tup=tuple([*range(1,10),*range(1,11)])

print('------------------------------')
#1 count(element ) #return the no of  ocuurence of the element in tuple
print("Count 10 in Tuple:",tup.count(10))
print("Count 5 in Tuple:",tup.count(5))

print('------------------------------')
#2 index(element,startind,endidx ) #return the first  ocuurence  index of the element in tuple


print("Index 10 in Tuple:",tup.index(10))
print("Index 5 in Tuple:",tup.index(5,1))



#some common method 

print('------------------------------')
#1.max(arg1,arg2,*Args,*[key=func])

print("Max Value In Tuple :",max(tup))


print('------------------------------')
#1.min(arg1,arg2,*Args,*[key=func])

print("Min Value In Tuple :",min(tup))


print('------------------------------')
#1.sum(itrable,start)

print("Sum of  Value In Tuple :",sum(tup))

print('------------------------------')
#1.sorted(itrable,key,reverse)

print("Sorted of  Value In Tuple :",sorted(tup,reverse=True))

print('------------------------------')
#1.len(itrable)

print("Length of  Tuple :",len(tup))


print('------------------------------')
#1.all()

print("Sorted of  Value In Tuple :",all(tup))j 