#Personal cards database

class BaseContact:
    def __init__(self, name, surname, email, private_num):
        self.name = name
        self.surname = surname
        self.email = email
        self.private_num = private_num
    @property
    def label_length(self):
        return f'Name length is: {len(self.name + self.surname) + 1}'
    def private_contact(self):
        return f'Contact with {self.name} {self.surname} via private phone number: {self.private_num}'
    def contact_email(self):
        return f'Contact with {self.name} {self.surname} via e-mail: {self.email}'
    def __str__(self):
        return f'{self.name} {self.surname} {self.private_num} {self.email}'
class BusinessContact(BaseContact):
    def __init__(self, company, job, business_num, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.company = company
        self.job = job
        self.business_num = business_num
    def business_contact(self):
        return f'Contact with {self.name} {self.surname} via business phone number: {self.business_num}'
    def __str__(self):
        return f'{self.name} {self.surname} {self.company} {self.job} {self.business_num}'
    def __repr__(self):
        return f"BusinessContact(name={self.name} surname={self.surname}, company={self.company}, job={self.job}, email={self.email}, private_num={self.private_num}, business_num={self.business_num})"
    @property
    def label_length(self):
        return f'Name length is: {len(self.name + self.surname) + 1}'

#Names database

person1 = BusinessContact(name="Elizabeth", surname="Martinez", company="Muscle Factory", job="Oceanographer", email="ElizabethMMartinez@dayrep.com", business_num="+48 239 234 987", private_num="+48 777 222 738")
person2 = BusinessContact(name="Carl", surname="McCarthy", company="Foxmoor", job="Labor relations manager", email="CarlDMcCarthy@jourrapide.com", business_num="+48 322 982 239", private_num="+48 8382 492 777")
person3 = BusinessContact(name="Kimberly", surname="Tyner", company="Zany Brainy", job="Nuclear medicine technologist", email="KimberlyTTyner@dayrep.com", business_num="+48 291 293 398", private_num="+48 382 888 222")
person4 = BusinessContact(name="Buford", surname="Duncan", company="Paul's Record Hut", job="Forester", email="BufordCDuncan@armyspy.com", business_num="+48 399 290 281", private_num="+48 333 339 220")
person5 = BusinessContact(name="Michelle", surname="McCormick", company="KG Menswear", job="Municipal court judge", email="MichelleBMcCormick@teleworm.us", business_num="+48 398 298 393", private_num="+48 492 399 333")

#Sorting by name, surname, email with using lambda

persons = [person1, person2, person3, person4, person5]
by_name = sorted(persons, key=lambda person: person.name)
by_surname = sorted(persons, key=lambda person: person.surname)
by_email = sorted(persons, key=lambda person: person.email)

#print(by_name)     #Remove if you want to print
#print(by_surname)  #Remove if you want to print
#print(by_email)    #Remove if you want to print

#Loop printing personal cards database

for person in [person1, person2, person3, person4, person5]:
    print(person.name, person.surname, person.email)

print(person1.business_contact())
print(person3.label_length)
