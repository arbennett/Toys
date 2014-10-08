#!/usr/bin/python
'''
The most simplistic form of the dfa.  Just looking to play with it.
Author: Andrew Bennett
Date: 10/6/2014
'''

# -----------
#   Imports
# -----------
import numpy as np
from matplotlib import pyplot as plt

# -------------
#   Variables
# -------------
plt.ion()
size = 500
nSteps = int(3e4)
grid = np.zeros([size,size])
stepArray = [ [1,0], [-1,0], [0,1], [0,-1] ] # Defines the ways that the particle can move 

# The initial seed
grid[size/2][size/2]+=5
grid[size/4][size/4]+=5 
grid[size/4][3*size/4]+=5
grid[3*size/4][size/4]+=5
grid[3*size/4][3*size/4]+=5

# ---------------
#   Definitions
# ---------------
def hasNeighbor(x,y):
    if grid[x+1][y]>0 or grid[x-1][y]>0 or grid[x][y+1]>0 or grid[x][y-1]>0:
        return True
        print "true"
    else:
        return False

def step(x,y):
    ind = np.random.randint(4)
    return x+stepArray[ind][0], y+stepArray[ind][1]

for t in range(nSteps):
    landed = False
    # Put down a new particle in a location that hasn't yet been occupied
    x, y = (np.random.randint(size-3))+2, (np.random.randint(size-3))+2
    while grid[x][y]!=0:
        x, y = (np.random.randint(size-3))+2, (np.random.randint(size-3))+2
        
    # Let it roam about until it has reached its final resting place
    while landed == False:
        # if it has a neighbor, lock it in
        if hasNeighbor(x,y):
            landed = True
            grid[x][y]=255-np.linalg.norm( np.array((x,y))-np.array((size/2,size/2)) )
        # otherwise let it roam
        else:
            x, y = step(x,y)
            x, y = np.min([size-2, np.max([2, x])]), np.min([size-2, np.max([2, y])])
    # Keep tabs
    print t
    # And plot it as time goes
    if np.mod(t,200)==0:       
        plot = plt.imshow(grid,cmap="afmhot",interpolation='nearest')
        plt.draw()
        plt.show()

plt.savefig("dla_complete.svg")
plt.savefig("dla_complete.png")


 