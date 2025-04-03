#recursive function to check palindrom  number

def is_palindrome_num(n):
    num=str(n)
    if n==" " or n=="":
        return ""
    else:
        return num[-1]+is_palindrome_num(num[:-1])
    
   


#function call
n=111
ans=is_palindrome_num(n)
print(ans)
if int(ans)==n:
    print(f"{n} is Plindrome:")
else:
    print(f"{n} is Not Palindrome:")
        
    