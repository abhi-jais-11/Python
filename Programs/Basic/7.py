#function to count number of vowel in s string

def vowel_count(str):
    vowels=['a','i','o','u','e']
    str=str.lower()
    count=0
    for i in str:
        if i in vowels:
            count+=1
    return count



#function call
str='Hello Welcome'
ans=vowel_count(str)
print(f"Number of Vowel in {str} is : {ans}")