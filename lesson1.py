print("hello , world")
print(10+12)
print("10+11")
print(10,11,22)
print("tom","juma","mike")


# personal projects (string), a string should always be in quotes
first_name = 'bro'
food='pizza'
email='bro123@gmail.com'

print(f'hello {first_name}')
print(f'you like {food}')
# integers should not have books
age=25
quantity=3
num_of_students=30
print(f'your age is {age}years old')
print(f'no of students is {num_of_students*quantity}')

# dealing with boolean quantities
is_student = False
for_sale = False
print(f'are you a student? {is_student}')

if is_student:
    print('you are a student')
else:
    print('you are not a student')

    #float no with decimal places
    price=10.99
    print(f'price is {price}')
     #conversions in python
    gpa=3.2
    age=25
    gpa=int(gpa)
    print(f'gpa is {gpa}')
    age=float(age)
    print(f'age is {age}')