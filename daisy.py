#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt


KELVIN_OFFSET = 273.15
Td_min = 5 + KELVIN_OFFSET
Td_max = 40 + KELVIN_OFFSET
Td_ideal_black = 22.5 + KELVIN_OFFSET
Td_ideal_white = 22.5 + KELVIN_OFFSET
So = 1000
sigma = 5.67032e-8

alb_white = 0.75
area_white = 0.01
alb_black = 0.25
area_black = 0.01
alb_barren = 0.5
insul = 20
drate = 0.3
maxconv = 1000
Sflux_min = 0.5
Sflux_max = 1.6
Sflux_step = 0.002

fluxes = np.arange(Sflux_min, Sflux_max, Sflux_step)
area_black_vec = np.zeros_like(fluxes)
area_white_vec = np.zeros_like(fluxes)
area_barren_vec = np.zeros_like(fluxes)
Tp_vec = np.zeros_like(fluxes)

j = 0
for flux in fluxes:
    if area_black == 0:
        area_black = 0
    elif area_black < 0.01:
        area_black = 0.01

    if area_white == 0:
        area_white = 0
    elif area_white < 0.01:
        area_white = 0.01

    area_barren = 1 - (area_black + area_white)
    darea_black_old = 0
    darea_white_old = 0
    darea_barren_old = 0

    i = 0
    while i <= maxconv:
        alb_p = (area_black * alb_black
                 + area_white * alb_white
                 + area_barren * alb_barren)
        Tp = np.power(flux*So*(1-alb_p)/sigma, 0.25)
        Td_black = insul*(alb_p-alb_black) + Tp
        Td_white = insul*(alb_p-alb_white) + Tp

        if (Td_black >= Td_min
                and Td_black <= Td_max
                and area_black >= 0.01):
            birth_black = 1 - 0.003265*(Td_ideal_black-Td_black)**2
        else:
            birth_black = 0.0

        if (Td_white >= Td_min
                and Td_white <= Td_max
                and area_white >= 0.01):
            birth_white = 1 - 0.003265*(Td_ideal_white-Td_white)**2
        else:
            birth_white = 0.0

        area_black_vec[j] = area_black
        area_white_vec[j] = area_white
        area_barren_vec[j] = area_barren
        Tp_vec[j] = Tp

        darea_black = area_black*(birth_black*area_barren-drate)
        darea_white = area_white*(birth_white*area_barren-drate)

        if ((abs(darea_black-darea_black_old) < 0.000001) and
                (abs(darea_white-darea_white_old) < 0.000001)):
            area_black = area_black+darea_black
            area_white = area_white+darea_white
            area_barren = 1-(area_black+area_white)
            break
        else:
            darea_black_old = darea_black
            darea_white_old = darea_white
            area_black = area_black+darea_black
            area_white = area_white+darea_white
            area_barren = 1-(area_black+area_white)
        i += 1
    j += 1

fig, ax = plt.subplots(2, 1)
print(ax)
ax[0].plot(fluxes, 100*area_black_vec, color='black', label='black')
ax[0].plot(fluxes, 100*area_white_vec, color='red', label='white')
ax[0].set_xlabel('solar luminosity')
ax[0].set_ylabel('area (%)')
plt.legend()

ax[1].plot(fluxes, Tp_vec-KELVIN_OFFSET, color='black')
ax[1].set_xlabel('solar luminosity')
ax[1].set_ylabel('global temperature (C)')

plt.show()
