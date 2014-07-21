#!/bin/python3

import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plot

gridx = np.linspace(-1,1,3)
gridy = np.linspace(-1,1,3)

data = np.random.random_sample([3,3])

fig = plot.figure()
ax = fig.add_subplot(111, projection='3d')

for i in range(3):
	for j in range(3):
		#data[i][j]=i
		ax.scatter(gridx[i],gridy[j],data[i][j],c='r')

print(gridx,gridy,data)

N=250
xinterps=np.zeros(N)
yinterps=np.zeros(N)
dataInterps=np.zeros(N)
for i in range(N):
	interpx=2*np.random.rand()-1
	interpy=2*np.random.rand()-1
	xinterps[i]=interpx
	yinterps[i]=interpy
	if interpx < 0 and  interpy < 0:
		A1=(interpx-gridx[0])*(interpy-gridy[0])
		A2=(gridx[1]-interpx)*(interpy-gridy[0])
		A3=(interpx-gridx[0])*(gridy[1]-interpy)
		A4=(gridx[1]-interpx)*(gridy[1]-interpy)
		dataInterps[i]=A1*data[1][1] + A2*data[0][1] + A3*data[1][0] + A4*data[0][0]
	elif interpx < 0 and interpy >= 0:
                A1=(interpx-gridx[0])*(interpy-gridy[1])
                A2=(gridx[1]-interpx)*(interpy-gridy[1])
                A3=(interpx-gridx[0])*(gridy[2]-interpy)
                A4=(gridx[1]-interpx)*(gridy[2]-interpy)
                dataInterps[i]=A1*data[1][2] + A2*data[0][2] + A3*data[1][1] + A4*data[0][1]
	elif interpx >= 0 and interpy < 0:
                A1=(interpx-gridx[1])*(interpy-gridy[0])
                A2=(gridx[2]-interpx)*(interpy-gridy[0])
                A3=(interpx-gridx[1])*(gridy[1]-interpy)
                A4=(gridx[2]-interpx)*(gridy[1]-interpy)
                dataInterps[i]=A1*data[2][1] + A2*data[1][1] + A3*data[2][0] + A4*data[1][0]
	elif interpx >= 0 and interpy >= 0:
                A1=(interpx-gridx[1])*(interpy-gridy[1])
                A2=(gridx[2]-interpx)*(interpy-gridy[1])
                A3=(interpx-gridx[1])*(gridy[2]-interpy)
                A4=(gridx[2]-interpx)*(gridy[2]-interpy)
                dataInterps[i]=A1*data[2][2] + A2*data[1][2] + A3*data[2][1] + A4*data[1][1]
	ax.scatter(interpx,interpy,dataInterps[i])


ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plot.show()


