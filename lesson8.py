#Dictionary
#list[],Tuple(),dictionary{}
student = {'name':'jane sarah','id':1234,'age':21,'gender':'F'}

print(student['name']) #prints a students detail

print(student)

student['weight']=61 # adds a componet
print(student)

#set {doesnt allow two identical values to be present}, it is unordered  keeps on changing position


people = {'jane','kinuthia','mwangi','jane'}
print(people)
people.add('willy')
print(people)
print(len(people))
people.discard('kevo')
print(people)