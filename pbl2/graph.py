import constants as c
import equations as e
import model as m
import matplotlib.pyplot as plt
import numpy as np

#check inhibitor conc:
time = np.linspace(0,71, 72)
inh = np.zeros(time.size)
for t in time:
    inh = e.inhibitor(time)

plt.plot(time, inh)
plt.savefig("pbl2/graphs/MAOIconc.png")