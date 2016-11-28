import random

def sampleQuizzes():
    inRange = 0.0
    outRange = 0.0
    for trial in range(0,10000):
        midterm1 = random.randint(50,80)
        midterm2 = random.randint(60,90)
        final = random.randint(55,95)
        score = 0.25*midterm1 + 0.25*midterm2+0.5*final
        if score <= 75 and score >=70:
            inRange+=1.0
        else:
            outRange+=1.0
    probability = inRange/(outRange+inRange)
    return probability
