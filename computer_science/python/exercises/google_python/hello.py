#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""A tiny Python program to check that Python is working.
Try running this program from the command line like this:
  python hello.py
  python hello.py Alice
That should print:
  Hello World -or- Hello Alice
Try changing the 'Hello' to 'Howdy' and run again.
Once you have that working, you're ready for class -- you can edit
and run Python code; now you just need to learn Python!
"""

import sys

def repeat(s,exclaim):
  """
  Returns the string 's' repeated exactly 3 times. If exclaim is true, add
  exclamation marks.
  """
  result = s+s+s
  if exclaim:
    result = result + '!!!'
  return result

# Define a main() function that prints a little greeting.
def main():
  print 'Running program named:',sys.argv[0] 
  # Get the name from the command line, using 'World' as a fallback.
  if len(sys.argv) >= 2:
    name = sys.argv[1]
    print 'Hi there,', name
  else:
    print 'Hello. I\'m so alone. You didn\'t give me any arguments. Please let me die.'
  
  repetitious_string = repeat("Fucking horker meat tastes so fucking good",True)
  print repetitious_string
  print repeat('Yay',False)
  print repeat('Woo Hoo',True)
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
