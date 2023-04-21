
# Dictionary Exercise
def dict_display_capitals(capitals): 
    print(len(capitals))
     
def dict_add_element(capitals):
    key,value = input("Enter the like Afghanistan': 'Kabul : ").split(":")
    
    capitals.update({key.replace('"','').strip():value.replace('"','').strip()})
    print(capitals)
        
def dict_add_elements(capitals):
    user_input_capitals = dict_input_elements({})
    capitals.update(user_input_capitals)
    print(capitals)    
    
    
def dict_remove_element(capitals):
    print(capitals)
    capitals.pop(input("Enter the Country/state you want to delete?"))
    print(capitals)

def dict_input_elements(capitals):
    for dict_elem in input('for ex:  India : New Delhi , USA : Washington DC, Nepal : Kathmandu, Ukraine :  Kyiv \n').split(","):
        key,val = dict_elem.split(":")
        capitals[key.replace('"','').strip()] = val.replace('"','').strip()
    return capitals

def my_dict_store():
    print("\n Welcome to Our Dict Store !!! ")
    print("Please enter a list Comma seperated dictionary elements that you would want to perform Operation Upon")
	
    capitals= dict_input_elements({})
    # for dict_elem in input('for ex:  India : New Delhi , USA : Washington DC, Nepal : Kathmandu, Ukraine :  Kyiv \n').split(","):
    #     key,val = dict_elem.split(":")
    #     capitals[key.replace('"','').strip()] = val.replace('"','').strip()
     
    while(True):
        print("\n*************** Menu **********************")
        print("Operations supported by our program are :")
        print("    1: Display number of elements in the capitals collection")
        print('    2: Add an element to the capitals collection like --> Afghanistan: Kabul')
        print('    3: Add multiple elements to the capitals collection like -->  Albania:Tirana,Algeria:Algiers,Andorra:Andorra la Vella')
        print("    4: Remove an element from the collection 	")
        print("    5: Exit the Program ")
        choice = int(input("Please enter your choice "))
        
        if choice   ==1:
            dict_display_capitals(capitals) 
        elif choice ==2:
            dict_add_element(capitals)
        elif choice ==3:
            dict_add_elements(capitals)
        elif choice ==4:
            dict_remove_element(capitals) 
        elif choice ==5:
            break
        else:
            print("Invalid Input , Please Try Again !!!!  ")

my_dict_store()