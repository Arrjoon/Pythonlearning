from src.Events import Events


class CharityEvent(Events):
    eventname = ''
    eventcode = ''
    eventTotalAvaibleSeat = 10
    eventType = ''


    def createEvent(self):
        self.eventType = "Charity"
        print("You are creating a Charity Event")
        self.eventname = input("Enter Event Name: ")
        self.eventcode = input("Enter Event Code: ")
        self.eventTotalAvaibleSeat = input("Enter Event Total Availble Seats: ")
        print("\n\n ------> Event Created!")
