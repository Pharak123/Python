from calculation import my_calculator

    
choice = "y"
while choice != "n":
   
    print("**********Menu**********")
    print("1.Addition 2.Square 3.Exponential 4.Division 5.multiplication : ")
    my_calculator()
    choice = input("Do you want to continue (y/n): ").lower()
    if(choice == "n"):
        break

    