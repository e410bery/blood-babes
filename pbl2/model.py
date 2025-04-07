import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import constants as c

vmax = 1 #placeholder
km = 1
ki = 1
inhibitor = 1
sub0 = 1
P0 = 1

initial_conditions = [P0, sub0]
t = np.linspace(0, 50, 50) 

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
plt.title('S* Concentration and S Concentration as a Product of Serotonin Metabolism')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

