import sys

class SubscriberOne:

    def __init__(self,name):
        self.name = name

    def update(self,message):
        print('{} got message "{}"'.format(self.name, message))

class SubscriberTwo:

    def __init__(self,name):
        self.name = name
    def receive(self,message):
        print('{} got message "{}" via receive method'.format(self.name, message))
    
    def update(self,message):
        print('{} got message "{}" via update method.'.format(self.name,message))

class Publisher:

    def __init__(self):
        self.subscribers = dict()

    # Here, we can give a specific function or method to this class ahead of
    # time, without the need to specify, thanks to python's function pointers.
    # callback may be set to any function or value, and then, we just call it
    # later and don't really need to know what it is.
    def register(self,who, callback=None):
        if callback == None:
            callback = getattr(who,'update')
        self.subscribers[who] = callback

    def unregister(self,who):
        del self.subscribers[who]

    def dispatch(self,message):
        for subscriber,callback in self.subscribers.items():
            callback(message)

def main():
    pub = Publisher()

    bob = SubscriberOne('bob')
    alice = SubscriberTwo('alice')
    john = SubscriberOne('john')
    rich = SubscriberTwo('rich')

    pub.register(bob, bob.update)

    # Example -> alice has a special subscriber function called recieve, not
    # update. Publisher searches for an attribute called 'update' if no
    # callback attribute is supplied.  Therefore, if alice is to be used with
    # Publisher, we must supply a callback, since alice (or any SubscriberTwo)
    # object does not have an 'update' method
    pub.register(alice, alice.receive)
    pub.register(rich)
    
    # Scary stuff: if you were to do this, then when Publisher tries to
    # callback john, he actually calls back alice, and no checking is done to
    # see if alice is john or not. Yikes...
    # --> pub.register(john, alice.receive)
    
    # Publisher looks to see if john has a method "update", if so it just sets
    # whatever that is to the callback
    pub.register(john)

    print("TEST 1:")
    pub.dispatch('Its lunchtime')

    print("TEST 2: Unregistering john")
    pub.unregister(john)
    pub.dispatch('Its dinnertime')

if __name__ == '__main__':
    sys.exit(main())
