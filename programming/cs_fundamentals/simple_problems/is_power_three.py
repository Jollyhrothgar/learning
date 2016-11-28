#! /usr/bin/env python

def isPowerOfThree(n):
    """
    :type n: int
    :rtype: bool
    """
    is_pow_three = False
    for i in range(1,n):
        if 3**i == n:
            is_pow_three = True
            break
    return is_pow_three 

print isPowerOfThree(9)
