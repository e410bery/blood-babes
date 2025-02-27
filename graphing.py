import equations as e
import initial_numbers as c
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

#~~~~~~~~ GRAPHS ~~~~~~~~~~#

#time vs accIron, accEstrogen, hepcidin in storage
plt.plot(e.time, e.ironStor, label='iron')
plt.plot(e.time, e.est, label='estrogen')
plt.plot(e.time, -(e.hep), label="hepcidin")
plt.xlabel("time (days)")
plt.ylabel("Stored (mg)")
plt.legend()
plt.savefig("storage")
plt.show()
plt.close()

#time vs accIron, accEstrogen, hepcidin in storage
fig, (ax1, ax2, ax3) = plt.subplots(3, figsize=(6, 8))
ax1.set_xlabel('Time (day)')
ax1.set_ylabel('Iron in Storage (mg)')
ax1.plot(e.time, e.ironStor)
ax1.tick_params(axis='y', labelcolor='black')
ax1.set_xticks(range(0, 7))  # Set tick positions
ax1.set_xticklabels(['0','1', '2', '3', '4', '5', '6'])  # Set tick labels

ax2.set_xlabel('Time (day)')
ax2.set_ylabel('Estrogen in Reproductive System (mg)')
ax2.plot(e.time, e.est, color = 'orange')
ax2.tick_params(axis='y', labelcolor='black')
ax2.set_xticks(range(0, 7))  # Set tick positions
ax2.set_xticklabels(['0', '1', '2', '3', '4', '5', '6'])


ax3.set_xlabel('Time (day)')
ax3.set_ylabel('Hepcidin in Storage (mg)')
ax3.plot(e.time, e.hep, color='green')  # Remove the negative sign
ax3.tick_params(axis='y', labelcolor='black')
ax3.set_xticks(range(0, 7))
ax3.set_xticklabels(['0', '1', '2', '3', '4', '5', '6'])
ax3.set_ylim(max(e.hep), min(e.hep))  # Reverse the order of limits
ax3.set_yticklabels([abs(tick) for tick in ax3.get_yticks()])
plt.show()


fig.tight_layout()
plt.savefig("EstHepIron.png", bbox_inches="tight")  # Ensure file extension
plt.show()  # Display the figure

#estrogen vs hepcidin linear
plt.plot(e.est, -0.891*e.est+e.hep[0])
plt.xlabel("Estrogen Present (mg)")
plt.ylabel("Change in Hepcidin (mg)")
plt.title("Estimated Relationship of Estrogen and Hepcidin")
plt.savefig("estHepLine")
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
ax2.set_ylabel('Change in Hepcidin (mg)', color=color)  
ax2.plot(e.time, -.891*e.est+e.hep[0], color=color)
ax2.tick_params(axis='y', labelcolor='black')
fig.tight_layout()  
plt.xticks([1,2,3,4,5,6])
plt.title("Estrogen and Hepcidin Relationship")
plt.savefig("estHep", bbox_inches="tight")
plt.show()

#iron and hepcidin relationship
fig, ax1 = plt.subplots()
color = 'red'
ax1.set_xlabel('Time (day)')
ax1.set_ylabel('Iron Lost (mg)', color=color)
ax1.plot(e.time, 0.42*e.blossrate, color=color)
ax1.tick_params(axis='y', labelcolor='black')
ax2 = ax1.twinx()  
color = 'blue'
ax2.set_ylabel('Hepcidin (mg)', color=color)  
ax2.plot(e.time, -0.138*(0.42*e.blossrate) + 25.75, color=color)
ax2.tick_params(axis='y', labelcolor='black')
fig.tight_layout()  
plt.xticks([1,2,3,4,5,6])
plt.title("Iron and Hepcidin Relationship")
plt.savefig("ironHep", bbox_inches="tight")
plt.show()



#total iron in blood over time (6 days)
plt.plot(e.time, e.ironStor)
plt.xlabel("time (days)")
plt.ylabel("iron in storage (mg)")
plt.show()

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
plt.text(.1,14, "Menstruation")
plt.title('Hormone Variation Over Cycle')
plt.savefig("hormones.png", bbox_inches="tight")
plt.show()

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
plt.savefig("bloodloss.png")
plt.show()


