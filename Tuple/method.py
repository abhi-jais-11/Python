'''
1.Tuple Built-In Methods
    -Tuples support only a few methods due to their immutable nature.
    -The two most commonly used methods are count() and index()

'''

tup=(1,2,3,4,5,5,5,6,6,7,8,9)

#index return the index of first occurence of  the element
print(tup.index(6))

# count retrun the number of occurence of the element in the tup
print(tup.count(5))


'''

2.Tuple Built-In Functions

'''

#all() Returns true if all element are true or if tuple is empty
print('-----------------------------------')
print(all((0,12)))
print(all(tup))

#any()	return true if any element of the tuple is true. if tuple is empty, return false
print('-----------------------------------')
tup=(1,2,3,40,0,0)
tup2=()
print(any(tup))
print(any(tup2))


#len()	Returns length of the tuple or size of the tuple

print('---------------------------')
print(len(tup))

#enumerate()	Returns enumerate object of tuple

enm=enumerate(tup)
print(enm)


print('---------------------------------')

#min()
print(min(tup))

#max()
print(max(tup))


#sum ()
print(sum(tup))


print('--------------------------------')

#sorted()
print(sorted(tup))