import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import constants as c

def inhibitor(time):
    time = time%24
    inh_mg = c.MAOI_2*(0.5)**(time/2) - 0.0146
    inh_moles = inh_mg*(1/1000)*(1/133.19)
    return inh_moles

time = np.linspace(0,50,50)

vmax = c.Vmax_maoA 
km = c.Km_maoA
ki = c.Ki_maoi_maoA
inhibitor = inhibitor(time)
sub0 = c.Serotonin_conc_B
P0 = 0

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

