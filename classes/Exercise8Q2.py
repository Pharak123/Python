
# -------------------------------------------
# Exercise 02 : Classes and objects -- try creating this in oops world
# -------------------------------------------
 
# Create a class that captures airline tickets. 
# Each ticket lists the departure and arrival cities, a flight number, and a seat assignment. 
# A seat assignment has both a row and a letter for the seat within the row (such as 12F). 

# main method:
# Make two examples of tickets being sold to passengers.
# display tickets booked details 


class AirlineTicket:
    
    def __init__(self,departure_city,arrival_city,flight_number,seat_assignment):
        self.departure_city = departure_city
        self.arrival_city = arrival_city
        self.flight_number = flight_number
        self.seat_assignment = seat_assignment
    
 
    def display_tickets(self):
        
        print(f"Departure city: {self.departure_city} \nArrival city: {self.arrival_city}\n Flight number: {self.flight_number} \n Seat assignment: {self.seat_assignment}")
    
    @staticmethod
    def ticket_booking_details():
        print("**********Ticket***********")
        print("Ticket booking details: ")
        print("**************************")
        
def main():
    print("Enter for passenger 1: ")
    departure_city = input("Enter the Departure City: ")
    arrival_city = input("Enter the Arrival city: ")
    flight_number = input("Enter the Flight number: ")
    row_number = input("Enter the seat row number : ")
    row_letter = input("Enter the row letter for row number: ")
    seat_assignment = row_number+row_letter
    passenger1 = AirlineTicket(departure_city,arrival_city,flight_number,seat_assignment)
    print("\nEnter for passenger 2: ")
    departure_city = input("Enter the Departure City: ")
    arrival_city = input("Enter the Arrival city: ")
    flight_number = input("Enter the Flight number: ")
    row_number = input("Enter the seat row number : ")
    row_letter = input("Enter the row letter for row number: ")
    seat_assignment = row_number+row_letter
    passenger2 = AirlineTicket(departure_city,arrival_city,flight_number,seat_assignment)
    
    
    
    AirlineTicket.ticket_booking_details()
    print("Passenger 1: ")    
    passenger1.display_tickets()
    print("-----------------------")
    print("passenger 2:")
    passenger2.display_tickets()
    print("-------------------------")

main()