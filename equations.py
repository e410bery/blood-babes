#import initial_numbers as c
import numpy as np
import initial_numbers as c
#equations: (use c.--- to use variables defined in initial numbers file.
#ironMR = c.bloodflowQ*c.ironC

#~~~~~~~~~~~  lists ~~~~~~~~~~#
time = np.linspace(1,6,num=141) #6 days , list values in hours.
cycle = np.linspace(1, 28, num=200) #28 days
blossrate = np.zeros(time.size)
totalblost = np.zeros(time.size)
estgraph = np.zeros(cycle.size)
est = np.zeros(time.size)
prog = np.zeros(cycle.size)
#iron acc:
#ironRep = np.zeros(time.size)    initial: acc = in-out-con
ironStor = np.zeros(time.size)
ironStor[0] = (c.m2iron + c.m6hemo) - (c.m4hemo + c.m5hemo) - c.conIron

#ironROB = np.zeros(time.size)

#hemo acc:
#hemoStor = np.zeros(time.size)
hemo6 = np.zeros(time.size)
hemo6[0] = c.m6hemo
hemo9 = np.zeros(time.size)
hemo9[0] = c.m9hemo
#hep mass in storage:
hep = np.zeros(time.size)


#~~~~~~~~~~ math models ~~~~~~~~~~~#

#bloodloss rate: 12mL first day, decreases until ~0 on 6th day
for i in range(time.size) :
    blossrate[i] = 12*np.e**(-((time[i]-1)/3)**2)
totalblost = np.cumsum(blossrate)

#estrogen: piecewise starting at 50pg/L, peaking (14 days, 150 pg/L) and (23 days, )
for i in range(cycle.size) :
    if(cycle[i]<14) : #0-14 days
        estgraph[i] = -220*(cycle[i]-14)*np.e**(.8*(cycle[i]-14)) + 50
    elif cycle[i]>14 and cycle[i]<=20 :
        estgraph[i] = 2.5*(cycle[i]-16)**2 + 50
    else:
        estgraph[i] = -2.3*(cycle[i]-22.7)**2 + 108
#estrogen just during menstruation - also converts est from pg/L to mg/dL
for i in range(time.size) :
    est[i] = c.bloodflowQ*0.0001*(-220*(time[i]-14)*np.e**(.8*(time[i]-14)) + 50)

#progesterone: .5 ug/L base amt, peaks (21 days, 20 ug/L)
for i in range(cycle.size) :
    prog[i] = 20*np.e**(-((cycle[i]-21)/4)**2)


#~~~~~~~~~~ mass balance equations ~~~~~~~~~#
#loops through storage, RS, and RoB in that order. 
#Calculates iron, hemo, hepcidin, and estrogen in each in that order.
#only tracking accumulation
#small intestine: no acc of anything, nothing to track.

#initial value for hepcidin: 
hep[0] = c.hepIron*blossrate[0] + 1220000 + c.hepEst*est[0] + 0.678

for i in range(time.size-1) :
    #STORAGE:
    ironStor[i+1] = ironStor[i] - c.ironHep*blossrate[i]*time[0]    
    #hemo 
    hemo6[i+1] = hemo6[i]-blossrate[i]*time[i]
    hemo9[i+1] = hemo9[i]-blossrate[i]*time[i]
    #hep is downregulated by estrogen and downregulated by low iron.
    hep[i+1] = hep[i] + c.hepEst*est[i]
    #if iron falls below normal/initial storage level, 
    if (ironStor[i]<ironStor[0]) : 
        hep[i+1] = hep[i] + c.hepIron*(ironStor[0] - ironStor[i])


print("times: ", time[::28])
print("iron in storage: ", ironStor[::28])
print("hep: ", hep[::28])
print("hemo6: ", hemo6[::28])
print("est: ", est[::28])








"""notes:
-for hepcidin, we can extrapolate a relationship (like assuming linear change and guess constants)
especially if we can find a experimental data point to extrapolalte from. 
"""


