import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import constants as c

t = np.linspace(0, 24, 24)  # 0 to 24 hours
DXM = [] #DXM in mols/cell
sat = [] #what percentage of SERTs bound by DXM
ser_sert = [] #amount of serotonin passing through SERT

def DXM_inhibitor(t):
    decay = 0.5 ** (t / 2)
    DXM_mol = c.DXM_2 * decay
    DXM_mol_cell = DXM_mol / c.S_cells * 1000
    DXM_saturation = DXM_mol_cell / (0.00368/c.S_cells)
    if DXM_saturation >= 100:
        DXM_saturation = 100
    #calculating the amount of serotonin that is moving through SERT/cell/hour
    S0 = c.S_5 * 60 #mol/cell/hour
    if c.DXM_2 == 0:
        S_new = S0
    else:
        S_new = S0 * (1/(DXM_saturation/100))
    return DXM_mol_cell, DXM_saturation, S_new  # mmol/cell


for time in t:  
    a = DXM_inhibitor(time)[0]
    DXM.append(a)
    o = DXM_inhibitor(time)[1]
    sat.append(o)
    f = DXM_inhibitor(time)[2]
    ser_sert.append(f)


plt.figure(figsize=(10, 8))
plt.plot(t, DXM)
plt.xlabel('Time (hours)')
plt.ylabel('Concentration (mmol/cell)')
plt.title('Dextromethorphan Breakdown Over 24 Hours')
plt.grid(True)
plt.savefig("pbl2/graphs/DexBreakdown.png")

plt.figure(figsize = (10, 8))
plt.plot(t, sat)
plt.xlabel('Time (hours)')
plt.ylabel('Saturation (%)')
plt.title('Dextromethorphan and Serotonin Saturation Over 24 Hours')
plt.grid(True)
plt.savefig("pbl2/graphs/DexSaturation.png")

plt.figure(figsize = (10, 8))
plt.plot(t, ser_sert)
plt.xlabel('Time (hours)')
plt.ylabel('Saturation (%)')
plt.title('Amount of Serotonin Passing Through SERT Over 24 Hours')
plt.grid(True)
plt.savefig("pbl2/graphs/SerotoninSERT.png")

'''
if DXM == 0:
    sertConstant = c.S_5
    serotonin = np.zeros(t.size())
    for s in serotonin: 
        serotonin.append(sertConstant)
    print(serotonin)

return sert
else:
return sert found in brainA!
'''

print(ser_sert)