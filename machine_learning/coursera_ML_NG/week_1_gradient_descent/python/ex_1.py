"""
Do 1D Gradient Descent Inefficiently.
"""

import numpy as np
import matplotlib.pyplot as plt
import time
import math

def show_ident(i):
    print (np.eye(i))

def load_data(fname, delim = ',', cast_type = 'float'):
    """
    returns a tuple of np.array objects in the order in which they exist in 
    fname.
    """
    out_data = None
    with open(fname, 'r') as f:
        for i,data in enumerate(f.readlines()):
            if i == 0:
                out_data = {key:[] for key in range(len(data.split(delim)))}
            for item,token in enumerate(data.split(delim)):
                if cast_type == 'float':
                    out_data[item].append(float(token))
    out_data = {k:v for k,v in out_data.items()}
    print(out_data)
    return out_data

def update_params(theta,x,y):
    """
    Update using numpy looping techniques.
    """
    temp_0 = 0
    temp_1 = 0
    for i,val_x in enumerate(x):
        temp_0 += theta[0] + theta[1]*val_x - y[i]
        temp_1 += (theta[0] + theta[1]*val_x - y[i])*val_x

    temp_0 = alpha*(1/len(x))*temp_0
    temp_1 = alpha*(1/len(x))*temp_1
    theta[0] = theta[0] - temp_0
    theta[1] = theta[1] - temp_1

def plot_2D(x, y, x_title, y_title, **kwargs):
    """
    x: 1D numpy array
    y: 1D numpy array
    x_title is the x axis title
    y_title is the y axis title

    idea: create a decorator to spawn this onto a thread which is cleaned up
    after the program is finished executing, allowing plots to be generated 
    and observed without blocking execution.
    """

def cost_function():
    """

    """
    pass

if __name__ == "__main__":
    show_ident(5)
    data = load_data('./ex1data1.txt')
    x = data[0]
    y = data[1]

    plt.show() # call once per program.
    plt.ion() # '(i)nteractive (on)


    # Plot the Data Set

    # needed to create an 'atomic' plot
    plt.figure() # needed to make a new plot window
    plt.plot(np.array(x),np.array(y),'r+')
    plt.ylabel('Profit in $10,00s');
    plt.xlabel('Population of City in 10,000s')
    plt.xlim((4,24))
    plt.ylim((-5,25))
    plt.draw()

    # feature normalization
    x_norm = np.array(x)/np.std(np.array(x))
    y_norm = np.array(y)/np.std(np.array(y))

    # Show normalized data
    plt.figure()
    plt.plot(x_norm,y_norm, 'b+')
    # plt.plot(np.arange(0,10,1),np.arange(0,10,1),'r') # show y = x
    plt.draw()

    # Perform Batch Gradient Descent on the Data
    # Initialize hyperparmeters of model
    theta_1D = [0,0]
    print(theta_1D)

    # Cost Function - 1D
    # (1/2m) SUM(0->m){( h(x)-y(x) )^2}
    # h(x) = theta_0 + theta_1 * x
    
    # Learning Rate - alpha
    alpha = 0.01

    # Gradient descent
    # temp0 = theta[0] - alpha*dJ/dtheta0(J(theta0,theta1)) | (theta0, theta1)
    # temp1 = theta[1] - alpha*dJ/dtheta1(J(theta0,theta1)) | (theta0, theta1)
    # theta0 = temp0
    # theta1 = temp1
    theta_prev = list(theta_1D)
    iterations = 0
    done = False
    # inefficient - can this be vectorized??
    while not done:
        x_norm = list(x_norm)
        y_norm = list(y_norm)
        update_params(theta_1D,x_norm,y_norm)
        show_x = np.arange(0,10,1)
        y_values = np.ones(show_x.size)*theta_1D[0] + theta_1D[1]*(show_x)
        if iterations%5 == 0:
            plt.plot(show_x,y_values,'g')
            plt.title("{} iterations".format(iterations))
            plt.pause(0.005)

        theta_next = list(theta_1D)
        
        diff_0 = 0
        diff_1 = 0

        diff_0 = math.fabs(theta_next[0] - theta_prev[0])
        diff_1 = math.fabs(theta_next[1] - theta_prev[1])
        
        theta_prev = list(theta_next)

        if diff_0 < 0.001 and diff_1 < 0.001: # better convergence - use cost function!
            print("Converged after {} iterations".format(iterations))
            print("Best params, y = mx + b, m = {}, b = {}".format(theta_1D[0],theta_1D[1]))
            plt.plot(show_x,y_values,'g')
            plt.title("{} iterations".format(iterations))
            done = True
        iterations += 1
    input("Press [return] key to continue")
