import constants as c
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

time = c.time

#enzyme reactions:
#vmax also = k2*E0
def enzyme_subtrate(sub, vmax, km) :
    return (vmax * sub) / (km + sub)

#finds the concentration of the inhibitor in moles as a function of time in hours
def inhibitor(time):
    time = time%24
    inh_mg = c.MAOI_conc*(0.5)**(time/2) - 0.0146
    inh_moles = inh_mg*(1/1000)*(1/133.19)
    return inh_moles

#m-m model to find rate of product concentration
#time in hours 
def competitive_inhibition(sub, vmax, km, ki, time):
    return (vmax * sub) / (km * (1 + inhibitor(time) / ki) + sub)

def noncompetitive_inhibition(sub, vmax, km, inhibitor, ki):
    return (vmax * sub) / ((km + sub) * (1 + inhibitor / ki))


'''
#check inhibitor conc:
time = np.linspace(0,71, 72)
inh = np.zeros(time.size)
for t in time:
    inh = inhibitor(time)

plt.plot(time, inh)
plt.show()
'''

#Brain B Model: Serotonin Metabolism #delete later we r not using for real
def enzyme_substrate(sub, vmax, km) :
    return (vmax * sub) / (km + sub)



#Brain B Model: 

#case 0: No MAOI 
dS_maoA = enzyme_substrate(c.Serotonin_conc_B, c.Vmax_maoA, c.Km_maoA) #returns ds*/dt
dS_maoB = enzyme_substrate(c.Serotonin_conc_B, c.Vmax_maoB, c.Km_maoB) #returns ds*/dt
dS_star_dt = dS_maoA + dS_maoB

#Plotting S* vs. S concentration case 0
if c.case == 0: 
    sub0 = c.Serotonin_conc_B 
    P0 = 0
    initial_conditions = [P0, sub0]
    t = np.linspace(0, 50, 50) 

    def solver(t,y):
        S_star, sub = y
        dS_maoA = enzyme_substrate(c.Serotonin_conc_B, c.Vmax_maoA, c.Km_maoA) #returns ds*/dt
        dS_maoB = enzyme_substrate(c.Serotonin_conc_B, c.Vmax_maoB, c.Km_maoB) #returns ds*/dt
        dS_star_dt = dS_maoA + dS_maoB
        dS_dt = -dS_star_dt
        return[dS_star_dt, dS_dt]
    S_star_8 = solve_ivp(solver, [0,1000], initial_conditions, t_eval=t, method='BDF')
#cases 1-7
else:  
    sub0 = c.Serotonin_conc_B
    P0 = 0
    initial_conditions = [P0, sub0]
    t = np.linspace(0, 7, 7)

    def solver(t,y):
        S_star, sub = y
        dS_maoi_maoA = (c.Vmax_maoA * sub ) / (c.Km_maoA * (1 + c.MAOI_2 / c.Ki_maoi_maoA) + sub)
        dS_maoi_maoB = (c.Vmax_maoB * sub ) / (c.Km_maoB * (1 + c.MAOI_2 / c.Ki_maoi_maoB) + sub)
        dS_star_dt = dS_maoi_maoA + dS_maoi_maoB
        dS_dt = -dS_star_dt
        return[dS_star_dt, dS_dt]
    S_star_8 = solve_ivp(solver, [0,1000], initial_conditions, t_eval=t, method='BDF')

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



'''
#cases 1-7: MAOI 
dS_maoi_maoA = competitive_inhibition(c.Serotonin_conc_B, c.Vmax_maoA, c.Km_maoA, c.Ki_maoi_maoA, time)
dS_maoi_maoB = competitive_inhibition(c.Serotonin_conc_B, c.Vmax_maoA, c.Km_maoB, c.Ki_maoi_maoB, time)
dS_star_dt = dS_maoA + dS_maoB 
'''
#Stream 7
DXM_7 = c #depends on how much CSY entering synaptic cleft binds, when it unbinds?? 

#Stream 8
S_star_8 = c
MAOI_8 = c
DXM_8 = DXM_7
