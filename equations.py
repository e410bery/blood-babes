#import initial_numbers as c
import numpy as np
import initial_numbers as c
#equations: (use c.--- to use variables defined in initial numbers file.
#ironMR = c.bloodflowQ*c.ironC

#~~~~~~~~~~~  lists ~~~~~~~~~~#
time = np.linspace(0,143,num=144)
blossrate = np.zeros(time.size)
#iron masses:
ironRep = np.zeros(time.size)
ironStor = np.zeros(time.size)
ironROB = np.zeros(time.size)
ironSI = np.zeros(time.size)
#hep mass in storage:
hep = np.zeros(time.size)

#small intestine:

#storage:

#slope for estrogen:


"""notes:
-for hepcidin, we can extrapolate a relationship (like assuming linear change and guess constants)
especially if we can find a experimental data point to extrapolalte from. 
"""
