import sys

COMMANDS = "uczen", "nauczyciel", "wychowawca", "koniec"

class School:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.tutors = []
        self.teachers = []
    
    def add_student(self):
        firstname = input('imię ucznia: ')
        lastname = input('nazwisko ucznia: ')
        clas = input('klasa ucznia: ')
        student = Student(firstname=firstname, lastname=lastname, clas=clas)
        self.students.append(student)
        print(f'uczen dodany do bazy: {student}')

    def add_tutor(self):
        firstname = input('imię wychowawcy: ')
        lastname = input('nazwisko wychowawcy: ')
        classes = [] 
        
        while True:
            clas = input('klasa: ')
            if clas=='':
                break
            classes.append(clas)
            
        tutor = Tutor(firstname=firstname, lastname=lastname, classes=classes)
        self.tutors.append(tutor)
        print('wychowawca dodany do bazy')

    def add_teacher(self):
        firstname = input('imię nauczyciela: ')
        lastname = input('nazwisko nauczyciela: ')
        subject = input('przedmiot: ')
        classes = [] 
        
        while True:
            clas = input('klasa: ')
            if clas=='':
                break
            classes.append(clas)
            
        teacher = Teacher(firstname=firstname, lastname=lastname, subject=subject, classes=classes)
        self.teachers.append(teacher)
        print('nauczyciel dodany do bazy')

class Tutor:
    def __init__(self, firstname, lastname, classes):
        self.firstname = firstname
        self.lastname = lastname
        self.classes = classes

    def __str__(self):
        return f'{self.firstname} {self.lastname} (klasy: {self.classes})'

    def __repr__(self):
        return f'{self.firstname} {self.lastname} (klasy: {self.classes})'

class Teacher:
    def __init__(self, firstname, lastname, subject, classes):
        self.firstname = firstname
        self.lastname = lastname
        self.subject = subject
        self.classes = classes

    def __str__(self):
        return f'{self.firstname} {self.lastname} (przedmiot: {self.subject}, klasy: {self.classes})'

    def __repr__(self):
        return f'{self.firstname} {self.lastname} (przedmiot: {self.subject}, klasy: {self.classes})'


class Student:
    def __init__(self, firstname, lastname, clas):
        self.firstname = firstname
        self.lastname = lastname
        self.clas = clas

    def __str__(self):
        return f'{self.firstname} {self.lastname} (klasa: {self.clas})'

    def __repr__(self):
        return f'{self.firstname} {self.lastname} (klasa: {self.clas})'

school = School(name = 'my school')

while True:
    action = input('Podaj komendę: ')

    if action not in COMMANDS:
        print('niepoprawna komenda!')
        continue
    
    if action == 'uczen':
       school.add_student()

    if action == 'wychowawca':
        school.add_tutor()

    if action == 'nauczyciel':
        school.add_teacher()
    
    if action == 'koniec':
        break

print(school.tutors)
print(school.teachers)
print(school.students)