my_addtion = lambda first_number,second_number: first_number+second_number
    
my_square = lambda first_number,second_number=None:first_number*first_number
my_exponential = lambda first_number,second_number:first_number**second_number
my_division = lambda first_number,second_number:first_number/second_number
my_multiplication = lambda first_number,second_number:first_number*second_number
class Calculator:
    @staticmethod
    def my_addition(first_number,second_number):
        return lambda first_number,second_number: first_number+second_number
    # def my_addtion(num1=10,num2=20):
    #     return num1+num2
    # def my_square(num1=4,num2=1):
    #     return num1**2
    # def my_exponential(num1=2,num2=3):
    #     return num1**num2
    # def my_division(num1=2,num2=3):
    #     return num1/num2
    # def my_multiplication(num1=3,num2=6):
    #     return num1*num2
    @staticmethod
    def accept_user():
        return int(input("please enter the number :"))

    def __init__(self,option) -> None:
        self.option = option

    @staticmethod
    def my_calculator(func_operation,num1,num2):   
        return func_operation(num1,num2)

    def main(self):
        
       
        my_invo_dict = {1:self.my_addition,2:my_square,3:my_exponential,4:my_division,5:my_multiplication}
        if self.option==2:
            print("square: ",end=' ')
            result = self.my_calculator(my_invo_dict.get(self.option),self.accept_user())
            print(result)
        else:
            
            result = self.my_calculator(my_invo_dict.get(self.option),self.accept_user(),self.accept_user())
            print('Addition: 'if self.option==1 else 'exponential' if self.option==3 else 'Division' if self.option==4 else 'multiply',end=' ')
            print(result)
        # if option==1:
        #     print("Addition:",my_calculator(my_addtion,accept_user(),accept_user()))
        
        # elif option==2:
        #     print("my_square:",my_calculator(my_square,accept_user()))
            
        # elif option==3:
        #     print("my_exponential:",my_calculator(my_exponential,accept_user(),accept_user()))
        
        # elif option==4:
        #     print("my_division:",my_calculator(my_division,accept_user(),accept_user()))
        
        # elif option==5:
        #     print("my_multiplication:",my_calculator(my_multiplication,accept_user(),accept_user()))    



  
choice = "y"
while choice != "n":
     
    print("**********Menu**********")
    print("1.Addition 2.Square 3.Exponential 4.Division 5.multiplication : ")
    option= int(input("Enter Your Option: "))
    cal = Calculator(option)
    cal.main()
    choice = input("Do you want to continue (y/n): ").lower()
    if(choice == "n"):
        break

# print("Addition:",my_calculator(my_addtion,accept_user(),accept_user()))