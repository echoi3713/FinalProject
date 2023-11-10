"""This class represents an event that the user can add.
"""
class Event:
    def __init__(self, title, location, date):
        self.title = title
        self.location = location
        self.date = date


"""This class represents the calendar that the user will access
and modify

    Attributes:
        events (dict): a dictionary of events the user has added
"""
class Planner:
    def __init__(self):
        self.events = dict()

    """This method allows the user to add events

        Arguments:
            event (Event): an event hte user will add
    """
    def add_event(self, event):
        self.events.append(event)

    """This method allows the user to view their events

        Arguments:
            event (Event): an event hte user will add
    """
    def view_events(self):
        if not self.events:
            print("No events found")
        else:
            print("Upcoming events: ")

        for event in self.events:
            print("Title: ", event.title)
            print("Location: ", event.location)
            print("Date: ", event.date)
            print()
