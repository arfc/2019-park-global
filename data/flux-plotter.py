import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('st-flux.csv')
g1 = df['group1']
g2 = df['group2']
g3 = df['group3']
g4 = df['group4']
g5 = df['group5']
g6 = df['group6']
temp = df['temp']
x = df['arc_length']

dfq = pd.read_csv('eq-flux.csv')
g1q = dfq['group1']
g2q = dfq['group2']
g3q = dfq['group3']
g4q = dfq['group4']
g5q = dfq['group5']
g6q = dfq['group6']
tempq = dfq['temp']
#x = df['arc_length']

dfl = pd.read_csv('el-flux.csv')
g1l = dfl['group1']
g2l = dfl['group2']
g3l = dfl['group3']
g4l = dfl['group4']
g5l = dfl['group5']
g6l = dfl['group6']
templ = dfl['temp']
#x = df['arc_length']

f = g1 + g2 + g3 + g4 + g5 + g6
fq = g1q + g2q + g3q + g4q + g5q + g6q
fl = g1l + g2l + g3l + g4l + g5l + g6l

fig, ax = plt.subplots()
#ax.set_xscale('log')
#ax.set_yscale('log')
ax.plot(x[:1000], f[:1000], label=r'Start-up')
ax.plot(x[:1000], fl[:1000], label=r'Early-life')
ax.plot(x[:1000], fq[:1000], label=r'Equilibrium')
ax.plot(0, 8.6e15, label=r'Fiorina et al.', marker='x')
#ax.plot(ts[1:], gs1[1:], label=r'Step')
ax.set_xlabel(r'Radius [cm]')
ax.set_ylabel(r'Total neutron flux [# cm$^{-2}$ s$^{-1}$]')
ax.legend()
plt.savefig('totalflux.png', dpi=400)

fig, ax = plt.subplots()
#ax.set_xscale('log')
#ax.set_yscale('log')
ax.plot(x[:1000], temp[:1000], label=r'Start-up')
ax.plot(x[:1000], templ[:1000], label=r'Early-life')
ax.plot(x[:1000], tempq[:1000], label=r'Equilibrium')
#ax.plot(ts[1:], gs1[1:], label=r'Step')
ax.set_xlabel(r'Radius [cm]')
ax.set_ylabel(r'Temperature [K]')
ax.legend()

fig, ax = plt.subplots()
#ax.set_xscale('log')
#ax.set_yscale('log')
ax.plot(x[:1000], g1[:1000], label=r'Group 1')
ax.plot(x[:1000], g2[:1000], label=r'Group 2')
ax.plot(x[:1000], g3[:1000], label=r'Group 3')
ax.plot(x[:1000], g4[:1000], label=r'Group 4')
ax.plot(x[:1000], g5[:1000], label=r'Group 5')
ax.plot(x[:1000], g6[:1000], label=r'Group 6')
#ax.plot(ts[1:], gs1[1:], label=r'Step')
ax.set_xlabel(r'Radius [cm]')
ax.set_ylabel(r'Neutron group flux [# cm$^{-2}$ s$^{-1}$]')
ax.legend()
plt.savefig('stflux.png', dpi=400)

fig, ax = plt.subplots()
#ax.set_xscale('log')
#ax.set_yscale('log')
ax.plot(x[:1000], g6[:1000], label=r'Start-up')
ax.plot(x[:1000], g6l[:1000], label=r'Early-life')
ax.plot(x[:1000], g6q[:1000], label=r'Equilibrium')
#ax.plot(ts[1:], gs1[1:], label=r'Step')
ax.set_xlabel(r'Radius [cm]')
ax.set_ylabel(r'Neutron group 6 flux [# cm$^{-2}$ s$^{-1}$]')
ax.legend()
plt.savefig('grp6flux.png', dpi=400)
