#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Basic string exercises
# Fill in the code for the functions below. main() is already set up
# to call the functions with a few different inputs,
# printing 'OK' when each function is correct.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code.
# It's ok if you do not complete all the functions, and there
# are some additional functions to try in string2.py.


# A. donuts
def donuts(count):
  # +++your code here+++
  '''
  Give an int, representing a number of doughnuts. Returns string which is of
  the form 'number of donuts: <count>', where <count> is the number passed in.
  However, this function defaults to setting <count> to 'many' in the event that
  <count> is 10 or more.
  '''
  if count >= 10:
    return "Number of donuts: many"
  else:
    return "Number of donuts: %d" % count

# B. both_ends
# Given a string s, return a string made of the first 2
# and the last 2 chars of the original string,
# so 'spring' yields 'spng'. However, if the string length
# is less than 2, return instead the empty string.
def both_ends(s):
  '''
  Takes a string, s as input, return a string made from the first two, and last
  two characters of the original string. However, if the string length is less
  than two, then return an empty string.
  '''
  if len(s) < 2:
    return ''
  else:
    start_str = s[0:2] # known: beginning element is 0 
    end_str   = s[-2:] # known: second to last character is -2
    return start_str+end_str

# C. fix_start
def fix_start(s):
  '''
  Given a string s, return a string where all instances of the first character
  have been changed to *, but do not change the first character itself. Returns
  an empty string in the case where there aren't enough characters do do the
  operation.
  '''
  first_character = s[0]
  tail_str = s[1:]
  new_tail_str = tail_str.replace(first_character,'*')
  return first_character + new_tail_str


# D. MixUp
# Given strings a and b, return a single string with a and b separated
# by a space '<a> <b>', except swap the first 2 chars of each string.
# e.g.
#   'mix', pod' -> 'pox mid'
#   'dog', 'dinner' -> 'dig donner'
# Assume a and b are length 2 or more.
def mix_up(a, b):
  return b[0:2] + a[2:] + ' ' + a[0:2] + b[2:]


# Provided simple test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))


# Provided main() calls the above functions with interesting inputs,
# using test() to check if each result is correct or not.
def main():
  print 'donuts'
  # Each line calls donuts, compares its result to the expected for that call.
  test(donuts(4), 'Number of donuts: 4')
  test(donuts(9), 'Number of donuts: 9')
  test(donuts(10), 'Number of donuts: many')
  test(donuts(99), 'Number of donuts: many')

  print
  print 'both_ends'
  test(both_ends('spring'), 'spng')
  test(both_ends('Hello'), 'Helo')
  test(both_ends('a'), '')
  test(both_ends('xyz'), 'xyyz')

  
  print
  print 'fix_start'
  test(fix_start('babble'), 'ba**le')
  test(fix_start('aardvark'), 'a*rdv*rk')
  test(fix_start('google'), 'goo*le')
  test(fix_start('donut'), 'donut')

  print
  print 'mix_up'
  test(mix_up('mix', 'pod'), 'pox mid')
  test(mix_up('dog', 'dinner'), 'dig donner')
  test(mix_up('gnash', 'sport'), 'spash gnort')
  test(mix_up('pezzy', 'firm'), 'fizzy perm')


# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  main()
