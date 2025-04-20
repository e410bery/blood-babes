import matplotlib.pyplot as plt
import numpy as np

#used to parse text files with lists for several cases and graph them

#user chooses text file to graph:
file = open("b.txt", 'r')

#make dictionary with key=case and value=accArray
dict = {}
for line in file:
    key, prevalues = line.split(':')
    values = [float(x) for x in prevalues.strip().split(',')]
    dict[key] = values

for case in dict.keys(): #used to print values
    print(case)
    print(dict[case][-1])

#colors to use:
myMAOI =  '#f66060'
myCough1 = '#80bebe'
myCough2 = '#007074'

time = np.linspace(0,24,500)

#brainA and Acc:
#linestyles = ['-', '--', '-', ':', '--', '-', '--', '-']
#colors = ['black', myMAOI, myMAOI, myMAOI, myCough1, myCough1, myCough2, myCough2]

#brainB:
linestyles = ['-', '-.', '-', '--', '-']
colors = [myMAOI, myCough2, myCough1, myMAOI, myCough2]

# Plot with different styles defined above
for (label, values), ls, color in zip(dict.items(), linestyles, colors):
    plt.plot(time, values, label=label, linestyle=ls, color=color)

# Add labels and legend
plt.xlabel("Time (hr)")
plt.ylabel("Serotonin in Pre-Synaptic Neuron (mmol)")
plt.title("Serotonin in Degradation/Release Unit with Varying D, Constant MAOI", loc='right')
plt.legend()
plt.grid(True)
plt.tight_layout()

#change file name to save figure:
name = "brainB.png" # <- user edits this
figname = "pbl2/graphs/" + name
plt.savefig(figname)
'''

# Load the data for both ser and degraded ser!
ser_dict = {}
degser_dict = {}
myMAOI =  '#f66060'
myCough1 = '#80bebe'
myCough2 = '#007074'
colors_list = ['black', myMAOI, myCough1, myCough2]

with open("deg.txt", 'r') as file:
    for line in file:
        key, prevalues = line.split(':')
        values = [float(x) for x in prevalues.strip().split(',')]
        if "DegSer" in key:
            case = key.replace("_DegSer", "")
            degser_dict[case] = values
        else:
            ser_dict[key] = values

# Time axis
time = np.linspace(0, 24, 500)

# Use a consistent colormap for shared cases
# Assign custom colors to cases
cases = sorted(ser_dict.keys())
colors = {case: colors_list[i % len(colors_list)] for i, case in enumerate(cases)}

# Plot both Ser and DegSer
for case in cases:
    plt.plot(time, ser_dict[case], label=f"{case} - Ser", color=colors[case], linestyle='-')
    if case in degser_dict:
        plt.plot(time, degser_dict[case], label=f"{case} - DegSer", color=colors[case], linestyle='--')

# Graph styling
plt.xlabel("Time (hr)")
plt.ylabel("Serotonin in Pre-Synaptic Neuron (mmol)")
plt.title(" Serotonin in Degradation/Release Unit with Varying MAOI Levels")
plt.legend()
plt.grid(True)
plt.tight_layout()

# Save the figure
name = "SerAndDeg"  # <- edit this if you want
figname = "pbl2/graphs/" + name
plt.savefig(figname)
'''