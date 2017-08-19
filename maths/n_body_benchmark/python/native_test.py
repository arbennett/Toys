#!/usr/bin/env python

import sys
import time
import random
from math import sqrt


def main(size: int, nstep: int, dt: float) -> None:
    G = 6.6741e-11
    pos = [[random.random(), random.random()] for i in range(size)]
    vel = [[random.random(), random.random()] for i in range(size)]
    for t in range(nstep):
        # Update velocity
        for i in range(size):
            for j in range(size):
                if i != j:
                    dv_abs = G / (sqrt((pos[i][0] - pos[j][0])**2
                                  + (pos[i][1] - pos[j][1])**2)**3)
                    vel[j][0] += dv_abs * dt * (pos[j][0] - pos[i][0])
                    vel[j][1] += dv_abs * dt * (pos[j][1] - pos[i][1])
        # Update position
        for i in range(size):
            pos[i][0] += dt * vel[i][0]
            pos[i][1] += dt * vel[i][0]


if __name__ == '__main__':
    size, nstep, dt = sys.argv[1:]
    size = int(size)
    nstep = int(nstep)
    dt = float(dt)
    t0 = time.time()
    main(size, nstep, dt)
    t1 = time.time()
    print("PYTHON NATIVE: {} seconds".format(t1-t0))
