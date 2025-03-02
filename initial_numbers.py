#initialize all constants here:
#put everything in micrograms, dL, and day.


#boolean controls which state we are in.
anem = True

c = 1 #placeholder to signal a value that changes based on day in the cycle - calculations for these values are done in loops in equations.py
m7ironBase = 0.145 #baseline value for m7iron (the actual value changes per day)
accIronBase = 250*1000 #mg/day, baseline value for accIron

bloodflowQ = 5 #L/min
bloodflowQ = 14400*bloodflowQ #convert to dL/day
bloodflowRepQ = 94.5 #mL/min
bloodflowRepQ = 14.4*bloodflowRepQ #dL/day
ironC = 92 #microg/dL
m1iron = 18 #mg/day
m11hemo = 126000000 #mg/day

if anem == False:
    m2iron = 0.1*m1iron #mg/day
    m2hemo = 0.1*m11hemo #mg/day
    m3iron = 0.9*m1iron #mg/day
    m3hemo = 0.9*m11hemo #mg/day

if anem == True:
    m2iron = 0.3*m1iron #mg/day #represents increase in absorption
    m2hemo = 0.3*m11hemo #mg/day
    m3iron = 0.7*m1iron #mg/day
    m3hemo = 0.7*m11hemo #mg/day
#mass rates:
m4hemo = 0.15*(m2iron + m2hemo) #mg/day
m5hemo = 0.85*(m2iron + m2hemo) #mg/day
m10iron = m3iron #mg/day
m6hemo = c #calculated like the base value is, but m9hemo changes per day (actual calculations are in equations.py)
m7hemo = c #mg/day
m8hemo = 20160000 #mg/day
m9hemo = c #calculated like the base value is, but m6hemo changes per day (actual calculations are in equations.py)
conIron = 25 #mg/day
genIron = c #changes to accommmodate the fluctuations in accumulation in storage
accEst = c #accumulation of estrogen in the reproductive system, varies per day

#relationships between hepcidin/iron/estrogen (normal)
if anem == True:
    hepIron = -0.138/2#*m7hemo + 25.75 #mg/day, used to calculate the amount of hepcidin based on amount of hemoglobin leaving through menstruation, changes daily
    ironHep = 12.26/2#*hepTotal +186.98 #total iron in storage

if anem == False:
    hepIron = -0.138#*m7hemo + 25.75 #mg/day, used to calculate the amount of hepcidin based on amount of hemoglobin leaving through menstruation, changes daily
    ironHep = 12.26#*hepTotal +186.98 #total iron in storage 

hepEst = -0.891#*accEst + 0.678 #mg/day, used to calculate the amount of hepcidin based on the amount of estrogen
hepTotal = hepIron + hepEst #total hepcidin per day


#normal values that are most relevant to graphing
accIronStorage = c #calculated based on the varying amounts of hepcidin resulting from the varying amounts of estrogen (accEst) and varying amounts of iron leaving through menstruation (m7hemo)
accRep = m4hemo + m8hemo - m7hemo - m9hemo #this value will change based on daily variations of m7hemo

#calculating base values
base_m7hemo = 0.14884 #mg/day
base_m9hemo = m4hemo + m8hemo - base_m7hemo #mg/day
base_m6hemo = m3hemo + base_m9hemo + m5hemo - m8hemo #mg/day


print('the base value for m7b is', base_m7hemo)
print('the base value for m9b is', base_m9hemo)
print('the base value for m6b is', base_m6hemo)
print('m1a is', m1iron)
print('m2a is', m2iron)
print('m2b is', m2hemo)
print('m3a is', m3iron)
print('m3b is', m3hemo)
print('m4b is', m4hemo)
print('m5b is', m5hemo)
print('m8b is', m8hemo)
print('m10a is', m10iron)
print('m11b is', m11hemo)




