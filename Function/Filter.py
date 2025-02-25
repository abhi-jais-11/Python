'''
filter() in python
    The filter() method filters the given sequence with the help of a function that tests each element in the sequence to be true or not.
    Let’s see a simple example of filter() function in python:

Python filter() Syntax
The filter() method in Python has the following syntax:

Syntax: filter(function, sequence)


function: A function that defines the condition to filter the elements.
    This function should return True for items you want to keep and False for those you want to exclude.
iterable: The iterable you want to filter (e.g., list, tuple, set).
    The result is a filter object, which can be converted into a list, tuple or another iterable type.

'''


#to check all element are even or odd


nums=[1,2,3,10,277,38,10]

even=list(filter(lambda n:n%2==0,nums))

print(even)