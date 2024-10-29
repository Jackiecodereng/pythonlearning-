# maths functionality
import math # adds itself after running the code

x = 90
print(x)

square_root = math.sqrt(x)
print('root is',square_root)

rounded = round(square_root,2)
print('rounded to two decimal places',rounded )

#function (args)
print(rounded)
# call a function
y=round(8.343633,3)
print(y)
print(math.pow(2,3)) # dont type the x and y just type 2,3

print('------------------------')
name='walter jYma'
print(len(name)) # counts no of characters
print(name.lower())
print(name.upper())
print(name.title()) #formats the word perfectly
print(name.capitalize())
print('---------------------------------')
post = 'the  thing is so easy and fluent' # changes
new_post =post.replace('fluent','flowing')
print(new_post)
