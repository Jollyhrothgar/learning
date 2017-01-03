import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import time
import math

# NP arrays default to inner-product multiplication.

def load_data(fname, delim = ',', cast_type = 'float'):
    """
    Returns design matrix X, and predicted outputs, y

    Assumes that x_i and y_i for each training example exist on a row of delim
    separated data.
    """
    X = []
    y = []
    with open(fname, 'r') as f:
        for line in f.readlines():
            tokens = line.split(delim)
            if cast_type == 'float':
                features = [float(token) for token in tokens[0:-1]]
                predict = [float(token) for token in tokens[-1:]]
            else:
                features = [token for token in tokens[0:-1]]
                predict = tokens[-1:]
            X.append(features)
            y.append(predict)
    return np.array(X), np.array(y)

if __name__ == '__main__':
    X, y = load_data('./ex1data2.txt')
    print(np.shape(X), np.shape(y))
    print(X,'\n',y)

    plt.ion()
    plt.show()

    plt.figure()
    plt.plot(np.transpose(X)[0],y,'b+')
    plt.draw()

    plt.figure()
    plt.plot(np.transpose(X)[1],y,'r+')
    plt.draw()

    plt.figure()
    plt.plot(np.transpose(X)[0],np.transpose(X)[1],'g+')
    plt.draw()

    input("Press [enter] to continue")


