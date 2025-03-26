'''
Dictionary Comprehension:

        {key_expression: value_expression for item in iterable  if condition [optional] }

'''

#creationg dictionary using two list
student_name=["Abhinav","Komal","Tulsi","Anchal","Divya","Sharddha","Satish"]
student_mark=[60,99,90,90,90,90,90] #max=100

print('---------------------------------------------------------------')
student_info={key:value for (key,value) in zip(student_name,student_mark)}
print(student_info)



print('--------------------------------------')
#remove duplicate from the dictionary

student_info={key:value for (key,value) in zip(student_name,student_mark)}
lst=[]

original_dct={}
for key,value in student_info.items():
        if value not in lst:
                lst.append(value)
                original_dct.update({key:value})

del lst
print(original_dct)
print('---------------------------------')






