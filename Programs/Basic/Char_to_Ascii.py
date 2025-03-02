# char=input("Enter Charecter:")
# print("ASCII of the cahrecter is :",ord(char))


#sentence to ascii
def sen_to_ascii(sen):
    for i in sen:
        print(ord(i),end=" ")


sen=input("Enter The Sentance:")
sen_to_ascii(sen)