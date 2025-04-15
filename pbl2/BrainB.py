import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import constants as c
import BrainA as A


Vmax = c.Vmax_maoA               # mmol/mg*hr

enzyme_per_cell = 1 # mg/cell #where did this come from? little confusing
Vmax_cell = Vmax * enzyme_per_cell  # mmol/ cell*hr

Km = c.Km_maoA                   # mM
Ki = c.Ki_maoi_maoA              # mM
TF = A.TF                        #dictionary of transport factors of serotonin
S0 = A.S0             # mM, for each time value over 24 hours (dictionary= time:ser_sert)
S_star0 = 0.0                    # mM
initial_conditions = [S0, S_star0]

def MAOI_inhibitor(t):
    decay = 0.5 ** (t / 2)
    MAOI_mg = (c.MAOI_in) * decay
    MAOI_mol = MAOI_mg / 1000 / c.MAOI_MM
    MAOI_mol_cell = MAOI_mol / c.S_cells * 1000 #mmol/cell
    return MAOI_mol_cell #mol/cell

def MAOI_inhibitor_2(t):
    decay = 0.5 ** (t / 2)
    MAOI_mg = 60 * decay
    MAOI_mol = MAOI_mg / 1000 / c.MAOI_MM
    MAOI_mol_cell = MAOI_mol / c.S_cells * 1000 #mmol/cell
    return MAOI_mol_cell

def MAOI_competitive_inhibition(t, y):
    S, P = y
    closest_key = min(TF.keys(), key=lambda k: abs(k - t))
    transport_factor = TF[closest_key]
    I = MAOI_inhibitor(t)
    #v = Vmax_cell * S / (Km * (1 + I / Ki) + S)
    v = (Vmax * S * transport_factor) / (Km * (1+ I / Ki) + S)
    dS_dt = -v
    dP_dt = v
    return [dS_dt, dP_dt]

def MAO_enzyme_reaction(t, y):
    S, P = y
    closest_key = min(TF.keys(), key=lambda k: abs(k - t))
    transport_factor = TF[closest_key]
    #v = (Vmax_cell * S) / (Km + S)  # mmol/cell/day
    v = (Vmax * S * transport_factor) / (Km + S)
    dS_dt = -v
    dP_dt = v
    return [dS_dt, dP_dt]


t_span = (0, 24) #see longer term equations in action
t_eval = np.linspace(t_span[0], t_span[1], 500)

if c.case == 0:
    sol = solve_ivp(MAO_enzyme_reaction, t_span, initial_conditions, t_eval=t_eval, method="Radau")
    plt.figure(figsize=(10,8))
    plt.plot(sol.t, sol.y[0], label='[Serotonin]', color='tab:blue')
    plt.plot(sol.t, sol.y[1], label='[Degraded Serotonin]', color='tab:green')
    plt.ylabel('Concentration (mmol/cell)')
    plt.title('Serotonin Breakdown Over 24 Hours')
    plt.legend()
    plt.grid(True)
    plt.savefig("pbl2/graphs/brainB_case0.png")
    S_star_8 = sol.y[1,-1]  #total amount of S_star created per day
    print(S_star_8)

else:
    sol = solve_ivp(MAOI_competitive_inhibition, t_span, initial_conditions, t_eval=t_eval)
    I_vals = [MAOI_inhibitor(t) for t in t_eval]

    plt.figure(figsize=(10, 8))
    plt.subplot(2, 1, 1)
    plt.plot(sol.t, sol.y[0], label='[Serotonin]', color='tab:blue')
    plt.plot(sol.t, sol.y[1], label='[Degraded Serotonin]', color='tab:green')
    plt.ylabel('Concentration (mmol/cell)')
    plt.title('Serotonin Breakdown Over 24 Hours')
    plt.legend()
    plt.grid(True)
    plt.subplot(2, 1, 2)
    plt.plot(t_eval, I_vals, label='[MAOI]', color='tab:purple', linestyle='--')
    plt.xlabel('Time (hours)')
    plt.ylabel('Concentration (mmol/cell)')
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    filepath = "pbl2/graphs/brainB_case" + str(c.case) + ".png"
    plt.savefig(filepath)
    S_star_8 = sol.y[1,-1]  #total amount of S_star created per day
    print(S_star_8)


