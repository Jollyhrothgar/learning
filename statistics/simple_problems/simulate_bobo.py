#!/usr/bin/env python
import random

n_amoeba = 1

def reproduce(n):
    '''
    Given a population of n ameobas, returns the number of offspring, with each amoeba having
    the following chances to produce offspring:
    0: 0.25
    1: 0.25
    2: 0.5
    '''
    new_population = 0
    for i in range(0,n):
        rand_int = random.randint(1,4)
        if rand_int == 2:
            new_population += 1
        if rand_int > 2:
            new_population += 2
    return new_population

def simulate_bobo(population):
    '''
    Given an initial population of amoebas (all named bobo), count the number of generations 
    it takes for bobo's lineage to die off.
    '''
    n_amoeba = population
    number_of_generations = 0
    while n_amoeba > 0:
        n_amoeba = reproduce(n_amoeba)
        number_of_generations+=1
        if number_of_generations == 30:
            break;
    return number_of_generations

print "simulating bobo"
number_of_generations = simulate_bobo(1)


lives_forever = 0
dies_tragically = 0
number_of_trials = 0
tenth_trial = False
prev_frac = 0
while(True):
    if simulate_bobo(1) == 30:
        lives_forever += 1
    else:
        dies_tragically +=1
    fraction_lives = float(dies_tragically)/(lives_forever+dies_tragically)
    number_of_trials += 1
    if number_of_trials == 10:
        prev_frac = fraction_lives
    elif number_of_trials > 10:
        if abs(fraction_lives-prev_frac) < 0.001:
            print "the fraction which lives:",fraction_lives,"found after",number_of_trials
            break
        else:
            prev_frac = fraction_lives
        

