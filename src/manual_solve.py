#!/usr/bin/python
## Name: Akanksha | Student Id: 20231242 ; Sophia Cogan | Student Id: 16366736 
### GitHub repository URL : https://github.com/anks310/ARC

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
    #"178fcbfb" include 3 task demonstration input-output pair and 1 test input grid.
    #Task includes manipulation of 3 colours that are refered as number 1,2 and 3 
    #blue(as 1), red (as 2), and green (as 3). If a cell has blue(1) or green(3) then each column against 
    #that row will be turn to 1 or 3 but if a cell has number-2 then all the row corrsponding to tha colunm
    #will be changed except those which has been already changed to 1 or 3. Solve function working for all input.
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

def solve_ba97ae07(x):
    #"ba97ae07" include 4 task demonstration input-output pair and 1 test input grid.
    #Solution include- any number(refered as color) in matrix other than 0 will be mapped to every column of that row.
    #Flip the color of the cell if the color(as number) matches with the color of the corresponding column or row
    #with the color of the previous row or column. Solve function working for all input.    
    x_hat= x.copy()
    for i in range(x_hat.shape[0]):
        if x_hat[i][0] !=0:
            for j in range(x_hat.shape[1]):
                if x_hat[i-1][j] !=0 and x_hat[i][j] !=x_hat[i][0]:
                    x_hat[i][j] =x_hat[i][0]
                elif x_hat[i-1][j] !=0 and  x_hat[i][j] ==x_hat[i][0]:
                    x_hat[i][j] =x_hat[i-1][j]
    x=x_hat               
    return x

def solve_a65b410d(x): 
    #"a65b410d" includes 4 task demonstration input-output pair and 1 test input grid.
    #Solution includes counting of red cells and its position. Then for loop used in reverse to fill the green cell
    #above red with the increment on 1 column on every iteration. Again for loop used to fill the row-column with blue
    #below red cell row-columns but incrementing the row and decrementing the column to match the pattern    
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

def solve_d4a91cb9(x):
    
    #from red, yellow can only move left or right (horizontal)
    #from blue, yellow can only traavel up or down (verticle)
    
    #blue = 8
    #red =2
    #yellow = 4

    #set inital  x and y to zero
    x1=0
    for arr in x:
        y1=0
        
        #find location of blue and red (8&2) and update x & y with new coordinates
        for i in arr:
            if str(i) == "8":
                blueL = (x1,y1)
            elif str(i) == "2":
                redL = (x1,y1)
            y1+=1
        x1+=1
        
    #Compare postions of blue and red locations. 
    #If blue is closer to the top of the grid it must move down
    
    #move down
    if blueL[0] < redL[0]: 
        a = redL[0] - blueL[0]
        yellow = blueL[0]
        #making verticle yellow line down
        for i in range(0,a):
            if blueL[0] < redL[0]:
                yellow = yellow+1    
                x[yellow,blueL[1]]=4
                
        #Move right
        if blueL[1] < redL[1]:
            b = redL[1] - blueL[1]
            yellow = redL[1]
            for i in range(0,b):
                #fill squares yellow (4) until in line with red
                if blueL[1] < redL[1]:
                    yellow = yellow-1    
                    x[redL[1]-1,yellow]=4  
        #move left
        if blueL[1] > redL[1]:
            b = blueL[1] - redL[1]
            yellow = redL[1]
            for i in range(0,b):
                #fill squares yellow (4) until in line with red
                if blueL[1] > redL[1]:
                    yellow = yellow+1    
                    x[redL[0],yellow]=4
                    
    #if blue is closer to the bottom than the top
    #blue must move up
    if blueL[0] > redL[0]:
        
        #make verticle yellow line up
        a = blueL[0] - redL[0]
        yellow = blueL[0]
        for i in range(0,a):
            if blueL[0] > redL[0]:
                yellow = yellow-1    
                x[yellow,blueL[1]]=4
         
        #move right
        if blueL[1] < redL[1]:    
            b = redL[1] - blueL[1]
            yellow = blueL[1]
            for i in range(0,b-1):
                if blueL[1] < redL[1]:
                    yellow = yellow +1
                    x[redL[0],yellow]=4
                    
        #move left            
        if blueL[1] > redL[1]:   
            b = blueL[1] - redL[1]
            yellow = redL[1]
            for i in range(0,b-1):
                if blueL[1] > redL[1]:
                    yellow = yellow -1
                    x[redL[0],yellow]=4          
                    
    return x

def solve_ea786f4a(x):
    #this problem needs two diagonal lines to pass through the center
    
    #fill diagonal top left to bottom right
    np.fill_diagonal(x,0, wrap=True)
    #fill reverse diagonal bottom left to top right
    np.fill_diagonal(np.fliplr(x), [0])
    return x

def solve_74dd1130(x):
    #to solve this problem the opposite corners need to be swapped around    
    n = len(x)
    # switch the top right triangle with the bottom left triangle
    for i in range(n):
        for j in range(i):
            x[i][j], x[j][i] = x[j][i], x[i][j]
    return x


def solve_a2fd1cf0(x):
    
    #this task is quite similar to task d4a91cb9 it only needed some minor adjustments
    #in the 'move left' and 'move right' code

    #from red, yellow can only move left or right (horizontal)
    #from blue, yellow can only traavel up or down (verticle)
   
    #blue = 8
    #red =2
    #green = 3

    #set inital  x and y to zero
    x1=0
    for arr in x:
        y1=0
       
        #find location of green and red (3&2) and update x & y with new coordinates
        for i in arr:
            if i == 3:
                greenL = (x1,y1)
            elif i == 2:
                redL = (x1,y1)
            y1+=1
        x1+=1
    
       
    #Compare postions of blue and red locations.
    #If green is closer to the top of the grid it must move down
   
    #move down
    if greenL[0] < redL[0]:
        
        a = redL[0] - greenL[0]
        blue = greenL[0]
        #making verticle blue line down
        for i in range(0,a):
            if greenL[0] < redL[0]:
                blue = blue+1    
                x[blue,greenL[1]]=8
               
        #Move right
        if greenL[1] < redL[1]:
            
            b = abs(redL[1] - greenL[1])
           
            blue = redL[1]
            for i in range(0,b-1):
                #fill squares blue (8) until in line with red
                if greenL[1] < redL[1]:
                    blue = blue+1    
                    x[redL[1]-1,blue]=8  
        #move left
        if greenL[1] > redL[1]:
            
            b = abs(redL[1] - greenL[1])
            blue = greenL[1]
            for i in range(0,b-1):
                #fill squares blue (8) until in line with red
                if greenL[1] > redL[1]:
                    blue = blue-1    
                    x[redL[0],blue]=8
                   
    #if green  is closer to the bottom than the top
    #green  must move up
    if greenL[0] > redL[0]:
        
        #make verticle blue line up
        a = greenL[0] - redL[0]
        blue = greenL[0]
        for i in range(0,a):
            if greenL[0] > redL[0]:
                blue = blue-1    
                x[blue,greenL[1]]=8
         
        #move right
        if greenL[1] < redL[1]:
           
            b = abs(redL[1] - greenL[1])
            blue = greenL[1]
            for i in range(0,b-1):
                if greenL[1] < redL[1]:
                    blue = blue +1
                    x[redL[0],blue]=8
                   
        #move left            
        if greenL[1] > redL[1]:
            
            b = abs(greenL[1] - redL[1])
            blue = greenL[1]
            for i in range(0,b-1):
                if greenL[1] > redL[1]:
                    blue = blue -1
                    x[redL[0],blue]=8                  
    
    return x

def solve_484b58aa(x):
    #"484b58aa" includes 4 task demonstration input-output pair and 1 test input grid.
    #Solution Added- 1st for loop we will get all the diagonal starting from top left till the mid.
    #2nd loop we will get diagonals starting from down right
    #We can seen every diagonal follows a certain kind of pattern like aaaa.. or ababab.. so by checking the previous 
    #values we will get the value from previous position to stamp on empty cell (of value 0)# for one input solve function is working.
    x_hat = x.copy()
    row =x_hat.shape[0]
    col =x_hat.shape[1]
    for k in range(col-1):
        i=row-1
        j=k
        while j <= col-2: 
            if x_hat[i][j] ==0:
                prev1= x_hat[i+1][j-1]
                prev2= x_hat[i+2][j-2]
                prev3= x_hat[i+3][j-3]
                
                if prev1 == prev2 ==prev3:
                    x_hat[i][j] =prev1
                    
                elif prev1 != prev2 and prev1 == prev3:
                    x_hat[i][j] =prev2  
                    
                elif j-4 <= col-2 and i+4 <=row-1:
                    prev4= x_hat[i+4][j-4]
                    if prev1 != prev2 and prev1 != prev3 and prev3 != prev4 and prev1 ==prev4:
                        x_hat[i][j] =prev3
                        
                elif j-5 <= col-2 and i+5 <=row-1:
                    prev5= x_hat[i+5][j-5]
                    if prev1 != prev2 and prev1 != prev3 and prev3 != prev4 and prev4 !=prev5 and prev5 == prev1:
                        x_hat[i][j] =prev4                   
            i=i-1
            j=j+1    
    
    for k in range(row-1):
        i=k;j=0
        while i>=0:
            if x_hat[i][j] ==0:
                prev1= x_hat[i+1][j-1]
                prev2= x_hat[i+2][j-2]
                prev3= x_hat[i+3][j-3]
                
                if prev1 == prev2 ==prev3:
                    x_hat[i][j] =prev1
                elif prev1 != prev2 and prev1 == prev3:
                    x_hat[i][j] =prev2 
                
                elif j-4 <= col-2 and i+4 <=row-1:
                    prev4= x_hat[i+4][j-4]
                    if prev1 != prev2 and prev1 != prev3 and prev3 != prev4 and prev1 ==prev4:
                        x_hat[i][j] =prev3
                
                elif j-5 <= col-2 and i+5 <=row-1:
                    prev5= x_hat[i+5][j-5]
                    if prev1 != prev2 and prev1 != prev3 and prev3 != prev4 and prev4 !=prev5 and prev5 == prev1:
                        x_hat[i][j] =prev4           
            i=i-1
            j=j+1
    
    return x_hat

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
