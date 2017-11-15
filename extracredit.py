import pickle

class employee:

    def __init__(self, name, id_num, depart, title):
        self.name = name
        self.id_num = id_num
        self.depart = depart
        self.title = title

    def name(self):
        return self.name()

    def id_num(self):
        return self.id_num()

    def depart(self):
        return self.depart()

    def title(self):
        return self.title()

    def print_employee(name, id_num, depart, title):
        print('\nName              ID Number    Department        Job Title')
        print('%-17s %-12d %-17s %s' % (
    name, id_num, depart, title))

while True:
    try:
        employees = pickle.load( open('test.p','rb'))
        break
    except FileNotFoundError:
        employees = {}
        break

while True:
    print('\nEmployee Menu')
    print('1-look up employee by ID')
    print('2-add a new employee')
    print('3-change employee name, department, and title')
    print('4-delete an employee')
    print('0-quit')
    option = input('\nEnter your choice: ')
    if option == '1':
        idnum = int(input('Enter employee ID Number: '))
        employee.print_employee(
            employees[idnum][0], idnum, employees[idnum][1], employees[idnum][2])
    elif option == '2':
        employees[int(input('Enter employee ID number: '))] = [
            input('Enter employee name: '),
            input('Enter employee Department: '),
            input('Enter employee Title: ')]
    elif option == '3':
        idnum = int(input('Enter employee ID number: '))
        employees[idnum] = [
            input('Change employee name: '),
            input('Change employee Department: '),
            input('Change employee Title: ')]
    elif option == '4':
        del employees[int(input('Enter employee ID number to delete: '))]
    elif option == '0':
        break

pickle.dump(employees,open('test.p','wb'))                
