import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import constants as c
import BrainAacc as A
import BrainBacc as B
import math

#used to track total accumulation of serotonin in cleft

initial = 0.0013480393692862748; #original value for case 0, starting point for all serotonin tracking.
t = np.linspace(0, 24, 500)
S_4 = []
S_9 = B.sol.y[0] - B.sol.y[1]
S_5 = B.sol.y[1]

for time in t:  
    S_4.append(c.S_4 * 1000)

#accumulation in the brain = serotonin released from nueron - serotonin uptaken by nueron - daily dietary intake.
acc = (S_9 - S_5 + S_4) * 500000 

#set initial value of accumulation:
if not (math.isclose(acc[0], initial, rel_tol=1e-18)):
    print("true")
    translate = initial - acc[0]
    for i in range(acc.size):
        acc[i] = acc[i]+translate

