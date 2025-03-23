from random import choices

letters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits="0123456789"
charectors=letters+digits

password="".join(choices(charectors,k=8))

print(f"Random Password Of Length 8 is : {password} ")