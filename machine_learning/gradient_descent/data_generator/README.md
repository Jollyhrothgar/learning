# General Idea

- Use the data generator module to create data sets which can be fit with linear models.

# Data Generator Spec

1. API
 - generate.py 
  - --relation f(x1,x2) = g(x3,x4): creates a set of data conforming exactly to this distribution
  - --fuzz (x1,numpy.dist(x1,vals)) (x2,numpy.dist...) ...: fuzz the data randomly according to the given distribution
  - --n number: number of rows to generate

2. Generates a file which conforms to the given parameters from left to right, x1...xN
