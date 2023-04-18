'''1) Accept two numbers from the user and print 
a) addition 
b) first number squared 2 
c) first number raised to number second number'''

# my_number1 = int(input("Enter the first number"))
# my_number2 = int(input("Enter the second number"))

# print ("addition",my_number1 + my_number2)
# print ("Square is", my_number1**2)
# print ("first number raised to second number", my_number1**my_number2)

###########################################################################################
#Accept String from user and output upper case of the input string
# my_str = input("Enter the string") 
# print (my_str.upper())

#######################################################################################
# #3) Define a variable named "raise_salary_percentage" and get the salary raise 
# percentage from the user, Now apply the raise to an employee
# with harcoded data Name= 'gaurav' existing_salary = 900 INR and 
# print the incremented salary to the console
# raise_salary_percentage = int(input("Enter the percentage"))
# raise_percent = (raise_salary_percentage * 900)/100
# print ("Raise percent : ",raise_percent)
# print(raise_percent+900)

######################################################################################
# #4) Get the height from the user in cms and display the user height back to console
# in foot/feet and inches

# my_height = int(input("Enter the value in cms: "))
# in_inches=0.394*my_height
# in_feet=0.0328*my_height
# print("The length in inches is ")
# print(round(in_inches,2))
# print("The length in feet is")
# print(round(in_feet,2))

#################################################################################
# 5) Get the no of the dollars from the user apply the conversion of 
# 1 dollar = 82 rupees and print the amount to the console in rupees

# dollars = int(input("Enter the $ value : "))
# print ("Amount in Rupees : ",dollars*82)

##########################################################################
# 6) Take the source, destination, fare in INR, discount_rate percentage from the user and display the 
# string ex: "fare from mumbai to pune is 300 INR with has a discount of 5%"

# source = input("Enter the soruce city")
# destination = input("Enter the destination city")

# fare = int(input("Enter the amount"))
# discount_rate_percentage = int(input("Enter the discount rate percentage"))
# fare = fare -(fare*discount_rate_percentage/100)
# print (f"fare from {source} to {destination} is {fare} INR with has a discount of {discount_rate_percentage}%")



##########################################################################################################

#funtions with parameters and return statment
# def my_addtion(num1=10,num2=20):
#     return num1+num2
# def my_square(num1=4):
#     return num1**2
# def my_exponential(num1=2,num2=3):
#     return num1**num2
# def my_input():
#     num1,num2=int(input("Enter the First Number: ")),int(input("Enter the Second Number: "))
#     print("Addition : ",my_addtion(num1,num2))
#     print("SQuare : ",my_square(num1))
#     print("Exponential : ",my_exponential(num1,num2))
    
    
# my_input()  

# ##########################################################################################################
# #Accept String from user and output upper case of the input string
# def my_str_upper(string):
#     print(string.upper())

# str=input()
# my_str_upper(str)

# ##########################################################################################################
# def raise_salary_percentage(salary,percent):
#     return salary+((salary*percent)/100)

# def my_input():
#         salary,percent=int(input("Enter the Salary: ")),int(input("Enter the percent: "))
#         print("Amount",raise_salary_percentage(salary,percent))
        

# my_input()

##########################################################################################################
# Get the height from the user in cms and display the user height back to console
# # in foot/feet and inches

# def my_height_inches(height):
#     return round(0.394*height,2)

 
# def my_height_feet(height):
#     return round(0.0328*height,2)
# #height=int(input("Enter the height: "))
# print("Inches: ",my_height_inches(int(input("Enter the height: "))))
# print("Feet: ", my_height_feet(int(input("Enter the height: "))))

##########################################################################################################
# Get the no of the dollars from the user apply the conversion of 
# # 1 dollar = 82 rupees and print the amount to the console in rupees
# def dollar_conversion(value_in_rupees):
#     return value_in_rupees*82
# #value_in_rupees = int(input("Enter the value"))
# print("Amount in rupees:",dollar_conversion(int(input("Enter the value in $: "))))

##########################################################################################################
def fare_discount_rate_percent_cal(source,destination,fare,dis_rate_percent):
    print(f"fare from {source} to {destination} is {fare-(fare*dis_rate_percent/100)} INR with has a discount of {dis_rate_percent} %")



source=input("Enter the Source city: ")
destination=input("Enter the Destination city: ")
fare=int(input("Enter the fare amount: "))
dis_rate_percent=int(input("Enter the Percentage rate: "))

fare_discount_rate_percent_cal(source,destination,fare,dis_rate_percent)