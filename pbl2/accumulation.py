import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import constants as c
import BrainA as A
import BrainB as B


t = np.linspace(0, 24, 500)
S_4 = []
S_9 = B.sol.y[0] - B.sol.y[1]
S_5 = B.sol.y[1]

for time in t:  
    S_4.append(c.S_4 * 1000)

acc = (S_9 - S_5 + S_4) * 500000 #accumulation in the brain


print(acc)

plt.figure(figsize = (10, 8))
plt.plot(t, acc)
plt.show()

