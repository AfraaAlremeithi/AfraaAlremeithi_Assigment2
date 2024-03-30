from datetime import datetime

class Artwork:
    def __init__(self, title, artist, date_ofCreation, description):
        self.title = title
        self.artist = artist
        self.date_ofCreation = date_ofCreation
        self.description = description
        self.exhibt_Location = None

class Exhibition:
    def __init__(self, title, duration, location):
        self.title = title
        self.duration = duration
        self.location = location
        self.artworks = []

    def add_artwork(self, artwork: Artwork):
        self.artworks.append(artwork)

class Visitor:
    def __init__(self, name, age, idNumber):
        self.name = name
        self.age = age
        self.idNumber = idNumber
        self.tickets = []

    def purchase_ticket(self, ticket):
        self.tickets.append(ticket)

class Ticket:
    def __init__(self, visitor, event, price):
        self.visitor = visitor
        self.event = event
        self.price = price

    def display_receipt(self):
        print("visitor name:", self.visitor.name)
        print("event title:", self.event.title)
        print("ticket price:", self.price)

class Event:
    def __init__(self, title, duration, location, ticketPrice):
        self.title = title
        self.duration = duration
        self.location = location
        self.ticketPrice = ticketPrice

class Payment:
    def __init__(self, amount, method):
        self.amount = amount
        self.method = method
        self.time = datetime.now()
