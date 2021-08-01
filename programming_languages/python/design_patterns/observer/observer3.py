"""
Goal: impliment observer pattern sensitive to multiple kinds of events +
standard python data structures.
""" 

import sys

class Subscriber:

    def __init__(self, name):
        self.name = name

    def update(self, message):
        print('{} got message "{}"'.format(self.name, message))
        
class Publisher:

    def __init__(self, events):
        # maps event names to subscribers
        # str -> dict
        # dict comprehension, not list comprehension
        self.events = { event : dict() for event in events }

    def get_subscribers(self, event):
        # Gets the dictionary of {subscriber:update_method} foran event in
        # events.
        # I don't understand why this needs a method, since no input checking
        # is performed. One could replace every instance of
        # self.get_subscribers with self.events[event]
        return self.events[event]

    def register(self, event, who, callback=None):
        if callback == None:
            callback = getattr(who, 'update')
        self.get_subscribers(event)[who] = callback

    def unregister(self, event, who):
        del self.get_subscribers(event)[who]

    def dispatch(self, event, message):
        for subscriber, callback in self.get_subscribers(event).items():
            callback(message)

def main():
    # maps 'lunch' to empty dict
    # maps 'dinner' to empty dict
    pub = Publisher(['lunch', 'dinner'])
    # pub.events:
    # { 'lunch':dict(), 'dinner':dict() }

    bob = Subscriber('Bob')
    alice = Subscriber('Alice')
    john = Subscriber('John')

    # Register different subscribers to different events
    pub.register("lunch", bob)
    pub.register("dinner", alice)
    pub.register("lunch", john)
    pub.register("dinner", john)
    # pub.events:
    # {'lunch':{alice:alice.update}}
    # {'lunch':{john}:john.update}}
    # {'lunch':{john'}:john.update}}
    # {'dinner':{alice:alice.update}}
    # {'dinner':{john:john.update}}

    pub.dispatch("lunch", "It's lunchtime!")
    pub.dispatch("dinner", "Dinner is served")


if __name__=='__main__':
    sys.exit(main())
