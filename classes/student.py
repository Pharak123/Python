class Student():
    institute_name = 'cdac'
    @classmethod
    def change_institute_name(cls,institute_name):
        cls.institute_name = institute_name
    def __init__(self,in_name,in_rollno,in_suject_enroll,in_pocket_money):
        self.name= in_name
        self.roll = in_rollno
        self.subject = in_suject_enroll
        self.pocket_money = in_pocket_money
    
    def display_object_details(self):
        print(f'name:{self.name} roll No:{self.roll} Suject enroll:{self.subject} Pocket Money:{self.pocket_money} ')
    @staticmethod
    def display_facilities():
        print("I am static method , i do not need any class or object reference (first parameter)")        
def main():
    
    sanika = Student("sanika",6,"python",10)
    sanika.display_object_details()
    
    aboli = Student("Aboli",1,"Linux",20)
    aboli.display_object_details()
    
    print(" Class variable printed ")
    print(f" Before Sanika's institute: {sanika.institute_name}")
    print(f"Before Aboli's institute: {aboli.institute_name}")
    Student.change_institute_name("Sunbeam")
    print(f" After Sanika's institute: {sanika.institute_name}")
    print(f"After Aboli's institute: {aboli.institute_name}")
    
    Student.display_facilities()
    aboli.display_facilities()
    sanika.display_facilities()
   
    
    
    
main()