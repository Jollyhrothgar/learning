def probTest(limit):
    probability = 1.0
    rolls = 0
    while probability >= limit:
        rolls += 1
        probability = (5.0/6.0)**rolls
    return rolls
