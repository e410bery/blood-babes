import numpy as np

case = 7 #user input to control case used by the model

#Case 0: No CSY, No MAOI, MDD
#Case 1: No CSY, Low MAOI, MDD
#Case 2: No CSY, Normal MAOI, MDD
#Case 3: No CSY, High Dose of MAOI, MDD
#Case 4: Low CSY, Normal MAOI, MDD
#Case 5: Normal CSY, Normal MAOI, MDD
#Case 6: Moderate 1 CSY, Normal MAOI, MDD
#Case 7: Moderate 2 CSY, Normal MAOI, MDD
#Case 8: Extreme CSY, Normal MAOI, MDD - no longer in use


#Molar Masses
DXM_MM = 2.71e2 #g/mol
MAOI_MM = 133.19 #g/mol
trp_MM = 2.04e2 #g/mol

#Relevant concentrations & densities 
DXM_conc = 3 #mg/ml
CSY_Density = 1.43 #g/mL
S_cells = 5e5 #cells 

#Stream 1
trp_in = 2.75e-05 #mol/day
if case ==0:
    CSY_in = 0 
    MAOI_in = 0
elif case == 1:
    CSY_in = 0
    MAOI_in = 30 #mg/day
elif case == 2:
    CSY_in = 7.5
    MAOI_in = 60 #mg/day
elif case == 3:
    CSY_in = 0
    MAOI_in = 200 #mg/day (Subject to change)
elif case == 4:
    CSY_in = 3 #mL (one time dose) 
    MAOI_in = 60 #mg/day
elif case == 5:
    CSY_in = 7.5 #mL
    MAOI_in = 60 #mg/day 
elif case == 6:
    CSY_in = 250 #mL
    MAOI_in = 60 #mg/day 
elif case == 7:
    CSY_in = 500 #mL
    MAOI_in = 60 #mg/day 
elif case == 8:
    CSY_in = 1000 #mL 
    MAOI_in = 60 #mg/day 

#Stream 2
DXM_2 = (DXM_conc * CSY_in) / 1000 / DXM_MM #mol/day
MAOI_2 = MAOI_in / 1000 / MAOI_MM #mol/day #Assume all MAOI consumed goes to Reactor/Brain
trp_2 = trp_in #mol/day #Assume all trp consumed goes to Reactor 

#Stream 3 - decay of MAOI and DMX incorporated into model
CSY_3 = ((CSY_in * CSY_Density * 1000) - (DXM_conc * CSY_in)) #mg/day

#Reactor
trp_reactor = (0.02*trp_in)/1000/trp_MM #mol/day
S_reactor = trp_reactor #mol/day 

#Stream 4
DXM_4 = DXM_2 #mol/day
MAOI_4 = MAOI_2 #mol/day
S_4 = S_reactor #mol/day

#S_5 = 5.12e-21
#Stream 5 #ELLA please consider that the DXM half life is 2 hours, these numebrs are the amount of S passing thru SERT when DXM is all there at t = 0, please figure out how to model these as functions of time 
if case <= 3: 
    S_5 = 5.12e-21 #mole/neuron*sec #constant we mathematically dervied for maximum serotonin passing through 
    Acc_0 = 0.005*5.12e-21 
elif case == 4:
    S_5 = 0.9997*5.12e-21 #percentage of 5.12e-21 depending on saturation 
    Acc_0 = 5.12e-21 - S_5
elif case == 5:
    S_5 = 0.9925*5.12e-21 #percentage of 5.12e-21 depending on saturation
    Acc_0 = 5.12e-21 - S_5 
elif case == 6:
    S_5 = 0.75*5.12e-21 #percentage of 5.12e-21 depending on saturation 
    Acc_0 = 5.12e-21 - S_5
elif case == 7:
    S_5 = 0.5*5.12e-21 #percentage of 5.12e-21 depending on saturation 
    Acc_0 = 5.12e-21 - S_5
elif case == 8:
    S_5 = 0 #percentage of 5.12e-21 depending on saturation 
    
MAOI_5 = MAOI_4 
DXM_5 = DXM_4

#Stream 6
S_6 = S_5
MAOI_6 = MAOI_5

#Stream 9 solved for in BrainB

#Brain B - Serotonin Metabolism 
Km_maoA = 0.192 #mM
Km_maoB = 0.192 #mM
Vmax_maoA = 21.7*24*10e-6 #mmoles/mg/hr 
Vmax_maoB = 21.7*24*10e-6 #mmoles/mg/hr 
Ki_maoi_maoA = 0.0373 / S_cells #mM per cell
Ki_maoi_maoB = 0.0136 / S_cells #mM per cell
Serotonin_conc_B = S_6 / S_cells *1000 #millimoles per cell 
brainSat = 0.011*1000 #mmol



