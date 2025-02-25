import random as rd

# print('------------------------------')
# print(rd.__all__)

#printing random value in range 0-1
print('-------------------------------------------')
print("Value Between 0-1:",(rd.random()))

#conveting into integer it will give only integer 
print("After Converting in integer:",int(rd.random()))

#multiply for numbers
print("Multiply from 10 to take number:",int(rd.random()*10))

print('-------------------------------------------')

#randint(range) it return the integer value between range
print("The integer value between 1-100:",rd.randint(1,100))

print('---------------------------------------------')

#randrange(range) it return the  value between range also take step
print("The integer value between 1-100:",rd.randrange(1,100,2))

print('---------------------------------------------')
#uniform() it return the value from the range in floating pont
print(rd.uniform(1,100))

print('-------------------------------')

lst=["Apple","Mango","Lichi"]

#choice ([iterator]) return random value from the iterator

print("My Choice is:",rd.choice(lst))

#choices ([iterator]) return random nultiple value from the iterator

print("My Choices Are :",rd.choices(lst,k=2))


print('----------------------------------------')


nlst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
rd.shuffle(nlst)
print("Suffeld List :",nlst)

print('----------------------------------------------------')
#samle(iterator,key=value) it return sample from the iterator key deside how many value you want
print("The random Sample from the The list:",rd.sample(nlst,k=3))

print('---------------------------------------------------')

#randbytes(numberof bytes) it return random bytes 
print("",rd.randbytes(4))
