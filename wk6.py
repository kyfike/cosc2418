## Ky Fike, 1 Oct 2022
## 

# Program 1: Build my first simple class in Python.
from copyreg import pickle
from re import I
from sys import displayhook


class Pet:
    name = str()
    animal_type = str()
    age = 0

    def __init__(self, n):
        self.name = n
    def set_animal_type(self, t):
        self.animal_type = t
    def set_age(self, a):
        self.age = a
    def get_name(self):
        return self.name
    def get_animal_type(self):
        return self.animal_type
    def get_age(self):
        return self.age

dog = Pet('Bud')
dog.set_age(4)
dog.set_animal_type('Shepherd')
print(dog.get_name(), dog.get_age(), dog.get_animal_type())


# Prog 2
import pickle

class Employee:
    __name = ''         # kind of funny that python doesn't have private member functions
    __id = 0
    __department = ''
    __job_title = ''

    def __init__(self):
        self.name = 'Empty Employee'
    
    def post_constructor(self, n, i, d, jt):
        self.name = n
        self.id = i
        self.department = d
        self.job_title = jt
    
    def get_id(self):
        return self.id
    
    def set_name(self):
        self.name = str(input('Name: '))

    def set_id(self):
        self.id = int(input('ID Number: '))

    def set_department(self):
        self.department = str(input('Department: '))

    def set_job_title(self):
        self.job_title = str(input('Job Title: '))

    def set_all(self):
        self.set_name()
        self.set_id()
        self.set_department()
        self.set_job_title()
    
    def transfer(self):
        self.department = str(input('New department: '))
        self.job_title = str(input('New job title: '))

    def display(self):
        print(self.name + '\t' + str(self.id) + '\t' + self.department + '\t' + self.job_title + '\n')


# initialize some objects for our dictionary
e1 = Employee()
e1.post_constructor('Jon', 1, 'HR', 'Hiring Manager')
e2 = Employee()
e2.post_constructor('Sara', 2, 'IT', 'Technology Intern')
e3 = Employee()
e3.post_constructor('J Bill', 3, 'Sales', 'Salesman')

employees = {e1.get_id(): e1, e2.get_id(): e2, e3.get_id(): e3}
# print(employees)

cntu = True
while cntu:
    print('Would you like to:\n\t1) look up an employee?\n\t2) add an employee?\n\t3) change an employee’s name department and/or job title?\n\t4) delete an employee?\n\t5) or exit?')
    x = int(input(''))
    if x == 5: cntu = False
    elif x == 1:    # search
        idnum = int(input('Enter the employee ID number: '))
        employees[idnum].display()
    elif x == 2:    # hire employee
        addE = Employee()
        addE.set_all()
        employees[addE.get_id()] = addE
        # print(employees)
    elif x == 3:    # transfer
        idnum = int(input('Enter the employee ID number of the employee getting transferred: '))
        employees[idnum].transfer()
        # employees[idnum].display()
    else:           # fire employee
        idnum = int(input('Enter the employee ID number of the employee getting fired: '))
        employees.pop(idnum)
        # print(employees)

    # pickle info ref: https://www.adamsmith.haus/python/answers/how-to-load-a-dictionary-from-a-file-with-pickle-in-python#:~:text=Use%20pickle.,the%20dictionary%20stored%20in%20it.
    # pickle saving
    file = open('p.txt', 'wb')
    pickle.dump(employees, file)
    file.close()
    # pickle reloading
    nfile = open('p.txt', 'rb')
    loaded_dict = pickle.load(nfile)
    print(loaded_dict)
    nfile.close()