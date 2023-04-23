# 1) Write a program that creates a dictionary like this 
# {
#     1: "red" , 2: "Blue" , 3: "Orange"
# }
# Now take the key as input from the user and print its corresponding colour 
# (Exception handle the code to terminate gracefully by printing 
# Colour not found if the key doesnot exists )

# class ColorNotFoundError(Exception):
#     pass
# try:
#     colors = {}
#     color_values = input("Enter the colors in comma seperated format e.g. red,blue,yellow:\n").split(",")
#     keys = list(range(1,len(color_values)+1))
#     for i in range(len(keys)):
#         colors[keys[i]] = color_values[i] 
#     color_key = int(input("Enter the key: "))
#     # for key,value in colors.items():
#     #     if color_value == value:
#     #         print("Color is exists")
#     #         break
#     # else:
#     #     raise  ColorNotFoundError()
#     if color_key in colors:
#         print(colors[color_key])
#     else:
#         raise ColorNotFoundError()

# except ColorNotFoundError:
#     print("Color does not exists in the dictionary!")


# finally:
#     print("This is finally block")
    
    
#################################################################################################

# 2) Write a program that creates a list of 5 elements of your choice 
# Now take the index that the user want the data of and print the value at that 
# location 
# Exception handle the code to  terminate gracefully by printing 
# Value not found if the index doesnot exists 
# list = ["red","pink","8","9","0","eee","7888","ioe"]
# class IndexNotFoundError(Exception):
#      pass
# try:
#     index = int(input("Enter the index to search in list: "))
#     if index<len(list):
#         print("Element is exists in the list",list[index])
#     else:
#         raise IndexNotFoundError()
# except IndexNotFoundError:
#     print("Index does not found!")
#################################################################################################

# 3) Create program that takes age of the user as input 
# and prints number of days that user has lived for 
# Exception handle the code such that if the user has lived for more than 
# 100001 days then user should get the message
# , you lived for so long , may be you will die soon:)
# class LiveMoreDays(Exception):
#     pass
# try:
#     age = int(input("Enter the Age : "))
#     number_of_days_present = age*365
#     if number_of_days_present > 100001:
#         raise LiveMoreDays()
# except LiveMoreDays:
#     print("you lived for so long, may be you will die soon")
     

#################################################################################################

#4) Complete the bits and pieces of the following below code
class negative_number_error(Exception):
    pass
class positive_number_error(Exception):
    pass
class homogenous_list_error(Exception):
    pass
class list_empty_error(Exception):
    pass
def create_positive_numbered_list(my_int_list1):
    positive_number = int(input("Enter the positive Number: "))
    if positive_number > 0:
        my_int_list1.append(positive_number)
        print(my_int_list1)
    else:
        raise negative_number_error()
    
    
      
def create_negative_numbered_list(my_int_list2):
    negative_number = int(input("Enter the Negative number:"))
    if negative_number < 0:
        my_int_list2.append(negative_number)   
        print(my_int_list2)
    else:
        raise positive_number_error()
    
    
def create_heterogenous_list(my_het_list3):
   
    for cntr in range(0,int(input("Please enter number of elements to the heterogenous list"))):
        print("1.Intger 2.str 3.float 4.dictionary 5.set 6.list 7.tupple")
        choice = int(input("enter the Choice type:"))
        datatype_choice = int(input("Please choose a datatype of the element to be added \
              \n 1) int \n 2) float \n 3) str \n 4) tuple \n 5) list \n 6) set \n 7) dictionary \n "))

        if datatype_choice == 1:
            my_het_list3.append(int(input("Please enter an integer to be added ")))
        if datatype_choice == 2:
            my_het_list3.append(float(input("Please enter a float to be added ")))
        if datatype_choice == 3:
            my_het_list3.append(input("Please enter a string to be added "))
        if datatype_choice == 4:
            my_het_list3.append(tuple(input("Please enter a tuple to be added like 1,2 ").split(",")))
        if datatype_choice == 5:
            my_het_list3.append(input("Please enter a list to be added like 1,2,3,4 ").split(","))
        if datatype_choice == 6:
            my_het_list3.append(set(input("Please enter a set to be added like 1,2 ").split(",")))
        if datatype_choice == 7:
            my_temp_tuple_list = []
            for str_elem in input("Please enter a dictionary to be added like key1:value1,key2:value2 ").split(","):
                my_temp_tuple_list.append(tuple(str_elem.split(":")))
            my_het_list3.append(dict(my_temp_tuple_list))
                
    if len(my_het_list3)==0:
            raise list_empty_error()       
        
    print(my_het_list3)   
        
    # check if we are have a homogenous list  
    is_heterogenous = False
    for subscript in range(1,len(my_het_list3)):
            if  type(my_het_list3[0]) != type(my_het_list3[subscript]):
                is_heterogenous = True
                break
            
    if not is_heterogenous:
            raise homogenous_list_error
    else:
            print("We received a Heterogenous list ")       
   
    
            
                
    
# def find_an_element(my_list):
#     if int(input("Enter the number to be search: ")) in my_list:
#         print("Element is exists in the list")
#         print(my_list)
    
def my_exception_store(): 
    my_int_list1=[]
    my_int_list2=[]
    my_het_list3=[]

    while(True):
        try:
            print("Welcome to my_exception_store !!!!")
            print("-------------------------------------")
            print("Following operations are supported :")
            print("1) Create a positive numbered list  ")
            print("2) Create a negative numbered list  ")
            print("3) Create a heterogenous list ")
            print("4) Check if the element is present in the list ")
            print("5) Refresh the program to start with blank lists")
            print("6) Exit  ")
            
            choice = int(input("Please enter your choice !!!! "))
            if choice ==1:
                create_positive_numbered_list(my_int_list1)
            elif choice ==2:
                create_negative_numbered_list(my_int_list2)
            elif choice ==3:
                create_heterogenous_list(my_het_list3)
            elif choice ==4:
                print("Lists created are as below \n ----------------------")
                print(f"1 : {my_int_list1}")
                print(f"2 : {my_int_list2}")
                print(f"3 : {my_het_list3}")
                
                # while True:
                #     check =int(input("Which of the below list you would want to search from "))
                    
                #     if  check == 1:
                #         find_an_element(my_int_list1)
                #         break
                #     elif check == 2:
                #         find_an_element(my_int_list2)
                #         break
                #     elif check ==3:
                #         find_an_element(my_het_list3)    
                #         break
                #     else:
                #         print("Please choose something from the above")
            elif choice ==5:
                my_int_list1.clear()
                my_int_list2.clear()
                my_het_list3.clear()
                print("Store restarted !!!! ")
            elif choice ==6:
                break
            else:
                print("Please choose something from the above")
        except negative_number_error:     
            print("We received a negative number in the list and I handled negative_number_error exception")
            my_int_list1.clear()
        except positive_number_error:     
            print("We received a positive number in the list and I handled positive_number_error exception")
            my_int_list2.clear()
        except homogenous_list_error:    
            print("We received a Homogenous list and I handled homogenous_list_error exception")
            my_het_list3.clear()
        except list_empty_error:
            print("List is empty")
            
            
my_exception_store()   
