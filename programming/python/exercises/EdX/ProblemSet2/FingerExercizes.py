#Finger Exersize Check - Week 2#
num = 10
while num > 3:
    num -= 1
    print(num)
    
numberOfLoops = 0
numberOfApples = 2
while numberOfLoops < 10:
    numberOfApples *= 2
    numberOfApples += numberOfLoops
    numberOfLoops -= 1
print("Number of apples: " + str(numberOfApples))
