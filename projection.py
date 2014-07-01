'''
A quick mockup for projecting n points onto m points in the GLL basis

''' 
import time
import numpy as np
import numpy.polynomial.legendre as legendre
import matplotlib.pyplot as plot
from scipy.interpolate import interp1d

Nin = 10
Nout = 20
Nfine = Nin**2
Xin = np.linspace(-1,1,Nin)
Fin = np.cos(Xin)
Xfine = np.linspace(-1,1,Nfine)
Fspline = interp1d(Xin,Fin,kind='cubic')
Xout = np.linspace(-1,1,Nout-1)
I = np.eye(Nout)

# Build our set of GLL nodes
indices = np.zeros([Nout,1])
indices[-1] = 1
indices = np.hstack(indices)
Xi = legendre.legroots(indices) # Still need to find out how to add +-1 at endpoints 

b = np.zeros([len(Xi)])
for i in range(len(Xi)):
    print legendre.legval(Xi[i], I[i])
    b[i] = Fspline(Xi[i])*legendre.legval(Xi[i],I[i])

print len(Xout), len(Xi)
plot.plot(Xin,Fin,'o', Xfine,Fspline(Xfine) , Xout, b,'x--')
plot.legend(['data', 'cubic', 'L2 Projection'], loc='best')
plot.draw()
plot.show()

# Don't kill the plots
#while True:
#    x=1
#    time.sleep(100)
    