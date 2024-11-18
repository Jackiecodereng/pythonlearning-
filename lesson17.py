#dates
from datetime import date, timedelta, datetime # it imported itself

today = date.today()
print(today)
 # how to format it in the kenyan way

formatted_date =today.strftime("%Y")
print(formatted_date)

formatted_date =today.strftime("%d-%m-%Y")
print(formatted_date)

formatted_date =today.strftime("%C")
print(formatted_date)
# calculate forty days from now using timedelta operator

after_forty_days = today + timedelta(days=40)   # ctrl + click time delta to see class
print(after_forty_days)

# figure out how old are u
dob = "2000-03-29"
# convert to date object
date_of_birth = datetime.strptime(dob, "%Y-%m-%d")
age= today.year - date_of_birth.year
print("i am",age,"years old")

age_in_days = datetime.today() - date_of_birth
print(age_in_days.days // 365)