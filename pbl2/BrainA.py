import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import constants as c


# Constants with proper units
Vmax = 23e-6        # µmol/min
Km = 1.9e-3       # mM
Ki = .0084e-3       # mM
half_life = 2.0     # hours
I0 = c.DXM_2 * (1000)  /50000     # mmol/cell (initial inhibitor)
S = c.S_4 * (1000)  /500000          # mmol/cell (substrate)
# Decay constant for inhibitor
k_decay = np.log(2) / half_life  # per hour
dserdt = []

# ODE: dP/dt = v(t)
def reaction_rate(t, P):
    I_t = I0 * np.exp(-k_decay * t)
    v = (Vmax / (1 + (I_t / Ki))) * (S / (Km + S))
    dserdt.append(v)
    return v  # µmol/min

# Time span (in hours), convert to minutes for finer resolution
t_span = (0, 24)  # hours
t_eval = np.linspace(t_span[0], t_span[1], 500)

# Solve ODE
sol = solve_ivp(reaction_rate, t_span, [S], t_eval=t_eval)

# Extract results
time_hr = sol.t
product_umol = sol.y[0]

# Plot product concentration over time
plt.figure(figsize=(8, 5))
plt.plot(time_hr, product_umol, label='[P](t)', color='green')
plt.xlabel('Time (hours)')
plt.ylabel('Product Concentration (µmol)')
plt.title('Product Formation Under Noncompetitive Inhibition')
plt.grid(True)
plt.legend()
plt.tight_layout()
#plt.show()