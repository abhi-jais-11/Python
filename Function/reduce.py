from functools import reduce
#reduce(function, iterable[, initial], /)


def sum(a,b):
    return a+b


sum=reduce(sum,[*range(1,5)])

print('-------------------------------------')
print("Using Function:")

print("Sum of nums:",sum)


print('-------------------------------------')
print("Using Lambda :")

sum=reduce(lambda n,m:n+m ,[*range(1,5)])
print("Sum of nums:",sum)
