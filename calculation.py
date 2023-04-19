#invoked file

def my_addtion(num1=10,num2=20):
    return num1+num2
def my_square(num1=4):
    return num1**2
def my_exponential(num1=2,num2=3):
    return num1**num2

    return num1**num2
def my_division(num1=2,num2=3):
    return num1/num2
def my_multiplication(num1=3,num2=6):
    return num1*num2

def accept_user():
    return int(input("please enter the number :"))

def my_calculator():
    
    option= int(input("Enter Your Option: "))
    
    if(option == 1):
        #first_num = int(input("Please Enter first number: "))
        #second_num = int(input("Please Enter second number: "))
        # print("Addtion:",my_addtion(first_num,second_num))
        print("Addtion:",my_addtion(accept_user(),accept_user()))

    elif(option == 2):
        # first_num = int(input("Please Enter first number: "))
        
        #print("Sqaure:",my_square(first_num))
        print("Square:",my_square(accept_user()))
    elif(option == 3):
        # first_num = int(input("Please Enter first number: "))
        # second_num = int(input("Please Enter second number: "))
        # print("Exponential: ",my_exponential(first_num,second_num))
        print("Exponential:",my_exponential(accept_user(),accept_user()))
    elif(option == 4):
        print("Division: ",my_division(accept_user(),accept_user()))
    elif(option == 5):
        print("Multiplication:",my_multiplication(accept_user(),accept_user()))
    else:
        print("Invalid Choice")
    

def my_input(num1,num2):
    #num1,num2=int(input("Enter the First Number: ")),int(input("Enter the Second Number: "))
    print("Addition : ",my_addtion(num1,num2))
    print("SQuare : ",my_square(num1))
    print("Exponential : ",my_exponential(num1,num2))
    
def my_str_upper(string):
    #print(string.upper())
    return string.upper()

def raise_salary_percentage(salary,percent):
    return salary+((salary*percent)/100)



def my_height_inches(height):
    return round(0.394*height,2)

 
def my_height_feet(height):
    return round(0.0328*height,2)
#height=int(input("Enter the height: "))
# print("Inches: ",my_height_inches(int(input("Enter the height: "))))
# print("Feet: ", my_height_feet(int(input("Enter the height: "))))


def dollar_conversion(value_in_rupees):
    return value_in_rupees*82
# print("Amount in rupees:",dollar_conversion(int(input("Enter the value in $: "))))

def fare_discount_rate_percent_cal(source,destination,fare,dis_rate_percent):
    #print(f"fare from {source} to {destination} is {fare-(fare*dis_rate_percent/100)} INR with has a discount of {dis_rate_percent} %")
    return f"fare from {source} to {destination} is {fare-(fare*dis_rate_percent/100)} INR with has a discount of {dis_rate_percent} %"

# def my_fare():
#     source=input("Enter the Source city: ")
#     destination=input("Enter the Destination city: ")
#     fare=int(input("Enter the fare amount: "))
#     dis_rate_percent=int(input("Enter the Percentage rate: "))

#     fare_discount_rate_percent_cal(source,destination,fare,dis_rate_percent)

def my_print(fare_messg):
    print("You are genius!!!")
   
    print(fare_messg)
    
    

