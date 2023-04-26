class Employee:
    
    department_name = "Networking"
    
    
    
    @classmethod #can be accessible by class name and objects but generally use classname
    def get_department_name(cls,department_name):
        cls.department_name = department_name        
    
    def __init__(self,emp_id,mgr_id):
        
        self.emp_id = emp_id
        #self.emp_salary = emp_salary
        self.mgr_id = mgr_id    
    
    
    @staticmethod #ca be accessible by class name,objects
    def field_expertise():
        print("Expertise for employees ")
        
    
    #can be accessible by objects/instance because get_emp_salary(),set_emp_salary(),display() are instance methods
    
    def get_emp_salary(self): 
        return int(input("Enter the Employee Salary: "))
        
    def set_emp_salary(self,emp_salary): 
        self.emp_salary = emp_salary
        
        
    def display(self):    
        print(f"Employee id:{self.emp_id} Employee salary:{self.emp_salary} Employee's Manager id: {self.mgr_id} Department Name: {Employee.department_name}")
            
def main():
    employee1 = Employee(11,203)        #instance creation
    salary1 = employee1.get_emp_salary() #get salary for emp1
    employee1.set_emp_salary(salary1) #set salary for emp1
    employee1.display() #display info for emp1
    
    employee2 = Employee(2,303) #instance creation
    salary2 = employee2.get_emp_salary() #get salary for emp2
    employee2.set_emp_salary(salary2) #set salary for emp2
    employee2.display() #display nfo for emp2
    
    
    dep_name = input("Enter the Department name: ") #department name is class variable and get_department_name is class method
    # employee1.get_department_name(dep_name)
    # employee2.get_department_name(dep_name)
    Employee.get_department_name(dep_name)
    
    employee1.display() #display info for emp1
    employee2.display() #display info for emp2
    
    
    Employee.field_expertise()    
    
    #optional but not recommanded
    print(f'Name: {employee1.emp_id}')
    
    
    
    
    
    
    
    
    








main()