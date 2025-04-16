import matplotlib.pyplot as plt
import numpy as np

file = open("output.txt", 'r')
#make dictionary with key=case and value=accArray
dict = {}
for line in file:
    key, prevalues = line.split(':')
    values = [float(x) for x in prevalues.strip().split(',')]
    dict[key] = values


time = np.linspace(0,24,500)
# Plot each case
for label, values in dict.items():
    plt.plot(time, values, label=label)

# Add labels and legend
plt.xlabel("Time")
plt.ylabel("Value")
plt.title("Cases Over Time")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
