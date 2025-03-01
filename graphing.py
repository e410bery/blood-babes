import equations as e
import initial_numbers as c
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

#~~~~~~~~ GRAPHS ~~~~~~~~~~#
mypink = "#d66363"
myblue = "#699fd1"
#total iron in blood over time (6 days)
plt.plot(e.time, [100,          43.75452695,  43.97870521,  44.5194474,   45.10206183, 45.52599844,  45.75374978], label='diseased case', color=mypink)
plt.plot(e.time, e.ironStor, label='normal case', color=myblue)
plt.xlabel("time (days)")
plt.ylabel("iron in storage (mg)")
plt.legend()
plt.savefig("iron in storage both")
plt.close()

#time vs accIron, accEstrogen, hepcidin in storage
plt.plot(e.time, e.ironStor, label='iron')
plt.plot(e.time, e.est, label='estrogen')
plt.plot(e.time, e.hep, label="hepcidin")
plt.xlabel("time (days)")
plt.ylabel("Stored (mg)")
plt.legend()
plt.savefig("storage")
#plt.show()
plt.close()

#estrogen vs hepcidin linear
plt.plot(e.est, -0.891*e.est+e.hep[0], color=myblue)
plt.xlabel("Estrogen Present (mg)")
plt.ylabel("Hepcidin (mg)")
plt.title("Estimated Relationship of Estrogen and Hepcidin")
plt.savefig("estHepLine")
#plt.show()
plt.close()

#Estrogen and Hepcidin Relationship
fig, ax1 = plt.subplots()
color = mypink
ax1.set_xlabel('Time (day)')
ax1.set_ylabel('Estrogen (mg)', color=color, fontweight="bold", fontsize='large')
ax1.plot(e.time, e.est, color=color, label="Estrogen")
plt.legend(bbox_to_anchor=(.3,.45))
ax1.tick_params(axis='y', labelcolor='black')
ax2 = ax1.twinx()  
color = myblue
ax2.set_ylabel('Hepcidin (mg)', color=color,fontweight="bold", fontsize='large')  
ax2.plot(e.time, -.891*e.est+e.hep[0], color=color, label="Hepcidin")
plt.legend(bbox_to_anchor=(0.3, 0.55))
ax2.tick_params(axis='y', labelcolor='black')
fig.tight_layout()  
plt.xticks([1,2,3,4,5,6])
plt.title("Estrogen and Hepcidin Relationship")
plt.savefig("estHep", bbox_inches="tight")
#plt.show()
plt.close()

fig, ax1 = plt.subplots()
color = mypink
ax1.set_xlabel('Time (day)')
ax1.set_ylabel('Iron Lost (mg)', color=color, fontweight='bold', fontsize='large')
ax1.plot(e.time, e.blossrate, color=color, label="    Iron    ")
ax1.tick_params(axis='y', labelcolor='black')
plt.legend(bbox_to_anchor=(0.7,.9))
ax2 = ax1.twinx()  
color = myblue
ax2.set_ylabel('Hepcidin (mg)', color=color, fontweight='bold', fontsize='large')  
ax2.plot(e.time, c.hepIron*e.blossrate + 25.75, color=color, label = 'Hepcidin')
ax2.tick_params(axis='y', labelcolor='black')
plt.legend(bbox_to_anchor=(0.7,1))
fig.tight_layout()  
plt.xticks([1,2,3,4,5,6])
plt.title("Iron and Hepcidin Relationship");
plt.savefig('ironHep.png', bbox_inches='tight')
#plt.show()
plt.close()

#time vs iron, prog, estrogen in reproductive


#'''#hormone variation over menstrual cycle
fig, ax1 = plt.subplots()
color = mypink
ax1.set_xlabel('Time (day)')
ax1.set_ylabel('Estrogen (pg/L)', fontweight='bold', fontsize='large', color=color)
ax1.plot(e.cycle, e.estgraph, color=color, label="Estrogen")
ax1.tick_params(axis='y', labelcolor='black')
plt.legend(loc='upper left', bbox_to_anchor=(0,.92), facecolor='white', framealpha=1.0)
ax2 = ax1.twinx()  
color = myblue
ax2.set_ylabel('Progesterone (μg/L)', color=myblue, fontweight='bold', size='large')  
ax2.plot(e.cycle, e.prog, color=color, label="Progesterone")
ax2.tick_params(axis='y', labelcolor='black')
fig.tight_layout()  
plt.xticks([1,4,8,12,16,20,24,28])
plt.axvspan(0, 6, 0,.84,facecolor='red', alpha=0.2)
#plt.axvspan(0,6, 135, 160, facecolor='white', alpha=1.0)
plt.text(.1,14, "Menstruation");
plt.title('Hormone Variation Over Cycle')
plt.legend(loc='upper left', bbox_to_anchor=(0, 1), framealpha=0.9)
plt.savefig("hormones.png", bbox_inches="tight")
plt.close()

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
plt.close()

#time vs accIron, hepcidin in storage
#vertical arrangement:
# fig, (ax1, ax2) = plt.subplots(2, figsize=(6, 8))
#horizontal arrangement:
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 3))
ax1.set_xlabel('Time (day)')
ax1.set_ylabel('Iron in Storage (mg)')
ax1.plot(e.time, e.ironStor, color=myblue)
ax1.tick_params(axis='y', labelcolor='black')
ax1.set_xticks(range(0, 7))  # Set tick positions
ax1.set_xticklabels(['0','1', '2', '3', '4', '5', '6'])  # Set tick labels
ax2.set_xlabel('Time (day)')
ax2.set_ylabel('Hepcidin in Storage (mg)')
ax2.plot(e.time, e.hep, color=mypink)  # Remove the negative sign
#ax3.tick_params(axis='y', labelcolor='black')
ax2.set_xticks(range(0, 7))
ax2.tick_params(axis='y', labelcolor='black')
ax2.set_xticklabels(['0', '1', '2', '3', '4', '5', '6'])
#ax3.set_ylim(max(e.hep), min(e.hep))  # Reverse the order of limits
#ax3.set_yticklabels([abs(tick) for tick in ax3.get_yticks()])
fig.tight_layout()
plt.savefig("EstHepIron.png", bbox_inches="tight")  # Ensure file extension
plt.close()  # Display the figure



