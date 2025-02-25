#import initial_numbers as c
import numpy as np
import initial_numbers as c
#equations: (use c.--- to use variables defined in initial numbers file.
#ironMR = c.bloodflowQ*c.ironC

#~~~~~~~~~~~  lists ~~~~~~~~~~#
time = np.linspace(1,6,num=144) #6 days , list values in hours.
cycle = np.linspace(1, 28, num=200) #28 days
blossrate = np.zeros(time.size)
totalblost = np.zeros(time.size)
estgraph = np.zeros(cycle.size)
est = np.zeros(time.size)
prog = np.zeros(cycle.size)
#iron acc:
ironRep = np.zeros(time.size)
ironStor = np.zeros(time.size)
for i in range(ironStor.size):
    ironStor[i]= 250;
ironROB = np.zeros(time.size)
#hemo acc:
hemoStor = np.zeros(time.size)

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
#estrogen just during menstruation
for i in range(time.size) :
    est[i] = -220*(time[i]-14)*np.e**(.8*(time[i]-14)) + 50

#progesterone: .5 ng/mL base amt, peaks (21 days, 20 ng/mL)
for i in range(cycle.size) :
    prog[i] = 20*np.e**(-((cycle[i]-21)/4)**2)


#~~~~~~~~~~ mass balance equations ~~~~~~~~~#
#loops through storage, RS, and RoB in that order. 
#Calculates iron, hemo, hepcidin, and estrogen in each in that order.
#only tracking accumulation
#small intestine: no acc of anything, nothing to track.

for i in range(time.size) :
    #STORAGE:
    #iron acc = in -out
    ironStor[i] = c.m2iron*time[i] + c.m6iron*time[i] - c.m4hemo*time[i] - c.m5hemo*time[i]
    #hemo acc=in-out
    #hemoStor[i] = c.m2hemo*time[i] + c.m6hemo*time[i] - c.m4hemo*time[i] - c.m5hemo*time[i]
    #hep is downregulated by estrogen and upregulated by high iron.
    hep[i] = 5.02 - est[i]/0.891 
    if (ironStor[i]>c.ironMax) :
        hep[i]+=c.hepUp*(ironStor[i] - c.ironMax)
    if (ironStor[i]<c.ironMin) :
        hep[i]-=c.hepDown*(c.ironMin - ironStor[i])


print("times: ", time)
print("times: ", time[::28])
print("iron in storage: ", ironStor[::29])
print("hep: ", hep[::29])
print("est: ", est[::29])








"""notes:
-for hepcidin, we can extrapolate a relationship (like assuming linear change and guess constants)
especially if we can find a experimental data point to extrapolalte from. 
"""


