import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import constants as c
import BrainA as A
import BrainB as B
import math

initial = 0.0013480393692862748;
t = np.linspace(0, 24, 500)
S_4 = []
S_9 = B.sol.y[0] - B.sol.y[1]
S_5 = B.sol.y[1]

for time in t:  
    S_4.append(c.S_4 * 1000)

acc = (S_9 - S_5 + S_4) * 500000 #accumulation in the brain

print(acc[1:500:50])
if not (math.isclose(acc[0], initial, rel_tol=1e-18)):
    print("true")
    translate = initial - acc[0]
    for i in range(acc.size):
        acc[i] = acc[i]+translate
print(acc[1:500:50])

plt.figure(figsize = (10, 8))
plt.plot(t, acc)
#plt.show()

