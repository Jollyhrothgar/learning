import sys

name = ''
val = ''
_concat = ''

def FunTime(_name = '',_val = ''):
    global name
    global val
    print ('initializing FunTime_module')
    name = _name
    val = _val

def Concat():
    global _concat
    _concat = str(val)+str(name)

def GetConcat():
    global _concat
    return _concat

