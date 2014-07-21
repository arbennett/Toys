"""
This is my first attempt at understanding 
    the Lattice Boltzmann model for CFD
    
    Author: Andrew Bennett
    Date: July 19, 2013

"""
import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA  

# Flow Parameters

T = 15000                   # Time Steps
R = 300.0                   # Reynolds Number
nx = 150                    # x size
ny = 75                     # y size
ly = ny-1.0                 # "fixed" y size
q = 9                       # number of directions
ox1 = nx/4 ; ox2 = nx/4 ; oy1 = ny/3 ; oy2 =2*ny/3 ; r1 = ny/12 ; r2 = ny/8 # Obstruction coords
u = 0.05                    # ~velocity
nu = (u*ny)/(10*R)          # ~kinematic viscosity
tau = (3.*nu+0.5)           # Relaxation Parameter

c = np.array([(x,y) for x in [0,-1,1] for y in [0,-1,1]])           # lattice directions
t = 1./36. * np.ones(q)                                             # lattice weights
t[np.asarray([LA.norm(ci)<1.1 for ci in c])] = 1./9.; t[0] = 4./9.  # setting quadrature abscissas
noslip = [c.tolist().index((-c[i]).tolist()) for i in range(q)]     # reverse flow direction at walls/obstacles
i1 = np.arange(q)[np.asarray([ci[0]<0 for ci in c])]    # in lattice 9 points     i1  i3  i3
i2 = np.arange(q)[np.asarray([ci[0]==0 for ci in c])]   # are arranged in         i1  i2  i3
i3 = np.arange(q)[np.asarray([ci[0]>0 for ci in c])]    # 3 columns like :        i1  i2  i3

#    Anonymous Functions
sumpop = lambda fin: np.sum(fin,axis=0) # used to calculate density
obst1 = np.fromfunction(lambda x,y: (x-ox1)**2+(y-oy1)**2<r1**2, (nx,ny))
obst2 = np.fromfunction(lambda x,y: (x-ox2)**2+(y-oy2)**2<r2**2, (nx,ny))
obstacles = obst1 + obst2

#    The equilibrium function using the BGK model collision function
def equilibrium(p,u):
    cu = 3.0 * np.dot(c,u.transpose(1,0,2))
    feq = np.zeros((q,nx,ny))
    for i in range(q): feq[i,:,:] = p*t[i]*(1.+cu[i]+0.5*cu[i]**2-3./2.*(u[0]**2+u[1]**2)) # calculate integral using quadrature
    return feq

vel = np.fromfunction(lambda d,x,y: (1-d)*u*(1.0+1e-4*np.sin(y/ly*2*np.pi)),(2,nx,ny)) # velocity profile coming in
feq = equilibrium(1.0,vel) 
fin = feq.copy() 

#    Make time go forward
for time in range(T):
    print(time)
    fin[i1,-1,:] = fin[i1,-2,:] # right wall boundary condition
    p = sumpop(fin) # density/velocity calc
    u = np.dot(c.transpose(),fin.transpose((1,0,2)))/p
    
    u[:,0,:] = vel[:,0,:] # left wall initial condition
    p[0,:] = 1./(1.-u[0,0,:]) * (sumpop(fin[i2,0,:]) + 2.*sumpop(fin[i1,0,:]))
    
    feq = equilibrium(p,u)
    fin[i3,0,:] = fin[i1,0,:] + feq[i3,0,:] - feq[i1,0,:]
    
    # output states tend towards equilibrium proportional to 1/tau
    fout = fin - (1/tau) * (fin-feq)
    
    # make fluids rebound off of obstacles
    for i in range(q): 
        fout[i,obstacles] = fin[noslip[i],obstacles]
    
    # make fluid move "forward"    
    for i in range(q):
        fin[i,:,:] = np.roll(np.roll(fout[i,:,:],c[i,0],axis=0),c[i,1],axis=1)  # the roll function saved me tons of code
    
    # plot it (then put together in a movie later, pythons dynamic plotting is its downfall thus far)    
    if(time%100==0):
        plt.clf(); plt.imshow(np.sqrt(u[0]**2+u[1]**2).transpose(),cmap=plt.get_cmap('jet'))
        plt.savefig("vel."+str(time/100).zfill(4)+".png") 
        