# Most comman interview question.


#count vowel in a string.

def count_vowel(str):
    vowel=['a','i','o','u','e']
    count=0
    for i in str.lower():
        if i in vowel:
            count+=1
    return count




#check palindrom string.

def is_str_plindrome(str):
    if str==str[::-1]:
        return True
    return False



#reverse of string.

def reverse_str(str):
    return str[::-1]



#remove duplicate char from the string.

def remove_duplicate(str):
    return ''.join(sorted(set(str)))




#count freuency of char in string.

def count_frequency(str):
    dct={}
    count=1
    for char in str.lower():
        if char in dct.keys():
            dct[char]=count+1
        else:
            dct[char]=count
    return dct


#check if a string is subtring of another string.

def sub_str_of_anotherstr(substr,str):
    if str.lower().find(substr.lower()) !=-1:
        return True
    return  False


#check anagram string.
 
def is_anagram(str1,str2):
    if sorted(str1.lower())==sorted(str2.lower()):
        return True
    return False




if __name__=='__main__':
    count_vowel()
    is_str_plindrome()
    reverse_str()
    remove_duplicate()
    count_frequency()
    sub_str_of_anotherstr()
    is_anagram()
    