import random as rd


#random()  gererate random number between 0-1.

print('------------------------------------')

print("Random Number from {} to {} :{:.2f}".format(0,1,rd.random()))
print('------------------------------------')

#randint(a,b) Return random integer in range [a, b], including both end points

print("Randome Number from {} to {} :{}".format(1,10,rd.randint(1,10)))

print('------------------------------------')

#randrange(start,end,step) Choose a random item from range(stop) or range(start, stop[, step]).
print("Random Number between {} to {} : {}".format(1,100,rd.randrange(1,100,4)))

print('------------------------------------')
#choice([itrable]) #return a single choice value from iterable

print("Random Top Most IT Company: {} ".format(rd.choice(["Google","Apple","Microsoft","Amazon","Flipkart"])))

print('------------------------------------')

#choices([itrable],k=nums[you want to select]) #return a list of  multiple  choice value from iterable

print("Random Top Most IT Company: {} ".format(rd.choices(["Google","Apple","Microsoft","Amazon","Flipkart"],k=2)))


print('------------------------------------')

lst=["Google","Apple","Microsoft","Amazon","Flipkart"]
rd.shuffle(lst)
print("Suffeld It Company are: {}".format(lst))


print('------------------------------------')
lst=[*range(1,101)]

print("Random Sapmle From The List of Data : {}".format(rd.sample(lst,k=5)))

print('------------------------------------')