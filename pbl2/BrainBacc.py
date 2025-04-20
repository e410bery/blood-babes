import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import constants as c
import BrainAacc as A

#used to calculate accumulation in the synaptic cleft after degradation of serotonin by MAO
#initial conditions from constants, applies decreased uptake through a transport_factor that corresponds to the dosage of DXM.

Vmax = c.Vmax_maoA  # mmol/mg*hr

enzyme_per_cell = 1 # mg/cell
Vmax_cell = Vmax * enzyme_per_cell  # mmol/ cell*hr

Km = c.Km_maoA                   # mM
Ki = c.Ki_maoi_maoA              # mM
TF = A.TF                        #dictionary of transport factors of serotonin
S0 = A.S0                        #mM
S_star0 = 0.0                    # mM
initial_conditions = [S0, S_star0]
print("S):", S0)

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
    closest_key = min(TF.keys(), key=lambda k: abs(k - t))
    transport_factor = TF[closest_key]
    I = MAOI_inhibitor(t)
    v = (Vmax * S * transport_factor) / (Km * (1+ I / Ki) + S)
    dS_dt = -v
    dP_dt = v
    return [dS_dt, dP_dt]

#solves Michaelis Menton equation when MAOI is not present
def MAO_enzyme_reaction(t, y):
    S, P = y
    closest_key = min(TF.keys(), key=lambda k: abs(k - t))
    transport_factor = TF[closest_key]
    v = (Vmax * S * transport_factor) / (Km + S)
    dS_dt = -v
    dP_dt = v
    return [dS_dt, dP_dt]


t_span = (0, 24)
t_eval = np.linspace(t_span[0], t_span[1], 500)

Deg_Ser = []
Ser = []

#solves and plots the IVP when no inhibitor is present
if c.case == 0:
    sol = solve_ivp(MAO_enzyme_reaction, t_span, initial_conditions, t_eval=t_eval, method="Radau")
    I_vals = np.zeros(t_eval.size)


#solves and plots the IVP when inhibitor is present
else:
    sol = solve_ivp(MAOI_competitive_inhibition, t_span, initial_conditions, t_eval=t_eval)
    I_vals = [MAOI_inhibitor(t) for t in t_eval]
