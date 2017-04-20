#!/usr/bin/python

import os
import re
import sys
import urllib
import urllib2
from bs4 import BeautifulSoup 

def download_ba(url_number):
  url_base = "http://www.beeradvocate.com/beer/profile/"
  url = url_base + str(url_number) + "/"
  print "scraping: ",url
  headers = { 'User-Agent' : 'Mozilla/5.0'  }
  req = urllib2.Request(url, None, headers)
  html = urllib2.urlopen(req).read()
  print html
  return

def main():
  print "trying some stuff..."
  download_ba(735)

if __name__ == '__main__':
  main()
