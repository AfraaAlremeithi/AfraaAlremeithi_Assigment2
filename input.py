#this code asks the user for an input to create a ticket system for the museum
# it gathers the visitors input then create the ticket and displays the receipt.
from System import Artwork, Visitor, Ticket, Exhibition, SpecialEvent

name = input("\nEnter your name: ")
age = int(input("Enter your age: "))
nationality = input("Enter your nationality: ")

print("Visitor Categories: teacher, student, senior")
category = input("Enter your category (leave blank if not): ")

visitor = Visitor(name, age, nationality, category)

exhibition_name = "World Masterpiece"
Standard_price = 63 #got the Standard price from louvre website

ticket = Ticket(visitor, exhibition_name, Standard_price)
ticket.display_receipt()
