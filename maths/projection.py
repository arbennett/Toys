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
Nout = 50                                    # Number of points we want to project onto
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
#print "GLL Points:", Xi

# Build the weight set
weights = np.zeros([len(Xi)])
for i in range(len(Xi)-2):
    weights[i+1] = 2/((Nout)*(Nout-1)*(legendre.legval(Xi[i+1],I[-1]))**2)

weights[0]=2.0/((Nout)*(Nout-1))
weights[-1]=weights[0]
#print "GLL Weights:", weights

# Calculate the norms    
norms = np.zeros(Nout)
for i in range(Nout):
    for k in range(Nout):
        norms[i]+=weights[k]*legendre.legval(Xi[k],I[i])**2
        
# Calculate the function coefficients        
c = np.zeros(Nout)
for i in range(Nout):
    for k in range(Nout):
        c[i]+=Fspline(Xi[k])*legendre.legval(Xi[k],I[i])*weights[k]   # Construct with a spline interpolation of input data
        #c[i]+=Fin[ np.abs(Xin-Xi[k]).argmin() ]*legendre.legval(Xi[k],I[i])*weights[k] # Construct with nearest known input data point
    c[i]=c[i]/norms[i]

uh=0
for i in range(Nout):
    uh+=c[i]*legendre.Legendre.basis(i)
    

# Plot what we got
#plot.plot(Xin,Fin,'o-' , Xi, b,'rx-')
plot.plot(Xin,Fin,'o-' , Xi, uh(Xi), 'rx-')
plot.legend(['Data', 'L2 Projection'], loc='best')
plot.draw()
plot.show()

# Don't kill the plots
#while True:
#    x=1
#    time.sleep(100)
    