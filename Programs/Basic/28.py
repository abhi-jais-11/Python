from functools import reduce

products=reduce(lambda x,y:x*y,[i for i in range(1,6)])

print(f"Products of list Element is : {products}")

