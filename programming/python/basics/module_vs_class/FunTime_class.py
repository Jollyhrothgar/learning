import sys

class FunTime:
    # no such thing as private variable, but convention is to 
    # prepend '_' to something that is private.

    # Note too that variables do not need to be explicitly called,
    # they are available as soon as we define them, within the scope
    # of the class.
    # or: _concat = ''
    def __init__(self,name='',val=''):
        print('initializing FunTime')
        self.name = name
        self.val = val
        # or
        self._concat = ''
    def Concat(self):
        self._concat = str(self.val)+str(self.name)
    def GetConcat(self):
        return self._concat

def main():

    # Default arguments allow an 'empty class call'
    inst1 = FunTime()

    # Unnamed arguments require correct order
    inst2 = FunTime("Sally","2131")

    # Named arguments are placed correctly
    inst3 = FunTime(val="4216",name="Thomas")

    # Error prone if you do not use named arguments.
    inst4 = FunTime("124","NAAME")

    # Can individually define the class by calling members directly
    inst1.name = "Harry"
    inst1.val = "12"

    inst1.Concat()
    inst2.Concat()
    inst3.Concat()
    inst4.Concat()

    # Demo what's going on
    print(inst1.GetConcat()) # does the right thing
    print(inst2.GetConcat()) # does the right thing
    print(inst3.GetConcat()) # does the right thing
    print(inst4.GetConcat()) # ERROR, arguments were supplied in wrong order!

    return 0

if __name__ == "__main__":
    sys.exit(main())
