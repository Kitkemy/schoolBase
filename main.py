import sys

COMMANDS = "uczen", "nauczyciel", "wychowawca", "koniec"

class School:
    def __init__(self, name):
        self.name = name
        self.students = {}
        self.tutors = {}
        self.teachers = {}
        self.school_classess = {}
    
    def add_student(self):
        name = input('imię i nazwisko ucznia: ')
        id_class = input('klasa ucznia: ')
        if id_class not in self.school_classess:
            self.school_classess[id_class]=School_class(name=id_class)
        
        student = Student(name=name, id_class=id_class)
        self.students[name]=student
        self.school_classess[id_class].students.append(name)

        print(f'uczen dodany do bazy: {student}')

    def add_tutor(self):
        name = input('imię i nazwisko wychowawcy: ')
        classes = [] 
        
        while True:
            id_class = input('klasa: ')
            if id_class=='':
                break
            if id_class not in self.school_classess and id_class !='':
                self.school_classess[id_class]=School_class(name=id_class)
                
            classes.append(id_class)
            
        tutor = Tutor(name=name, classes=classes)
        self.tutors[name]=tutor

        for id_class in classes:
            self.school_classess[id_class].tutors.append(name)

        print('wychowawca dodany do bazy')

    def add_teacher(self):
        name = input('imię i nazwisko nauczyciela: ')
        subject = input('przedmiot: ')
        classes = [] 
        
        while True:
            id_class = input('klasa: ')
            if id_class=='':
                break
            if id_class not in self.school_classess and id_class !='':
                self.school_classess[id_class]=School_class(name=id_class)

            classes.append(id_class)
            
        teacher = Teacher(name=name, subject=subject, classes=classes)
        self.teachers[name]=teacher
        
        for id_class in classes:
            self.school_classess[id_class].teachers.append(name)
            self.school_classess[id_class].subjects.append(subject)
        print('nauczyciel dodany do bazy')

class School_class:
    def __init__(self, name):
        self.name=name
        self.students=[]
        self.tutors=[]
        self.teachers=[]
        self.subjects=[]

class Tutor:
    def __init__(self, name, classes):
        self.name = name
        self.classes = classes

    def __str__(self):
        return f'{self.name} (klasy: {self.classes})'

    def __repr__(self):
        return f'{self.name} (klasy: {self.classes})'

class Teacher:
    def __init__(self, name, subject, classes):
        self.name = name
        self.subject = subject
        self.classes = classes

    def __str__(self):
        return f'{self.name} (przedmiot: {self.subject}, klasy: {self.classes})'

    def __repr__(self):
        return f'{self.name} (przedmiot: {self.subject}, klasy: {self.classes})'

class Student:
    def __init__(self, name, id_class):
        self.name = name
        self.id_class = id_class

    def __str__(self):
        return f'{self.name} (klasa: {self.id_class})'

    def __repr__(self):
        return f'{self.name} (klasa: {self.id_class})'

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

phrase = sys.argv[1]

if phrase in school.students:
    ##wypisz wszystkie lekcje, które ma uczeń i nauczycieli, którzy je prowadzą
    print('Uczeń ma następujące lekcje z nauczycielami:')

    class_to_check = school.students[phrase].id_class
    teachers_list = school.school_classess[class_to_check].teachers
    for teacher in teachers_list:
        print(teacher)
        print(school.teachers[teacher].subject)

elif phrase in school.tutors:
    ##wypisz wszystkich uczniów, których prowadzi wychowawca
    print('Wychowawca prowadzi następujących uczniów:')

    class_to_check = school.tutors[phrase].classes
    for id_class in class_to_check:
       print(school.school_classess[id_class].students)

elif phrase in school.teachers:
    ##wypisz wychowawców wszystkich klas, z którym ma zajęcia nauczyciel
    print('Nauczyciel ma zajęcia z klasami którymi wychowawcy to:')

    class_to_check = school.teachers[phrase].classes
    for id_class in class_to_check:
       print(school.school_classess[id_class].tutors)
    
else:
    ##wychowawca i uczniowie w klasie
    print(school.school_classess[phrase].tutors)
    print(school.school_classess[phrase].students)