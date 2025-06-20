import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import constants as c

#used to graph Dextromethorphan breakdown over 24 hours, dextromethorphan and serotonin saturation over 24 hours, and the amount of serotonin passing through SERT over time

t = np.linspace(0, 24, 500)  # 0 to 24 hours
DXM = [] #DXM in mols/cell
sat = [] #what percentage of SERTs bound by DXM

#amount of serotonin passing through SERT
ser_sert =[]
S0 = c.S_5 * 60000 #mmol/cell/hour, mol/minute --> mmol/hour
print("S0: ", c.case, S0)

def DXM_inhibitor(t):
    decay = 0.5 ** (t / 2)
    DXM_mol = c.DXM_2 * decay
    DXM_mol_cell = DXM_mol / c.S_cells * 1000
    DXM_saturation = DXM_mol_cell / (c.brainSat/c.S_cells)
    if DXM_saturation >= 100:
        DXM_saturation = 100
    #calculating the amount of serotonin that is moving through SERT/cell/hour
    S_new = c.S_5 * ((DXM_saturation)/100)
    return DXM_mol_cell, DXM_saturation, S_new  # mmol/cell


for time in t:  
    if(c.DXM_2 == 0): #if Dextromethorphan = 0, there is no inhibition
        ser_sert.append(S0)
        sat.append(0)
    else:
        a = DXM_inhibitor(time)[0]
        DXM.append(a)
        o = DXM_inhibitor(time)[1]
        sat.append(o)
        f = DXM_inhibitor(time)[2]
        ser_sert.append(f)


#calculates the values used as the initial values in the serotonin degradation box (final values of the transport box)
t_rounded = [round(time, 5) for time in t]
sert_dict = {float(t): float(v) for t, v in zip(t_rounded, ser_sert)}
tfs = []
for dx in sat:
    tfs.append(1 - float(dx)/100.0)

#for serotonin degradation:
TF = {float(t): float(v) for t, v in zip(t_rounded, tfs)}
