#initialize all constants here:
#put everything in micrograms, dL, and day.

z = 1 #placeholder

bloodflowQ = 5 #L/min
bloodflowQ = 14400*bloodflowQ #convert to dL/day
ironC = 92 #microg/dL

#mass rates (normal):
m1iron = 18 #mg/day
m1hemo = z
m2iron = 0.1*m1iron #mg/day
m2hemo = 13.3 #g/L (need this out of a concentration and into a rate)
m3iron = m1iron-m2iron #mg/day
m3hemo = 13.4 #g/L (need this out of a concentration and into a rate)
m4iron = 0.15*m2iron #mg/day
m4hemo = 13.4 #g/L (need this out of a concentration and into a rate)
m5iron = 0.85*m2iron #mg/day
m6iron = z
m6hemo = 6000 #mg/day
m7iron = 0.145 #mg/day
m8iron = 54.4*(60*24) #mL/min --> mL/day (**need this in mg)
m10iron = 16.2 #mg/day
accIron = 250*1000 #mg/day
conIron = 25 #mg/day
genHemo = 25 #mg/day


#mass rates (anemic):
am2iron = z*m1iron #mg/day - this value should be changing depending on the absorption rate of iron in people with anemia
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