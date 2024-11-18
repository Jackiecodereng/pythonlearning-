# digitizing police records to store criminals
class Criminal:
 def __init__(self, name,id_number,crime,gender):
        self.name=name
        self.id_number=id_number
        self.crime = crime
        self.gender=gender
 def show_details(self):
     print(f'name:{self.name}\nID:{self.id_number}\nIssue:{self.crime}\nGender:{self.gender}')

c1=Criminal('john dukes','5252566','stealing chickens','male')
c1.show_details()
