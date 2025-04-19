import matplotlib.pyplot as plt
import numpy as np

file = open("output.txt", 'r')
#make dictionary with key=case and value=accArray
dict = {}
for line in file:
    key, prevalues = line.split(':')
    values = [float(x) for x in prevalues.strip().split(',')]
    dict[key] = values

#for case in dict.keys(): #used to print values
#    print(case)
#    print(dict[case][-1])

time = np.linspace(0,24,500)
# Plot each case
for label, values in dict.items():
    plt.plot(time, values, label=label)


# Add labels and legend
plt.xlabel("Time (hr)")
plt.ylabel("Serotonin")
plt.title("Accumulation in Brain B, Serotonin that leaves without degradation.")
plt.legend()
plt.grid(True)
plt.tight_layout()

#change name to savefig:
name = "BrainB_AllCases.png" # <- edit this
figname = "pbl2/graphs/" + name
plt.savefig(figname)

'''
# Load the data for both ser and degraded ser!
ser_dict = {}
degser_dict = {}

with open("output.txt", 'r') as file:
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
color_map = plt.get_cmap('tab10')
cases = sorted(ser_dict.keys())
colors = {case: color_map(i % 10) for i, case in enumerate(cases)}

# Plot both Ser and DegSer
for case in cases:
    plt.plot(time, ser_dict[case], label=f"{case} ", color=colors[case], linestyle='-')
    if case in degser_dict:
        plt.plot(time, degser_dict[case], label=f"{case} ", color=colors[case], linestyle='--')

# Graph styling
plt.xlabel("Time (hr)")
plt.ylabel("Serotonin Concentration in Nueron")
plt.title("Serotonin (solid) and Degraded Product (  ) from MAO activity")
plt.legend()
plt.grid(True)
plt.tight_layout()

# Save the figure
name = "SerAndDegAllCases"  # <- edit this if you want
figname = "pbl2/graphs/" + name
plt.savefig(figname)
'''