#Problem 3

import time

balance = 987654321
annualInterestRate = 0.2

b=balance
aiR=annualInterestRate
t=0
j=1
low=balance/12.
high=balance*((1+annualInterestRate/12)**12)/12
def bal(x):
    p=x
    b=balance
    t=0
    for i in range(12):
        b=(b-p)*(1+aiR/12)
        t=t+p
    return b
#print(bal(451.63))    
    
while abs(round(b,2))>0.01:
    fp=(low+high)/2.
    bl=bal(low)
    bh=bal(high)
    b=bal(fp)
    
    if b<0:
        high=fp

    else:
        
        if(b>bl and b>0):
            high=fp
        else:
            low=fp
#    print('I entered '+str(j)+' times.')
    j=j+1
    
print('Lowest Payment: '+str(round(fp,2)))
print('Time: ' + str(time.clock()))
