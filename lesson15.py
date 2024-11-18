# inheritance
#error handling
# dates
from datetime import datetime

from lesson17 import date_of_birth


class Employee:   # this is the parent class
     def __init__(self, name, id_number, dob , gender):
         self.name = name
         self.id_number = id_number
         self.dob = dob
         self.gender = gender
         date_of_birth = datetime.strptime(dob, '%Y-%m-%d')
         self.age = date_of_birth.year - date_of_birth.year

     def print_details(self):
         print(f"name:{self.name}\nID:{self.id_number}\ndob:{self.dob}\ngender:{self.gender}\nage:{self.age}")


class PermanentEmployee(Employee):      # this are called child classes
    def __init__(self, name, id_number, dob , gender, salary):
        super().__init__(name,id_number,dob,gender)   # prevents u from repeating yourself
        self.salary = salary
    def print_salary(self):
        print(f"salary is {self.salary}")
# overide
    def print_details(self): # helps print the details individually.
      super().print_details()
      print(f"salary is {self.salary}")

class TemporaryEmployee(Employee):
    def __init__(self, name, id_number, dob , gender, hourly_pay,end_date):
        super().__init__(name, id_number, dob, gender)
        self.hourly_pay = hourly_pay
        self.end_date = end_date
    def print_hourly_pay(self):
        print(f"hourly pay is {self.hourly_pay}")
    def print_end_date(self):
        print(f"end date is {self.end_date}")

p1 = PermanentEmployee(salary=10000,name="jane said",id_number="1234",dob="2001-01-01",gender="male")
p1.print_details()
p1.print_salary()


t1 = TemporaryEmployee("jin","222222222","1995-11-12","m",hourly_pay=10000,end_date="2024-01-01")
t1.print_details()