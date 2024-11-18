# functions
# program to calculate area of a triangle
# t1=0.5*10*12 then print results can work but its very tedious
from datetime import date # this statement importd itself after the date function

from lesson2 import today_date


def calc_area_triangle(b,h):
    area =0.5*b*h
    print(area)
def sayHi(name,age=21):
    print('hello ',name,'i am', age,'years old')

def calc_area_circle(radius): # function to calculate area of a circle
     area = 3.14*radius*radius
     area = round(area,2) # rounds off area to 2 decimal places
     print('area of a circle is?',area,'cm^2')
def print_todays_date(): # calls a date
    today = date.today()
    print(today)
def add(*args): # returns multiple numbers takes that number to the total
    total = 0
    for num in args:
        total += num
        print('total is ?',total)

#calling a function
sayHi("mary")
sayHi('kevo',23 )

calc_area_triangle(8,13) # only type 8,13
calc_area_triangle(40,14)
    #multiple callings which further simplifies the tedious process
triangles=[[8,9],[5,6],[9,3],[10,4]]
for t in triangles: # t is just a variable u can put anything
        calc_area_triangle(t[0],t[1])

calc_area_circle(2.76)

print(today_date)

add(1,2) # prints 1, 1+2
add(7,8,9)
add(74,65,77,76,79)























# create a bank system containing data,name,phone,gender ,amt
# account
# depsit,withdrawal,check balance,
# otp
#matatu  > number ,driver,conductor route