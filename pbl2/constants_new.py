case = 0
#Case 0: No CSY, No MAOI, MDD
#Case 1: No CSY, Normal MAOI, MDD
#Case 2: No CSY, High Dose of MAOI, MDD
#Case 3: Normal CSY, Normal MAOI, MDD
#Case 4: Moderate 1 CSY, Normal MAOI, MDD
#Case 5: Moderate 2 CSY, Normal MAOI, MDD
#Case 6: Moderate 3 CSY, Normal MAOI, MDD
#Case 7: Extreme CSY, Normal MAOI, MDD

#Stream Constants 
c = 1

#Molar Masses
DXM_MM = 2.71e2 #g/mol
MAOI_MM = 133.19 #g/mol
trp_MM = 2.04e2 #g/mol

#Relevant concentrations & densities 
DXM_conc = 3 #mg/ml
CSY_Density = 1.43 #g/mL

#Stream 1
trp_in = 2.75e-05 #mol/day
if case ==0:
    CSY_in = 0 
    MAOI_in = 0
elif case == 1:
    CSY_in = 0
    MAOI_in = 60 #mg/day
elif case == 2:
    CSY_in = 0
    MAOI_in = 200 #mg/day (Subject to change)
elif case == 3:
    CSY_in = 7.5 #mL (one time dose) 
    MAOI_in = 60 #mg/day
elif case == 4:
    CSY_in = 250 #mL
    MAOI_in = 60 #mg/day 
elif case == 5:
    CSY_in = 500 #mL
    MAOI_in = 60 #mg/day 
elif case == 6:
    CSY_in = 750 #mL
    MAOI_in = 60 #mg/day 
elif case == 7:
    CSY_in = 1000 #mL 
    MAOI_in = 60 #mg/day 

#Stream 2
DXM_2 = (DXM_conc * CSY_in) / 1000 / DXM_MM #mol/day
DXM_2 = 8.29e-05 #mol/day
MAOI_2 = MAOI_in / 1000 / MAOI_MM #mg/day #Assume all MAOI consumed goes to Reactor/Brain
trp_2 = trp_in #mol/day #Assume all trp consumed goes to Reactor 

#Stream 3
CSY_3 = ((CSY_in * CSY_Density * 1000) - (DXM_conc * CSY_in)) #mg/day
DXM_3 = c #should be equal to DXM_8 
MAOI_3 = c #should be equal to MAOI_8 #use half life? 

#Reactor
trp_reactor = (0.02*trp_in)/1000/trp_MM #mol/day
S_reactor = trp_reactor #mol/day 

#Stream 4
DXM_4 = DXM_2 #mol/day
MAOI_4 = MAOI_2 #mol/day
S_4 = S_reactor #mol/day

#Stream 5
if case == 0 or case == 1 or case == 2: 
    S_5 = 2.56e-15 #mole/neuron*sec #constant we mathematically dervied for maximum serotonin passing through 
elif case == 3:
    S_5 = c #percentage of 2.56e-15 depending on saturation 
elif case == 4:
    S_5 = c #percentage of 2.56e-15 depending on saturation 
elif case == 5:
    S_5 = c #percentage of 2.56e-15 depending on saturation 
elif case == 6:
    S_5 = c #percentage of 2.56e-15 depending on saturation 
elif case == 7:
    S_5 = c #percentage of 2.56e-15 depending on saturation 
MAOI_5 = MAOI_4 
DXM_5 = DXM_4

#Stream 6
S_6 = S_5
MAOI_6 = MAOI_5

#Stream 7
DXM_7 = c #depends on how much CSY entering synaptic cleft binds, when it unbinds?? 

#Stream 8
S_star_8 = c
MAOI_8 = c
DXM_8 = DXM_7

#Stream 9
S_9 = c

#Box Constants:

#Brain B - Serotonin Metabolism 
Km_maoA = 0.192 #mM
Km_maoB = 0.192 #mM
Vmax_maoA = 21.7 #nmoles/mg/hr 
Vmax_maoB = 21.7 #nmoles/mg/hr 
Ki_maoi_maoA = 0.0373 #mM
Ki_maoi_maoB = 0.0136 #mM


#inhibition:
sertDexKi = 40 #nmoles


Km_maoA = 0.192 #mM
Km_maoB = 0.192 #mM

Vmax_maoA = 21.7 #nmoles/mg/hr 
Vmax_maoB = 21.7 #nmoles/mg/hr 

Ki_maoi_maoA = 0.0373 #mM
Ki_maoi_maoB = 0.0136 #mM

Serotonin_to_brain = 5.52e-7 #mol/day
MAOI_to_brain = 2.25e-4 #mol/day


Serotonin_conc = #2.56e-15 #mol/neuron
MAOI_conc = 60 #mg 

#Storage Box 
S_acc = S_4 - S_5 + S_9 


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
dS_maoA = enzyme_substrate(Serotonin_conc, Vmax_maoA, Km_maoA) #returns ds*/dt
dS_maoB = enzyme_substrate(Serotonin_conc, Vmax_maoB, Km_maoB) #returns ds*/dt
dS_star_dt = dS_maoA + dS_maoB

#cases 1-7: MAOI 
dS_maoi_maoA = competitive_inhibition(Serotonin_conc, Vmax_maoA, Km_maoA, Ki_maoi_maoA, time)
dS_maoi_maoB = competitive_inhibition(Serotonin_conc, Vmax_maoA, Km_maoB, Ki_maoi_maoB, time)
dS_star_dt = dS_maoA + dS_maoB 

S_star_conc = solve_ivp(solver, [0,1000], initial_conditions, t_eval=t, method='BDF')
