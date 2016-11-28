#!/usr/bin/env python

def count_ones(n):
        """
        :type n: int
        :rtype: int
        """
        if n < 0:
            return
        if n % 1 > 0:
            return
        
        # Brute Force
        import re
        number_of_ones = 0
        for i in range(1,n+1):
            my_str = str(i)
            for char in my_str:
                if char == '1':
                    number_of_ones += 1
        return number_of_ones
print count_ones(3184191) 
