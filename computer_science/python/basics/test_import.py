from FunTime_class import FunTime
import FunTime_module

# Default arguments allow an 'empty class call'
inst1 = FunTime()

# Unnamed arguments require correct order
inst2 = FunTime("Sally","2131")

# Named arguments are placed correctly
inst1 = FunTime()
inst2 = FunTime(name="studly",val='doodad')
inst3 = FunTime(val="4216",name="Thomas")


# Importing the module creates a single namespace for that
# module. We cannot expect the same behavior as with a class.
inst4 = FunTime_module
inst5 = FunTime_module

inst4.FunTime(_name="test",_val="val")

print("setting inst5, pointing to FunTime_module")
inst5.name = "test2" ## Overwrites anything in inst4 because it points
inst5.val = "val2"   ## to the same area
## I think this is terrible behavior, and it should be avoided.
## Maybe a module is kind of like a singleton

inst1.Concat()
inst2.Concat()
inst3.Concat()
inst4.Concat()

print("inst1: ", inst1.GetConcat()) # does the right thing
print("inst2: ", inst2.GetConcat()) # does the right thing
print("inst3: ", inst3.GetConcat()) # does the right thing
print("inst4: ", inst4.GetConcat())
print("inst5: ", inst5.GetConcat())
