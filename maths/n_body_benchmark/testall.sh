#!/usr/bin/env bash

N_BODY=3000
N_STEP=3000
DT=0.01

./python/native_test.py $N_BODY $N_STEP $DT
sleep 1
./julia/native.jl $N_BODY $N_STEP $DT
sleep 1
./python/numba_test.py $N_BODY $N_STEP $DT
sleep 1
