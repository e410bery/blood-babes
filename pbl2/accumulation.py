import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import constants as c
import BrainA as A
import BrainB as B


t = np.linspace(0, 24, 24)

for time in t:  
    S_9 = B.sol.y[1] - B.sol.y[0]

print(S_9)

