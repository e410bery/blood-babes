import constants as c
import equations as e


import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

vmax = 
km = 
ki = 
inhibitor = 
sub0 = 
P0 = 

initial_conditions = [P0, sub0]
t = np.linspace(0, 1000, 1000) 

def solver(t,y):
    P, sub = y
    dP_dt = (vmax * sub) / (km * (1 + inhibitor / ki) + sub)
    dsub_dt = -((vmax*sub) / (km * (1 + inhibitor / ki) + sub))
    return[dP_dt, dsub_dt]

solution = solve_ivp(solver, [0,1000], initial_conditions, t_eval=t, method='BDF')
plt.plot(t, solution.y[0], label='[S*]')
plt.plot(t, solution.y[1], label='[S]')
plt.xlabel('Time (sec)')
plt.ylabel('Concentration')
plt.title('S* Concentration in the Synaptic Cleft Over Time')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()