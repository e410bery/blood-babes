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
m7iron = c #mg/day
m8hemo = 11000000 #mg/day
m9hemo = m6hemo + m8hemo - m3hemo - m5hemo #mg/day
print(m9hemo)
accIron = c


#mass rates (anemic):
am2iron = 0.75*m1iron #mg/day - decreased absorption by 25%
am2hemo = z
am3iron = m1iron-am2iron #mg/day
am3hemo = z
am4iron = 0.15*am2iron #mg/day
am4hemo = z
am5iron = 0.85*am2iron #mg/day
am6iron = z
am6hemo = 1200 #mg/L (need this out of a concentration and into a rate)
am7iron = z
am8iron = z 
accairon = z
aconIron = z
agenHemo = z

#relationships between hepcidin/iron/estrogen
hep = z
est = -0.891*hep + 4.47 #estrogen concentration in ng/mL, calculations done to find equation