
#interaction state control variable:
syrup = False;

c = 1 #placeholder
if (syrup is True):
    sert = 0;
else:
    sert = c;

#intake:
dexIn = [0, c, c, c] #none, normal, some, a lot. 
trypIn = c
csyIn = c
maoiIn = c

#out
csyOut = c
maoiOut = c


#liver/kidney:


#absorbtion:


#movement:

#ES binding:
#trp -> S


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

