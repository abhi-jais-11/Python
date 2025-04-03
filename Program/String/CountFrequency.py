'''

Program to count the Frequency of the word in a string.

'''

def word_frequency(str,word):

    return  str.split(" ").count(word)



str=input("Enter The String:")
word=input("Enter The Word To Count Frequency:")
print(f"Frequency of the words is:{word_frequency(str,word)}")