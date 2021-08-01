import sys

class Subscriber:
    def __init__(self,name):
        self.name = name
    def update(self,message):
        print('{} got message "{}"'.format(self.name, message))

class Publisher:
    def __init__(self):
        self.subscribers = set()
    def register(self,who):
        self.subscribers.add(who)
    def unregister(self,who):
        self.subscribers.discard(who)
    def dispatch(self,message):
        for subscriber in self.subscribers:
            subscriber.update(message)

def main():
    pub = Publisher()

    bob = Subscriber('bob')
    alice = Subscriber('alice')
    john = Subscriber('john')

    pub.register(bob)
    pub.register(alice)
    pub.register(john)

    pub.dispatch('Its lunchtime')

    pub.unregister(john)

    pub.dispatch('Its dinnertime')

if __name__ == '__main__':
    sys.exit(main())
