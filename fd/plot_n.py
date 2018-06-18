#!/usr/bin/env python2

import matplotlib.pyplot as plt
from glob import glob

colors = ["red", "blue", "green", "orange"]

files = sorted(glob("*.res"))

fig, ax = plt.subplots()
ax.set_xlabel("Rozmiar siatki")
ax.set_ylabel("Czas [s]")
ax.set_xscale("log", basex=2)

x_t = []

for f, c in zip(files, colors):
    lines = open(f, "r").readlines()
    l = [l.split(",") for l in lines]
    x = [int(i[0]) for i in l]
    y = [float(i[1]) for i in l]

    if len(x_t) < len(x):
        x_t = x
        
    print x, y
    ax.scatter(x, y, color=c, label=f[6:-7])


ax.legend(loc=2)

ax.set_xticks(x_t)
plt.grid(True)


plt.savefig("plot.png")
plt.show()
