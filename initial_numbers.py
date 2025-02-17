#initialize all constants here:
#put everything in micrograms, dL, and day.

bloodflowQ = 5 #L/min
bloodflowQ = 14400*bloodflowQ #convert to dL/day
ironC = 92 #microg/dL

#mass rates:
m1iron = 18 #mg/day
m2iron = 0.1*m1iron
m3iron = m1iron-m2iron
m4iron = None
m5iron = 0.15&m2iron 

accIron = 250 #200-300 mg
accIron = accIron*1000 #convert microg

