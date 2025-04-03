from random import choices

letters="abcdefghijklmnopqrstuvwxyz"

string=''.join(choices(letters,k=10))

print(f"A random string of length 10 using lowercase letters :{string} ")
