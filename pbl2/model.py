import constants as c
import equations as e


import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

k1 = 1e4        # L/(mol-sec)
k_r1 = 0.1  # 1/sec
k2 = 4e3        # L/(mol-sec)
k_r2 = 0.001  # 1/sec
Avo = 6.022e23
R10 = (10000 * 1e5 * 1000) / Avo #mol/L
R20 = (1000 * 1e5 * 1000) / Avo #mol/L
L = 1e-6  # M
R1L0 = 0
R2L0 = 0

initial_conditions = [R1L0, R2L0, R10, R20, L]
t = np.linspace(0, 1000, 1000) 

def solver(t,y):
    R1L, R2L, R1, R2, L = y
    dR1L_dt = k1 * L * R1 - k_r1 * R1L
    dR2L_dt = k2 * L * R2 - k_r2 * R2L
    dR1_dt = -k1 * L * R1 + k_r1 * R1L
    dR2_dt = -k2 * L * R2 + k_r2 * R2L
    dL_dt = -dR1L_dt - dR2L_dt 
    return[dR1L_dt, dR2L_dt, dR1_dt, dR2_dt, dL_dt]

solution = solve_ivp(solver, [0,1000], initial_conditions, t_eval=t, method='BDF')
plt.plot(t,solution.y[0], label='[R1L]')
plt.plot(t, solution.y[1], label='[R2L]')
plt.plot(t, solution.y[2], label='[R1]')
plt.plot(t, solution.y[3], label='[R2]')
plt.xlabel('Time (sec)')
plt.ylabel('Concentration (receptors/L) or (bound receptors/L)')
plt.title('Receptor-Ligand Concentrations over Time')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

