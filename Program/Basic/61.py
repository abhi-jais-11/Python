def generate_sub_str(str):
    sub_str = []
    n = len(str)
    for i in range(n):
        for j in range(i + 1, n + 1):
            sub_str.append(str[i:j])
    
    return sub_str


#driver code 
str = "abc"
sub_str = generate_sub_str(str)
print("All possible sub_str of",str, ":\n",*sub_str)
