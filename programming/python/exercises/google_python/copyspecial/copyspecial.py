#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them

def get_files(dir):
  cmd = 'ls ' + dir
  #print 'calling get_files:',dir,'with command',cmd
  (status,output) = commands.getstatusoutput(cmd)
  abs_path = os.path.abspath(dir)
  #print abs_path
  files_in_path = []
  if status: 
    sys.stderr.write(output)
  else:
    files_in_path = output.split('\n')
  special_files = []
  for file in files_in_path:
    if is_special(file):
      print file
      special_files.append(abs_path+'/'+file)
  return special_files

def is_special(filename):
  """
  Takes a filename with or without a prepended path and determins whether or not
  the file is 'special'. Specialness is determined based on whether or not the
  filename contains a string: __<stuff>__
  """
  #print "calling is_special:",filename
  matches = re.findall(r'__.*__',filename)
  if len(matches) > 0:
    return True
  return False

def copy_to(paths,dir):
  """
  Given a list of paths, copies special files into a directory, dir.
  """
  if len(paths) == 0:
    sys.stderr.write("No paths to copy")
    sys.exit(1)
  for file in paths:
    print "copying",file,"to",dir
    shutil.copy(file,dir)
  #print "calling copy_to",paths,dir
  return

def zip_to(paths,zippath):
  """
  given a list of paths, zip those files up into zippath
  """
  cmd = 'zip -j '+zippath+' '+' '.join(paths)
  print cmd
  (status,output) = commands.getstatusoutput(cmd)
  if status:
    sys.stderr.write('Problem zipping files!')
    sys.exit(1)
  else:
    print 'zipping successful!'
  return

def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  print "CHECK THAT ARGS ARE EXACTLY --todir or --tozip"
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  # Order of arguments matters.
  todir = ''
  if args[0] == '--todir':
    print 'deleting todir!'
    todir = args[1]
    print todir
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    print 'deleting tozip!'
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  # +++your code here+++
  # Call your functions
  print args
  for dir in args:
    if todir: # copy directories
      copy_to(get_files(dir),todir)
    elif tozip: # zip special files to zip file
      zip_to(get_files(dir),tozip)
  
if __name__ == "__main__":
  main()
