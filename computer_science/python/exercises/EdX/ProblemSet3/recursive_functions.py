def reCursive(varName):
    '''
    varName: give an integer less than 1000, and
    this function will add one to it, and then return
    the integer plus the result of this function until
    your integer is equal to 1000
    '''
    if varName + reCursive(varName) >= 1000:
        print "overflow"
    else:
        varName+=1
        print varName
        return varName + reCursive(varName)
