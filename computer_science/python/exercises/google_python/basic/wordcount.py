#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys
import re

def load_file(filename):
  file_dict = {}
  in_file = open(filename,'rU')
  for line in in_file:
    for word in line.lower().split():
      match = re.search(r'[A-Za-z\']+',word)
      if match:
        if file_dict.has_key(match.group()):
          file_dict[match.group()] += 1
        else:
          file_dict[match.group()] = 1
  in_file.close()
  return file_dict

def print_words(filename):
  file_dict = load_file(filename)
  #for k,v in file_dict.items():
  #  print k,v
  for word in sorted(file_dict, key=file_dict.get, reverse=True):
    print word, file_dict[word]
  return

def print_top(filename):
  file_dict = load_file(filename)
  counter = 0
  for word in sorted(file_dict, key=file_dict.get, reverse=True):
    if counter == 20: break
    print word, file_dict[word]
    counter+=1
  return

def find_word(word,filename):
  file_dict = load_file(filename)
  if file_dict.has_key(word):
    return file_dict[word]
  else :
    return -1

def list_all_words(filename):
  file_dict = load_file(filename)
  for word in sorted(file_dict, key=file_dict.get, reverse=True):
    print word, file_dict[word]
  return

# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.

###

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
  if len(sys.argv) != 3:
    print 'usage: ./wordcount.py {--count | --topcount | --listall} file'
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  elif option == '--listall':
    list_all_words(filename)
  else:
    print 'unknown option: ' + option
    sys.exit(1)

if __name__ == '__main__':
  main()
