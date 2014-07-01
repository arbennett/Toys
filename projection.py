'''
A quick mockup for projecting Nin points onto Nout points in the GLL basis

''' 
import time
import numpy as np
import numpy.polynomial.legendre as legendre
import matplotlib.pyplot as plot
from scipy.interpolate import interp1d

Nin = 10                                    # Number of data points in 
Nout = 20                                   # Number of points we want to project onto
Nfine = Nin**2                              # Number of points for plotting pretty 
Xin = np.linspace(-1,1,Nin)                 # The space of points
Fin = np.cos(Xin)                           # Evaluate some fake data
Xfine = np.linspace(-1,1,Nfine)             # Linspace for plotting pretty
Fspline = interp1d(Xin,Fin,kind='cubic')    # A spline interpolation of the data
Xout = np.linspace(-1,1,Nout-1)             # Probably don't need this since we want to plot at the GLL nodes
I = np.eye(Nout)                            # A hack for choosing the right polynomial orders 


# Build our set of GLL nodes
indices = np.zeros([Nout,1])
indices[-1] = 1                 # Corresponds to using the Nout'th Legendre polynomial
indices = np.hstack(indices)  
Xi = legendre.legroots(indices) # Something about these doesn't seem quite right - double check me


# So it would seem we do need the weights for something ( this is a terrible approximation ).
b = np.zeros([len(Xi)])
for i in range(len(Xi)):
    print legendre.legval(Xi[i], I[i])
    b[i] = Fspline(Xi[i])*legendre.legval(Xi[i],I[i])

# Plot what we got
plot.plot(Xin,Fin,'o', Xfine,Fspline(Xfine) , Xi, b,'x--')
plot.legend(['data', 'cubic', 'L2 Projection'], loc='best')
plot.draw()
plot.show()

# Don't kill the plots
#while True:
#    x=1
#    time.sleep(100)
    