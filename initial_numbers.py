#initialize all constants here:
#put everything in micrograms, dL, and day.

z = 1 #placeholder
c = 1 #placeholder to signal a value that changes based on day in the cycle
m7ironBase = 0.145 #baseline value for m7iron (the actual value changes per day)
accIronBase = 250*1000 #mg/day, baseline value for accIron

bloodflowQ = 5 #L/min
bloodflowQ = 14400*bloodflowQ #convert to dL/day
ironC = 92 #microg/dL

#mass rates (normal):
m1iron = 18 #mg/day
m1hemo = 126000000 #mg/day
m2iron = 0.1*m1iron #mg/day
m2hemo = 0.1*m1hemo #mg/day
m3iron = 0.9*m1iron #mg/day
m3hemo = 0.9*m1hemo #mg/day
m4ironHemo = 0.15*m2iron #mg/day, this is actually hemoglobin since it's coming out of storage, but I wanted to differentiate it
m4hemo = 0.15*m2hemo #mg/day
m4hemo = m4ironHemo + m4hemo #mg/day
m5ironHemo = 0.85*m2iron #mg/day, this is actually hemoglobin since it's coming out of storage, but I wanted to differentiate it
m5hemo = 0.85*m2hemo #mg/day
m5hemo = m5ironHemo + m5hemo #mg/day
m10iron = 16.2 #mg/day
m6iron = m3iron - m10iron #mg/day
m6hemo = 272000000 #mg/day
m7hemo = c #mg/day
m8hemo = 11000000 #mg/day
m9hemo = m6hemo + m8hemo - m3hemo - m5hemo #mg/day
conIron = 25 #mg/day
accEst = c #accumulation of estrogen in the reproductive system, varies per day


#mass rates (anemic):
anem_m2iron = 0.075*m1iron #mg/day - decreased absorption by 25%
anem_m2hemo = 0.075*m1hemo #mg/day - decreased absorption by 25%
anem_m3iron = 0.925*m1iron #mg/day
anem_m3hemo = 0.925*m1hemo #mg/day
anem_m4ironHemo = 0.15*anem_m2iron #mg/day, this is actually hemoglobin since it's coming out of storage, but I wanted to differentiate it
anem_m4hemo = 0.15*anem_m2hemo #mg/day
anem_m4hemo = anem_m4ironHemo + anem_m4hemo #mg/day
anem_m5ironHemo = 0.85*anem_m2iron #mg/day, this is actually hemoglobin since it's coming out of storage, but I wanted to differentiate it
anem_m5hemo = 0.85*anem_m2hemo #mg/day
anem_m5hemo = anem_m5ironHemo + anem_m5hemo #mg/day
anem_m10iron = 16.2 #mg/day
anem_m6iron = anem_m3iron - anem_m10iron #mg/day
anem_m6hemo = 272000000 #mg/day
anem_m7hemo = c #mg/day
anem_m8hemo = 11000000 #mg/day
anem_m9hemo = anem_m6hemo + anem_m8hemo - anem_m3hemo - anem_m5hemo #mg/day
anem_conIron = 25 #mg/day
anem_accEst = c #accumulation of estrogen in the reproductive system, varies per day

#relationships between hepcidin/iron/estrogen (normal)
hepIron = z #this should be a formula, undetermined currently
hepEst = 5.02 + accEst/-0.891

#relationships between hepcidin/iron/estrogen (anemic)
anem_hepIron = z #this should be a formula, undetermined currently
anem_hepEst = 5.02 + anem_accEst/-0.891

#normal values that are most relevant to graphing
accIronStorage = c #calculate this based on the varying amounts of hepcidin resulting from the varying amounts of estrogen (accEst) and varying amounts of iron leaving through menstruation (m7hemo)
accRep = m4hemo + m8hemo - m7hemo - m9hemo #this value will change based on daily variations of m7hemo


#anemic values that are most relevant to graphing
anem_accIronStorage = c #calculate this based on the varying amounts of hepcidin resulting from the varying amounts of estrogen (anem_accEst) and varying amounts of iron leaving through menstruation (anem_m7hemo)
anem_accRep = anem_m4hemo + anem_m8hemo - anem_m7hemo - anem_m9hemo #this value will change based on daily variations of anem_m7hemo