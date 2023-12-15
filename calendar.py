class Calendar:
    def __init__(self, name):
        self.name = name
        self.events = dict()
    
    def add_event(self, event):
        self.events[event.name] = event
    
    def delete_event(self, event_name):
        del self.events[event_name]
    
    def display_events(self):
        print("--------------------------------")
        print(self.name + ": \n")
        for event in self.events:
            event = self.events[event]
            print("Event name: " + event.name)
            print("Date: " + event.date)
            
            if (event.time==None):
                print("Time: All day")
            else:
                print("Time: " + str(event.time))
            
            if (event.location==None):
                print("Location: None")
            else:
                print("Location: " + event.location)
            
            if (event.recurring==None):
                print("Recurring: Never")
            else:
                print("Recurring: " + event.recurring)
            print()
        
    

class Event:
    def __init__(self, details):
        details = details.split(', ')

        self.name = details[0]
        self.date = details[1]

        if details[2] != "None":
            print(details[2]+"a")
            time = details[2]
            if (int(time)<1000):
                self.time = "0" + time
        else:
            self.time = details[2]
        
        self.location = details[3]
        
        self.recurring = details[4]


def get_user_input():

    while True:

        name = input("Enter calendar name: ")

        if name:

            return Calendar(name)

        else:

            print("Invalid input. Please enter a name for the calendar.")

if __name__ == "__main__":
    calendars = []

    while True:
        print("================================")
        print("1. Create Calendar")
        print("2. Add Event")
        print("3. Delete Event")
        print("4. Display Events")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            calendars.append(get_user_input())

        elif choice == '2':
            if not calendars:
                print("Please create a calendar first.")

            else:
                calendar_name = input("Enter calendar name to add event: ")
                calendar = next((cal for cal in calendars if cal.name == calendar_name), None)

                if calendar:
                    event = Event(input("Enter event details (name, date, time(None), location(None), recurring(None) ): "))
                    calendar.add_event(event)
                    print("Event added successfully.")

                else:

                    print(f"Calendar '{calendar_name}' not found.")

        elif choice == '3':
            if not calendars:
                print("Please create a calendar first.")

            else:
                calendar_name = input("Enter calendar name to delete event: ")
                calendar = next((cal for cal in calendars if cal.name == calendar_name), None)

                if calendar:
                    event_name = input("Enter event name to delete: ")
                    calendar.delete_event(event_name)

                else:
                    print(f"Calendar '{calendar_name}' not found.")

        elif choice == '4':
            if not calendars:
                print("Please create a calendar first.")

            else:
                calendar_name = input("Enter calendar name to display events: ")
                calendar = next((cal for cal in calendars if cal.name == calendar_name), None)

                if calendar:
                    if calendar.events:
                        for calendar in calendars:
                            calendar.display_events()
                    else: 
                        print("No events to display")

                else: 
                    print(f"Calendar '{calendar_name}' not found.")

        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
