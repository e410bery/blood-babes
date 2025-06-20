import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import constants as c
import BrainA as A

#used to calculate and graph the amount of serotonin and degraded serotonin present in the serotonin degradation box over time
#initial conditions come from output of brainA

Vmax = c.Vmax_maoA               # mmol/mg*hr

enzyme_per_cell = 1 # mg/cell
Vmax_cell = Vmax * enzyme_per_cell  # mmol/ cell*hr

Km = c.Km_maoA                   # mM
Ki = c.Ki_maoi_maoA              # mM
S0 = A.product_mmol[-1]          # mM
S_star0 = 0.0                    # mM
initial_conditions = [S0, S_star0]
dserdt = []
dstardt = []


#decay of MAOI
def MAOI_inhibitor(t):
    decay = 0.5 ** (t / 2)
    MAOI_mg = (c.MAOI_in) * decay
    MAOI_mol = MAOI_mg / 1000 / c.MAOI_MM
    MAOI_mol_cell = MAOI_mol / c.S_cells * 1000 #mmol/cell
    return MAOI_mol_cell #mol/cell

#solves Michaelis Menton equation when MAOI is present
def MAOI_competitive_inhibition(t, y):
    S, P = y
    I = MAOI_inhibitor(t)
    v = (Vmax * S) / (Km * (1+ I / Ki) + S)
    dS_dt = -v
    dserdt.append(dS_dt)
    dP_dt = v
    dstardt.append(dP_dt)
    return [dS_dt, dP_dt]

#solves Michaelis Menton equation when MAOI is not present
def MAO_enzyme_reaction(t, y):
    S, P = y
    v = (Vmax * S) / (Km + S)
    dS_dt = -v
    dserdt.append(dS_dt)
    dP_dt = v
    dstardt.append(dP_dt)
    return [dS_dt, dP_dt]


t_span = (0, 24) 
t_eval = np.linspace(t_span[0], t_span[1], 500)


#solves the IVP when no inhibitor is present
if c.case == 0:
    sol = solve_ivp(MAO_enzyme_reaction, t_span, initial_conditions, t_eval=t_eval)
    I_vals = np.zeros(t_eval.size)
    
#solves the IVP when inhibitor is present
else:
    sol = solve_ivp(MAOI_competitive_inhibition, t_span, initial_conditions, t_eval=t_eval)
    I_vals = [MAOI_inhibitor(t) for t in t_eval]
