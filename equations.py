#import initial_numbers as c
import numpy as np
import initial_numbers as c
#equations: (use c.--- to use variables defined in initial numbers file.
#ironMR = c.bloodflowQ*c.ironC

#~~~~~~~~~~~  lists ~~~~~~~~~~#
time = np.linspace(0,143,num=144)
blossrate = np.zeros(time.size)
est = np.zeros(time.size)
#iron masses:
ironRep = np.zeros(time.size)
ironStor = np.zeros(time.size)
ironROB = np.zeros(time.size)
ironSI = np.zeros(time.size)
#hep mass in storage:
hep = np.zeros(time.size)


#math models:
#bloodloss rate: 12mL first day, decreases until ~0 on 6th day
for i in range(time.size) :
    blossrate[i] = 12*np.e**(-(time[i]/3)**2)

#estrogen: 
for i in range(time.size) :
    est[i] = 12*np.e**(-(time[i]/3)**2)


#small intestine:


#storage:

#slope for estrogen:







"""notes:
-for hepcidin, we can extrapolate a relationship (like assuming linear change and guess constants)
especially if we can find a experimental data point to extrapolalte from. 
"""
