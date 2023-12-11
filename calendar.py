class Calendar:
    def __init__(self, name):
        self.name = name
        self.events = dict()
    
    def add_event(self, event):
        self.events[event.name] = event
    
    def delete_event(self, event_name):
        del self.events[event_name]
    
    def display_events(self):
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
        print("---------------------------------------")
    

class Event:
    def __init__(self, name, date, time=None, location=None, recurring=None):
        self.name = name
        self.date = date
        
        if (time!=None and time<1000):
            time_to_string = str(time)
            self.time = "0" + time_to_string
        else:
            self.time = time
        
        self.location = location
        self.recurring = recurring
    
if __name__ == "__main__":
        calendar1 = Calendar("To Do")
        calendar1.add_event(Event("Club Meeting", "12/11/2023", 1600, "Tawes"))
        calendar1.add_event(Event("Work", "12/11/2023", 900, "Work", "daily"))
        calendar1.add_event(Event("Homework", "12/13/2023", 1900, None, "weekly"))
        calendar1.display_events()
        calendar1.delete_event("Homework")
        print("\nAFTER DELETION:\n")
        calendar1.display_events()
        
        calendar2 = Calendar("Final Exams")
        calendar2.add_event(Event("Math Exam", "12/18/2023", 800, "Math building"))
        calendar2.add_event(Event("Physics Exam", "12/18/2023", 1330, "Physics building"))
        calendar2.add_event(Event("History Exam", "12/19/2023", 1600, "Online"))
        calendar2.display_events()
