import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import constants as c

c.case = 1

Vmax = c.Vmax_maoA               # mmol/mg*hr

enzyme_per_cell = 1  # mg/cell 
Vmax_cell = Vmax * enzyme_per_cell / 1000  # mol/cell/day

Km = c.Km_maoA                   # mM
Ki = c.Ki_maoi_maoA              # mM
S0 = c.Serotonin_conc_B          # mM
S_star0 = 0.0                    # mM
initial_conditions = [S0, S_star0]


def MAOI_inhibitor(t):
    decay = 0.5 ** (t / 2)
    MAOI_mg = (c.MAOI_in) * decay
    MAOI_mol = MAOI_mg / 1000 / c.MAOI_MM
    MAOI_mol_cell = MAOI_mol / c.S_cells
    return MAOI_mol_cell 

def MAOI_inhibitor_2(t):
    decay = 0.5 ** (t / 2)
    MAOI_mg = 60 * decay
    MAOI_mol = MAOI_mg / 1000 / c.MAOI_MM
    MAOI_mol_cell = MAOI_mol / c.S_cells
    return MAOI_mol_cell

def MAOI_competitive_inhibition(t, y):
    S, P = y
    I = MAOI_inhibitor(t)
    v = Vmax_cell * S / (Km * (1 + I / Ki) + S)
    dS_dt = -v
    dP_dt = v
    return [dS_dt, dP_dt]

def MAO_enzyme_reaction(t, y):
    S, P = y
    v = (Vmax_cell * S) / (Km + S)  # mol/cell/day
    dS_dt = -v
    dP_dt = v
    return [dS_dt, dP_dt]



t_span = (0, 24)
t_eval = np.linspace(t_span[0], t_span[1], 500)

if c.case == 0:
    sol = solve_ivp(MAO_enzyme_reaction, t_span, initial_conditions, t_eval=t_eval)
    plt.figure(figsize=(10,8))
    plt.plot(sol.t, sol.y[0], label='[Serotonin]', color='tab:blue')
    plt.plot(sol.t, sol.y[1], label='[Degraded Serotonin]', color='tab:green')
    plt.ylabel('Concentration (mol/cell)')
    plt.title('Serotonin Breakdown Over 24 Hours')
    plt.legend()
    plt.grid(True)
    plt.show()
    S_star_8 = sol.y[1,-1]  #total amount of S_star created per day
    print(S_star_8)

else:
    sol = solve_ivp(MAOI_competitive_inhibition, t_span, initial_conditions, t_eval=t_eval)
    I_vals = [MAOI_inhibitor_2(t) for t in t_eval]

    plt.figure(figsize=(10, 8))
    plt.subplot(2, 1, 1)
    plt.plot(sol.t, sol.y[0], label='[Serotonin]', color='tab:blue')
    plt.plot(sol.t, sol.y[1], label='[Degraded Serotonin]', color='tab:green')
    plt.ylabel('Concentration (mol/cell)')
    plt.title('Serotonin Breakdown Over 24 Hours')
    plt.legend()
    plt.grid(True)
    plt.subplot(2, 1, 2)
    plt.plot(t_eval, I_vals, label='[MAOI]', color='tab:purple', linestyle='--')
    plt.xlabel('Time (hours)')
    plt.ylabel('Concentration (mol/cell)')
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.show()
    S_star_8 = sol.y[1,-1]  #total amount of S_star created per day
    print(S_star_8)
