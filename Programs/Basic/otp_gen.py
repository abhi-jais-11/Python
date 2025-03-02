
#otp generator using random

import random as ran

def otp_genrator():
    otp=int(ran.random()*10000)
    return otp


def validate_otp(current_otp,user_otp):
    if user_otp == current_otp:
        return "OTP VERIFIEND"
    if user_otp !=current_otp:
        return "INVALID OTP"
    

current_otp=otp_genrator()
print(f"Hii , Your OTP is :{current_otp}")
user_otp=int(input("Enter the OTP to verify:"))
print(f"{validate_otp(current_otp,user_otp)}")
    
    