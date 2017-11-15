master_list = []
class Employee:
    def __init__(self, name, ID_number, Department, Job_Title):
        self.idnumber = ID_number
        self.name = name
        self.department = Department
        self.job_title = Job_Title
        
    def append(name,idnumber,department,job):
        tmp_list = []
        
        tmp_list.append(name)
        tmp_list.append(idnumber)
        tmp_list.append(department)
        tmp_list.append(job)
        
        master_list.append(tmp_list)

while True:
    
    emp = Employee(input('Please Enter Employee Name\n'),
                   input('Please Enter Employee ID Number:\n'),
                   input('Please Enter The Department:\n'),
                   input('Please Enter The Job Title:\n'))
    
    Employee.append(emp.name, emp.idnumber, emp.department,emp.job_title)
    




    
    chocice = input('Would you like to enter another Employee?[y,n]\n')
    if chocice == 'n':
        break
    
for (s,n,v,c) in master_list:
    print("Name: %s\nID_Number: %s\nDepartment: %s\nJob Title: %s\n" % (s,n,v,c))
