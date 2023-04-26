
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

class Person:
    def __init__(self,name,place_of_residence) -> None:
        
       self.name = name
       self.place_of_residence = place_of_residence
       
    def display_attributes_person(self):
        print(f"Name : {self.name}\nPlace of residence: {self.place_of_residence}")
# def main(): #for class person
#     person = Person("sanika","pune")
#     person.display_attributes()
# main()

class Sister(Person):
    
    def __init__(self,name,place_of_residence,exam_subjects) -> None:
        super().__init__(name,place_of_residence)
        self.exam_subjects = exam_subjects
    
    def display_attributes_sister(self):
        super().display_attributes_person()
        print(f"Exam subjects: {self.exam_subjects}")
    
    
class Uncle(Person):
    def __init__(self, name, place_of_residence,business) -> None:
        super().__init__(name, place_of_residence)
        self.business = business    
    
    def display_attributes_uncle(self):
        super().display_attributes_person()
        print(f"Business: {self.business}")
    
def main():
    sister = Sister("sanika","pune","Python")
    uncle = Uncle("aboli","pune","Computer Engineer Sales")
    print("For Sister:-------------------")
    sister.display_attributes_sister()
    print("For Uncle:--------------------- ")
    uncle.display_attributes_uncle()
        
main()
       
 
