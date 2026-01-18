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
