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
c = 1 #asking questions 
d = 1 #things we calculate in the code 

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
MAOI_2 = MAOI_in / 1000 / MAOI_MM #mg/day #Assume all MAOI consumed goes to Reactor/Brain
trp_2 = trp_in #mol/day #Assume all trp consumed goes to Reactor 

#Stream 3
CSY_3 = ((CSY_in * CSY_Density * 1000) - (DXM_conc * CSY_in)) #mg/day
DXM_3 = c #should be equal to DXM_8 
MAOI_3 = d #should be equal to MAOI_8 #use half life? #using inhibitor(time)

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
S_star_8 = d #solve ivp MAOI brain B 
MAOI_8 = d #inhibitor time function 
DXM_8 = DXM_7

#Stream 9
S_9 = c #negative feedback loop - Geena Luise 

#Brain B - Serotonin Metabolism 
Km_maoA = 0.192 #mM
Km_maoB = 0.192 #mM
Vmax_maoA = 21.7 #nmoles/mg/hr 
Vmax_maoB = 21.7 #nmoles/mg/hr 
Ki_maoi_maoA = 0.0373 #mM
Ki_maoi_maoB = 0.0136 #mM
Serotonin_conc_B = d #find somewhere in spreadsheet #do first 




