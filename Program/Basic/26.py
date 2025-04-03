
#extract even from the list usig filter and lambda

even_list=list(filter(lambda x:x%2==0,[i for i in range(1,19)]))

print(f"List of Even Numbers:{even_list}")