
'''
----- Inheritance exercise ----
1. Define  
  Person (superclass) that has name , place_of_residence , display_attributes()
  Sister (subclass of Person)  that has additionally exam_subjects , display_attributes()
  Uncle (subclass of Person)  that has additionally business , display_attributes()

main method:
create a sister class object and display its attributes 
create a Uncle class object and display its attributes 
'''
class car: #base class for person
    def __init__(self,car_name,car_model) -> None:
        self.car_name = car_name
        self.car_model = car_model
    
    def display_attributes(self):
        print(f"CarName : {self.car_name}\nCarmodel: {self.car_model}")
    

class Person(car): #child/derived class from person
    def __init__(self,car_name,car_model,name,place_of_residence) -> None:
       super().__init__(car_name,car_model)
       self.name = name
       self.place_of_residence = place_of_residence
       
    def display_attributes(self):
        super().display_attributes()
        print(f"Name : {self.name}\nPlace of residence: {self.place_of_residence}")
# def main(): #for class person
#     person = Person("sanika","pune")
#     person.display_attributes()
# main()

class Sister(Person):
    
    def __init__(self,name,car_name,car_model,place_of_residence,exam_subjects) -> None:
        super().__init__(car_name,car_model,name,place_of_residence)
        self.exam_subjects = exam_subjects
    
    def display_attributes(self):
        super().display_attributes()
        print(f"Exam subjects: {self.exam_subjects}")
    
    
class Uncle(Person):
    def __init__(self,car_name,car_model,name, place_of_residence,business) -> None:
        super().__init__(car_name,car_model,name, place_of_residence)
        self.business = business    
    
    def display_attributes(self):
        super().display_attributes()
        print(f"Business: {self.business}")
    
def main():
    person = Person("tata","89FFF","ruchi","pune")
    sister = Sister("hundai","56Ggg","sanika","pune","Python")
    uncle = Uncle("vista","56TTT","aboli","pune","Computer Engineer Sales")
    print("For Person:-------------------")
    person.display_attributes()
    print("For Sister:-------------------")
    sister.display_attributes()
    print("For Uncle:--------------------- ")
    uncle.display_attributes()
        
main()
       
 
