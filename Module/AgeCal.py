import datetime as d
current_year=input("Enter The Current Year,month,date:")
birth_year=input("Enter The Birth Year,month,date:")

print(f"DOB:{d.date(current_year)-d.date(birth_year)}")
