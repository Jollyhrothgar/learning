#!/usr/bin/env python

import random as rand

def make_gaus_data():
    lines = []
    for i in range(0,500):
        x_0 = rand.gauss(1,0.1) 
        y_0 = rand.gauss(0,0.1)
        x_1 = rand.gauss(-1,0.1)
        y_1 = rand.gauss(0,0.1)
        data = str(x_0)+','+str(y_0)+':0'
        lines.append(data)
        data = str(x_1)+','+str(y_1)+':1'
        lines.append(data)
    return lines


# Assume that data is in four clusters, and that we give the algorithm the 
# centroid of the cluster the data belongs to
def make_clustered_data():
    lines = []
    for i in range(0,500):
        d_0 = '.256,.632:0'
        d_1 = '-0.1,-.2622:1'
        lines.append(d_0)
        lines.append(d_1)

    return lines

gaus_data = make_gaus_data()
centroid_data = make_clustered_data()

rand.shuffle(centroid_data)
with open('clustered_data.txt','w') as out_file:
    for line in centroid_data:
        out_file.write(line+'\n')
