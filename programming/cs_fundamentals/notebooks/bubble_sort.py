#!/usr/bin/env python
import random


def bubble_sort(my_list):
    number_of_iterations = 0
    unsorted = True
    while(unsorted == True):
        unsorted = False
        for index in range(len(unsorted_list)-1):
            current_entry = my_list[index]
            next_entry = my_list[index+1]
            if  next_entry < current_entry:
                my_list[index] = next_entry
                my_list[index+1] = current_entry
                unsorted = True
        print my_list
        number_of_iterations += 1
    return my_list

unsorted_list = []
for x in range(100):
    unsorted_list.append(random.randint(1,100))
number_of_iterations = bubble_sort(unsorted_list)
