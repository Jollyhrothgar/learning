#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""
def get_rank(baby_names_tuple):
  return baby_names_tuple[0]

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]

  Keep names with highest rank as a means of handling duplicate names for boys
  and girls names which match (i.e. "Taylor")
  """
  # +++your code here+++
  print "reading:",filename
  input_file = open(filename,'rU')
  whole_file = input_file.read()
  year_match = re.findall(r'<h3 align="center">Popularity in (\d+)</h3>',whole_file)
  name_tuples = re.findall(r'<tr align="right"><td>(\d+)</td><td>([a-zA-Z]+)</td><td>([a-zA-Z]+)</td>',whole_file)
  if not year_match:
    sys.stderr.write("Couln\'t find a matching year in file: "+filename)
    sys.exit(1)
  list_names = []
  list_names.append(year_match[0])

  # in case names are not sorted by rank
  rank_sorted_tuple = sorted(name_tuples,key=get_rank) # returns a sorted list!
  
  names_dict = {}
  for name_tuple in name_tuples:
    rank = name_tuple[0]
    print rank
    boy_name = name_tuple[1]
    girl_name = name_tuple[2]
    if boy_name not in names_dict:
      names_dict[boy_name] = rank
    if girl_name not in names_dict:
      names_dict[girl_name] = rank

  # this is a list
  sorted_names = sorted(names_dict.keys())
  for name in sorted_names:
    list_str = name+' '+names_dict[name]
    list_names.append(list_str)
  return  list_names

def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  # check if there was anything
  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    # now we want summaries, not just baby-names
    summary = True
    del args[0]
  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
    
  for filename in args:
    names_data = extract_names(filename)
    if summary:
      # okay, print the name to a summary file
      out_file = open(filename+'.summary','w')
      out_string = '\n'.join(names_data)
      out_file.write(out_string)
      out_file.close()
    else:
      for name in names_data:
        print name
if __name__ == '__main__':
  main()
