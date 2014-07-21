'''
A quick script using barycentric lagrange interpolation to interpolate
a hex27-like element
'''
import numpy as np
import matplotlib.pyplot as plot

n = 3
XYZ = np.linspace(-1,1,n)
x, y, z = np.meshgrid(XYZ, XYZ, XYZ) # A 27 vertex element 

# For now just define data points manually
data = np.ones([3,3,3])
#data = np.random.random_sample([3,3,3])

# Also just defining the interpolation point manually for the moment
iPoint = [.25, .25, .25] #np.random.random_sample(3)

# Interpolate in 1 dimension
def intp1D(x , Xin):
    return Xin[0]/((1/(x-1))-(2/x)) + Xin[1]/((1/(x+1))+(1/(x-1))) + Xin[2]/((1/(x+1))-(2/x))

# Now do it for 2
def intp2D(x,y, XYin ):
    Xin2D = [ intp1D(y, XYin[:][0]), intp1D(y, XYin[:][1]), intp1D(y, XYin[:][2]) ]
    return intp1D(x, Xin2D)

# And finally we can do it for three
def intp3D(x,y,z, XYZin ):
    XYin3D = [ intp2D(x,y, XYZin[:][:][0]), intp2D(x,y, XYZin[:][:][1]), intp2D(x,y, XYZin[:][:][2])]
    return intp1D(z, XYin3D)

print intp3D(iPoint[0], iPoint[1], iPoint[2], data)    