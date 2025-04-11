import constants as c
import numpy as np
import matplotlib.pyplot as plt

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

#Brain B Model: Serotonin Metabolism
def enzyme_substrate(sub, vmax, km) :
    return (vmax * sub) / (km + sub)

def inhibitor(time):
    time = time%24
    inh_mg = c.MAOI_conc*(0.5)**(time/2) - 0.0146
    inh_moles = inh_mg*(1/1000)*(1/133.19)
    return inh_moles

#m-m model to find rate of product concentration
#time in hours 
def competitive_inhibition(sub, vmax, km, ki, time):
    return (vmax * sub) / (km * (1 + inhibitor(time) / ki) + sub)

#MAOI is a competitive Inhibitor 

#case 0: No MAOI 
dS_maoA = enzyme_substrate(c.Serotonin_conc_B, c.Vmax_maoA, c.Km_maoA) #returns ds*/dt
dS_maoB = enzyme_substrate(c.Serotonin_conc_B, c.Vmax_maoB, c.Km_maoB) #returns ds*/dt
dS_star_dt = dS_maoA + dS_maoB

#cases 1-7: MAOI 
dS_maoi_maoA = competitive_inhibition(c.Serotonin_conc_B, c.Vmax_maoA, c.Km_maoA, c.Ki_maoi_maoA, time)
dS_maoi_maoB = competitive_inhibition(c.Serotonin_conc_B, c.Vmax_maoA, c.Km_maoB, c.Ki_maoi_maoB, time)
dS_star_dt = dS_maoA + dS_maoB 


