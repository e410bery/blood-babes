'''
import numpy as np
import matplotlib.pyplot as plt
import constants as c
import BrainA as A
import BrainB as B
from scipy.integrate import solve_ivp
from scipy.interpolate import interp1d

# Pull in precomputed rates
dserA = np.array(A.dserdt)
dserB = np.array(B.dserdt)
dstar = np.array(B.dstardt)

# Time points
t = np.linspace(0, 24, 500)
t_span = (t[0], t[-1])

# ✅ Compute the rate array before using it
daccdt = dserA + (dserB - dstar)

# ✅ Create interpolation function from time and rate
dacc_func = interp1d(t, daccdt, bounds_error=False, fill_value="extrapolate")

# Define ODE
def daccdt_ode(t, y):
    return dacc_func(t)

# Initial condition
S0 = c.S_4 * 1000 / 500000

# Solve the ODE
acc = solve_ivp(daccdt_ode, t_span, [S0], t_eval=t)

# Optional: Plot
plt.figure(figsize=(8, 5))
plt.plot(t, acc.y[0], label='Accumulated Serotonin')
plt.xlabel('Time (hours)')
plt.ylabel('Concentration (mmol/cell)')
plt.title('Total Serotonin Accumulation Over Time')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
'''
    


'''
constantS_9 = B.sol.y[0,0] - B.sol.y[1,-1]
S_9 = []
for i in range(t.size):
    S_9.append(constantS_9)

S_4 = []
for i in range(t.size):
    S_4.append(c.S_4*1000/500000)

S_5 = A.product_umol/1000

#for time in t:  
#    S_4.append(c.S_4 * 1000)

acc = (np.array(S_9) + np.array(S_4) - S_5) * 500000 #accumulation in the brain
'''

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import constants as c
import BrainAacc as A
import BrainBacc as B
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