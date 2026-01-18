#Personal cards database

class Personal_card:
    def __init__(self, name, surname, company, job, email):
        self.name = name
        self.surname = surname
        self.company = company
        self.occupation = job
        self.email = email
    def __str__(self):
        return f'{self.name} {self.surname} {self.mail}'
    def __repr__(self):
        return f"Personal_card(name={self.name} surname={self.surname}, company={self.company}, job={self.job}, mail={self.email})"
    def contact(self):
        return f'Contact with {self.name} {self.surname} via e-mail: {self.mail}'
    @property
    def name_length(self):
        return f'Name length is: {len(self.name + self.surname) + 1}'

#Names database

person1 = Person(name="Elizabeth", surname="Martinez", company="Muscle Factory", job="Oceanographer", email="ElizabethMMartinez@dayrep.com")
person2 = Person(name="Carl", surname="McCarthy", company="Foxmoor", job="Labor relations manager", email="CarlDMcCarthy@jourrapide.com")
person3 = Person(name="Kimberly", surname="Tyner", company="Zany Brainy", job="Nuclear medicine technologist", email="KimberlyTTyner@dayrep.com")
person4 = Person(name="Buford", surname="Duncan", company="Paul's Record Hut", job="Forester", email="BufordCDuncan@armyspy.com")
person5 = Person(name="Michelle", surname="McCormick", company="KG Menswear", job="Municipal court judge", email="MichelleBMcCormick@teleworm.us")