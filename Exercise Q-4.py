def list_display_members(members):
    print(members)

def list_add_element(members):

    members.append(input("Enter the Name : "))

def list_add_elements(members):
    members.extend(input("Enter the Name : ").split(","))
    
    
def list_remove_element(members):
    #members.remove(input("Enter the Name which you  want Remove: "))
    #subscript using index
    members.pop(int(input("Enter the Name which you index no want Remove: ")))

def remove_last_element(members):
    members.pop()
    
def display_3_4_5_element(members):
    if len(members)<=5:
        print("please enter more names to display 3rd 4rth 5th indexes: .")
        list_add_elements(members)
    else:
       
        list_display_members(members[2:5])

def my_list_restore():
    print("\n Welcome to our List Store!!!!")
    print("Please enter a list Comma seperated that you would want to perform")
    members = input('for ex:Sanika,Aboli,Shradha,Ruchi,Manjiri,etc.\n').split(",")
    while(True):
        print("\n*********************Menu*****************")
        print("Operations supported by our program are :")
        print("  1:  Display number of elements in the members list")
        print("  2:  Add an element to the members collection like 'Sehwag' ")
        print("  3:  Add elements to the members collection like ['David','Bret','Sanju']")
        print("  4:  Remove a member from the collection at a given subscript")
        print("  5:  Remove the last member from the collection ")
        print("  6:  Display third, fourth and fifth element from the collection ")
        print("  7: Exit the Program ")
        choice = int(input("Please enter your choice "))
        
        if choice==1:
            list_display_members(members)
        elif choice==2:
            list_add_element(members)  
        elif choice==3:
            list_add_elements(members)
        elif choice==4:
            list_remove_element(members) 
        elif choice ==5:
            remove_last_element(members) 
        elif choice==6:
            display_3_4_5_element(members) 
        elif choice ==7:
            break
        else:
            print("Invalid Input , Please Try Again !!!!  ")
            
            
my_list_restore()