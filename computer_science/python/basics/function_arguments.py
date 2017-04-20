def funky_1(*args):
    """
    takes a list of args
    """
    print(args)

def funky_2(**kwargs):
    """
    takes arguments by keyword
    """
    print(kwargs)

def funky_3(this, foo):
    """
    named arguments - no kwargs OR args
    """
    print("this = {0}, foo = {1}".format(this,foo))

if __name__ == "__main__":
    funky_1(1,2,3)
    try:
        funky_1(one=1, two=2, three=3)
    except:
        print("Error - you can't give this function named arguments!")

    list_args = [1,2,3]
    funky_1(*[1,2,3]) # unpack list args

    funky_2(this="that", foo="bar")
    try:
        funky_2(1,2,3)
    except:
        print("Error - you can't give this function a list of arguments!")

    # unpack a dictionary of arguments

    mydict = {"this":"that","foo":"bar"}
    funky_2(**mydict) # you can unpack a dictionary into function arguements!
    funky_3(**mydict) # it even works for functions with named arguements!
