import equations as e
import initial_numbers as c
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

#~~~~~~~~ GRAPHS ~~~~~~~~~~#

#time vs accIron, accEstrogen, hepcidin in storage
plt.plot(e.time, e.ironStor, label='iron')
plt.plot(e.time, e.est, label='estrogen')
plt.plot(e.time, e.hep, label="hepcidin")
plt.xlabel("time (days)")
plt.ylabel("Stored (mg)")
plt.legend()
plt.show()

#Estrogen and Hepcidin Relationship
fig, ax1 = plt.subplots()
color = 'red'
ax1.set_xlabel('Time (day)')
ax1.set_ylabel('Estrogen (mg)', color=color)
ax1.plot(e.time, e.est, color=color)
ax1.tick_params(axis='y', labelcolor='black')
ax2 = ax1.twinx()  
color = 'blue'
ax2.set_ylabel('Hepcidin (mg)', color=color)  
ax2.plot(e.time, -.891*e.est+0.678, color=color)
ax2.tick_params(axis='y', labelcolor='black')
fig.tight_layout()  
plt.xticks([1,2,3,4,5,6])
plt.title("Estrogen and Hepcidin Relationship");
plt.show()

fig, ax1 = plt.subplots()
color = 'red'
ax1.set_xlabel('Time (day)')
ax1.set_ylabel('Iron Lost (mg)', color=color)
ax1.plot(e.time, e.blossrate, color=color)
ax1.tick_params(axis='y', labelcolor='black')
ax2 = ax1.twinx()  
color = 'blue'
ax2.set_ylabel('Hepcidin (mg)', color=color)  
ax2.plot(e.time, 7298*e.blossrate + 1220000, color=color)
ax2.tick_params(axis='y', labelcolor='black')
fig.tight_layout()  
plt.xticks([1,2,3,4,5,6])
plt.title("Iron and Hepcidin Relationship");
plt.show()
#time vs iron, prog, estrogen in reproductive


#total iron in blood over time (6 days)
plt.plot(e.time, e.ironStor)
plt.xlabel("time (days)")
plt.ylabel("iron in storage (mg)")
#plt.show()

#'''#hormone variation over menstrual cycle
fig, ax1 = plt.subplots()
color = 'purple'
ax1.set_xlabel('Time (day)')
ax1.set_ylabel('Estrogen (pg/L)', color=color)
ax1.plot(e.cycle, e.estgraph, color=color)
ax1.tick_params(axis='y', labelcolor='black')
ax2 = ax1.twinx()  
color = 'green'
ax2.set_ylabel('Progesterone (μg/L)', color=color)  
ax2.plot(e.cycle, e.prog, color=color)
ax2.tick_params(axis='y', labelcolor='black')
fig.tight_layout()  
plt.xticks([1,4,8,12,16,20,24,28])
plt.axvspan(0, 6, facecolor='red', alpha=0.2)
plt.text(.1,14, "Menstruation");
plt.title('Hormone Variation Over Cycle')
#plt.savefig("hormones.png", bbox_inches="tight")
#plt.show()

#blood loss over time during cycle
fig, ax = plt.subplots(1)
plt.plot(e.time, e.blossrate, "red", label='mL lost per day')
#plt.plot(e.time,e.totalblost, 'blue', label='total lost')
plt.title("Blood Loss Per Day Over Cycle")
plt.xlabel("Time (days)")
plt.ylabel("Blood Lost (mL)")
plt.fill_between(e.time, e.blossrate, alpha=0.2, color='red')
rect = patches.Rectangle((3.7, 11), .2, .4, linewidth=1, edgecolor='r', facecolor='red', alpha = .2)
ax.add_patch(rect)
plt.text(4,11,'Total Blood Lost = 35mL')
#plt.savefig("bloodloss.png")
#plt.show()


