
from datetime import datetime
import random

"""This class represents an event that the user can add.

Attributes:
    name (str): name of the event
    date (str): date of the event
    time (int): time of the event
    location (str): location of the event
    repeats (str): how often the event repeats
    alerts (boolean): whether alerts are on or off for the event    
"""

class Event:
    def __init__(self,name,date,time=None, location=None,repeats=None, alerts=False):
        self.name = name
        self.date = self.validate_date(date)
        self.time = self.validate_time(time)
        self.location = location
        self.repeats = repeats
        self.alerts = alerts

    """This method validates if the date is in the correct format.

    Arguments:
        date (str): date of event
    """
    def validate_date(self,date):

        try: 
            datetime.strptime(date, '%m/%d,%Y')
            #Validate date format ( two digit for month,day,and four digit for years)
            parts = date.split('/')
            if len(parts) == 3 and len(parts [0]) == 2 and len(parts[1]) == 2 and len(parts[2]) == 4:
               in(parts [0]), int(parts[1]), int(part[2])
                return date
            else: 
                raise ValueError("Date format should be MM/DD/YYYY")
        except ValueError:
            raise ValueError("Date format should be MM/DD/YYYY")

    
    """This method validates if the time is in the correct format.
    
    Arguments:
        time (str): Time of event
    """
    def validate_time(self, time):
        if time is None:
            return None
        try:
            # Validate military time
            datetime.strptime(time, '%H%M')
            return time
        except ValueError:
            raise ValueError("Time format should be in HM, i.e 1830")


"""This class represents the calendar that the user will access and modify.

Attributes:
    name (str): name of the calendar
    events (dict): a dictionary of events the user has added
"""
class Planner:
    def __init__(self,name):
        self.name = name
        self.events = dict()

    
    def add_event(self, event):
    """This method allows the user to add events

    Arguments:
        name (str): name of the calendar 
        event (Event): an event the user will add
    """
        self.events.append(event)


    """This method allows the user to view their events

    Arguments:
        event (Event): an event the user will add
    """
    def view_events(self):
        if not self.events:
            print("No events found")
        else:
            print("Upcoming events: ")

        for event in self.events:
            print("==========================")
            print("Title: ", event.title)
            print("Location: ", event.location)
            print("Date: ", event.date)
            print()


    """This method allows the user to delete their events
            
    Arguments:    
        name (str): name of the event
        event (Event): an event will add

    """
    def delete_events(self,name,event name):
    
         if self.name == name:
             for idx, event in enumerate(self.events):
                 if event.name == event_name: 
                     del self.events[idx]
                     break


if __name__ == "__main__""
   calender = Calendar("My Calender")

    event_to_delete = None
    for i in range(5):
        event_name = "Event# " + str(random.randint(1, 10))
        new_event = Event(name=event_name, date="01/01/2024", time="1830", location="Some Location", repeats="weekly", alerts=True)
        calender.add_event("Example", new_event, event_name)
        event_to_delete = event_name
    
    calender.view_events()
    calender.delete_events("My Calender", event_to_delete)

    print("------------- AFTER DELETION --------------")
    calender.view_events()

