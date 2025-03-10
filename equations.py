
import numpy as np
import initial_numbers as c
#equations: (use c.--- to use variables defined in initial numbers file.

#~~~~~~~~~~~  lists ~~~~~~~~~~#
time = np.linspace(0,6,num=7) #7 days , list values in days.
cycle = np.linspace(1, 28, num=200) #28 days
blossrate = np.zeros(time.size)
totalblost = np.zeros(time.size)
estgraph = np.zeros(cycle.size)
est = np.zeros(time.size)
prog = np.zeros(cycle.size)
ironStor = np.zeros(time.size)
genIron = np.zeros(time.size)
if c.anem == False:
    ironStor[0] = 250 #mg

if c.anem==True:
    ironStor[0] = 100



hemo6 = np.zeros(time.size)
hemo6[0] = c.base_m6hemo
hemo9 = np.zeros(time.size)
hemo9[0] = c.base_m9hemo

#hep mass in storage:
hep = np.zeros(time.size)


#~~~~~~~~~~ math models ~~~~~~~~~~~#

#bloodloss rate: 12mL first day, decreases until ~0 on 6th day
for i in range(time.size) :
    blossrate[i] = 12*np.e**(-((time[i]-1)/3)**2)
totalblost = np.cumsum(blossrate)

#estrogen: piecewise starting at 50pg/mL, peaking (14 days, 150 pg/mL) and (23 days, ~110 pg/mL)
for i in range(cycle.size) :
    if(cycle[i]<14) : #0-14 days
        estgraph[i] = -220*(cycle[i]-14)*np.e**(.8*(cycle[i]-14)) + 50
    elif cycle[i]>14 and cycle[i]<=20 :
        estgraph[i] = 2.5*(cycle[i]-16)**2 + 50
    else :
        estgraph[i] = 58*np.e**((-1/7)*(cycle[i]-21.5)**2) +50

#estrogen just during menstruation - also converts est from to mg/dL
for i in range(time.size) :
    est[i] = c.bloodflowRepQ*0.0001*(-220*(time[i]-14)*np.e**(.8*(time[i]-14)) + 50)

#progesterone: .5 ug/L base amt, peaks (21 days, 20 ug/L)
for i in range(cycle.size) :
    prog[i] = 20*np.e**(-((cycle[i]-20.8)/3)**2)


#~~~~~~~~~~ mass balance equations ~~~~~~~~~#
#loops through storage, RS, and RoB in that order. 
#Calculates iron, hemo, hepcidin, and estrogen in each in that order.
#only tracking accumulation
#small intestine: no acc of anything, nothing to track.

#initial value for hepcidin: 
if c.anem == False:
    hep[0] = c.hepIron*(0)*.00343 + 25.75 + c.hepEst*est[0] + 0.678
if c.anem == True:
    hep[0] = c.hepIron*(0)*.00343 + 25.75/2 + c.hepEst*est[0] + 0.678

blossrate[0] = 0 #day 0 of cycle, no bloodlost.

for i in range(1,time.size) :
    
    hemo9[i] = (c.m4hemo + c.m8hemo - 0.42*blossrate[i]) #42% of blood is hemoglobin
    hemo6[i] = (c.m3hemo  + hemo9[i] + c.m5hemo - c.m8hemo)

    if c.anem == False:
        hep[i] = c.hepIron*0.42*blossrate[i] + 25.75 + c.hepEst*est[0] + 0.678  #42% of blood is hemoglobin
    if c.anem == True:
        hep[i] = c.hepIron*0.42*blossrate[i] + 25.75/2 + c.hepEst*est[0] + 0.678  #42% of blood is hemoglobin


    #STORAGE:
    ironStor[i] = c.ironHep*hep[i]
    genIron[i] = ironStor[i] - c.m2iron + c.conIron

    #generation term calculation


    #hep is downregulated by estrogen and downregulated by low iron.
    #if iron falls below normal/initial storage level, hep is decreased.
    # or ironStor[0] - ironStor[i]


print("times: ", time)
print("iron in storage: ", ironStor)
print("hep: ", hep)
print("est: ", est)
print("blood: ", blossrate)
print("genIron:", genIron)
print("m6b is", hemo6)
print("m9b is", hemo9)
print(np.max(estgraph))
print(np.max(prog))








"""notes:
-for hepcidin, we can extrapolate a relationship (like assuming linear change and guess constants)
especially if we can find a experimental data point to extrapolalte from. 
"""

