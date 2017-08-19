#!/usr/bin/env bash

N_BODY=1000
N_STEP=100
DT=0.01

#./python/native_test.py $N_BODY $N_STEP $DT
sleep 1
./julia/native.jl $N_BODY $N_STEP $DT
sleep 1
./python/numba_test.py $N_BODY $N_STEP $DT
sleep 1
gfortran -O1 fortran/allocatable.f90 -o fortran/allocatable
sleep 1
./fortran/allocatable $N_BODY $N_STEP $DT
