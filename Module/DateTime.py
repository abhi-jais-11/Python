import datetime as d

print("Date:",d.datetime.now())

print('-------------------------------')

print("Time:",d.datetime.now().time())

print('-------------------------------')

print("Only Date:",d.date.today())

print('-----------------------------------')
print(d.__all__)
print('-----------------------------------')

print("Carete Date:",d.date(2024,12,23))

print('-------------------------------------')
print("Month:",d.datetime.now().month)
print('--------------------------------------')

print("Week Day:",d.datetime.now().weekday())
print('-------------------------------')

print("MINYEAR:",d.MINYEAR)
print("MAXYEAR:",d.MAXYEAR)