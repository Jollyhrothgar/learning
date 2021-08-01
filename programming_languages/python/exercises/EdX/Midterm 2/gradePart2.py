import random, pylab

def generateScores(trials):
    gradeList = []
    for trial in range(0,trials):
        midterm1 = random.randint(50,80)
        midterm2 = random.randint(60,90)
        final = random.randint(55,95)
        score = 0.25*midterm1 + 0.25*midterm2+0.5*final
        gradeList.append(score)
    return gradeList

def plotQuizzes():
    scores = generateScores(10000)
    pylab.hist(scores,7)
    pylab.title("Distribution of Scores")
    pylab.xlabel("Final Score")
    pylab.ylabel("Number of Trials")
    pylab.show()
