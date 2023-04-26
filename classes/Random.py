
# -------------------------------------------
# Exercise 02 : Classes and objects -- try creating this in oops world
# -------------------------------------------
 
# Create a class that captures airline tickets. 
# Each ticket lists the departure and arrival cities, a flight number, and a seat assignment. 
# A seat assignment has both a row and a letter for the seat within the row (such as 12F). 

# main method:
# Make two examples of tickets being sold to passengers.
# display tickets booked details 
#Hierarchical inheritence

import random
class AirlineTicket:
    cities = {'pune','mumbai','hydrabad','tiruanatpuram','nashik','kochi','banglore'}
    
    flight_number = set(range(1,999))
    row_letter = {'a','b','c','d','e','f','g'}
    # random.shuffle(row_letter)
    
    seat_assignment = str(random.randint(1,99))+row_letter.pop()
    
    
    def __init__(self,departure_city=None,arrival_city=None,flight_number=None,seat_assignment=None):
        self.departure_city = self.cities.pop() if departure_city is None else departure_city
        self.arrival_city = self.cities.pop() if arrival_city is None else arrival_city
        self.flight_number = self.flight_number.pop() if flight_number is None else flight_number
        self.seat_assignment = self.seat_assignment if seat_assignment is None else seat_assignment

 
    def display_tickets(self):
        
        print(f"Departure city: {self.departure_city} \nArrival city: {self.arrival_city}\n Flight number: {self.flight_number} \n Seat assignment: {self.seat_assignment}")
    
    @staticmethod
    def ticket_booking_details():
        print("**********Ticket***********")
        print("Ticket booking details: ")
        print("**************************")
        
def main():
    # print("Enter for passenger 1: ")
    # departure_city = input("Enter the Departure City: ")
    # arrival_city = input("Enter the Arrival city: ")
    # flight_number = input("Enter the Flight number: ")
    # row_number = input("Enter the seat row number : ")
    # row_letter = input("Enter the row letter for row number: ")
    # seat_assignment = row_number+row_letter
    # passenger1 = AirlineTicket()
    # print("\nEnter for passenger 2: ")
    # departure_city = input("Enter the Departure City: ")
    # arrival_city = input("Enter the Arrival city: ")
    # flight_number = input("Enter the Flight number: ")
    # row_number = input("Enter the seat row number : ")
    # row_letter = input("Enter the row letter for row number: ")
    # seat_assignment = row_number+row_letter
    # passenger2 = AirlineTicket()
    number_of_passengers = int(input("Enter the number of passengers: "))
    passenger = []
    
    for i in range(0,number_of_passengers):
        if input("You want user defined then press 'Y':") == 'Y':
                print(f"Enter for passenger {i}: ")
                departure_city = input("Enter the Departure City: ")
                arrival_city = input("Enter the Arrival city: ")
                flight_number = input("Enter the Flight number: ")
                row_number = input("Enter the seat row number : ")
                row_letter = input("Enter the row letter for row number: ")
                seat_assignment = row_number+row_letter
                passenger.append(AirlineTicket(departure_city,arrival_city,flight_number,seat_assignment))
        else:
            
                print(f"Automatically Ticket is Generated for passenger {i}")
                passenger.append(AirlineTicket())
        
    AirlineTicket.ticket_booking_details()
    for i in range(number_of_passengers):
        print("-------------------------")
        print(f"Passenger {i}: ")    
        passenger[i].display_tickets()
        print("-----------------------")
        

main()