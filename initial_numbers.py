#initialize all constants here:
#put everything in micrograms, dL, and day.


#restructure so that a boolean controls which state we are in.
anem = True

z = 1 #placeholder
c = 1 #placeholder to signal a value that changes based on day in the cycle
m7ironBase = 0.145 #baseline value for m7iron (the actual value changes per day)
accIronBase = 250*1000 #mg/day, baseline value for accIron

bloodflowQ = 5 #L/min
bloodflowQ = 14400*bloodflowQ #convert to dL/day
ironC = 92 #microg/dL
m1iron = 18 #mg/day
m1hemo = 126000000 #mg/day

if anem == False:
    m2iron = 0.1*m1iron #mg/day
    m2hemo = 0.1*m1hemo #mg/day
    m3iron = 0.9*m1iron #mg/day
    m3hemo = 0.9*m1hemo #mg/day

if anem == True:
    m2iron = 0.050*m1iron #mg/day
    m2hemo = 0.050*m1hemo #mg/day
    m3iron = 0.95*m1iron #mg/day
    m3hemo = 0.95*m1hemo #mg/day
#mass rates:
m4ironHemo = 0.15*m2iron #mg/day, this is actually hemoglobin since it's coming out of storage, but I wanted to differentiate it
m4hemo = 0.15*m2hemo #mg/day
m4hemo = m4ironHemo + m4hemo #mg/day
m5ironHemo = 0.85*m2iron #mg/day, this is actually hemoglobin since it's coming out of storage, but I wanted to differentiate it
m5hemo = 0.85*m2hemo #mg/day
m5hemo = m5ironHemo + m5hemo #mg/day
m10iron = m3iron #mg/day
m6iron = m3iron - m10iron #mg/day
m6hemo = 272000000 #mg/day
m7hemo = c #mg/day
m8hemo = 11000000 #mg/day
m9hemo = m6hemo + m8hemo - m3hemo - m5hemo #mg/day
conIron = 25 #mg/day
accEst = c #accumulation of estrogen in the reproductive system, varies per day

#relationships between hepcidin/iron/estrogen (normal) - all of these values should be calculated from the lists in the for loops
hepIron = 7298(m7hemo) + 1220000 #mg/day, used to calculate the amount of hepcidin based on amount of hemoglobin leaving through menstruation, changes daily
hepEst = 5.02 + accEst/-0.891
hepTotal = hepIron + hepEst #total hepcidin per day
ironHep = 0.00137(hepTotal) - 3275.4 #total iron in storage


#thresholds:
ironMax = 160
ironMin = 60
#magnitudes of slopes, dependent on how much excess/unexcess iron
hepUp = 10
hepDown = 10

#normal values that are most relevant to graphing
accIronStorage = c #calculate this based on the varying amounts of hepcidin resulting from the varying amounts of estrogen (accEst) and varying amounts of iron leaving through menstruation (m7hemo)
accRep = m4hemo + m8hemo - m7hemo - m9hemo #this value will change based on daily variations of m7hemo

#how I would go about doing this: use changing amounts of estrogen to calculate hepcidin, changing amounts of blood through menstruation to calculate hepcidin, and then adding the two
#THEN, plug that value back into the hepcidin/iron relationship equation to get a new value of iron (this is iron in storage)

print(m9hemo)
print(m6iron)