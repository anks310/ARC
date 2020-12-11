#!/usr/bin/python

import os, sys
import json
import numpy as np
import re

### YOUR CODE HERE: write at least three functions which solve
### specific tasks by transforming the input x and returning the
### result. Name them according to the task ID as in the three
### examples below. Delete the three examples. The tasks you choose
### must be in the data/training directory, not data/evaluation.
def solve_178fcbfb(x):
    x_hat= x.copy()
    for i in range(x_hat.shape[0]):
        for j in range (x_hat.shape[1]):
            if x_hat[i][j] == 3:
                for k in range(x_hat.shape[1]):
                    x_hat[i][k] =3

            elif x_hat[i][j] == 1:
                for k in range(x_hat.shape[1]):
                    x_hat[i][k] =1

            elif x_hat[i][j] == 2:
                for k in range(x_hat.shape[0]):
                    if x_hat[k][j] ==0:
                        x_hat[k][j] =2     
    x=x_hat
    return x

def solve_a65b410d(x):
    x_hat = x.copy()
    B1=0;B2=0;G=0;B=0
    pos1,pos2=0,0
    for i in range(x_hat.shape[0]):
        for j in range (x_hat.shape[1]):
            if x_hat[i][j] ==2:
                B2+=1
                pos1,pos2=i,j 
    G = B2+1
    for g in reversed(range(pos1)):
        for g_j in range(G):
            x_hat[g][g_j]=3   
        G +=1 
        
    B = B2-1;b_col = B2-1;p1=pos1
    for b in range(B):
        p1 +=1 
        for b_j in range(b_col):
            x_hat[p1][b_j]=1
        b_col = b_col-1
    x=x_hat
    return x


def main():
    # Find all the functions defined in this file whose names are
    # like solve_abcd1234(), and run them.

    # regex to match solve_* functions and extract task IDs
    p = r"solve_([a-f0-9]{8})" 
    tasks_solvers = []
    # globals() gives a dict containing all global names (variables
    # and functions), as name: value pairs.
    for name in globals(): 
        m = re.match(p, name)
        if m:
            # if the name fits the pattern eg solve_abcd1234
            ID = m.group(1) # just the task ID
            solve_fn = globals()[name] # the fn itself
            tasks_solvers.append((ID, solve_fn))

    for ID, solve_fn in tasks_solvers:
        # for each task, read the data and call test()
        directory = os.path.join("..", "data", "training")
        json_filename = os.path.join(directory, ID + ".json")
        data = read_ARC_JSON(json_filename)
        test(ID, solve_fn, data)
    
def read_ARC_JSON(filepath):
    """Given a filepath, read in the ARC task data which is in JSON
    format. Extract the train/test input/output pairs of
    grids. Convert each grid to np.array and return train_input,
    train_output, test_input, test_output."""
    
    # Open the JSON file and load it 
    data = json.load(open(filepath))

    # Extract the train/test input/output grids. Each grid will be a
    # list of lists of ints. We convert to Numpy.
    train_input = [np.array(data['train'][i]['input']) for i in range(len(data['train']))]
    train_output = [np.array(data['train'][i]['output']) for i in range(len(data['train']))]
    test_input = [np.array(data['test'][i]['input']) for i in range(len(data['test']))]
    test_output = [np.array(data['test'][i]['output']) for i in range(len(data['test']))]

    return (train_input, train_output, test_input, test_output)


def test(taskID, solve, data):
    """Given a task ID, call the given solve() function on every
    example in the task data."""
    print(taskID)
    train_input, train_output, test_input, test_output = data
    print("Training grids")
    for x, y in zip(train_input, train_output):
        yhat = solve(x)
        show_result(x, y, yhat)
    print("Test grids")
    for x, y in zip(test_input, test_output):
        yhat = solve(x)
        show_result(x, y, yhat)

        
def show_result(x, y, yhat):
    print("Input")
    print(x)
    print("Correct output")
    print(y)
    print("Our output")
    print(yhat)
    print("Correct?")
    # if yhat has the right shape, then (y == yhat) is a bool array
    # and we test whether it is True everywhere. if yhat has the wrong
    # shape, then y == yhat is just a single bool.
    print(np.all(y == yhat))

if __name__ == "__main__": main()
