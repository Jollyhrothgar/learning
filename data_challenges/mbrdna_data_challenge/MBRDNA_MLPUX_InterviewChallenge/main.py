import matplotlib.pyplot as plt
import mnbayes as classifier
import numpy as np
import random as rand

# Notes
# Naive Bayes will overfit if the data is collinear (nerd-speak for linearly
# related). For multicollinear data, we may be able to use linear regression and
# obtain the varience from the data to compare things that are not correllated.

DEBUG_VISUALIZATION = False

classifier.reset()

def predict(input):
#     #Debug the debug visualization
#     return 0 if input[0] < .25 else 1
    return classifier.predict(input)

def train(input, output):
    classifier.train(input, output)

# Data Exploration
def get_feature_arrays(filename):
    val1 = []
    val2 = []
    with open(filename,'r') as in_file:
        for line in in_file.readlines():
            values = line.split(',')
            (data,label) = values[1].split(':')
            val1.append(values[0])
            val2.append(data)
    data_1 = np.array(val1)
    data_2 = np.array(val2)
    return (data_1,data_2)
print "loading training data:"
(data_1,data_2) = get_feature_arrays('SQUASHED')
if DEBUG_VISUALIZATION:
    plt.scatter(data_1,data_2)
    plt.show()

#
# # Edit everything above here
#######################################
# # Plumbing below here

PROBLEM = "SQUASHED"

print "Reading input"

file_stream = open(PROBLEM, 'r')
full_text = file_stream.read();
 
train_set = []
test_set = []

lines = full_text.split("\n")
for line in lines:
    if line:
        input_output = line.split(":")
    
        input = input_output[0].split(",")
        input = map(lambda x : float(x), input)
    
        output = float(input_output[1])    
        example_dest = test_set if rand.randint(0, 1) == 1 else train_set
        example_dest.append((input, output))
    
    
print "Training..."
for x, y in train_set:
    train(x, y)
# train([x for x, y in train_set], [y for x, y in train_set])

print "Predicting..."
correct = 0
for i in xrange(len(train_set)):
    if int(predict(train_set[i][0]) + .5) == train_set[i][1]:
        correct += 1
            
print "Train:", str(100 - 100.0 * correct / len(train_set)) + "% error"

correct = 0
for i in xrange(len(test_set)):
    if int(predict(test_set[i][0]) + .5) == test_set[i][1]:
        correct += 1
            
print "Test:", str(100 - 100.0 * correct / len(test_set)) + "% error"

if DEBUG_VISUALIZATION:
    print "Drawing...\n\n"
    
    # Draw the color background grid
    
    GRID_MAX = 1.2
    GRID_MIN = -.2
    GRID_DELTA = .02
    
    GRID_MAX += GRID_DELTA
    grid_x, grid_y = np.meshgrid(np.arange(GRID_MIN, GRID_MAX, GRID_DELTA), np.arange(GRID_MIN, GRID_MAX, GRID_DELTA))
    
    colors = np.zeros((len(grid_x), len(grid_y)))
    
    for x in xrange(len(grid_x)):
        for y in xrange(len(grid_y)):
            colors[x][y] = predict([grid_x[x][y], grid_y[x][y]])
    
    
    
    cdict = {'red': ((0.0, 1.0, 1.0),
                     (1.0, 0.5, 0.5)),
             'green': ((0.0, 0.5, 0.5),
                       (1.0, 0.5, 0.5)),
             'blue': ((0.0, 0.5, 0.5),
                      (1.0, 1.0, 1.0))}
    
    plt.register_cmap(name='muted_rdbl', data=cdict)
            
    plt.pcolormesh(grid_x, grid_y, colors, cmap='muted_rdbl')
    
    # Scatter plot of examples
    
    input = [u for u, v in test_set]
    output = np.array([v for u, v, in test_set])
    
    x = np.array([u[0] for u in input])
    y = np.array([u[1] for u in input])
    
    colors = ['r', 'b']
    color_values = [colors[int(c) % len(colors)] for c in output]
    
    plt.scatter(x, y, color=color_values)
    
    plt.show()
