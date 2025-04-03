from str_module import sub_str_of_anotherstr

str=input("Enter The String :")
sub_str=input("Enter The Substring:")

is_substr=sub_str_of_anotherstr(substr=sub_str,str=str)

if is_substr:
    print(f"{sub_str} is the substring of {str}")
else:
    print(f"{sub_str} is not substring of {str}")


