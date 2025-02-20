#initialize all constants here:
#put everything in micrograms, dL, and day.

x = 1 #placeholder

bloodflowQ = 5 #L/min
bloodflowQ = 14400*bloodflowQ #convert to dL/day
ironC = 92 #microg/dL

#mass rates (normal):
m1iron = 18 #mg/day
m2iron = 0.1*m1iron #mg/day
m3iron = m1iron-m2iron #mg/day
m4iron = 0.12*m2iron #mg/day
m5iron = 0.85*m2iron #mg/day
m6iron = x #placeholder - need this value
m7iron = 0.145 #mg/day
m8iron = 54.4*(60*24) #mL/min --> mL/day (**need this in mg)
m10iron = 16.2 #mg/day

#mass rates (anemic):
am2iron = 0.1*m1iron #mg/day - this value should be changing depending on the absorption rate of iron in people with anemia
am3iron = m1iron-am2iron #mg/day
am4iron = 0.12*am2iron #mg/day
am5iron = 0.85*am2iron #mg/day
am6iron = x #placeholder - need this value
am7iron = x
am8iron = x 

accIron = 250 #200-300 mg
accIron = accIron*1000 #convert microg

