#!/bin/python
'''
A quick mockup for projecting Nin points onto Nout points in the GLL basis
''' 
import time
import numpy as np
import numpy.polynomial.legendre as legendre
import matplotlib.pyplot as plot
from scipy.interpolate import interp1d

Nin = 10                                    # Number of data points in 
Nout = 30                                    # Number of points we want to project onto
Nfine = Nin**2                              # Number of points for plotting pretty 
Xin = np.linspace(-1,1,Nin)                 # The space of points
Fin = np.cos(20*Xin)+np.sin(7*Xin)          # Evaluate some fake data
Xfine = np.linspace(-1,1,Nfine)             # Linspace for plotting pretty
Fspline = interp1d(Xin,Fin,kind='cubic')    # A spline interpolation of the data
Xout = np.linspace(-1,1,Nout-1)             # Probably don't need this since we want to plot at the GLL nodes
I = np.eye(Nout)                            # A hack for choosing the right polynomial orders 
zero = np.zeros(Nout-1)

# Build our set of GLL nodes
pts = legendre.legroots(legendre.legder(I[-1])) # GLL points
Xi = [-1, list(pts), 1]
Xi = np.hstack(Xi)
print "GLL Points:", Xi

# Build the weight set
weights = np.zeros([len(Xi)])
for i in range(len(Xi)-2):
    weights[i+1] = 2/((Nout)*(Nout-1)*(legendre.legval(Xi[i+1],I[-1]))**2)

weights[0]=2.0/((Nout)*(Nout-1))
weights[-1]=weights[0]
print "GLL Weights:", weights


''' 
# Construct b using nearest known data points
b = np.zeros(len(Xi))
for i in range(len(Xi)):          # For each data point
    for j in range(len(Xi)):      # Need to sum over all basis functions
            b[i]+=legendre.legval(Xi[i],I[j])*Fin[ np.abs(Xin-Xi[i]).argmin() ] 
''' 
# Construct b using a spline interpolation evaluated at the quadrature points
b = np.zeros(len(Xi))
for i in range(len(Xi)):
    for j in range(len(Xi)):
        b[i]+=legendre.legval(Xi[i],I[j])*Fspline(Xi[i])
        
print b
#'''    
# Plot what we got
plot.plot(Xin,Fin,'o-' , Xi, b,'rx-')
plot.legend(['Data', 'L2 Projection'], loc='best')
plot.draw()
plot.show()

# Don't kill the plots
#while True:
#    x=1
#    time.sleep(100)
    