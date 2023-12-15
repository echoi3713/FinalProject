"""Script for Calendar Event Planning Program
    """
import datetime
import calendar


#global variables for iteration use within classes
months = ["January","Febuary","March","April","May","June"
,"July","August","September","October","November","December"]

days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]


class Event:
    """Event class that holds all event details and method used to display details
    """
    def __init__(self, name, date, time, location, details):
        self.name = name
        self.date = date
        self.time = time
        self.location = location
        self.details = details

    def __repr__(self) -> str:
        print(f"Event name: {self.name} ")
        print(f"Date: {self.date} ")
        print(f"Time: {self.time} ")
        print(f"Location: {self.location} ")
        print(f"Details: {self.details} ")


class Eventplanner:
    """Eventplanner class that holds, adds, and switches calendars
    """
    def __init__(self, name):

        self.name = name

        self.calendars = []
    
    def add_calendars(self,calendar):
        if isinstance(calendar, Calendar): 
            self.calendars.append(calendar)
        
        else: 
            print("Invalid Object")
    
    def new_calendar(self):
        
        print("Which Month are you planning in? \n")
        print("0: January")
        print("1: Febuary")
        print("2: March")
        print("3: April")
        print("4: May")
        print("5: June")
        print("6: July")
        print("7: August")
        print("8: September")
        print("9: October")
        print("10: November")
        print("11: December")

        selection2 = input("Enter your selection: (1-11): ")
        
        #checking if month selected already exists within self.calendars
        for c in self.calendars:
            if c.monthindex == selection2:
                print("Calendar already exists!")
                main(self)

        self.add_calendars(Calendar(selection2))
        
        #matches the calendars correct month index after being appended to self.calendars to enter through main loop
        for c in self.calendars:
            if c.monthindex == selection2:
                m = self.calendars.index(c)

        main(self, int(m))
    
    def switch_calendar(self):
        print("Choose a Calendar:")

        counter = 0
        picklist = []
        #Displays all calendars in self.calendar to choose which to switch to
        for c in self.calendars:
            print(f"{counter}. Calendar for month '{c.month}'")
            picklist.append(c)
            counter += 1
        
        pick = input(f"Enter your selection (0-{counter-1}): ")
        
        #matches index of selection to enter through main loop 
        for p in picklist:
            if picklist.index(p) == int(pick):
                n = picklist.index(p)

        main(self,int(n))


class Calendar:
    """Calendar class, creates calendar matrix (monthplanner) upon creation,
    holds events for respective month, adds and deletes events, and contains
    month name and index for interation and identification
    """
    def __init__(self, month): 

        self.events = []
        self.monthplanner = []
        self.monthindex = month
        self.month = months[int(month)]
        
        #use calendar and datetime to retrieve a matrix model of calendar
        planner = calendar.monthcalendar(datetime.datetime.now().year+1,(int(self.monthindex) + 1))
        
        #cleans up matrix model removing zeroes and sorting into dictionary by weeks and day of/date 
        weeks = 0
        for w in planner:
            counter = 0
            self.monthplanner.append({})
            for wd in w:
                week = {}
                
                if wd == 1:
                    week[days[counter]] = wd
                    self.monthplanner[weeks].update(week)
                
                if wd > 1:
                    week[days[counter]] = wd
                    self.monthplanner[weeks].update(week)

                counter +=1
            
            weeks += 1
    
    def add_event(self):
        name = input("What's the name for this Event? ")
        date = input("Enter a date for an Event: ")
        time = input("Now enter a time ")
        location = input("Where will this Event take place? ")
        details = input("Additional details: ")

        self.events.append(Event(name,date,time,location,details))

    def delete_event(self):
        if not self.events:
            print("No Events found!")
            return
        else:
            print("Which event would you like to delete?")
        counter = 0
        picklist = []
        for event in self.events:
            print(f"{counter}. Event named '{event.name}'")
            picklist.append(event)
            counter += 1
        
        pick = input(f"Enter your selection (0-{counter-1}): ")

        del self.events[int(pick)]

    def view_events(self):
        if not self.events:
            print("No Events found!")
            return
        else:
            print("Which event would you like to view?")
        counter = 0
        picklist = []
        for event in self.events:
            print(f"{counter}. Event named '{event.name}'")
            picklist.append(event)
            counter += 1
        
        pick = input(f"Enter your selection (0-{counter-1}): ")
        
        self.events[int(pick)].__repr__()


def main(planner,month=0):
    """Main loop used as main menu and to reach methods and make decisions

    Args:
        planner (EventPlanner Class): The initial eventplanner created will be reused 
        month (int, optional): initially will be zero but will be replaced with proper index after planner.new_calendar()
        most actions in main are used from planner methods or planner.calendar methods 
    """
    
    print(f"\nWelcome to Event Planner '{planner.name}'")
    print(f"Current Calendar month: {planner.calendars[month].month}")
    print("================================")
    
    while True:
        print("\n1: Switch/Create Calendar")
        print("2: View Calendar Matrix")
        print("3: Add Event")
        print("4: Delete Event")
        print("5: Display Events")
        print("6: Exit")

        choice = input("Enter your selection (1-6): ")

        if choice == '1':
            if len(planner.calendars) == 1:
                print("\nNo other Calendars found. Creating a Calendar..")
                print("================================")
                planner.new_calendar()
            else:
                print("1: Switch Calendar")
                print("2: Create Calendar")
                pick = input("Enter your selection: (1-2): ")
                if pick == '1':
                    planner.switch_calendar()
                else:
                    planner.new_calendar()
    
        if choice == '2':
            print(planner.calendars[month].monthplanner)

            print(f"\nThere are {len(planner.calendars[month].monthplanner)} weeks in the month of {planner.calendars[month].month} ")
            cont = input("\nEnter 'Y' when ready to continue...")
            if cont == 'Y':
                pass
            else:
                pass

        if choice == '3':
            planner.calendars[month].add_event()
            print("Event Successfully added.")
            cont = input("\nEnter 'Y' when ready to continue...")
            if cont == 'Y':
                pass
            else:
                pass

        if choice == '4':
            planner.calendars[month].delete_event()
            print("Event Successfully deleted.")
            cont = input("\nEnter 'Y' when ready to continue...")
            if cont == 'Y':
                pass
            else:
                pass

        if choice == '5':
            planner.calendars[month].view_events()
            cont = input("\nEnter 'Y' when ready to continue...")
            if cont == 'Y':
                pass
            else:
                pass
            
        if choice == '6':
            print("Exiting the program. Goodbye!")
            quit()



if __name__ == "__main__":
        
    print("Welcome to the Event Planner Program for 2024! \n")
    print ("1: Open Event Planner") 
    print("2: Close Program")  
        
    selection = input("Enter your selection: (1-2): ")

        
    if selection == "1":
        title = input("Name your Event Planner: ")
        planner = Eventplanner(title)
            
            
        
    else:
        print("Goodbye!")
        quit()

    planner.new_calendar()
