import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('losca-st_out.csv')
t = df['time']
g1 = df['group1_current']
g2 = df['group2_current']
g3 = df['group3_current']
g4 = df['group4_current']
g5 = df['group5_current']
g6 = df['group6_current']
temp = df['temp_fuel']
heat = df['heat']
#maxe = df['max_temp_fuel']

dfl = pd.read_csv('losca-el_out.csv')
tl = dfl['time']
g1l = dfl['group1_current']
g2l = dfl['group2_current']
g3l = dfl['group3_current']
g4l = dfl['group4_current']
g5l = dfl['group5_current']
g6l = dfl['group6_current']
templ = dfl['temp_fuel']
heatl = dfl['heat']

dfq = pd.read_csv('losca-eq_out.csv')
tq = dfq['time']
g1q = dfq['group1_current']
g2q = dfq['group2_current']
g3q = dfq['group3_current']
g4q = dfq['group4_current']
g5q = dfq['group5_current']
g6q = dfq['group6_current']
tempq = dfq['temp_fuel']
heatq = dfq['heat']

fig, ax = plt.subplots()
ax.set_xscale('log')
#ax.set_yscale('log')
ax.plot(t[1:], g1[1:], label=r'Start-up')
ax.plot(tl[1:], g1l[1:], label=r'Early-life')
ax.plot(tq[1:], g1q[1:], label=r'Equilibrium')
#ax.plot(ts[1:], gs1[1:], label=r'Step')
ax.set_xlabel(r'Time [s]')
ax.set_ylabel(r'Integral group 1 flux [# cm$^{-2}$ s$^{-1}$]')
ax.legend()

fig, ax = plt.subplots()
#ax.set_xscale('log')
#ax.set_yscale('log')
ax.plot(t[1:], temp[1:] - temp[1], label=r'Start-up')
ax.plot(tl[1:], templ[1:] - templ[1], label=r'Early-life')
ax.plot(tq[1:], tempq[1:] - tempq[1], label=r'Equilibrium')
#ax.plot(te[1:], maxe[1:])
#ax.plot(ts[1:], temps[1:], label=r'Step')
ax.set_xlabel(r'Time [s]')
ax.set_ylabel(r'Rise in average fuel temperature in core [K]')
ax.legend()
plt.savefig('loscatemp.png', dpi=400)

fig, ax = plt.subplots()
ax.plot(t[1:], heat[1:] / max(heat), label=r'Start-up')
ax.plot(tl[1:], heatl[1:] / max(heatl), label=r'Early-life')
ax.plot(tq[1:], heatq[1:] / max(heatq), label=r'Equilibrium')
#ax.plot(ts[1:], heats[1:], label=r'Step')
ax.set_xlabel(r'Time [s]')
ax.set_ylabel(r'Power [%]')
ax.legend()
#ax.set_xscale('log')
#ax.set_yscale('log')
plt.savefig('loscaheat.png', dpi=400)