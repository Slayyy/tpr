#!/usr/bin/env python2
# -*- coding: utf-8 -*-


import matplotlib.pyplot as plt
from glob import glob

colors = ["red", "blue", "green", "orange"]

files = sorted(glob("*.block"))

fig, ax = plt.subplots()
ax.set_yscale("log", basey=2)
ax.set_xlabel(u"Wielkość bloku wątków")
ax.set_ylabel("Czas [s]")

x_t = []

for f, c in zip(files, colors):
    lines = open(f, "r").readlines()
    l = [l.split(",") for l in lines]
    x = [int(i[0]) for i in l]
    y = [float(i[1]) for i in l]

    if len(x_t) < len(x):
        x_t = x
        
    print x, y
    ax.scatter(x, y, color=c, label=f[6:-9])


ax.legend(loc=1)

ax.set_xticks([1] + x_t[1::2])
plt.grid(True)


plt.savefig("plot.png")
plt.show()
