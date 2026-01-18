#Personal cards database

class PersonalCard:
    def __init__(self, name, surname, email):
        self.name = name
        self.surname = surname
        self.email = email
class BusinessContact(PersonalCard):
    def __init__(self, company, job, business_num, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.company = company
        self.job = job
        self.business_num = business_num
    def __str__(self):
        return f'{self.name} {self.surname} {self.email}'
    def __repr__(self):
        return f"PersonalCard(name={self.name} surname={self.surname}, company={self.company}, job={self.job}, mail={self.email})"
    def contact_email(self):
        return f'Contact with {self.name} {self.surname} via e-mail: {self.email}'
    @property
    def name_length(self):
        return f'Name length is: {len(self.name + self.surname) + 1}'

#Names database

person1 = BusinessContact(name="Elizabeth", surname="Martinez", company="Muscle Factory", job="Oceanographer", email="ElizabethMMartinez@dayrep.com", business_num="+48 239 234 987")
person2 = BusinessContact(name="Carl", surname="McCarthy", company="Foxmoor", job="Labor relations manager", email="CarlDMcCarthy@jourrapide.com", business_num="+48 322 982 239")
person3 = BusinessContact(name="Kimberly", surname="Tyner", company="Zany Brainy", job="Nuclear medicine technologist", email="KimberlyTTyner@dayrep.com", business_num="+48 291 293 398")
person4 = BusinessContact(name="Buford", surname="Duncan", company="Paul's Record Hut", job="Forester", email="BufordCDuncan@armyspy.com", business_num="+48 399 290 281")
person5 = BusinessContact(name="Michelle", surname="McCormick", company="KG Menswear", job="Municipal court judge", email="MichelleBMcCormick@teleworm.us", business_num="+48 398 298 393")

#Sorting by name, surname, email with using lambda

persons = [person1, person2, person3, person4, person5]
by_name = sorted(persons, key=lambda person: person.name)
by_surname = sorted(persons, key=lambda person: person.surname)
by_email = sorted(persons, key=lambda person: person.email)

#print(by_name)     #Reomove if you want to print
#print(by_surname)  #Reomove if you want to print
#print(by_email)    #Reomove if you want to print

#Loop printing personal cards database

for person in [person1, person2, person3, person4, person5]:
    print(person.name, person.surname, person.email)
print(person2)
print(repr(person1))